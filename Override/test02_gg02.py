import bpy
print("@@@@@@@@@@@@@########xxxxxxxxxxxxxxxxxx########@@@@@@@@@@@@@")

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
        #list_prefix = ["a", "b", "c"]
        list_prefix = []
        for col in selected_col:
            cleaned_name = col.name.replace('_COL', '')
            print(f"cleaned_name: {cleaned_name}")
            list_prefix.append(cleaned_name)
            print(f"list_prefix: {list_prefix}")
            col_name = col.name  # Memorizza il nome dell'oggetto
            bpy.ops.outliner.liboverride_operation(type="OVERRIDE_LIBRARY_CREATE_HIERARCHY", selection_set="SELECTED_AND_CONTENT")
            print(f"Override applicato per la collection: {col_name}")

            # Verifica se un oggetto è selezionato
            selected_objects = bpy.context.selected_objects
            if not selected_objects:
                print("Nessun oggetto selezionato")
                return
            
            # Prendi il primo oggetto selezionato
            obj = selected_objects[0]
            
            bpy.ops.object.make_override_library()
            
        return list_prefix


        """     def get_all_objects(list_prefix):
                list_obj = []
                for pref in list_prefix:
                    for obj in bpy.context.scene.objects:
                        if obj.name.startswith("pad"):
                            obj.select_set(True)
                            list_obj.append()

                return """
    



    def main():
        # Ottieni le collection selezionate
        list_prefix = over_sel_collections()
        
        if not list_prefix:
            print("Nessuna lista pervenuta.")
        else:
            # Applica l'override alle collection selezionate
            #override_collections(selected_collections)
            print(f"OK lista pervenuta: {list_prefix}")
            global new_list_prefix
            new_list_prefix = list_prefix
           
        print(f"OK new_list_prefix creata !!!: {new_list_prefix}")



        
    # Esegui la funzione principale
    main()


    

    