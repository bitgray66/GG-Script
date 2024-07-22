import bpy
print("@@@@@@@@@@@@@################@@@@@@@@@@@@@")

def over_sel_collections_and_data():
    print("------context------> ", bpy.context)
    selected_objects = bpy.context.selected_objects[:]
    print("------selected_objects------> ", selected_objects)
    #list_assets = ["a", "b", "c"]
    list_assets = []
    for col in selected_objects:
        cleaned_name = col.name.replace('_COL', '')
        print(f"cleaned_name: {cleaned_name}")
        list_assets.append(cleaned_name)
        print(f"list_assets: {list_assets}")
        
    for col in selected_objects:
        col_name = col.name  # Memorizza il nome dell'oggetto
        bpy.ops.outliner.liboverride_operation(type="OVERRIDE_LIBRARY_CREATE_HIERARCHY", selection_set="SELECTED_AND_CONTENT")
        print(f"Override applicato per la collection: {col_name}")

    return list_assets

""" def sel_obj_by_pref(pref):
    list_objects = []   # non è uguale alla lisata delle collection visto che alcune coll possono contenere più oggetti
    for obj in bpy.context.scene.objects:
        if obj.name.startswith(pref):
            # obj.select_set(True)
            list_objects.append(obj.name)

    return list_objects
 """

    
area = next(area for area in bpy.context.window.screen.areas if area.type == 'OUTLINER')

with bpy.context.temp_override(
    window=bpy.context.window,
    area=area,
    region=next(region for region in area.regions if region.type == 'WINDOW'),
    screen=bpy.context.window.screen
):
    #over_sel_collections_and_data()


    def main():
        # Ottieni le collection selezionate
        list_assets = over_sel_collections_and_data()
        
        if not list_assets:
            print("Nessuna lista pervenuta.")
        else:
            # Applica l'override alle collection selezionate
            #override_collections(selected_collections)
            print(f"OK lista pervenuta: {list_assets}")

    # Esegui la funzione principale
    main()