import bpy
from bl_operators.presets import AddPresetBase
from bl_ui.utils import PresetPanel

#━━━━━━━━━━━━━━━━━━━
#     Operators     
#━━━━━━━━━━━━━━━━━━━

# Preset menu operator
class PresetMenu(bpy.types.Menu): 
    bl_label = 'Limb Presets' 
    bl_idname = 'opr.presetmenu'
    preset_subdir = 'IK-FK_Snapping_Tool/Armature_&_Bones_Presets'
    preset_operator = 'script.execute_preset' 
    draw = bpy.types.Menu.draw_preset

# Preset panel operator
class PresetPanel(PresetPanel, bpy.types.Panel):
    bl_label = 'Limb Presets'
    preset_subdir = 'IK-FK_Snapping_Tool/Armature_&_Bones_Presets'
    preset_operator = 'script.execute_preset'
    preset_add_operator = 'opr.presetadd'

# Arm L IK to FK operator
class ArmL_IKtoFK(bpy.types.Operator):
    bl_idname = 'opr.arml_ikfk'
    bl_label = 'Snap to FK'

    def execute(self, context):
        arma = bpy.data.objects[context.scene.armature_name]
        self.snap_IK_to_FK(
            arma.pose.bones[context.scene.IK_Arm_Pole_Target_L],
            arma.pose.bones[context.scene.IK_Arm_Target_L],
            arma.pose.bones[context.scene.FK_Arm_End_L],
            arma.pose.bones[context.scene.IK_Arm_Pole_L],
            arma.pose.bones[context.scene.IK_Arm_Effector_L],
            arma.pose.bones[context.scene.IK_Arm_End_L],
        )
            
        return {'FINISHED'}
    
    def snap_IK_to_FK(self, IK_pole_target, IK_target, FK_end, IK_pole, IK_effector, IK_end):
        IK_pole.matrix = IK_pole_target.matrix
        bpy.context.view_layer.update()
        
        IK_effector.matrix = IK_target.matrix
        bpy.context.view_layer.update()
        
        IK_relative_to_FK = FK_end.bone.matrix_local.inverted() @ IK_end.bone.matrix_local
        IK_end.matrix = FK_end.matrix @ IK_relative_to_FK

# Arm L FK to IK operator
class ArmL_FKtoIK(bpy.types.Operator):
    bl_idname = 'opr.arml_fkik'
    bl_label = 'Snap to IK'

    def execute(self, context):
        arma = bpy.data.objects[context.scene.armature_name]
        self.snap_FK_to_IK(
            arma.pose.bones[context.scene.IK_Arm_Upper_L],
            arma.pose.bones[context.scene.IK_Arm_Lower_L],
            arma.pose.bones[context.scene.IK_Arm_End_L],
            arma.pose.bones[context.scene.FK_Arm_Upper_L],
            arma.pose.bones[context.scene.FK_Arm_Lower_L],
            arma.pose.bones[context.scene.FK_Arm_End_L],
        )
            
        return {'FINISHED'}
    
    def snap_FK_to_IK(self, IK_upper, IK_lower, IK_end, FK_upper, FK_lower, FK_end):
        FK_upper.matrix = IK_upper.matrix
        bpy.context.view_layer.update()
        
        FK_lower.matrix = IK_lower.matrix
        bpy.context.view_layer.update()
        
        FK_relative_to_IK = IK_end.bone.matrix_local.inverted() @ FK_end.bone.matrix_local
        FK_end.matrix = IK_end.matrix @ FK_relative_to_IK

# Arm R IK to FK operator
class ArmR_IKtoFK(bpy.types.Operator):
    bl_idname = 'opr.armr_ikfk'
    bl_label = 'Snap to FK'

    def execute(self, context):
        arma = bpy.data.objects[context.scene.armature_name]
        self.snap_IK_to_FK(
            arma.pose.bones[context.scene.IK_Arm_Pole_Target_R],
            arma.pose.bones[context.scene.IK_Arm_Target_R],
            arma.pose.bones[context.scene.FK_Arm_End_R],
            arma.pose.bones[context.scene.IK_Arm_Pole_R],
            arma.pose.bones[context.scene.IK_Arm_Effector_R],
            arma.pose.bones[context.scene.IK_Arm_End_R],
        )
            
        return {'FINISHED'}
    
    def snap_IK_to_FK(self, IK_pole_target, IK_target, FK_end, IK_pole, IK_effector, IK_end):
        IK_pole.matrix = IK_pole_target.matrix
        bpy.context.view_layer.update()
        
        IK_effector.matrix = IK_target.matrix
        bpy.context.view_layer.update()
        
        IK_relative_to_FK = FK_end.bone.matrix_local.inverted() @ IK_end.bone.matrix_local
        IK_end.matrix = FK_end.matrix @ IK_relative_to_FK

# Arm R FK to IK operator
class ArmR_FKtoIK(bpy.types.Operator):
    bl_idname = 'opr.armr_fkik'
    bl_label = 'Snap to IK'

    def execute(self, context):
        arma = bpy.data.objects[context.scene.armature_name]
        self.snap_FK_to_IK(
            arma.pose.bones[context.scene.IK_Arm_Upper_R],
            arma.pose.bones[context.scene.IK_Arm_Lower_R],
            arma.pose.bones[context.scene.IK_Arm_End_R],
            arma.pose.bones[context.scene.FK_Arm_Upper_R],
            arma.pose.bones[context.scene.FK_Arm_Lower_R],
            arma.pose.bones[context.scene.FK_Arm_End_R],
        )
            
        return {'FINISHED'}
    
    def snap_FK_to_IK(self, IK_upper, IK_lower, IK_end, FK_upper, FK_lower, FK_end):
        FK_upper.matrix = IK_upper.matrix
        bpy.context.view_layer.update()
        
        FK_lower.matrix = IK_lower.matrix
        bpy.context.view_layer.update()
        
        FK_relative_to_IK = IK_end.bone.matrix_local.inverted() @ FK_end.bone.matrix_local
        FK_end.matrix = IK_end.matrix @ FK_relative_to_IK

# Leg L IK to FK operator
class LegL_IKtoFK(bpy.types.Operator):
    bl_idname = 'opr.legl_ikfk'
    bl_label = 'Snap to FK'

    def execute(self, context):
        arma = bpy.data.objects[context.scene.armature_name]
        self.snap_IK_to_FK(
            arma.pose.bones[context.scene.IK_Leg_Pole_Target_L],
            arma.pose.bones[context.scene.IK_Leg_Target_L],
            arma.pose.bones[context.scene.FK_Leg_End_L],
            arma.pose.bones[context.scene.IK_Leg_Pole_L],
            arma.pose.bones[context.scene.IK_Leg_Effector_L],
            arma.pose.bones[context.scene.IK_Leg_End_L],
        )
            
        return {'FINISHED'}
    
    def snap_IK_to_FK(self, IK_pole_target, IK_target, FK_end, IK_pole, IK_effector, IK_end):
        IK_pole.matrix = IK_pole_target.matrix
        bpy.context.view_layer.update()
        
        IK_effector.matrix = IK_target.matrix
        bpy.context.view_layer.update()
        
        IK_relative_to_FK = FK_end.bone.matrix_local.inverted() @ IK_end.bone.matrix_local
        IK_end.matrix = FK_end.matrix @ IK_relative_to_FK

# Leg L FK to IK operator
class LegL_FKtoIK(bpy.types.Operator):
    bl_idname = 'opr.legl_fkik'
    bl_label = 'Snap to IK'

    def execute(self, context):
        arma = bpy.data.objects[context.scene.armature_name]
        self.snap_FK_to_IK(
            arma.pose.bones[context.scene.IK_Leg_Upper_L],
            arma.pose.bones[context.scene.IK_Leg_Lower_L],
            arma.pose.bones[context.scene.IK_Leg_End_L],
            arma.pose.bones[context.scene.FK_Leg_Upper_L],
            arma.pose.bones[context.scene.FK_Leg_Lower_L],
            arma.pose.bones[context.scene.FK_Leg_End_L],
        )
            
        return {'FINISHED'}
    
    def snap_FK_to_IK(self, IK_upper, IK_lower, IK_end, FK_upper, FK_lower, FK_end):
        FK_upper.matrix = IK_upper.matrix
        bpy.context.view_layer.update()
        
        FK_lower.matrix = IK_lower.matrix
        bpy.context.view_layer.update()
        
        FK_relative_to_IK = IK_end.bone.matrix_local.inverted() @ FK_end.bone.matrix_local
        FK_end.matrix = IK_end.matrix @ FK_relative_to_IK

# Leg R IK to FK operator
class LegR_IKtoFK(bpy.types.Operator):
    bl_idname = 'opr.legr_ikfk'
    bl_label = 'Snap to FK'

    def execute(self, context):
        arma = bpy.data.objects[context.scene.armature_name]
        self.snap_IK_to_FK(
            arma.pose.bones[context.scene.IK_Leg_Pole_Target_R],
            arma.pose.bones[context.scene.IK_Leg_Target_R],
            arma.pose.bones[context.scene.FK_Leg_End_R],
            arma.pose.bones[context.scene.IK_Leg_Pole_R],
            arma.pose.bones[context.scene.IK_Leg_Effector_R],
            arma.pose.bones[context.scene.IK_Leg_End_R],
        )
            
        return {'FINISHED'}
    
    def snap_IK_to_FK(self, IK_pole_target, IK_target, FK_end, IK_pole, IK_effector, IK_end):
        IK_pole.matrix = IK_pole_target.matrix
        bpy.context.view_layer.update()
        
        IK_effector.matrix = IK_target.matrix
        bpy.context.view_layer.update()
        
        IK_relative_to_FK = FK_end.bone.matrix_local.inverted() @ IK_end.bone.matrix_local
        IK_end.matrix = FK_end.matrix @ IK_relative_to_FK

# Leg R FK to IK operator
class LegR_FKtoIK(bpy.types.Operator):
    bl_idname = 'opr.legr_fkik'
    bl_label = 'Snap to IK'

    def execute(self, context):
        arma = bpy.data.objects[context.scene.armature_name]
        self.snap_FK_to_IK(
            arma.pose.bones[context.scene.IK_Leg_Upper_R],
            arma.pose.bones[context.scene.IK_Leg_Lower_R],
            arma.pose.bones[context.scene.IK_Leg_End_R],
            arma.pose.bones[context.scene.FK_Leg_Upper_R],
            arma.pose.bones[context.scene.FK_Leg_Lower_R],
            arma.pose.bones[context.scene.FK_Leg_End_R],
        )
            
        return {'FINISHED'}
    
    def snap_FK_to_IK(self, IK_upper, IK_lower, IK_end, FK_upper, FK_lower, FK_end):
        FK_upper.matrix = IK_upper.matrix
        bpy.context.view_layer.update()
        
        FK_lower.matrix = IK_lower.matrix
        bpy.context.view_layer.update()
        
        FK_relative_to_IK = IK_end.bone.matrix_local.inverted() @ FK_end.bone.matrix_local
        FK_end.matrix = IK_end.matrix @ FK_relative_to_IK

# Limb presets operator
class PresetAdd(AddPresetBase, bpy.types.Operator):
    bl_idname = 'opr.presetadd'
    bl_label = 'Add A preset'
    preset_menu = 'opr.presetmenu'
    preset_defines = [
                        'obj = bpy.context.object',
                        'scene = bpy.context.scene'
                     ]
    preset_values = [
                        'scene.armature_name',
                        'scene.FK_Arm_Upper_L',
                        'scene.FK_Arm_Lower_L',
                        'scene.FK_Arm_End_L',
                        'scene.IK_Arm_Upper_L',
                        'scene.IK_Arm_Lower_L',
                        'scene.IK_Arm_End_L',
                        'scene.IK_Arm_Effector_L',
                        'scene.IK_Arm_Pole_L',
                        'scene.IK_Arm_Target_L',
                        'scene.IK_Arm_Pole_Target_L',
                        'scene.FK_Arm_Upper_R',
                        'scene.FK_Arm_Lower_R',
                        'scene.FK_Arm_End_R',
                        'scene.IK_Arm_Upper_R',
                        'scene.IK_Arm_Lower_R',
                        'scene.IK_Arm_End_R',
                        'scene.IK_Arm_Effector_R',
                        'scene.IK_Arm_Pole_R',
                        'scene.IK_Arm_Target_R',
                        'scene.IK_Arm_Pole_Target_R',
                        'scene.FK_Leg_Upper_L',
                        'scene.FK_Leg_Lower_L',
                        'scene.FK_Leg_End_L',
                        'scene.IK_Leg_Upper_L',
                        'scene.IK_Leg_Lower_L',
                        'scene.IK_Leg_End_L',
                        'scene.IK_Leg_Effector_L',
                        'scene.IK_Leg_Pole_L',
                        'scene.IK_Leg_Target_L',
                        'scene.IK_Leg_Pole_Target_L',
                        'scene.FK_Leg_Upper_R',
                        'scene.FK_Leg_Lower_R',
                        'scene.FK_Leg_End_R',
                        'scene.IK_Leg_Upper_R',
                        'scene.IK_Leg_Lower_R',
                        'scene.IK_Leg_End_R',
                        'scene.IK_Leg_Effector_R',
                        'scene.IK_Leg_Pole_R',
                        'scene.IK_Leg_Target_R',
                        'scene.IK_Leg_Pole_Target_R'
                    ]
    preset_subdir = 'IK-FK_Snapping_Tool/Armature_&_Bones_Presets'

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#     Register & Unregister     
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

classes = [
    PresetMenu,
    PresetPanel,
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