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
        
        
def relocate_objects(prefix_location):
    print("get_prefix_location ------------> ", prefix_location)    
        
        
# Esegui la funzione
selected_col, list_location = get_list_selected()
print("return_selected_col ------------> ", selected_col)
print("return_list_location ------------> ", list_location)


override_collections(selected_col)

list_prefixes = get_list_prefixes(selected_col)
print("return_list_prefixes ------------> ", list_prefixes)


reselect_objects(list_prefixes)
print("return_list_objects ------------> ")


prefix_location = list(zip(list_prefixes, list_location))
print("create_prefix_location ------------> ", prefix_location)
            
override_selected_object()

relocate_objects(prefix_location)

""" list_prefixes = override_collections(selected_col)
print("selected_col ------------> ", selected_col) """


# list_data = override_collections(selected_col)