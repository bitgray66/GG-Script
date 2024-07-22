import bpy

def get_selected_collections():
    selected_collections = []
    
    # Itera sugli ID degli oggetti selezionati nel contesto corrente
    for obj in bpy.context.selected_ids:
        if isinstance(obj, bpy.types.Collection):
            selected_collections.append(obj)
    
    return selected_collections

def override_collections(collections):
    for collection in collections:
        # Crea un override per la collection
        override = bpy.context.scene.view_layers["View Layer"].layer_collection.children.get(collection.name)
        if override is None:
            print(f"Errore nel creare l'override per la collection: {collection.name}")
        else:
            print(f"Override creato per la collection: {collection.name}")

def main():
    # Ottieni le collection selezionate
    selected_collections = get_selected_collections()
    
    if not selected_collections:
        print("Nessuna collection selezionata.")
    else:
        # Applica l'override alle collection selezionate
        override_collections(selected_collections)

# Esegui la funzione principale
get_selected_collections()
