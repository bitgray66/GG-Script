# give Python access to Blender's functionality
import bpy

# Note: make sure to run this script start_scene_collection_exercises.py https://gist.github.com/CGArtPython/8adc0c15813684db465a359313060164
# before executing the rest of this script

col_name = "monkeys"
collection = bpy.data.collections.new(name=col_name)

# if you didn't create a variable
collection = bpy.data.collections['monkeys']

# retrieve the scene collection
scene_collection = bpy.context.scene.collection

# link the new collection into the scene
scene_collection.children.link(collection)

# get the active object
obj = bpy.context.active_object

# add the object into the collection called "monkeys"
collection.objects.link(obj)

# unlink the active object from the original collection it was added to
bpy.data.collections['Collection'].objects.unlink(obj)


# move the rest of the monkey meshes into the collection called "monkeys"
source_collection = bpy.data.collections['Collection']
destination_collection = collection

# loop over all the objects in the scene
for obj in bpy.data.objects:

    # filter only the objects that have a name that starts with "Suz", this will select only the Suzanne objects
    if "Suz" in obj.name:
        source_collection.objects.unlink(obj)
        destination_collection.objects.link(obj)

# exercise #1 
# move the Ico Spheres add Cubes into their own collection

destination_collection = bpy.data.collections.new(name="cubes")
scene_collection.children.link(destination_collection)

for obj in bpy.data.objects:
    if "Cube" in obj.name:
        source_collection.objects.unlink(obj)
        destination_collection.objects.link(obj)

destination_collection = bpy.data.collections.new(name="icospheres")
scene_collection.children.link(destination_collection)

for obj in bpy.data.objects:
    if "Ico" in obj.name:
        source_collection.objects.unlink(obj)
        destination_collection.objects.link(obj)

# exercise #2
# move all the new collections under a new collection called "objects"

destination_collection = bpy.data.collections.new(name="objects")
scene_collection.children.link(destination_collection)

cube_collection = bpy.data.collections["cubes"]
ico_collection = bpy.data.collections["icospheres"]
monkey_collection = bpy.data.collections["monkeys"]

destination_collection.children.link(cube_collection)
scene_collection.children.unlink(cube_collection)

destination_collection.children.link(ico_collection)
scene_collection.children.unlink(ico_collection)

destination_collection.children.link(monkey_collection)
scene_collection.children.unlink(monkey_collection)