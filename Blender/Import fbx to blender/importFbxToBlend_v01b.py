import os
import bpy

# Cartella da analizzare
folder_path = 'C:\\Users\\luigi.marazzi\\Desktop\\Prova'

def create_collections_for_empty_nodes(folder_path):
    # Scansiona la cartella
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.fbx'):
                # Costruisci il percorso completo del file FBX
                fbx_file_path = os.path.join(root, file)
                
                # Importa il file FBX in Blender
                bpy.ops.import_scene.fbx(filepath=fbx_file_path)
                
                # Applica la trasformazione agli oggetti prima di procedere
                bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
                
                # Sostituisci i nodi Empty con nodi Collection e modifica il suffisso GRP con COL
                for obj in bpy.context.scene.objects:
                    if obj.type == 'EMPTY':
                        # Crea una nuova Collection con lo stesso nome dell'Empty
                        collection_name = obj.name.replace('_GRP', '_COL')
                        collection = bpy.data.collections.new(collection_name)
                        
                        # Ottieni la collezione principale della scena
                        main_collection = bpy.context.scene.collection
                        
                        # Aggiungi la nuova collezione come figlia della collezione principale
                        main_collection.children.link(collection)
                        
                        # Aggiungi gli oggetti dell'Empty alla Collection
                        for child in obj.children:
                            if child.users_collection:  # Verifica se l'oggetto è già collegato a una collezione
                                child.users_collection[0].objects.unlink(child)  # Rimuovi l'oggetto dalla sua collezione precedente
                            collection.objects.link(child)
                        
                        # Rimuovi l'Empty dalla scena
                        bpy.data.objects.remove(obj)
                
                # Rimuovi gli oggetti non collegati a nessuna collezione dalla scena
                for obj in bpy.context.scene.objects:
                    if not obj.users_collection:
                        bpy.data.objects.remove(obj)
                
                # Salva il file in formato Blender
                blend_file_path = fbx_file_path[:-3] + 'blend'  # Sostituisci l'estensione .fbx con .blend
                bpy.ops.wm.save_as_mainfile(filepath=blend_file_path)
                
                # Pulisci la scena di Blender per il prossimo file
                bpy.ops.wm.read_factory_settings(use_empty=True)

# Esegui la funzione per creare le collezioni corrispondenti ai nodi Empty
create_collections_for_empty_nodes(folder_path)
