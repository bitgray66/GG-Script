import bpy



for ob in bpy.data.objects:
    print (ob.name)
    try:
        ob.location=(0.0, 0.0, 0.0)
        bpy.context.area.type = 'OUTLINER'
        bpy.ops.outliner.liboverride_operation(type="OVERRIDE_LIBRARY_CREATE_HIERARCHY",selection_set="SELECTED_AND_CONTENT")
        bpy.context.area.type = 'TEXT_EDITOR'
    except:
        print (ob.name + " except.")