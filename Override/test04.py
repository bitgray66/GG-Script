import bpy
print("@@@@@@@@@@@@@@@@@@@@@@@@@@")


def override_collections():
    selected_collections = []

    # Trova tutte le collezioni selezionate
    for collection in bpy.context.scene.collection.children:
        if collection.name.endswith('_COL') and not collection.hide_viewport:
            selected_collections.append(collection)

    for collection in selected_collections:
        # Seleziona la collezione nella vista Outliner
        bpy.context.view_layer.active_layer_collection = bpy.context.view_layer.layer_collection.children[collection.name]

        # Applica l'override
        bpy.ops.outliner.liboverride_operation(type="OVERRIDE_LIBRARY_CREATE_HIERARCHY", selection_set="SELECTED_AND_CONTENT")
        print(f"Override applicato per la collection: {collection.name}")

# Esegui la funzione per applicare gli override alle collezioni selezionate
override_collections()

