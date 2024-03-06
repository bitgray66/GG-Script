import bpy
import os

from bpy_extras.node_shader_utils import PrincipledBSDFWrapper
from bpy_extras.image_utils import load_image

# Cartella degli asset
texture_folder = 'C:\\Users\\luigi.marazzi\\Desktop\\PRP'
file_name = 'MM_PRP_AlarmClock_A_A'

def find_textures(file_name, texture_folder):
    # Lista dei suffissi da cercare
    suffices = ['_DIF', '_NRM', '_RGH']

    # Ottieni il prefisso del nome del file
    prefix = file_name

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

    # Filtra i file trovati in base ai suffissi desiderati
    matching_files_with_suffix = []
    for file_path in matching_files:
        for suffix in suffices:
            if file_path.endswith(suffix + '.png'):
                matching_files_with_suffix.append(file_path)
                break

    return matching_files_with_suffix

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
    principled.base_color_texture.image = load_image("R:\\Melody_Momon\\Production\\Assets\\Models\\PRP\\A\\MM_PRP_AlarmClock_A_A\\Tx\\Hi\\MM_PRP_AlarmClock_A_A_DIF.png") 
    principled.roughness_texture.image = load_image("R:\\Melody_Momon\\Production\\Assets\\Models\\PRP\\A\\MM_PRP_AlarmClock_A_A\\Tx\\Hi\\MM_PRP_AlarmClock_A_A_RGH.png") 
    principled.normalmap_texture.image = load_image("R:\\Melody_Momon\\Production\\Assets\\Models\\PRP\\A\\MM_PRP_AlarmClock_A_A\\Tx\\Hi\\MM_PRP_AlarmClock_A_A_NRM.png") 

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










import bpy
import os


print('@@@@@@@@@@@@@@@@@@@@@@@@@@@')
# Definizione del nome del file iniziale e della cartella delle texture
file_name = 'MM_PRP_AlarmClock_A_A'
texture_folder = 'C:\\Users\\luigi.marazzi\\Desktop\\PRP'

# Lista dei suffissi da cercare
suffices = ['_DIF', '_NRM', '_RGH']

# Ottieni il prefisso del nome del file
prefix = file_name
for suffix in suffices:
    prefix = prefix.replace(suffix, '')

# Lista dei file trovati
matching_files = []

# Funzione per trovare i file con il suffisso specificato nella cartella specificata
def find_matching_files(folder, prefix, suffix):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.startswith(prefix) and file.endswith(suffix + '.png'):  # Puoi modificare l'estensione qui se necessario
                matching_files.append(os.path.join(root, file))

# Iterazione su tutti i suffissi per trovare i file corrispondenti
for suffix in suffices:
    find_matching_files(texture_folder, prefix, suffix)

# Stampa dei file trovati
print("File trovati per '{}':".format(file_name))
for file_path in matching_files:
    print(file_path)
