import bpy
import os

def create_asset_material(asset_name, asset_folder):
    def find_textures(folder_asset):
        texture_folder = os.path.join(asset_folder, folder_asset, "Tx", "hi")
        textures = []
        if os.path.exists(texture_folder):
            for root, dirs, files in os.walk(texture_folder):
                for file in files:
                    if file.endswith(".png"):
                        textures.append(os.path.join(root, file))
        return textures

    textures = find_textures(asset_name)

    # Crea un nuovo materiale
    material = bpy.data.materials.new(name=asset_name + "_mat")
    
    # Aggiungi il nodo Principled BSDF al materiale
    principled_bsdf = material.node_tree.nodes.new('ShaderNodeBsdfPrincipled')
    principled_bsdf.location = (-200, 200)  # Posizione del nodo nell'editor dei nodi
    
    # Aggiungi un nodo Image Texture per ciascuna texture trovata nella cartella dell'asset
    for texture_path in textures:
        image_texture = material.node_tree.nodes.new('ShaderNodeTexImage')
        image_texture.image = bpy.data.images.load(texture_path)
        image_texture.location = (-400, 200)  # Posizione del nodo nell'editor dei nodi
        
        # Aggiungi il nodo Mapping
        mapping = material.node_tree.nodes.new('ShaderNodeMapping')
        mapping.location = (-600, 200)  # Posizione del nodo nell'editor dei nodi
        material.node_tree.links.new(mapping.inputs['Vector'], image_texture.outputs['Vector'])
        
        # Aggiungi il nodo Texture Coordinate
        texture_coord = material.node_tree.nodes.new('ShaderNodeTexCoord')
        texture_coord.location = (-800, 200)  # Posizione del nodo nell'editor dei nodi
        material.node_tree.links.new(mapping.inputs['Vector'], texture_coord.outputs['UV'])
        
        # Collega il nodo Image Texture al nodo Principled BSDF
        material.node_tree.links.new(image_texture.outputs['Color'], principled_bsdf.inputs['Base Color'])
    
    return material

# Cartella degli asset
asset_folder = 'C:\\Users\\luigi.marazzi\\Desktop\\PRP'
asset_name = 'MM_PRP_AlarmClock_A_A'

# Creazione del materiale dell'asset
material = create_asset_material(asset_name, asset_folder)

# Assegnazione del materiale a tutti gli oggetti mesh nella scena
for obj in bpy.context.scene.objects:
    if obj.type == 'MESH':
        obj.data.materials.append(material)
