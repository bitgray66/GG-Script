import bpy

print("----------------------------------------------------------------------------------------------------------- ")

def get_list_selected():
    # Verifica se un oggetto è selezionato
    list_selected = bpy.context.selected_objects
    selected_col = [o.name for o in list_selected]
    
    list_location =[]
    for obj in list_selected:
        print("item location", obj.location)
        list_location.append(obj.location) 
         
         
    return selected_col, list_location

            
def override_collections(selected_col):
    for obj in selected_col:
        print("obj ------------> ", selected_col)
        col = bpy.data.objects.get(obj)
        bpy.context.view_layer.objects.active = col
        bpy.ops.object.make_override_library()
        print(f"Override eseguito per l'oggetto: {obj}")
    

def get_list_prefixes(selected_col):
    list_prefixes =[]
    for item in selected_col:
        print("item", item)
        cleaned_name = item.replace('_COL', '')
        print(f"cleaned_name: {cleaned_name}")
        list_prefixes.append(cleaned_name)

    return list_prefixes

def reselect_objects(list_prefixes):
    meshes = bpy.data.meshes
    print("meshes ------------> ", meshes)
    for mesh in meshes:
        mesh_name = mesh.name
        print("----mesh-----", mesh_name)
        for prefix in list_prefixes:
            print("----prefix-----", prefix)
            # check if the message starts with prefix
            if mesh_name.startswith(prefix):
                print("trovata corrispondenza ", prefix)
                obj = bpy.data.objects.get(mesh_name)
                print("trovata obj ", obj)
                obj.select_set(True)
                bpy.context.view_layer.objects.active = obj
                
                #bpy.ops.object.make_override_library()
                #print(f"Override eseguito per l'oggetto: {mesh_name}")
    return meshes


def override_selected_object():
    # Verifica se un oggetto è selezionato
    selected_objects = bpy.context.selected_objects

    for obj in selected_objects:
        obj = bpy.data.objects.get(obj.name)
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.make_override_library()
        print(f"Override eseguito per l'oggetto: {obj.name}")
        
        
""" def relocate_objects(prefix_location):
    print("get_prefix_location ------------> ", prefix_location)    
    meshes = bpy.data.meshes
    print("meshes ------------> ", meshes)
    for mesh in meshes:
        mesh_name = mesh.name
        print("----mesh-----", mesh_name)
        for key in prefix_location:
            print("----key-----", key)
            # check if the message starts with prefix
            if mesh_name.startswith(key):
                print("trovata corrispondenza key ", key)
                obj = bpy.data.objects.get(mesh_name)
                print("trovata obj-key", obj)
                obj.select_set(True)
                bpy.context.view_layer.objects.active = obj
 """


import ast

def relocate_objects(prefix_location):
    print("get_prefix_location ------------> ", prefix_location)    
    ob_selected = bpy.context.selected_objects
    print("meshes ------------> ", ob_selected)
    for ob in ob_selected:
        ob_name = ob.name
        print("----mesh-----", ob_name)
        for key in prefix_location:
            print("----key-----", key)
            if ob_name.startswith(key):
                print("trovata corrispondenza key ", key)
                obj = bpy.data.objects.get(ob_name)
                if obj:
                    print("trovata obj-key", obj)
                    bpy.context.view_layer.objects.active = obj
                    val = prefix_location[key]
                    print("trovata obj-val", val)
                    
                    # Convertire la stringa 'val' in una tupla
                    try:
                        val_tuple = ast.literal_eval(val)
                        if isinstance(val_tuple, tuple) and len(val_tuple) == 3:
                            obj.location = val_tuple
                            print(f"Oggetto {obj.name} spostato a {val_tuple}")
                        else:
                            print(f"Formato posizione non valido per {val}: deve essere una tupla di tre valori.")
                    except (ValueError, SyntaxError):
                        print(f"Errore nella conversione di {val} in una tupla.")
                else:
                    print(f"Oggetto non trovato: {ob_name}")

                







        
# Esegui la funzione
selected_col, list_location = get_list_selected()
print("return_selected_col ------------> ", selected_col)
print("return_list_location ------------> ", list_location)

list_position = []
for loc in list_location:
    print("type loc ------------> ", type(loc))
    newloc = str(loc)
    newloc = newloc[8:-1]
    list_position.append(newloc)
print("return_list_position ------------> ", list_position)

override_collections(selected_col)

list_prefixes = get_list_prefixes(selected_col)
print("return_list_prefixes ------------> ", list_prefixes)

reselect_objects(list_prefixes)
print("return_list_objects ------------> ")
            
override_selected_object()

prefix_location = {list_prefixes[i]: list_position[i] for i in range(len(list_prefixes))}
print("create_prefix_location ------------> ", prefix_location)

relocate_objects(prefix_location)

""" list_prefixes = override_collections(selected_col)
print("selected_col ------------> ", selected_col) """






