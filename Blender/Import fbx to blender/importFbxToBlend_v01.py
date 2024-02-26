import os
import bpy

# Cartella da analizzare
folder_path = 'C:\\Users\\luigi.marazzi\\Desktop\\Prova\\a\\ab\\aba'

def process_fbx_files(folder_path):
    # Scansiona la cartella
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.fbx'):
                # Costruisci il percorso completo del file FBX
                fbx_file_path = os.path.join(root, file)
                
                # Importa il file FBX in Blender
                bpy.ops.import_scene.fbx(filepath=fbx_file_path)
                
                # Sostituisci i nodi Empty con nodi Collection e modifica il suffisso GRP con COL
                for obj in bpy.context.scene.objects:
                    if obj.type == 'EMPTY':
                        # Crea una nuova Collection con lo stesso nome dell'Empty
                        collection_name = obj.name.replace('_GRP', '_COL')
                        collection = bpy.data.collections.new(collection_name)
                        
                        # Aggiungi gli oggetti dell'Empty alla Collection
                        for child in obj.children:
                            collection.objects.link(child)
                        
                        # Rimuovi l'Empty dalla scena
                        bpy.data.objects.remove(obj)
                
                # Salva il file in formato Blender
                blend_file_path = fbx_file_path[:-3] + 'blend'  # Sostituisci l'estensione .fbx con .blend
                
                # Rimuovi le collezioni vuote
                for collection in bpy.data.collections:
                    if len(collection.objects) == 0:
                        bpy.data.collections.remove(collection)
                
                # Salva il file in formato Blender
                bpy.ops.wm.save_as_mainfile(filepath=blend_file_path)
                
                # Pulisci la scena di Blender per il prossimo file
                bpy.ops.wm.read_factory_settings(use_empty=True)

# Esegui la funzione per processare i file FBX
process_fbx_files(folder_path)
