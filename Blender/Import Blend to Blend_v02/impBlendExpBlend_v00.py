import bpy
import os

# Percorso della cartella master contenente i file .blend
master_folder_path = "/path/to/master/folder"

# Funzione per aggiungere una sfera alla scena
def add_sphere(scene):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(0, 0, 0))

# Ciclo attraverso tutti i file .blend nella cartella master e sottocartelle
for root, dirs, files in os.walk(master_folder_path):
    for file in files:
        if file.endswith(".blend"):
            # Costruisci il percorso completo del file .blend
            blend_file_path = os.path.join(root, file)
            
            # Carica la scena dal file .blend
            with bpy.data.libraries.load(blend_file_path) as (data_from, data_to):
                data_to.scenes = data_from.scenes

            # Ciclo attraverso tutte le scene nel file .blend
            for scene_name in data_to.scenes:
                # Attiva la scena corrente
                bpy.context.window.scene = bpy.data.scenes[scene_name]

                # Aggiungi una sfera alla scena
                add_sphere(bpy.context.scene)

                # Stampa il nome della scena aperta
                print("Scene Name:", bpy.context.scene.name)

                # Salva la scena con lo stesso nome della scena aperta, ma con il suffisso "_v02"
                bpy.ops.wm.save_as_mainfile(filepath=blend_file_path.replace(".blend", f"_{scene_name}_v02.blend"), check_existing=False)

                # Rinomina la scena originale aggiungendo "_v02"
                bpy.context.scene.name = f"{scene_name}_v02"

                # Pulisci tutto per importare la scena successiva
                bpy.ops.wm.read_factory_settings(use_empty=True)
