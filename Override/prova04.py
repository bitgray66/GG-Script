import bpy

def get_selected_collections(layer_collection):
    selected_collections = []
    
    # Funzione ricorsiva per iterare su tutte le collection
    def iterate_collections(layer_collection):
        if layer_collection.collection.select:
            selected_collections.append(layer_collection.collection)
        
        for child in layer_collection.children:
            iterate_collections(child)
    
    # Inizia l'iterazione dalla root layer collection
    iterate_collections(layer_collection)
    
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
    # Ottieni la root layer collection
    root_layer_collection = bpy.context.view_layer.layer_collection
    
    # Ottieni le collection selezionate
    selected_collections = get_selected_collections(root_layer_collection)
    
    if not selected_collections:
        print("Nessuna collection selezionata.")
    else:
        # Applica l'override alle collection selezionate
        override_collections(selected_collections)

# Esegui la funzione principale
main()
