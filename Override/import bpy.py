import bpy
import time
print("----------------------------------------------------------------------------------------------------------- ")

def get_selected():
    print("------context------> ", bpy.context)
    selected_objects = bpy.context.selected_objects
    print("------selected_objects------> ", selected_objects)
    list_selected = [o.name for o in selected_objects]
    print("------------> ", list_selected)

    return list_selected

def over_collections(list_selected):
    print(f"DEF list_selected pervenuta: {list_selected}")
    for sel in list_selected:
        bpy.ops.outliner.liboverride_operation(type="OVERRIDE_LIBRARY_CREATE_HIERARCHY", selection_set="SELECTED_AND_CONTENT")
        print(f"Override applicato per la collection: {sel}")

def over_objects(list_names):
    print(f"DEF list_names pervenuta: {list_names}")
    meshes = bpy.data.meshes

    for me in meshes:
        me_name = me.name
        print("----me-----", me_name)
        for item in list_names:
            print("----item-----", item)
            # check if the message starts with item
            if me_name.startswith(item):
                print("trovata corrispondenza ", item)
                obj = bpy.data.objects.get(me_name)
                bpy.context.view_layer.objects.active = obj
                bpy.ops.object.make_override_library()
                #print(f"Override eseguito per l'oggetto: {obj.name}")

    oggetti = "gigi"
    return oggetti
    



area = next(area for area in bpy.context.window.screen.areas if area.type == 'OUTLINER')

with bpy.context.temp_override(
    window=bpy.context.window,
    area=area,
    region=next(region for region in area.regions if region.type == 'WINDOW'),
    screen=bpy.context.window.screen
):

    def main():
        # Ottieni le collection selezionate
        list_selected = get_selected()

        if not list_selected:
            print("Nessuna lista pervenuta.")
        else:
            print(f"OK lista selected pervenuta: {list_selected}")

            list_selected_cleaned =[]
            for aaa in list_selected:
                cleaned_name = aaa.replace('_COL', '')
                print(f"cleaned_name: {aaa}")
                list_selected_cleaned.append(cleaned_name)

            print(f"OK list_selected_cleaned: {list_selected_cleaned}")   
          
            global list_names
            list_names = list_selected_cleaned
            print(f"OK list_names: {list_names}")

            over_collections(list_selected)

            print('Sleep time:', str(3), 'seconds')
            time.sleep(20)
            print('Woke up after:', str(3), 'seconds')

            oggetti = over_objects(list_names)
            print(f"OK oggetti: {oggetti}")

    # Esegui la funzione principale
    main()