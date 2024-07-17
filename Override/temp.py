import bpy

def override_selected_object():
    # Verifica se un oggetto è selezionato
    selected_objects = bpy.context.selected_objects

    for obj in selected_objects:
        object_name = obj.name
        obj = bpy.data.objects.get(object_name)
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.make_override_library()
        # print(f"Override eseguito per l'oggetto: {obj.name}")
            

# Esegui la funzione
override_selected_object()
