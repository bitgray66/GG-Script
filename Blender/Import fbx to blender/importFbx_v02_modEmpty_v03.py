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

                        # Cartella degli asset
                        texture_folder = 'C:\\Users\\luigi.marazzi\\Desktop\\PRP'

                        def find_textures(file_name, texture_folder):
                            # Lista dei suffissi da cercare
                            suffices = ['_DIF', '_NRM', '_RGH']

                            # Ottieni il prefisso del nome del file
                            prefix = file_name
                            print('prefix  =', prefix)

                            # Lista dei file trovati
                            matching_files = []

                            # Funzione per trovare i file con il prefisso specificato nella cartella specificata
                            def find_matching_files_with_prefix(folder, prefix):
                                for root, dirs, files in os.walk(folder):
                                    for file in files:
                                        if file.startswith(prefix):
                                            matching_files.append(os.path.join(root, file))

                            # Trova tutti i file con il prefisso specificato
                            find_matching_files_with_prefix(texture_folder, prefix)

                            # Lista dei path delle texture corrispondenti
                            return matching_files



                        def create_asset_material(file_name):

                            matching_textures = find_textures(file_name, texture_folder)

                            for file_path in matching_textures:
                                print(file_path)

                            # Nome del materiale
                            material_name = file_name+'_MAT'

                            # Creazione del materiale
                            mat = bpy.data.materials.new(name=material_name)

                            # Assegna un colore al materiale (opzionale)
                            mat.diffuse_color = (0.8, 0.2, 0.2, 1)  # Colori RGBA (rossastro)

                            mat.use_nodes = True
                            nodescale = 300
                            principled = PrincipledBSDFWrapper(mat, is_readonly=False)
                            principled.base_color = (0.8, 0.8, 0.5)

                            print("File trovati per '{}':".format(file_name))

                            for file_path in matching_textures:
                                tipo = file_path[-8:-4]  # Prendi gli ultimi 4 caratteri prima dell'estensione (.png)
                                if tipo == '_DIF':
                                    print("_DIF:", file_path)
                                    principled.base_color_texture.image = load_image(file_path) 
                                elif tipo == '_RGH':
                                    print("_RGH:", file_path)
                                    principled.roughness_texture.image = load_image(file_path) 
                                elif tipo == '_NRM':
                                    print("_NRM:", file_path)
                                    principled.normalmap_texture.image = load_image(file_path) 

                            bpy.data.materials["MM_PRP_AlarmClock_A_A_MAT"].node_tree.nodes["Principled BSDF"].label = material_name

                                    
                            # materiale 
                            return mat



                        # Creazione del materiale dell'asset
                        mat = create_asset_material(file_name)

                        # Seleziona tutte le mesh nella scena
                        bpy.ops.object.select_all(action='DESELECT')
                        bpy.ops.object.select_by_type(type='MESH')

                        # Assegna il materiale a tutti gli oggetti selezionati
                        for obj in bpy.context.selected_objects:
                            obj.data.materials.clear()  # Rimuove tutti i materiali esistenti
                            obj.data.materials.append(mat)  # Aggiunge il nuovo materiale












                    







                        # Salva il file .blend nella stessa cartella del file FBX
                        blend_file_path = os.path.join(root, f"{file_name}.blend")
                        bpy.ops.wm.save_as_mainfile(filepath=blend_file_path)


                        # Mark as Asset   
                        coll_for_asset = file_name+'_COL'
                        print('coll_for_asset =', coll_for_asset)
                        bpy.data.collections[coll_for_asset].asset_mark()
                        #bpy.data.objects['my_object'].asset_generate_preview()


                        # Salva il file .blend nella stessa cartella del file FBX
                        blend_file_path = os.path.join(root, f"{file_name}_marked.blend")
                        bpy.ops.wm.save_as_mainfile(filepath=blend_file_path)

                        

                        

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
