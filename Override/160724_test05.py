import bpy


print("#######################################")

def override_selected_object():
    # Verifica se un oggetto è selezionato
    selected_objects = bpy.context.selected_objects
    if not selected_objects:
        print("Nessun oggetto selezionato")
        return
    
    # Prendi il primo oggetto selezionato
    obj = selected_objects[0]
    
    bpy.ops.object.make_override_library()
    #bpy.ops.object.liboverride_operation(type="OVERRIDE_LIBRARY_CREATE_HIERARCHY", selection_set="SELECTED_AND_CONTENT")

    # Verifica se l'oggetto è linkato
    if obj.library:
       
        print(f"Override eseguito per l'oggetto: {obj.name}")
    else:
        print(f"L'oggetto {obj.name} non è un oggetto collegato (linked object)")



    

# Esegui la funzione
override_selected_object()




####################### funge lanciata due volte BL

import bpy

def override_selected_object():
    # Verifica se un oggetto è selezionato
    selected_objects = bpy.context.selected_objects

    for obj in selected_objects:
        obj = bpy.data.objects.get(object_name)
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.make_override_library()
        # print(f"Override eseguito per l'oggetto: {obj.name}")
            

# Esegui la funzione
override_selected_object()


############################### disco

def ctxOverwrite():
    """
    Overwrite Blender context to set the correct area and region.
    @return: dict - Overridden context
    """
    win = bpy.context.window
    scr = win.screen
    areas3d = [area for area in scr.areas if area.type == 'VIEW_3D']

    if not areas3d:
        print("No 3D View found.")
        return None

    region = [region for region in areas3d[0].regions if region.type == 'WINDOW']

    if not region:
        print("No WINDOW region found in the 3D View area.")
        return None

    override = {
        'window': win,
        'screen': scr,
        'area': areas3d[0],
        'region': region[0],
        'scene': bpy.context.scene,
        'space_data': areas3d[0].spaces.active,
    }
    return override

###############

def get_3d_view_context():
    """
    Get the context override dictionary for the 3D View area.
    @return: dict - Overridden context
    """
    for window in bpy.context.window_manager.windows:
        for area in window.screen.areas:
            if area.type == 'VIEW_3D':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        override = {
                            'window': window,
                            'screen': window.screen,
                            'area': area,
                            'region': region,
                            'scene': bpy.context.scene,
                            'space_data': area.spaces.active,
                        }
                        return override
    return None


# ad esempio se vuoi importare un file devi fare cosi per il context
override = bl_utils.get_3d_view_context()
bl_utils.import_alembic_file(override, camera_path, Path(camera_path).stem)
# se noti come primo argomento gli passsi il context override e lo fai quasi su tutti i comandi di blender in pratica usi quella funzione per fare diventare blender normale

############

bpy.ops.ed.lib_id_override_editable_toggle()