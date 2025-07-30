import bpy
import os
from bl_operators.presets import AddPresetBase
from bl_ui.utils import PresetPanel
from . import utilities

#━━━━━━━━━━━━━━━━━━━
#     Operators     
#━━━━━━━━━━━━━━━━━━━

# ----------------------------------------------
#     Operator for Opening Preset Directory     
# ----------------------------------------------

class OpenPresetDirectoryOperator(bpy.types.Operator):
    bl_idname = "opr.open_preset_directory"
    bl_label = "Open Preset Directory"

    def execute(self, context):
        # Get the list of preset paths
        preset_paths = bpy.utils.preset_paths("IK-FK_Snapping_Tool") 
        # Select the first path from the list (usually the user's preset directory)
        if preset_paths:
            preset_path = preset_paths[0]
            # Open the directory
            bpy.ops.wm.path_open(filepath=preset_path)
        else:
            self.report({'ERROR'}, "Preset directory not found")
        return {'FINISHED'}

# ----------------------------------
#     Operators for Preset Menu     
# ----------------------------------

# --- Preset menu operator ---
class Preset_Menu(bpy.types.Menu): 
    bl_label = 'Preset Menu' 
    bl_idname = 'PRESET_MT_menu'
    # Subdirectory within the preset folder to store limb presets
    preset_subdir = 'IK-FK_Snapping_Tool'
    # Operator to execute when a preset is selected from the menu
    preset_operator = 'script.execute_preset'
    # Use the default draw function for preset menus
    draw = bpy.types.Menu.draw_preset

# --- Preset panel operator ---
class PRESET_PT_Panel(PresetPanel, bpy.types.Panel):
    bl_label = 'Preset panel'
    # Subdirectory within the preset folder to store limb presets
    preset_subdir = 'IK-FK_Snapping_Tool'
    # Operator to execute when a preset is selected from the panel
    preset_operator = 'script.execute_preset'
    # Operator to add a new preset to the menu/panel
    preset_add_operator = 'opr.presetadd'

# -----------------------------------------------
#     Operators for Snapping Actions (Arm L)     
# -----------------------------------------------

# --- Arm L IK to FK operator ---
class ArmL_IKtoFK(bpy.types.Operator):
    bl_idname = 'opr.arml_ikfk'
    bl_label = 'Snap to FK'

    def execute(self, context):
        # Retrieve the names of the relevant bones from scene properties
        bone_names = [
            context.scene.IK_Arm_Pole_Target_L,
            context.scene.IK_Arm_Target_L,
            context.scene.FK_Arm_End_L,
            context.scene.IK_Arm_Pole_L,
            context.scene.IK_Arm_Control_L,
            context.scene.IK_Arm_End_L
        ]
        # Get the bone objects and perform error checking
        bones = utilities.get_bones_with_check(context, bone_names)
        if not bones:
            # Report an error if any bone is missing or invalid
            self.report({'ERROR'}, "Missing or invalid bone names for Arm L IK-FK snapping")
            return {'CANCELLED'}
        # Perform the IK to FK snapping using the retrieved bone objects
        utilities.snap_IK_to_FK(*bones)
        return {'FINISHED'}

# --- Arm L FK to IK operator ---
class ArmL_FKtoIK(bpy.types.Operator):
    bl_idname = 'opr.arml_fkik'
    bl_label = 'Snap to IK'

    def execute(self, context):
        # Retrieve the names of the relevant bones from scene properties
        bone_names = [
            context.scene.IK_Arm_Upper_L,
            context.scene.IK_Arm_Lower_L,
            context.scene.IK_Arm_End_L,
            context.scene.FK_Arm_Upper_L,
            context.scene.FK_Arm_Lower_L,
            context.scene.FK_Arm_End_L
        ]
        # Get the bone objects and perform error checking
        bones = utilities.get_bones_with_check(context, bone_names)
        if not bones:
            # Report an error if any bone is missing or invalid
            self.report({'ERROR'}, "Missing or invalid bone names for Arm L FK-IK snapping")
            return {'CANCELLED'}
        # Perform the IK to FK snapping using the retrieved bone objects
        utilities.snap_FK_to_IK(*bones)
        return {'FINISHED'}

# -----------------------------------------------
#     Operators for Snapping Actions (Arm R)     
# -----------------------------------------------

# --- Arm R IK to FK operator ---
class ArmR_IKtoFK(bpy.types.Operator):
    bl_idname = 'opr.armr_ikfk'
    bl_label = 'Snap to FK'

    def execute(self, context):
        # Retrieve the names of the relevant bones from scene properties
        bone_names = [
            context.scene.IK_Arm_Pole_Target_R,
            context.scene.IK_Arm_Target_R,
            context.scene.FK_Arm_End_R,
            context.scene.IK_Arm_Pole_R,
            context.scene.IK_Arm_Control_R,
            context.scene.IK_Arm_End_R
        ]
        # Get the bone objects and perform error checking
        bones = utilities.get_bones_with_check(context, bone_names)
        if not bones:
            # Report an error if any bone is missing or invalid
            self.report({'ERROR'}, "Missing or invalid bone names for Arm R IK-FK snapping")
            return {'CANCELLED'}
        # Perform the IK to FK snapping using the retrieved bone objects
        utilities.snap_IK_to_FK(*bones)
        return {'FINISHED'}

# --- Arm R FK to IK operator ---
class ArmR_FKtoIK(bpy.types.Operator):
    bl_idname = 'opr.armr_fkik'
    bl_label = 'Snap to IK'

    def execute(self, context):
        # Retrieve the names of the relevant bones from scene properties
        bone_names = [
            context.scene.IK_Arm_Upper_R,
            context.scene.IK_Arm_Lower_R,
            context.scene.IK_Arm_End_R,
            context.scene.FK_Arm_Upper_R,
            context.scene.FK_Arm_Lower_R,
            context.scene.FK_Arm_End_R
        ]
        # Get the bone objects and perform error checking
        bones = utilities.get_bones_with_check(context, bone_names)
        if not bones:
            # Report an error if any bone is missing or invalid
            self.report({'ERROR'}, "Missing or invalid bone names for Arm R FK-IK snapping")
            return {'CANCELLED'}
        # Perform the IK to FK snapping using the retrieved bone objects
        utilities.snap_FK_to_IK(*bones)
        return {'FINISHED'}

# -----------------------------------------------
#     Operators for Snapping Actions (Leg L)     
# -----------------------------------------------

# --- Leg L IK to FK operator ---
class LegL_IKtoFK(bpy.types.Operator):
    bl_idname = 'opr.legl_ikfk'
    bl_label = 'Snap to FK'

    def execute(self, context):
        # Retrieve the names of the relevant bones from scene properties
        bone_names = [
            context.scene.IK_Leg_Pole_Target_L,
            context.scene.IK_Leg_Target_L,
            context.scene.FK_Leg_Knee_L,
            context.scene.TWEAK_Leg_Knee_L,
            context.scene.FK_Leg_Lower_L,
            context.scene.FK_Leg_End_L,
            context.scene.IK_Leg_Pole_L,
            context.scene.IK_Leg_Control_L,
            context.scene.IK_Leg_Knee_L,
            context.scene.IK_Leg_End_L,
            context.scene.IK_Leg_Lower_L,
            context.scene.TWEAK_Leg_Lower_L
        ]
        # Get the bone objects and perform error checking
        bones = utilities.get_bones_with_check(context, bone_names)
        if not bones:
            # Report an error if any bone is missing or invalid
            self.report({'ERROR'}, "Missing or invalid bone names for Leg L IK-FK snapping")
            return {'CANCELLED'}
        # Perform the IK to FK snapping using the retrieved bone objects
        utilities.snap_IK_to_FK_knee(*bones)
        return {'FINISHED'}

# --- Leg L FK to IK operator ---
class LegL_FKtoIK(bpy.types.Operator):
    bl_idname = 'opr.legl_fkik'
    bl_label = 'Snap to IK'

    def execute(self, context):
        # Retrieve the names of the relevant bones from scene properties
        bone_names = [
            context.scene.IK_Leg_Upper_L,
            context.scene.IK_Leg_Knee_L,
            context.scene.TWEAK_Leg_Knee_L,
            context.scene.IK_Leg_Lower_L,
            context.scene.TWEAK_Leg_Lower_L,
            context.scene.IK_Leg_End_L,
            context.scene.FK_Leg_Upper_L,
            context.scene.FK_Leg_Knee_L,
            context.scene.FK_Leg_Lower_L,
            context.scene.FK_Leg_End_L 
        ]
        # Get the bone objects and perform error checking
        bones = utilities.get_bones_with_check(context, bone_names)
        if not bones:
            # Report an error if any bone is missing or invalid
            self.report({'ERROR'}, "Missing or invalid bone names for Leg L FK-IK snapping")
            return {'CANCELLED'}
        # Perform the IK to FK snapping using the retrieved bone objects
        utilities.snap_FK_to_IK_knee(*bones)
        return {'FINISHED'}

# -----------------------------------------------
#     Operators for Snapping Actions (Leg R)     
# -----------------------------------------------

# --- Leg R IK to FK operator ---
class LegR_IKtoFK(bpy.types.Operator):
    bl_idname = 'opr.legr_ikfk'
    bl_label = 'Snap to FK'

    def execute(self, context):
        # Retrieve the names of the relevant bones from scene properties
        bone_names = [
            context.scene.IK_Leg_Pole_Target_R,
            context.scene.IK_Leg_Target_R,
            context.scene.FK_Leg_Knee_R,
            context.scene.TWEAK_Leg_Knee_R,
            context.scene.FK_Leg_Lower_R,
            context.scene.FK_Leg_End_R,
            context.scene.IK_Leg_Pole_R, 
            context.scene.IK_Leg_Control_R,
            context.scene.IK_Leg_Knee_R,
            context.scene.IK_Leg_Lower_R,
            context.scene.IK_Leg_End_R,
            context.scene.TWEAK_Leg_Lower_R
        ]
        # Get the bone objects and perform error checking
        bones = utilities.get_bones_with_check(context, bone_names)
        if not bones:
            # Report an error if any bone is missing or invalid
            self.report({'ERROR'}, "Missing or invalid bone names for Leg R IK-FK snapping")
            return {'CANCELLED'}
        # Perform the IK to FK snapping using the retrieved bone objects
        utilities.snap_IK_to_FK_knee(*bones)
        return {'FINISHED'}

# --- Leg R FK to IK operator ---
class LegR_FKtoIK(bpy.types.Operator):
    bl_idname = 'opr.legr_fkik'
    bl_label = 'Snap to IK'

    def execute(self, context):
        # Retrieve the names of the relevant bones from scene properties
        bone_names = [
            context.scene.IK_Leg_Upper_R,
            context.scene.IK_Leg_Knee_R,
            context.scene.TWEAK_Leg_Knee_R,
            context.scene.IK_Leg_Lower_R,
            context.scene.TWEAK_Leg_Lower_R,
            context.scene.IK_Leg_End_R,
            context.scene.FK_Leg_Upper_R,
            context.scene.FK_Leg_Knee_R,
            context.scene.FK_Leg_Lower_R,
            context.scene.FK_Leg_End_R 
        ]
        # Get the bone objects and perform error checking
        bones = utilities.get_bones_with_check(context, bone_names)
        if not bones:
            # Report an error if any bone is missing or invalid
            self.report({'ERROR'}, "Missing or invalid bone names for Leg R FK-IK snapping")
            return {'CANCELLED'}
        # Perform the IK to FK snapping using the retrieved bone objects
        utilities.snap_FK_to_IK_knee(*bones)
        return {'FINISHED'}

# -----------------------------------------
#     Operator for Adding Limb Presets     
# -----------------------------------------

class PresetAdd(AddPresetBase, bpy.types.Operator):
    bl_idname = 'opr.presetadd'
    bl_label = 'Add A preset'
    # Specify the preset menu where the new preset will be added
    preset_menu = 'PRESET_MT_menu'
    preset_defines = [
                        'obj = bpy.context.object',
                        'scene = bpy.context.scene'
                     ]
    # Specify the values to be stored in the preset
    preset_values = [
                        'scene.FK_Arm_Upper_L',
                        'scene.FK_Arm_Lower_L',
                        'scene.FK_Arm_End_L',
                        'scene.IK_Arm_Upper_L',
                        'scene.IK_Arm_Lower_L',
                        'scene.IK_Arm_End_L',
                        'scene.IK_Arm_Control_L',
                        'scene.IK_Arm_Pole_L',
                        'scene.IK_Arm_Target_L',
                        'scene.IK_Arm_Pole_Target_L',
                        'scene.FK_Arm_Upper_R',
                        'scene.FK_Arm_Lower_R',
                        'scene.FK_Arm_End_R',
                        'scene.IK_Arm_Upper_R',
                        'scene.IK_Arm_Lower_R',
                        'scene.IK_Arm_End_R',
                        'scene.IK_Arm_Control_R',
                        'scene.IK_Arm_Pole_R',
                        'scene.IK_Arm_Target_R',
                        'scene.IK_Arm_Pole_Target_R',
                        'scene.FK_Leg_Upper_L',
                        'scene.FK_Leg_Knee_L',
                        'scene.FK_Leg_Lower_L',
                        'scene.FK_Leg_End_L',
                        'scene.IK_Leg_Upper_L',
                        'scene.IK_Leg_Knee_L',
                        'scene.TWEAK_Leg_Knee_L',
                        'scene.IK_Leg_Lower_L',
                        'scene.TWEAK_Leg_Lower_L',
                        'scene.IK_Leg_End_L',
                        'scene.IK_Leg_Control_L',
                        'scene.IK_Leg_Pole_L',
                        'scene.IK_Leg_Target_L',
                        'scene.IK_Leg_Pole_Target_L',
                        'scene.FK_Leg_Upper_R',
                        'scene.FK_Leg_Knee_R',
                        'scene.TWEAK_Leg_Knee_R',
                        'scene.FK_Leg_Lower_R',
                        'scene.TWEAK_Leg_Lower_R',
                        'scene.FK_Leg_End_R',
                        'scene.IK_Leg_Upper_R',
                        'scene.IK_Leg_Knee_R',
                        'scene.IK_Leg_Lower_R',
                        'scene.IK_Leg_End_R',
                        'scene.IK_Leg_Control_R',
                        'scene.IK_Leg_Pole_R',
                        'scene.IK_Leg_Target_R',
                        'scene.IK_Leg_Pole_Target_R'
                    ]
    # Subdirectory within the preset folder to store limb presets
    preset_subdir = 'IK-FK_Snapping_Tool'

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#     Register & Unregister     
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

classes = [
    OpenPresetDirectoryOperator,
    Preset_Menu,
    PRESET_PT_Panel,
    ArmL_IKtoFK,
    ArmL_FKtoIK,
    ArmR_IKtoFK,
    ArmR_FKtoIK,
    LegL_IKtoFK,
    LegL_FKtoIK,
    LegR_IKtoFK,
    LegR_FKtoIK,
    PresetAdd
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
