import bpy

# Definizione della classe operatore
class ConvertEmptyToCollectionOperator(bpy.types.Operator):
    # Identificatori univoci per l'operatore
    bl_idname = "wm.empty_to_collection"
    bl_label = "Convert Empty to Collection"  # Etichetta visualizzata nell'interfaccia utente

    # Metodo chiamato quando l'operatore è eseguito
    def execute(self, context):
        print('@@@@@@@@@@@@@@@@@@@@@@@@')

        # Applica le trasformazioni a tutti gli oggetti selezionati
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

        # Deseleziona tutti gli oggetti attualmente selezionati
        bpy.ops.object.select_all(action='DESELECT')
        
        # Verifica se ci sono oggetti selezionati
        if len(bpy.context.selected_objects):
            objects = bpy.context.selected_objects  # Recupera gli oggetti selezionati
        else:
            objects = get_scene_children()  # Se nessun oggetto selezionato, ottieni tutti gli oggetti nella scena
        # Itera su ogni oggetto
        for o in objects:
            # Determina la collezione genitore
            if len(o.users_collection):
                parent_collection = o.users_collection[0]  # Prende la prima collezione associata all'oggetto
            else:
                parent_collection = bpy.context.scene.collection  # Se non è associato a nessuna collezione, usa la collezione della scena
            # Converte le EMPTY in collezioni
            self.empties_to_collections(o, parent_collection)
        
        # Trova la collezione principale e crea una nuova collezione "_GEO" basata su di essa
        self.create_geo_collection()
        
        # Deseleziona tutti gli oggetti attualmente selezionati
        bpy.ops.object.select_all(action='ELECT')

        # Applica le trasformazioni a tutti gli oggetti selezionati
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        
        # Rimuove la collezione con suffisso "_COL"
        for ch_col in bpy.context.scene.collection.children:
            print(ch_col)
            suffix = '_COL'
            scene_collection = bpy.context.scene.collection
            if ch_col.name.endswith(suffix):
                print('ch_col =', ch_col.name)
                scene_collection.children.unlink(ch_col)


        
        return {'FINISHED'}  # Restituisce un segnale di completamento

    # Metodo per la conversione delle EMPTY in collezioni
    def empties_to_collections(self, o, parent_collection):
        children = get_objects_children(o)  # Ottiene gli oggetti figlio
        # Se l'oggetto è di tipo EMPTY
        if hasattr(o, 'type') and o.type == 'EMPTY':
            o.name = o.name.replace("_GRP", "_COL")
            # Crea una nuova collezione
            new_collection = bpy.data.collections.new(o.name)
            parent_collection.children.link(new_collection)  # Aggiunge la nuova collezione come figlia della collezione genitore
            # Sposta tutti gli oggetti figlio nella nuova collezione
            for ch in o.children_recursive:
                for old_collection in ch.users_collection:
                    old_collection.objects.unlink(ch)  # Rimuove l'oggetto dalla sua collezione precedente
                new_collection.objects.link(ch)  # Aggiunge l'oggetto alla nuova collezione
            bpy.data.objects.remove(o)  # Rimuove l'EMPTY
            # Richiama ricorsivamente per ogni figlio dell'EMPTY
            for ch in children:
                self.empties_to_collections(ch, new_collection)
        else:
            # Se l'oggetto non è di tipo EMPTY, chiama empties_to_collections su tutti i suoi figli
            for ch in children:
                self.empties_to_collections(ch, parent_collection)
                
    # Metodo per trovare la collezione principale e creare una nuova collezione "_GEO" basata su di essa
    def create_geo_collection(self):
        # Trova la collezione principale
        master_collection = self.find_master_collection()
        if not master_collection:
            self.report({'ERROR'}, "Non è stata trovata una collezione principale.")
            return {'CANCELLED'}
        
        # Crea una nuova collezione con il suffisso "_GEO"
        new_collection_name = master_collection.name.replace("_COL", "_GEO")
        new_collection = bpy.data.collections.new(new_collection_name)
        
        # Aggiungi la nuova collezione alla collezione principale
        bpy.context.collection.children.link(new_collection)
        
        # Sposta la collezione principale e tutto il suo contenuto nella nuova collezione "_GEO"
        self.move_collection(master_collection, new_collection)
    
    # Metodo per trovare la collezione principale nella scena
    def find_master_collection(self):
        for collection in bpy.context.scene.collection.children:
            if collection.objects:
                return collection
        return None
    
    # Metodo per spostare la collezione e il suo contenuto in una nuova collezione
    def move_collection(self, src_collection, dst_collection):
        # Sposta la collezione sorgente nella collezione di destinazione
        dst_collection.children.link(src_collection)
        




    
# Funzione per ottenere gli oggetti figlio
def get_objects_children(obj):
    obs = []
    if hasattr(obj, 'children'):
        obs.extend(obj.children)
    if hasattr(obj, 'objects'):
        obs.extend(obj.objects)
    return obs

# Funzione per ottenere gli oggetti di primo livello nella scena
def get_scene_children():
    """List of the 'Scene' collection's children."""
    children = []
    for o in bpy.data.objects:
        if hasattr(o, 'parent') and o.parent is None:
            children.append(o)
    return children

# Registra la classe dell'operatore in Blender
bpy.utils.register_class(ConvertEmptyToCollectionOperator)

# Esegui l'operatore
bpy.ops.wm.empty_to_collection()
