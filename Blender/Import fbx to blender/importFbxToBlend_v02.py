import os
import bpy

# Cartella da analizzare
folder_path = 'C:\\Users\\luigi.marazzi\\Desktop\\Prova'

def add_object_to_collection(obj, collection):
    if obj and obj.type == 'OBJECT' and obj.name not in collection.objects:
        collection.objects.link(obj)

def add_objects_to_collections(obj, parent_collection):
    # Aggiunge l'oggetto alla collezione genitore solo se non è già presente
    add_object_to_collection(obj, parent_collection)
    
    # Se l'oggetto è un Empty, esplora i suoi figli
    if obj.type == 'EMPTY':
        collection_name = obj.name.replace('_GRP', '_COL')
        
        # Crea una nuova collezione
        collection = bpy.data.collections.new(collection_name)
        bpy.context.scene.collection.children.link(collection)
        
        # Aggiunge l'oggetto alla collezione appena creata
        collection.objects.link(obj)
        
        # Esplora i figli dell'Empty ricorsivamente
        for child in obj.children:
            add_objects_to_collections(child, collection)


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
                
                # Esplora gli oggetti della scena
                for obj in bpy.context.scene.objects:
                    # Se l'oggetto non ha una collezione, aggiungilo direttamente alla collezione principale
                    if not obj.users_collection:
                        main_collection.objects.link(obj)
                    # Se l'oggetto ha una collezione, aggiungilo come figlio della collezione genitore
                    else:
                        parent_collection = obj.users_collection[0]
                        add_objects_to_collections(obj, parent_collection)
                
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
