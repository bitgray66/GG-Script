'''
#*************************************************************************

                       Lazy Vault:
                       LAZY UPDATER

#*************************************************************************
Compatibility: Redshift Render Engine (2.48 and above)
Maya: 2020
Python: 2.7
#*************************************************************************
Description: lazy updater

#*************************************************************************
 Author: Laura Siviero
         laura.seav@gmail.com
#*************************************************************************
'''

import maya.cmds as cmds
import os

# FUNCTION:
########################################################################

def update_references():
    selections = cmds.ls (references=True)
    print ("#####################################################################")
    print ("######################## UPDATE REFERENCES ##########################")
    print ("#####################################################################")
    print ("\n")
    
    for selection in selections:
        reference_namespace = selection.split(":")[0] + "RN"
        if reference_namespace.endswith("RNRN"):
            reference_namespace = reference_namespace.replace("RNRN", "RN")
        reference_path_asset = cmds.referenceQuery(selection, filename = True)
        reference_path_folders = reference_path_asset.split("/")[:-1]
        reference_path = ("/").join(reference_path_folders)
        files = os.listdir(reference_path)
        updated_file = files = sorted(files)[-1]
        updated_reference_path = reference_path + "/" + updated_file
        
        if reference_path_asset.endswith("}"):
            reference_path_asset = reference_path_asset[:-3]
        
        if reference_path_asset == updated_reference_path:
            print (reference_namespace[:-2] + " is already updated at latest " + reference_path_folders[-1]+" version")
        
        else:
            cmds.file(updated_reference_path, loadReference=reference_namespace, type="mayaAscii", options="v=0;")
            print (reference_namespace[:-2] + " has been updated at the latest " + reference_path_folders[-1]+" version")
    print ("\n")
    cmds.warning ("DONE! Check the script editor for more details")



def pop_up_check_for_references():
    message = "This action is undoable. A large amount of references can bring down maya. \n\nAre you sure to proceed?"
    answer = cmds.confirmDialog(title="Ready for Export",
                           message=message,
                           button=["Yes", "No"],
                           defaultButton="No",
                           icon="question")
    if answer == "Yes":
        update_references()
    
    else:
        print ("I'll wait until you're ready")
        

# UI
########################################################################


def lazy_updater_ui():
    ui_title = "lazy_updater"
    theme_color = [0.286, 0.286, 0.286]
    analogue_color = [0.2, 0.2, 0.2]
    complementary_color = [0.792, 0.195, 0.203]

    # DELETE if it already exists:
    if cmds.window(ui_title, exists=True):
        cmds.deleteUI(ui_title)

    window = cmds.window(ui_title, title="LAZY UPDATER",
                         backgroundColor=theme_color,
                         resizeToFitChildren=True)
                         
    cmds.columnLayout(adjustableColumn=True)
    cmds.text("Update References:", backgroundColor=theme_color,
              font="boldLabelFont", align="left", height=35, width=300)
    cmds.separator()
    cmds.button('import_setup_planet', label='UPDATE ALL REFERENCES',
                backgroundColor=analogue_color,
                height = 50,
                command="pop_up_check_for_references()")

    
    cmds.showWindow(window)


lazy_updater_ui()