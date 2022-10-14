import bpy
from . import operators
from . import utilities

#━━━━━━━━━━━━━━━━━━━━
#     Tool Panel     
#━━━━━━━━━━━━━━━━━━━━

class ToolPanel(bpy.types.Panel):
    bl_idname = 'panel.tool'
    bl_label = 'Snapping Tool'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'IK-FK Snap'
    
    def draw_header_preset(self, _context): 
        operators.PresetPanel.draw_panel_header(self.layout)
    
    def draw(self, context):
        layout = self.layout
        col = layout.column()
        scene = bpy.context.scene
        # Bone sets
        Bones_All = {
            scene.FK_Arm_Upper_L,
            scene.FK_Arm_Lower_L,
            scene.FK_Arm_End_L,
            scene.IK_Arm_Upper_L,
            scene.IK_Arm_Lower_L,
            scene.IK_Arm_End_L,
            scene.IK_Arm_Pole_L,
            scene.IK_Arm_Effector_L,
            scene.IK_Arm_Pole_Target_L,
            scene.IK_Arm_Target_L,
            scene.FK_Arm_Upper_R,
            scene.FK_Arm_Lower_R,
            scene.FK_Arm_End_R,
            scene.IK_Arm_Upper_R,
            scene.IK_Arm_Lower_R,
            scene.IK_Arm_End_R,
            scene.IK_Arm_Pole_R,
            scene.IK_Arm_Effector_R,
            scene.IK_Arm_Pole_Target_R,
            scene.IK_Arm_Target_R,
            scene.FK_Leg_Upper_L,
            scene.FK_Leg_Lower_L,
            scene.FK_Leg_End_L,
            scene.IK_Leg_Upper_L,
            scene.IK_Leg_Lower_L,
            scene.IK_Leg_End_L,
            scene.IK_Leg_Pole_L,
            scene.IK_Leg_Effector_L,
            scene.IK_Leg_Pole_Target_L,
            scene.IK_Leg_Target_L,
            scene.FK_Leg_Upper_R,
            scene.FK_Leg_Lower_R,
            scene.FK_Leg_End_R,
            scene.IK_Leg_Upper_R,
            scene.IK_Leg_Lower_R,
            scene.IK_Leg_End_R,
            scene.IK_Leg_Pole_R,
            scene.IK_Leg_Effector_R,
            scene.IK_Leg_Pole_Target_R,
            scene.IK_Leg_Target_R
        }
        IKtoFK_ArmL_Bones = {
            scene.IK_Arm_Pole_Target_L,
            scene.IK_Arm_Target_L,
            scene.FK_Arm_End_L,
            scene.IK_Arm_Pole_L,
            scene.IK_Arm_Effector_L,
            scene.IK_Arm_End_L
        }
        FKtoIK_ArmL_Bones = {
            scene.IK_Arm_Upper_L,
            scene.IK_Arm_Lower_L,
            scene.IK_Arm_End_L,
            scene.FK_Arm_Upper_L,
            scene.FK_Arm_Lower_L,
            scene.FK_Arm_End_L
        }
        IKtoFK_ArmR_Bones = {
            scene.IK_Arm_Pole_Target_R,
            scene.IK_Arm_Target_R,
            scene.FK_Arm_End_R,
            scene.IK_Arm_Pole_R,
            scene.IK_Arm_Effector_R,
            scene.IK_Arm_End_R
        }
        FKtoIK_ArmR_Bones = {
            scene.IK_Arm_Upper_R,
            scene.IK_Arm_Lower_R,
            scene.IK_Arm_End_R,
            scene.FK_Arm_Upper_R,
            scene.FK_Arm_Lower_R,
            scene.FK_Arm_End_R
        }
        IKtoFK_LegL_Bones = {
            scene.IK_Leg_Pole_Target_L,
            scene.IK_Leg_Target_L,
            scene.FK_Leg_End_L,
            scene.IK_Leg_Pole_L,
            scene.IK_Leg_Effector_L,
            scene.IK_Leg_End_L
        }
        FKtoIK_LegL_Bones = {
            scene.IK_Leg_Upper_L,
            scene.IK_Leg_Lower_L,
            scene.IK_Leg_End_L,
            scene.FK_Leg_Upper_L,
            scene.FK_Leg_Lower_L,
            scene.FK_Leg_End_L
        }
        IKtoFK_LegR_Bones = {
            scene.IK_Leg_Pole_Target_R,
            scene.IK_Leg_Target_R,
            scene.FK_Leg_End_R,
            scene.IK_Leg_Pole_R,
            scene.IK_Leg_Effector_R,
            scene.IK_Leg_End_R
        }
        FKtoIK_LegR_Bones = {
            scene.IK_Leg_Upper_R,
            scene.IK_Leg_Lower_R,
            scene.IK_Leg_End_R,
            scene.FK_Leg_Upper_R,
            scene.FK_Leg_Lower_R,
            scene.FK_Leg_End_R
        }

        # Pre-check
        if not context.scene.armature_name:
            col.label(text= "No Armature Added", icon= 'ERROR')
            return
        if not any(Bones_All):
            col.label(text= "No Bones Added", icon= 'ERROR')
            return

        # Arm L Snapping Tool
        box = col.box()
        box.label(text= "Arm L Snapping", icon= 'SNAP_ON')
        if not all(IKtoFK_ArmL_Bones) and not all(FKtoIK_ArmL_Bones):
            box.label(text= "Bone Incomplete", icon= 'ERROR')
        else:
            grid = box.grid_flow(columns=2, align=True)
            if all(IKtoFK_ArmL_Bones):
                arml_ikfk_oprator = grid.operator('opr.arml_ikfk', text='Snap to FK')
            else:
                box.label(text= "IK to FK Incomplete", icon= 'ERROR')
            if all(FKtoIK_ArmL_Bones):
                arml_fkik_oprator = grid.operator('opr.arml_fkik', text='Snap to IK')
            else:
                box.label(text= "FK to IK Incomplete", icon= 'ERROR')

        # Arm R Snapping Tool  
        box = col.box()
        box.label(text= "Arm R Snapping", icon= 'SNAP_ON')
        if not all(IKtoFK_ArmR_Bones) and not all(FKtoIK_ArmR_Bones):
            box.label(text= "Bone Incomplete", icon= 'ERROR')
        else:
            grid = box.grid_flow(columns=2, align=True)
            if all(IKtoFK_ArmR_Bones):
                armr_ikfk_oprator = grid.operator('opr.armr_ikfk', text='Snap to FK')
            else:
                box.label(text= "IK to FK Incomplete", icon= 'ERROR')
            if all(FKtoIK_ArmR_Bones):
                armr_fkik_oprator = grid.operator('opr.armr_fkik', text='Snap to IK')
            else:
                box.label(text= "FK to IK Incomplete", icon= 'ERROR')

        # Leg L Snapping Tool
        box = col.box()
        box.label(text= "Leg L Snapping", icon= 'SNAP_ON')
        if not all(IKtoFK_LegL_Bones) and not all(FKtoIK_LegL_Bones):
            box.label(text= "Bone Incomplete", icon= 'ERROR')
        else:
            grid = box.grid_flow(columns=2, align=True)
            if all(IKtoFK_LegL_Bones):
                legl_ikfk_oprator = grid.operator('opr.legl_ikfk', text='Snap to FK')
            else:
                box.label(text= "IK to FK Incomplete", icon= 'ERROR')
            if all(FKtoIK_LegL_Bones):
                legl_fkik_oprator = grid.operator('opr.legl_fkik', text='Snap to IK')
            else:
                box.label(text= "FK to IK Incomplete", icon= 'ERROR')

        # Leg R Snapping Tool
        box = col.box()
        box.label(text= "Leg R Snapping", icon= 'SNAP_ON')
        if not all(IKtoFK_LegR_Bones) and not all(FKtoIK_LegR_Bones):
            box.label(text= "Bone Incomplete", icon= 'ERROR')
        else:
            grid = box.grid_flow(columns=2, align=True)
            if all(IKtoFK_LegR_Bones):
                armr_ikfk_oprator = grid.operator('opr.legr_ikfk', text='Snap to FK')
            else:
                box.label(text= "IK to FK Incomplete", icon= 'ERROR')
            if all(FKtoIK_LegR_Bones):
                armr_fkik_oprator = grid.operator('opr.legr_fkik', text='Snap to IK')
            else:
                box.label(text= "FK to IK Incomplete", icon= 'ERROR')

#━━━━━━━━━━━━━━━━━━━━━━━━
#     Armature Panel     
#━━━━━━━━━━━━━━━━━━━━━━━━

class Armature_MappingPanel(bpy.types.Panel):
    bl_idname = 'panel.armature_mapping'
    bl_label = 'Armature & Bones'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'IK-FK Snap'
    
    def draw_header_preset(self, _context): 
        operators.PresetPanel.draw_panel_header(self.layout)
    
    def draw(self, context):
        col = self.layout.column()
        col.prop_search(context.scene, "armature_name", bpy.data, "armatures")

#━━━━━━━━━━━━━━━━━━━━━
#     Bones Panel     
#━━━━━━━━━━━━━━━━━━━━━

# Arm L panel
class ArmL_MappingPanel(bpy.types.Panel):
    bl_idname = 'panel.arml_mapping'
    bl_label = 'Arm L'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'IK-FK Snap'
    bl_parent_id = "panel.armature_mapping"
    
    def draw(self, context):
        arma = bpy.data.armatures.get(context.scene.armature_name)
        col = self.layout.column()
        if arma is not None:
            col.prop_search(context.scene, "FK_Arm_Upper_L", arma, "bones")
            col.prop_search(context.scene, "FK_Arm_Lower_L", arma, "bones")
            col.prop_search(context.scene, "FK_Arm_End_L", arma, "bones")
            col.prop_search(context.scene, "IK_Arm_Upper_L", arma, "bones")
            col.prop_search(context.scene, "IK_Arm_Lower_L", arma, "bones")
            col.prop_search(context.scene, "IK_Arm_End_L", arma, "bones")
            col.prop_search(context.scene, "IK_Arm_Effector_L", arma, "bones")
            col.prop_search(context.scene, "IK_Arm_Pole_L", arma, "bones")
            col.prop_search(context.scene, "IK_Arm_Target_L", arma, "bones")
            col.prop_search(context.scene, "IK_Arm_Pole_Target_L", arma, "bones")
            return
        col.label(text= "No Armature Added", icon= 'ERROR')

# Arm R panel
class ArmR_MappingPanel(bpy.types.Panel):
    bl_idname = 'panel.armr_mapping'
    bl_label = 'Arm R'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'IK-FK Snap'
    bl_parent_id = "panel.armature_mapping"
    
    def draw(self, context):
        arma = bpy.data.armatures.get(context.scene.armature_name)
        col = self.layout.column()
        if arma is not None:
            col.prop_search(context.scene, "FK_Arm_Upper_R", arma, "bones")
            col.prop_search(context.scene, "FK_Arm_Lower_R", arma, "bones")
            col.prop_search(context.scene, "FK_Arm_End_R", arma, "bones")
            col.prop_search(context.scene, "IK_Arm_Upper_R", arma, "bones")
            col.prop_search(context.scene, "IK_Arm_Lower_R", arma, "bones")
            col.prop_search(context.scene, "IK_Arm_End_R", arma, "bones")
            col.prop_search(context.scene, "IK_Arm_Effector_R", arma, "bones")
            col.prop_search(context.scene, "IK_Arm_Pole_R", arma, "bones")
            col.prop_search(context.scene, "IK_Arm_Target_R", arma, "bones")
            col.prop_search(context.scene, "IK_Arm_Pole_Target_R", arma, "bones")
            return
        col.label(text= "No Armature Added", icon= 'ERROR')

# Leg L panel
class LegL_MappingPanel(bpy.types.Panel):
    bl_idname = 'panel.legl_mapping'
    bl_label = 'Leg L'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'IK-FK Snap'
    bl_parent_id = "panel.armature_mapping"
    
    def draw(self, context):
        arma = bpy.data.armatures.get(context.scene.armature_name)
        col = self.layout.column()
        if arma is not None:
            col.prop_search(context.scene, "FK_Leg_Upper_L", arma, "bones")
            col.prop_search(context.scene, "FK_Leg_Lower_L", arma, "bones")
            col.prop_search(context.scene, "FK_Leg_End_L", arma, "bones")
            col.prop_search(context.scene, "IK_Leg_Upper_L", arma, "bones")
            col.prop_search(context.scene, "IK_Leg_Lower_L", arma, "bones")
            col.prop_search(context.scene, "IK_Leg_End_L", arma, "bones")
            col.prop_search(context.scene, "IK_Leg_Effector_L", arma, "bones")
            col.prop_search(context.scene, "IK_Leg_Pole_L", arma, "bones")
            col.prop_search(context.scene, "IK_Leg_Target_L", arma, "bones")
            col.prop_search(context.scene, "IK_Leg_Pole_Target_L", arma, "bones")
            return
        col.label(text= "No Armature Added", icon= 'ERROR')

# Leg R panel
class LegR_MappingPanel(bpy.types.Panel):
    bl_idname = 'panel.legr_mapping'
    bl_label = 'Leg R'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'IK-FK Snap'
    bl_parent_id = "panel.armature_mapping"
    
    def draw(self, context):
        arma = bpy.data.armatures.get(context.scene.armature_name)
        col = self.layout.column()
        if arma is not None:
            col.prop_search(context.scene, "FK_Leg_Upper_R", arma, "bones")
            col.prop_search(context.scene, "FK_Leg_Lower_R", arma, "bones")
            col.prop_search(context.scene, "FK_Leg_End_R", arma, "bones")
            col.prop_search(context.scene, "IK_Leg_Upper_R", arma, "bones")
            col.prop_search(context.scene, "IK_Leg_Lower_R", arma, "bones")
            col.prop_search(context.scene, "IK_Leg_End_R", arma, "bones")
            col.prop_search(context.scene, "IK_Leg_Effector_R", arma, "bones")
            col.prop_search(context.scene, "IK_Leg_Pole_R", arma, "bones")
            col.prop_search(context.scene, "IK_Leg_Target_R", arma, "bones")
            col.prop_search(context.scene, "IK_Leg_Pole_Target_R", arma, "bones")
            return
        col.label(text= "No Armature Added", icon= 'ERROR')

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
    ToolPanel,
    Armature_MappingPanel,
    ArmL_MappingPanel,
    ArmR_MappingPanel,
    LegL_MappingPanel,
    LegR_MappingPanel
]