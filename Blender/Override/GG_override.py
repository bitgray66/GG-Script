import bpy
import ast


def get_list_selected():
    try:
        list_selected = bpy.context.selected_objects
        selected_col = [o.name for o in list_selected]

        list_location = []
        for obj in list_selected:
            list_location.append(obj.location)
        
        return selected_col, list_location
    except Exception as e:
        print(f"Errore in get_list_selected: {e}")
        return [], []

def override_collections(selected_col):
    for obj in selected_col:
        try:
            col = bpy.data.objects.get(obj)
            if col:
                bpy.context.view_layer.objects.active = col
                bpy.ops.object.make_override_library()
                print(f"Override eseguito per l'oggetto: {obj}")
            else:
                print(f"Oggetto non trovato: {obj}")
        except Exception as e:
            print(f"Errore in override_collections per l'oggetto {obj}: {e}")

def get_list_prefixes(selected_col):
    try:
        list_prefixes = []
        for item in selected_col:
            cleaned_name = item.replace('_COL', '')
            list_prefixes.append(cleaned_name)

        return list_prefixes
    except Exception as e:
        print(f"Errore in get_list_prefixes: {e}")
        return []

def reselect_objects(list_prefixes):
    try:
        meshes = bpy.data.meshes
        for mesh in meshes:
            mesh_name = mesh.name
            for prefix in list_prefixes:
                if mesh_name.startswith(prefix):
                    obj = bpy.data.objects.get(mesh_name)
                    if obj:
                        obj.select_set(True)
                        bpy.context.view_layer.objects.active = obj
                    else:
                        print(f"Oggetto non trovato: {mesh_name}")
        return meshes
    except Exception as e:
        print(f"Errore in reselect_objects: {e}")
        return []

def override_selected_object():
    try:
        selected_objects = bpy.context.selected_objects
        for obj in selected_objects:
            obj = bpy.data.objects.get(obj.name)
            if obj:
                bpy.context.view_layer.objects.active = obj
                bpy.ops.object.make_override_library()
                print(f"Override eseguito per l'oggetto: {obj.name}")
            else:
                print(f"Oggetto non trovato: {obj.name}")
    except Exception as e:
        print(f"Errore in override_selected_object: {e}")

def relocate_objects(prefix_location):
    try:
        ob_selected = bpy.context.selected_objects
        for ob in ob_selected:
            ob_name = ob.name
            for key in prefix_location:
                if ob_name.startswith(key):
                    obj = bpy.data.objects.get(ob_name)
                    if obj:
                        bpy.context.view_layer.objects.active = obj
                        val = prefix_location[key]
                        
                        try:
                            val_tuple = ast.literal_eval(val)
                            if isinstance(val_tuple, tuple) and len(val_tuple) == 3:
                                obj.location = val_tuple
                                print(f"Oggetto {obj.name} spostato a {val_tuple}")
                            else:
                                print(f"Formato posizione non valido per {val}: deve essere una tupla di tre valori.")
                        except (ValueError, SyntaxError) as ve:
                            print(f"Errore nella conversione di {val} in una tupla: {ve}")
                    else:
                        print(f"Oggetto non trovato: {ob_name}")
    except Exception as e:
        print(f"Errore in relocate_objects: {e}")

try:
    selected_col, list_location = get_list_selected()

    list_position = []
    for loc in list_location:
        newloc = str(loc)
        newloc = newloc[8:-1]
        list_position.append(newloc)

    override_collections(selected_col)

    list_prefixes = get_list_prefixes(selected_col)

    reselect_objects(list_prefixes)

    override_selected_object()

    prefix_location = {list_prefixes[i]: list_position[i] for i in range(len(list_prefixes))}

    relocate_objects(prefix_location)
except Exception as e:
    print(f"Errore nell'esecuzione principale: {e}")
