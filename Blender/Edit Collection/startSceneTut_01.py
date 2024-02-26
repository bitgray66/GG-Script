# give Python access to Blender's functionality
import bpy

# create a variable to set the spacing between object origins
location_offset = 3

# create a row of cubes along the X-axis
for i in range(10):
    bpy.ops.mesh.primitive_cube_add(location=(i * location_offset, 0, 0))

# create a row of icospheres along the X-axis
for i in range(10):
    bpy.ops.mesh.primitive_ico_sphere_add(location=(i * location_offset, 0, location_offset))

# create a row of monkey heads along the X-axis
for i in range(10):
    bpy.ops.mesh.primitive_monkey_add(location=(i * location_offset, 0, 2 * location_offset))