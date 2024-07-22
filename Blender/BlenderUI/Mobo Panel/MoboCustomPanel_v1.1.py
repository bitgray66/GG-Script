
from typing import Set
import bpy
import os
from bpy.types import Context
import ast


class CAT_OT_RenameDataOperator(bpy.types.Operator):
    bl_label = "Rename Data"
    bl_idname = "cat.rename_data"

    def execute(self, context):

        MoboType = [
            'CURVE', 'MESH', 'CAMERA', 'CURVE', 'LIGHT',
            'GPENCIL', 'META', 'VOLUME', 'FONT', 'SPEAKER',
            'LATTICE', 'ARMATURE', 'LIGHT_PROBE', 'CURVES'
        ]


        for obj in bpy.context.selected_objects:
            if obj.type in MoboType:
                obj.data.name = obj.name

        return {"FINISHED"}


class CAT_OT_DeletAllOrphan(bpy.types.Operator):
    bl_label = "Delete Orphan"
    bl_idname = "cat.delete_orphan"

    def execute(self, context):

        for obj in bpy.data.objects:
            bpy.data.objects.remove(obj, do_unlink=True)


        for mesh in bpy.data.meshes:
            bpy.data.meshes.remove(mesh, do_unlink=True)


        for coll in bpy.data.collections:
            bpy.data.collections.remove(coll)


        for mat in bpy.data.materials:
            bpy.data.materials.remove(mat, do_unlink=True)

        return {"FINISHED"}


class CAT_OT_Override(bpy.types.Operator):
    bl_label = "Override Obj"
    bl_idname = "cat.over_objects"

    @staticmethod
    def get_list_selected():

        try:
            list_selected = bpy.context.selected_objects
            selected_col = [o.name for o in list_selected]

            list_location = [obj.location for obj in list_selected]

            return selected_col, list_location
        except Exception as e:
            print(f"Errore in get_list_selected: {e}")
            return [], []

    @staticmethod
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

    @staticmethod
    def get_list_prefixes(selected_col):

        try:
            list_prefixes = [item.replace('_COL', '') for item in selected_col]
            return list_prefixes
        except Exception as e:
            print(f"Errore in get_list_prefixes: {e}")
            return []

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    def execute(self, context):

        try:
            selected_col, list_location = self.get_list_selected()

            list_position = [str(loc)[8:-1] for loc in list_location]

            self.override_collections(selected_col)

            list_prefixes = self.get_list_prefixes(selected_col)

            self.reselect_objects(list_prefixes)

            self.override_selected_object()

            prefix_location = {list_prefixes[i]: list_position[i] for i in range(len(list_prefixes))}

            self.relocate_objects(prefix_location)
        except Exception as e:
            print(f"Errore nell'esecuzione principale: {e}")

        return {"FINISHED"}


class VIEW3D_PT_MoboPanel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = 'Mobo'
    bl_label = "Mobo Scripts"
    bl_idname = "VIEW3D_PT_MoboPanel"

    def draw(self, context):
        layout = self.layout


        row = layout.row(align=True)
        row.operator("cat.rename_data", text="Rename Data")
        row.separator()
        row.operator("cat.delete_orphan", text="Delete Orphan")


        layout.separator()
        

        row = layout.row(align=True)
        row.operator("cat.over_objects", text="Override OBJ")
        row.separator()



classes = (
    CAT_OT_RenameDataOperator,
    CAT_OT_DeletAllOrphan,
    CAT_OT_Override,
    VIEW3D_PT_MoboPanel,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
