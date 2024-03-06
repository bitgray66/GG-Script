import bpy
import os

from bpy_extras.node_shader_utils import PrincipledBSDFWrapper
from bpy_extras.image_utils import load_image

# Nome del materiale
material_name = "NomeAsset_mat"

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

# Seleziona tutte le mesh nella scena
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')

# Assegna il materiale a tutti gli oggetti selezionati
for obj in bpy.context.selected_objects:
    obj.data.materials.clear()  # Rimuove tutti i materiali esistenti
    obj.data.materials.append(mat)  # Aggiunge il nuovo materiale