import bpy

def over_sel_collections():
    print("------context------> ", bpy.context)
    selected_objects = bpy.context.selected_objects
    print("------selected_objects------> ", selected_objects)
    names = [o.name for o in selected_objects]
    print("------------> ", names)
    for name in names:
        # Imposta l'override
        bpy.ops.outliner.liboverride_operation(type="OVERRIDE_LIBRARY_CREATE_HIERARCHY", selection_set="SELECTED_AND_CONTENT")
        print(f"Override applicato per la collection: {name}")

def over_sel_collections_and_data():
    print("------context------> ", bpy.context)
    selected_objects = bpy.context.selected_objects[:]
    print("------selected_objects------> ", selected_objects)
    
    # Primo passaggio: Override per le collezioni
    for obj in selected_objects:
        obj_name = obj.name  # Memorizza il nome dell'oggetto
        bpy.ops.outliner.liboverride_operation(type="OVERRIDE_LIBRARY_CREATE_HIERARCHY", selection_set="SELECTED_AND_CONTENT")
        print(f"Override applicato per la collection: {obj_name}")
    
    # Secondo passaggio: Recupera nuovamente gli oggetti selezionati
    selected_objects = bpy.context.selected_objects[:]
    
    # Override per i data blocks
    for obj in selected_objects:
        if obj.data:
            obj_data_name = obj.data.name
            bpy.ops.outliner.liboverride_operation(type="OVERRIDE_LIBRARY_CREATE_HIERARCHY", selection_set="SELECTED_AND_CONTENT")
            print(f"Override applicato per il data block: {obj_data_name}")

area = next(area for area in bpy.context.window.screen.areas if area.type == 'OUTLINER')

with bpy.context.temp_override(
    window=bpy.context.window,
    area=area,
    region=next(region for region in area.regions if region.type == 'WINDOW'),
    screen=bpy.context.window.screen
):
    over_sel_collections_and_data()




list_assets = []
    for obj in selected_collections:
        
        obj_name = obj.name  # Memorizza il nome dell'oggetto
        cleaned_name = obj.name.replace('_COL', '')
        list_assets.append(cleaned_name)
        print("------list_assets 2------> ", list_assets)