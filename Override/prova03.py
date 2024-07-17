import bpy

def get_selected_collections():
    selected_collections = []
    
    # Itera su tutte le collection
    for collection in bpy.data.collections:
        if collection.select:
            selected_collections.append(collection)
    
    return selected_collections

def override_collections(collections):
    for collection in collections:
        # Ottieni l'override per la collection nel view layer corrente
        view_layer = bpy.context.view_layer
        layer_collection = view_layer.layer_collection.children.get(collection.name)
        
        if layer_collection is None:
            print(f"Errore nel trovare la collection: {collection.name}")
        else:
            # Imposta l'override
            layer_collection.exclude = False
            print(f"Override applicato per la collection: {collection.name}")

def main():
    # Ottieni le collection selezionate
    selected_collections = get_selected_collections()
    
    if not selected_collections:
        print("Nessuna collection selezionata.")
    else:
        # Applica l'override alle collection selezionate
        override_collections(selected_collections)

# Esegui la funzione principale
main()
