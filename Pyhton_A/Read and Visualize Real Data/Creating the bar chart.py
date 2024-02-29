import bpy

# read data
filepath = r'C:\Works\GG-Script\Pyhton_A\tutorial.txt'
data = dict() # è come scrivere data{}
with open(filepath, 'r') as txt_file:
    #print(txt_file.readlines())
    for idx, line in enumerate(txt_file.readlines()): # uso un ulteriore key(idx) perchè essendoci nel txt chiavi doppie verrebbero sovrascritte vedi # esempio01
        # print(line)
        if idx > 0:
            line = line.rstrip('\n')
            #print(line)
            # test = line.split(',')
            # print(test)
            day = line.split(',')[0]
            hours_worked = line.split(',')[1]
            # print(day, hours_worked)
            # data[day] = hours_worked # esempio01 - questo data conterrà solo l'ultima settimana perche le key uguali ferranno sempre sovrascritte
            data[idx] = {
                'label' : day,
                'value' : hours_worked,
            }
# print(data)
            

# Cleanup scene
for obj in bpy.data.objects:
    bpy.data.objects.remove(obj)

# Visualize data
for idx, data_entry in enumerate(data): #   enumerate ci sblocca l'uso di idx univoco
    print(data[data_entry])
    # create bar
    heigth = float(data[data_entry]['value']) # aggiungo float perchè i nostro value lo vediamo in print come numero ma è una stringa
    # print(value)
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, idx, 0))
    bpy.ops.transform.resize(value=(1, 1, heigth), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
    bpy.ops.transform.translate(value=(0, 0, heigth*0.5), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)

  