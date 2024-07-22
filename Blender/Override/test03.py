import bpy
print("################################################")
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
    
    # Memorizza le informazioni sugli oggetti e sui loro data blocks
    obj_data_pairs = [(obj.name, obj.data.name) for obj in selected_objects if obj.data]
    
    # Secondo passaggio: Debug per selezione oggetti e data blocks
    for obj_name, obj_data_name in obj_data_pairs:
        obj = bpy.data.objects.get(obj_name)
        if obj:
            # Seleziona l'oggetto per garantire che l'override del data block funzioni correttamente
            bpy.context.view_layer.objects.active = obj
            obj.select_set(True)
            print(f"Oggetto attivo: {bpy.context.view_layer.objects.active.name}")
            print(f"Oggetto selezionato: {obj.name}")
            print(f"Data block dell'oggetto: {obj_data_name}")
            # Per ora commentiamo l'override del data block
            # bpy.ops.object.make_override_library()
            # print(f"Override applicato per il data block: {obj_data_name}")

area = next(area for area in bpy.context.window.screen.areas if area.type == 'OUTLINER')

with bpy.context.temp_override(
    window=bpy.context.window,
    area=area,
    region=next(region for region in area.regions if region.type == 'WINDOW'),
    screen=bpy.context.window.screen
):
    over_sel_collections_and_data()
