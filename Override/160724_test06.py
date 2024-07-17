import bpy
import time
print("@@@@@@@@@@@@@########xxxxxxxxxxxxxxxxxx########@@@@@@@@@@@@@")




def over_col_selected(new_list_prefix):
    collections = bpy.data.collections
    for collection in collections:
        for prefix in new_list_prefix:
            if collection.name.startswith(prefix):
                obj = bpy.data.objects.get(collection.name)
                bpy.context.view_layer.objects.active = obj
                bpy.ops.object.make_override_library()
                #time.sleep(0.1)
                #obj.select_set(True)
                #bpy.ops.object.make_override_library()
                """ if collection.library:
                    print(f"Override eseguito per l'oggetto: {collection.name}")
                else:
                    print(f"L'oggetto {collection.name} non è un oggetto collegato (linked object)") """

               # print("Collection_extra:", collection.name)
    


area = next(area for area in bpy.context.window.screen.areas if area.type == 'OUTLINER')

with bpy.context.temp_override(
    window=bpy.context.window,
    area=area,
    region=next(region for region in area.regions if region.type == 'WINDOW'),
    screen=bpy.context.window.screen
):
    #over_sel_collections()

    def over_sel_collections():
        print("------context------> ", bpy.context)
        selected_col = bpy.context.selected_objects[:]
        print("------selected_col------> ", selected_col)

        list_prefix = []

        for col in selected_col:
            cleaned_name = col.name.replace('_COL', '')
            print(f"cleaned_name: {cleaned_name}")
            list_prefix.append(cleaned_name)
            print(f"list_prefix: {list_prefix}")
            # col_name = col.name  # Memorizza il nome dell'oggetto
            # bpy.ops.outliner.liboverride_operation(type="OVERRIDE_LIBRARY_CREATE_HIERARCHY", selection_set="SELECTED_AND_CONTENT")
            # print(f"Override applicato per la collection: {col_name}")
            
        return list_prefix



    



    def main():
        # Ottieni le collection selezionate
        list_prefix = over_sel_collections()
        
        if not list_prefix:
            print("Nessuna lista pervenuta.")
        else:
            print(f"OK lista pervenuta: {list_prefix}")
            global new_list_prefix
            new_list_prefix = list_prefix


        print(f"OK new_list_prefix creata !!!: {new_list_prefix}")

        over_col_selected(new_list_prefix)


        
    # Esegui la funzione principale
    main()


    

    