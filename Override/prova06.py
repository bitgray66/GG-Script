
import bpy
from bpy.types import Object, Scene

print("gg01---> ")
print("gg02---> ", bpy.context.area.type)
def make_override_editable():

    for area in bpy.context.screen.areas:
        print("gg03---> ", bpy.context.area.type)
        if area.type == "OUTLINER":
            ctx = bpy.context.copy()
            ctx["area"] = area
            with bpy.context.temp_override(area=area):
                print("gg04---> ",bpy.context.area.type)
                bpy.ops.outliner.liboverride_operation(
                    type="OVERRIDE_LIBRARY_CREATE_HIERARCHY",
                    selection_set="SELECTED_AND_CONTENT",
                )





# Esegui la funzione principale
make_override_editable()