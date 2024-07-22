import bpy

def override_linked_datablock(object_name):
    # Trova l'oggetto linkato
    obj = bpy.data.objects.get(object_name)
    if obj and obj.library:
        # Esegui l'override
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.make_override_library()

# Esempio di utilizzo
override_linked_datablock("NameOfLinkedObject")

######################

import bpy

def add_suffix_to_data_blocks(list_prefix, suffix="_OK"):
    for data_block in bpy.data.objects:
        for prefix in list_prefix:
            if data_block.name.startswith(prefix):
                data_block.name = data_block.name + suffix

# Esempio di utilizzo
list_prefix = ['MM_PRP_Backpack_A_A', 'MM_PRP_Bagpipe_A_A']
add_suffix_to_data_blocks(list_prefix)



######################

import bpy
print("@@@@@@@@@@@@@########xxxxxxxxxxxxxxxxxx########@@@@@@@@@@@@@")

area = next(area for area in bpy.context.window.screen.areas if area.type == 'OUTLINER')

with bpy.context.temp_override(
    window=bpy.context.window,
    area=area,
    region=next(region for region in area.regions if region.type == 'WINDOW'),
    screen=bpy.context.window.screen
):
    #over_sel_collections_and_data()

    def over_sel_collections_and_data():
        print("------context------> ", bpy.context)
        selected_objects = bpy.context.selected_objects[:]
        print("------selected_objects------> ", selected_objects)
        #list_assets = ["a", "b", "c"]
        list_assets = []
        for col in selected_objects:
            cleaned_name = col.name.replace('_COL', '')
            print(f"cleaned_name: {cleaned_name}")
            list_assets.append(cleaned_name)
            print(f"list_assets: {list_assets}")
            col_name = col.name  # Memorizza il nome dell'oggetto
            bpy.ops.outliner.liboverride_operation(type="OVERRIDE_LIBRARY_CREATE_HIERARCHY", selection_set="SELECTED_AND_CONTENT")
            print(f"Override applicato per la collection: {col_name}")
  
            


        return list_assets


    def main():
        # Ottieni le collection selezionate
        list_assets = over_sel_collections_and_data()
        
        if not list_assets:
            print("Nessuna lista pervenuta.")
        else:
            # Applica l'override alle collection selezionate
            #override_collections(selected_collections)
            print(f"OK lista pervenuta: {list_assets}")
            global new_list_assets
            new_list_assets = list_assets
           
        print(f"OK new_list_assets creata !!!: {new_list_assets}")



        
    # Esegui la funzione principale
    main()


    

    