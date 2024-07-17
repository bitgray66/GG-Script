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

area = next(area for area in bpy.context.window.screen.areas if area.type == 'OUTLINER')

with bpy.context.temp_override(
    window=bpy.context.window,
    area=area,
    region=next(region for region in area.regions if region.type == 'WINDOW'),
    screen=bpy.context.window.screen
):
    over_sel_collections()
