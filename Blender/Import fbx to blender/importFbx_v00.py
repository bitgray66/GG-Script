import os
import bpy

# Cartella da analizzare
folder_path = 'C:\\Users\\luigi.marazzi\\Desktop\\PRP'


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
                
                # Collezione principale della scena
                main_collection = bpy.context.scene.collection
                
                # AZIONI DA COMPIERE
                
                
                # Salva il file in formato Blender
                blend_file_path = fbx_file_path[:-3] + 'blend'  # Sostituisci l'estensione .fbx con .blend
                bpy.ops.wm.save_as_mainfile(filepath=blend_file_path)
                
                # Pulisci la scena di Blender per il prossimo file
                bpy.ops.wm.read_factory_settings(use_empty=True)

# Esegui la funzione per creare le collezioni corrispondenti ai nodi Empty
create_collections_for_empty_nodes(folder_path)
