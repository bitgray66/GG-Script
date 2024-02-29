

import bpy

class ConvertEmptyToCollectionOperator(bpy.types.Operator):
    bl_idname = "wm.empty_to_collection"
    bl_label = "Convert Empty to Collection"

    def execute(self, context):
        if len(bpy.context.selected_objects):
            objects = bpy.context.selected_objects
        else:
            objects = get_scene_children()
            
        for o in objects:
            if len(o.users_collection):
                parent_collection = o.users_collection[0]
            else:
                parent_collection = bpy.context.scene.collection
                
            self.empties_to_collections(o, parent_collection)
        return {'FINISHED'}

    def empties_to_collections(self, o, parent_collection):
        children = get_objects_children(o)
        if hasattr(o, 'type') and o.type == 'EMPTY':
            # Create a new collection
            new_collection = bpy.data.collections.new(o.name)
            parent_collection.children.link(new_collection)

            # Move all children into the collection
            for ch in o.children_recursive:
                for old_collection in ch.users_collection:
                    old_collection.objects.unlink(ch)
                new_collection.objects.link(ch)

            bpy.data.objects.remove(o)
            for ch in children:
                self.empties_to_collections(ch, new_collection)
        else:
            for ch in children:
                self.empties_to_collections(ch, parent_collection)

def get_objects_children(obj):
    obs = []
    if hasattr(obj, 'children'):
        obs.extend(obj.children)
    if hasattr(obj, 'objects'):
        obs.extend(obj.objects)
    return obs

def get_scene_children():
    """List of the 'Scene' collection's children."""
    children = []
    for o in bpy.data.objects:
        if hasattr(o, 'parent') and o.parent is None:
            children.append(o)
    return children

bpy.utils.register_class(ConvertEmptyToCollectionOperator)


from pathlib import Path
import bpy

folder = Path(r"C:\Users\luigi.marazzi\Desktop\PRP")
fbx_files = [f for f in folder.glob("**/*.fbx") if f.is_file()]
for fbx_file in fbx_files:
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.import_scene.fbx(filepath=str(fbx_file))
    for obj in bpy.context.selected_objects:
        obj.name = fbx_file.stem
        print(obj)