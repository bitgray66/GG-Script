import bpy

def get_selected_collections():
    selected_collections = []
    
    # Salva il contesto attuale
    original_area_type = bpy.context.area.type
    
    try:
        # Cambia il contesto all'Outliner
        bpy.context.area.type = 'OUTLINER'
        
        # Itera su tutte le collection
        def iterate_collections(layer_collection):
            if layer_collection.collection.select:
                selected_collections.append(layer_collection.collection)
            
            for child in layer_collection.children:
                iterate_collections(child)
        
        # Ottieni la root layer collection
        root_layer_collection = bpy.context.view_layer.layer_collection
        iterate_collections(root_layer_collection)
    
    finally:
        # Ripristina il contesto originale
        bpy.context.area.type = original_area_type
    
    return selected_collections

def override_collections(collections):
    # Salva il contesto attuale
    original_area_type = bpy.context.area.type
    
    try:
        # Cambia il contesto all'Outliner
        bpy.context.area.type = 'OUTLINER'
        
        for collection in collections:
            # Imposta l'override
            bpy.ops.outliner.liboverride_operation(type="OVERRIDE_LIBRARY_CREATE_HIERARCHY", selection_set="SELECTED_AND_CONTENT")
            print(f"Override applicato per la collection: {collection.name}")
    
    finally:
        # Ripristina il contesto originale
        bpy.context.area.type = original_area_type

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
