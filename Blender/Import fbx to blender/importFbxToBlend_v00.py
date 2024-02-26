import os
import bpy

# Cartella da analizzare
folder_path = 'C:\\Users\\luigi.marazzi\\Desktop\\Prova\\a\\ab\\aba'

def import_fbx_and_save_blend(folder_path):
    # Scansiona la cartella
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.fbx'):
                # Costruisci il percorso completo del file FBX
                fbx_file_path = os.path.join(root, file)
                
                # Importa il file FBX in Blender
                bpy.ops.import_scene.fbx(filepath=fbx_file_path)
                
                # Salva il file in formato Blender
                blend_file_path = fbx_file_path[:-3] + 'blend'  # Sostituisci l'estensione .fbx con .blend
                bpy.ops.wm.save_as_mainfile(filepath=blend_file_path)
                
                # Pulisci la scena di Blender per il prossimo file
                bpy.ops.wm.read_factory_settings(use_empty=True)

# Esegui la funzione per importare i file FBX e salvarli in formato Blender
import_fbx_and_save_blend(folder_path)
