import bpy
import os
import time

from bpy_extras.node_shader_utils import PrincipledBSDFWrapper
from bpy_extras.image_utils import load_image



# Definizione della classe operatore BATCH
class ConvertFBXOperator(bpy.types.Operator):
    # Identificatori univoci per l'operatore
    bl_idname = "wm.convert_fbx"
    bl_label = "Convert FBX Files"

    # Metodo chiamato quando l'operatore è eseguito
    def execute(self, context):
        # Cartella di origine dei file FBX
        folder_path = 'C:\\Users\\luigi.marazzi\\Desktop\\PRP'
        # Percorso del file di log
        log_file_path = os.path.join(folder_path, "processing_log.txt")

        # Inizializza il tempo di inizio
        start_time = time.time()

        # Apri il file di log per scrivere
        with open(log_file_path, "w") as log_file:
            log_file.write("Processing Log:\n")

            # Inizializza il conteggio dei file elaborati
            total_files = 0
            changed_files = 0
            failed_files = 0

            # Itera ricorsivamente attraverso i file nella cartella sorgente
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    # Controlla se il file è un file FBX
                    if file.lower().endswith(".fbx"):
                        total_files += 1
                        fbx_path = os.path.join(root, file)
                        # Ottieni il nome del file senza estensione
                        file_name = os.path.splitext(file)[0]
                        print('file_name =', file_name)
                        asset_name = file_name[:-3]
                        print('asset_name =', asset_name)

                        # Pulisci la scena
                        for obj in bpy.data.objects:
                            bpy.data.objects.remove(obj)

                        for mesh in bpy.data.meshes:
                            bpy.data.meshes.remove(mesh)

                        for coll in bpy.data.collections:
                            bpy.data.collections.remove(coll)

                        for mat in bpy.data.materials:
                            bpy.data.materials.remove(mat)

                        # Importa il file FBX
                        bpy.ops.import_scene.fbx(filepath=fbx_path)

                        # Effettua le operazioni aggiuntive
                        # In questo esempio, aggiungiamo una sfera
                        # bpy.ops.mesh.primitive_uv_sphere_add(radius=1.0, location=(0, 0, 0))
                        
                        # bpy.ops.node.nw_add_textures_for_principled() NON FUNZIONA!!!

                        # add_principled_setup()  # Aggiungi il materiale Principled BSDF OK !!

                        # gestione nodi empty
                        bpy.ops.wm.empty_to_collection()





























                        # gestione materiali

                       




                    







                        # Salva il file .blend nella stessa cartella del file FBX
                        blend_file_path = os.path.join(root, f"{file_name}_v01.blend")
                        bpy.ops.wm.save_as_mainfile(filepath=blend_file_path)


                        """  # Mark as Asset   
                        coll_for_asset = asset_name+'_COL'
                        print('coll_for_asset =', coll_for_asset)
                        bpy.data.collections[coll_for_asset].asset_mark()


                        # Salva il file .blend nella stessa cartella del file FBX
                        blend_file_path = os.path.join(root, f"{file_name}_marked.blend")
                        bpy.ops.wm.save_as_mainfile(filepath=blend_file_path) """

                        

                        

                        # Aggiorna il file di log
                        changed_files += 1
                        log_file.write(f"{changed_files}\t{file_name}_v01.blend\n")

            # Scrivi il tempo totale impiegato per processare i file
            end_time = time.time()
            total_time = end_time - start_time
            log_file.write(f"\nTotal processing time: {total_time} seconds\n")

        # Stampa le informazioni
        self.report({'INFO'}, f"Total files {total_files} | Changed {changed_files} | Failed {failed_files}")
        return {'FINISHED'}





# Definizione della classe operatore EMPTY
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
        
        # Trova la collezione principale e crea una nuova collezione "_GEO_COL" 
        self.create_geo_collection()
        
        # Deseleziona tutti gli oggetti attualmente selezionati
        bpy.ops.object.select_all(action='SELECT')

        # Applica le trasformazioni a tutti gli oggetti selezionati
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        
        # Rimuove la collezione con suffisso "_COL"
        for ch_col in bpy.context.scene.collection.children:
            print(ch_col)
            suffix = '_COL'
            suffixNo = '_GEO_COL'
            scene_collection = bpy.context.scene.collection
            if  ch_col.name.endswith(suffixNo):
                print('ch_col =', ch_col.name)
                nameGeoCol = ch_col.name[:-8]
                print('nameGeoCol =', nameGeoCol)
                nameCol = nameGeoCol+'_COL'
                print('nameCol =', nameCol)
            elif ch_col.name.endswith(suffix):
                print('IF = OUT')
                scene_collection.children.unlink(ch_col)

        old_geoCol_name = nameGeoCol+'_GEO_COL'
        print('old_geoCol_name =', old_geoCol_name)
        new_geoCol_name = nameCol
        print('new_geoCol_name =', new_geoCol_name)
        # Find the old GEO_COL collection by name
        old_geoCol = bpy.data.collections.get(old_geoCol_name)
        print('old_geoCol =', old_geoCol)

        old_col_name = nameCol
        print('old_col_name =', old_col_name)
        new_col_name = old_geoCol_name
        print('new_col_name =', new_col_name)
        # Find the old _COL collection by name
        old_Col = bpy.data.collections.get(old_col_name)
        print('old_Col =', old_Col)
        

         # Rename the old _GEO_COL collection
        old_geoCol.name = new_geoCol_name

        # Rename the old _COL collection
        old_Col.name = new_col_name

        # Update the Outliner to reflect the change
        bpy.context.view_layer.update()
        
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
                
    # Metodo per trovare la collezione principale e creare una nuova collezione "_GEO" 
    def create_geo_collection(self):
        # Trova la collezione principale
        master_collection = self.find_master_collection()
        if not master_collection:
            self.report({'ERROR'}, "Non è stata trovata una collezione principale.")
            return {'CANCELLED'}
        
        # Crea una nuova collezione con il suffisso "_GEO"
        new_collection_name = master_collection.name.replace("_COL", "_GEO_COL")
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
bpy.utils.register_class(ConvertFBXOperator)
bpy.utils.register_class(ConvertEmptyToCollectionOperator)

# Esegui l'operatore
bpy.ops.wm.convert_fbx()
