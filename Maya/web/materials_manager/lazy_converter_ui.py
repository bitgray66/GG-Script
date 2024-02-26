'''
#*************************************************************************

                       Lazy Vault:
                   LAZY CONVERTER MATS

#*************************************************************************
Compatibility: Redshift Render Engine (2.48 and above)
Maya: 2020
Python: 2.7
#*************************************************************************
Description: material from lambert to Vray
             material forma lambert to Redshift

#*************************************************************************
 Author: Laura Siviero
         laura.seav@gmail.com
#*************************************************************************
'''
import maya.cmds as cmds


def convert_material_from_lambert(render_engine):
    selections = cmds.ls(type="lambert")
    if render_engine == "Vray":
        shader_type = "VRayMtl"
        diffuse_parameter = ".color"
        refraction_parameter = ".refractionColor"
    if render_engine == "Redshift":
        shader_type = "RedshiftMaterial"
        diffuse_parameter = ".diffuse_color"

    for selection in selections:
        if selection != "lambert1":

            # GESTIONE/COPIA PARAMETRI:
            R_refraction, G_refraction, B_refraction = cmds.getAttr(
                selection + ".transparency")[0]

            if not cmds.listConnections(selection + ".color", source=True):
                R_diffuse, G_diffuse, B_diffuse = cmds.getAttr(
                    selection + ".color")[0]

            # CREAZIONE MATERIALE E COLLEGAMENTO CON INPUT ENTRATA E USCITA:
            diffuse_input = cmds.listConnections(selection + ".color",
                                                 source=True)
            shading_group = cmds.listConnections(selection,
                                                 type="shadingEngine")[0]
            cmds.delete(selection)
            updated_shader = cmds.shadingNode(shader_type, asShader=True,
                                              name=selection)

            if render_engine == "Vray":
                cmds.setAttr(updated_shader + refraction_parameter,
                             R_refraction, G_refraction, B_refraction,
                             type="double3")

            if render_engine == "Redshift":
                if R_refraction + G_refraction + B_refraction != 0:
                    cmds.setAttr(updated_shader + ".refr_weight",
                                 (R_refraction + G_refraction + B_refraction) / 3)
                    cmds.setAttr(updated_shader + ".diffuse_weight", 0)
                else:
                    cmds.setAttr(updated_shader + ".refl_roughness", 1)

            if diffuse_input:
                cmds.connectAttr(diffuse_input[0] + ".outColor",
                                 updated_shader + diffuse_parameter)
            else:
                cmds.setAttr(updated_shader + diffuse_parameter,
                             R_diffuse, G_diffuse, B_diffuse,
                             type="double3")

            cmds.connectAttr(updated_shader + ".outColor",
                             shading_group + ".surfaceShader")

            print(selection + " has been updated")

    cmds.warning("DONE! All the material have been updated to "
                 + render_engine)


# UI
########################################################################


def lazy_converter_ui():
    ui_title = "lazy_converter_vRay"
    theme_color = [0.286, 0.286, 0.286]
    analogue_color = [0.2, 0.2, 0.2]
    complementary_color = [0.792, 0.195, 0.203]

    # DELETE if it already exists:
    if cmds.window(ui_title, exists=True):
        cmds.deleteUI(ui_title)

    window = cmds.window(ui_title, title="LAZY CONVERTER",
                         backgroundColor=theme_color,
                         resizeToFitChildren=True)

    cmds.columnLayout(adjustableColumn=True)
    cmds.text("Convert to:", backgroundColor=theme_color,
              font="boldLabelFont", align="left", height=35, width=300)
    cmds.separator()
    cmds.button('lazy_converter_button_Redshift', label='Convert lambert to Redshift',
                backgroundColor=analogue_color,
                height=50,
                command="convert_material_from_lambert('Redshift')")
    cmds.setParent("..")
    cmds.rowLayout(numberOfColumns=2,adjustableColumn=1 )
    cmds.button('lazy_converter_button_Vray', label='Convert lambert to Vray',
                backgroundColor=analogue_color,
                width = 250,
                height=50,
                command="convert_material_from_lambert('Vray')")
    cmds.button('lazy_converter_button_documentation', label='Vray Doc',
                backgroundColor=analogue_color,
                height=50,
                command="cmds.launch(web='https://docs.chaos.com/display/VMAYA/VRayMtl')")

    cmds.showWindow(window)


lazy_converter_ui()
