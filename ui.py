import bpy
from . import operators
from . import utilities

#━━━━━━━━━━━━━━━━━━━━
#     Tool Panel     
#━━━━━━━━━━━━━━━━━━━━

class ToolPanel(bpy.types.Panel):
    bl_idname = 'TOOL_PT_panel'
    bl_label = 'Snapping Tool'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'IK-FK Snap'
    
    # Draw the preset menu button in the panel header
    def draw_header_preset(self, _context):
        operators.PRESET_PT_Panel.draw_panel_header(self.layout)
    
    def draw(self, context):
        layout = self.layout
        col = layout.column()
        scene = bpy.context.scene
        obj = bpy.context.active_object
        # Check if an armature is active
        if obj and obj.type == 'ARMATURE':
            # Bones needed for IK to FK snapping on left arm
            IKtoFK_ArmL_Bones = {
                obj.pose.bones.get(scene.IK_Arm_Pole_Target_L),
                obj.pose.bones.get(scene.IK_Arm_Target_L),
                obj.pose.bones.get(scene.FK_Arm_End_L),
                obj.pose.bones.get(scene.IK_Arm_Pole_L),
                obj.pose.bones.get(scene.IK_Arm_Control_L),
                obj.pose.bones.get(scene.IK_Arm_End_L)
            }
            # Bones needed for FK to IK snapping on left arm
            FKtoIK_ArmL_Bones = {
                obj.pose.bones.get(scene.IK_Arm_Upper_L),
                obj.pose.bones.get(scene.IK_Arm_Lower_L),
                obj.pose.bones.get(scene.IK_Arm_End_L),
                obj.pose.bones.get(scene.FK_Arm_Upper_L),
                obj.pose.bones.get(scene.FK_Arm_Lower_L),
                obj.pose.bones.get(scene.FK_Arm_End_L)
            }
            # Bones needed for IK to FK snapping on right arm
            IKtoFK_ArmR_Bones = {
                obj.pose.bones.get(scene.IK_Arm_Pole_Target_R),
                obj.pose.bones.get(scene.IK_Arm_Target_R),
                obj.pose.bones.get(scene.FK_Arm_End_R),
                obj.pose.bones.get(scene.IK_Arm_Pole_R),
                obj.pose.bones.get(scene.IK_Arm_Control_R),
                obj.pose.bones.get(scene.IK_Arm_End_R)
            }
            # Bones needed for FK to IK snapping on right arm
            FKtoIK_ArmR_Bones = {
                obj.pose.bones.get(scene.IK_Arm_Upper_R),
                obj.pose.bones.get(scene.IK_Arm_Lower_R),
                obj.pose.bones.get(scene.IK_Arm_End_R),
                obj.pose.bones.get(scene.FK_Arm_Upper_R),
                obj.pose.bones.get(scene.FK_Arm_Lower_R),
                obj.pose.bones.get(scene.FK_Arm_End_R)
            }
            # Bones needed for IK to FK snapping on left leg
            IKtoFK_LegL_Bones = {
                obj.pose.bones.get(scene.IK_Leg_Pole_Target_L),
                obj.pose.bones.get(scene.IK_Leg_Target_L),
                obj.pose.bones.get(scene.FK_Leg_Knee_L),
                obj.pose.bones.get(scene.FK_Leg_End_L),
                obj.pose.bones.get(scene.IK_Leg_Pole_L),
                obj.pose.bones.get(scene.IK_Leg_Control_L),
                obj.pose.bones.get(scene.IK_Leg_Knee_L),
                obj.pose.bones.get(scene.IK_Leg_End_L)
            }
            # Bones needed for FK to IK snapping on left leg
            FKtoIK_LegL_Bones = {
                obj.pose.bones.get(scene.IK_Leg_Upper_L),
                obj.pose.bones.get(scene.IK_Leg_Knee_L),
                obj.pose.bones.get(scene.IK_Leg_Lower_L),
                obj.pose.bones.get(scene.IK_Leg_End_L),
                obj.pose.bones.get(scene.FK_Leg_Upper_L),
                obj.pose.bones.get(scene.FK_Leg_Knee_L),
                obj.pose.bones.get(scene.FK_Leg_Lower_L),
                obj.pose.bones.get(scene.FK_Leg_End_L)
            }
            # Bones needed for IK to FK snapping on right leg
            IKtoFK_LegR_Bones = {
                obj.pose.bones.get(scene.IK_Leg_Pole_Target_R),
                obj.pose.bones.get(scene.IK_Leg_Target_R),
                obj.pose.bones.get(scene.FK_Leg_Knee_R),
                obj.pose.bones.get(scene.FK_Leg_End_R),
                obj.pose.bones.get(scene.IK_Leg_Pole_R),
                obj.pose.bones.get(scene.IK_Leg_Control_R),
                obj.pose.bones.get(scene.IK_Leg_Knee_R),
                obj.pose.bones.get(scene.IK_Leg_End_R)
            }
            # Bones needed for FK to IK snapping on right leg
            FKtoIK_LegR_Bones = {
                obj.pose.bones.get(scene.IK_Leg_Upper_R),
                obj.pose.bones.get(scene.IK_Leg_Knee_R),
                obj.pose.bones.get(scene.IK_Leg_Lower_R),
                obj.pose.bones.get(scene.IK_Leg_End_R),
                obj.pose.bones.get(scene.FK_Leg_Upper_R),
                obj.pose.bones.get(scene.FK_Leg_Knee_R),
                obj.pose.bones.get(scene.FK_Leg_Lower_R),
                obj.pose.bones.get(scene.FK_Leg_End_R)
            }

            # Check if any relevant bones are found
            if utilities.any_snapping_possible(IKtoFK_ArmL_Bones, FKtoIK_ArmL_Bones, 
                                               IKtoFK_ArmR_Bones, FKtoIK_ArmR_Bones, 
                                               IKtoFK_LegL_Bones, FKtoIK_LegL_Bones,
                                               IKtoFK_LegR_Bones, FKtoIK_LegR_Bones):

                # --- Arm L Snapping Tool ---
                box = col.box()
                box.label(text= "Arm L Snapping", icon= 'SNAP_ON')
                # Check if all required bones are present for both snapping directions
                if not all(IKtoFK_ArmL_Bones) and not all(FKtoIK_ArmL_Bones):
                    box.label(text= "Bone Incomplete", icon= 'ERROR')
                else:
                    # Create a grid layout for buttons
                    grid = box.grid_flow(columns=2, align=True)
                    if all(IKtoFK_ArmL_Bones):
                        # Add the "Snap to FK" button and link it to the corresponding operator
                        arml_ikfk_oprator = grid.operator('opr.arml_ikfk', text='Snap to FK')
                    else:
                        box.label(text= "IK to FK Incomplete", icon= 'ERROR')
                    if all(FKtoIK_ArmL_Bones):
                        # Add the "Snap to IK" button and link it to the corresponding operator
                        arml_fkik_oprator = grid.operator('opr.arml_fkik', text='Snap to IK')
                    else:
                        box.label(text= "FK to IK Incomplete", icon= 'ERROR')

                # --- Arm R Snapping Tool ---
                box = col.box()
                box.label(text= "Arm R Snapping", icon= 'SNAP_ON')
                # Check if all required bones are present for both snapping directions
                if not all(IKtoFK_ArmR_Bones) and not all(FKtoIK_ArmR_Bones):
                    box.label(text= "Bone Incomplete", icon= 'ERROR')
                else:
                     # Create a grid layout for buttons
                    grid = box.grid_flow(columns=2, align=True)
                    if all(IKtoFK_ArmR_Bones):
                        # Add the "Snap to FK" button and link it to the corresponding operator
                        armr_ikfk_oprator = grid.operator('opr.armr_ikfk', text='Snap to FK')
                    else:
                        box.label(text= "IK to FK Incomplete", icon= 'ERROR')
                    if all(FKtoIK_ArmR_Bones):
                    # Add the "Snap to IK" button and link it to the corresponding operator
                        armr_fkik_oprator = grid.operator('opr.armr_fkik', text='Snap to IK')
                    else:
                        box.label(text= "FK to IK Incomplete", icon= 'ERROR')

                # --- Leg L Snapping Tool ---
                box = col.box()
                box.label(text= "Leg L Snapping", icon= 'SNAP_ON')
                # Check if all required bones are present for both snapping directions
                if not all(IKtoFK_LegL_Bones) and not all(FKtoIK_LegL_Bones):
                    box.label(text= "Bone Incomplete", icon= 'ERROR')
                else:
                    # Create a grid layout for buttons
                    grid = box.grid_flow(columns=2, align=True)
                    if all(IKtoFK_LegL_Bones):
                        # Add the "Snap to FK" button and link it to the corresponding operator
                        legl_ikfk_oprator = grid.operator('opr.legl_ikfk', text='Snap to FK')
                    else:
                        box.label(text= "IK to FK Incomplete", icon= 'ERROR')
                    if all(FKtoIK_LegL_Bones):
                        # Add the "Snap to IK" button and link it to the corresponding operator
                        legl_fkik_oprator = grid.operator('opr.legl_fkik', text='Snap to IK')
                    else:
                        box.label(text= "FK to IK Incomplete", icon= 'ERROR')

                # --- Leg R Snapping Tool ---
                box = col.box()
                box.label(text= "Leg R Snapping", icon= 'SNAP_ON')
                # Check if all required bones are present for both snapping directions
                if not all(IKtoFK_LegR_Bones) and not all(FKtoIK_LegR_Bones):
                    box.label(text= "Bone Incomplete", icon= 'ERROR')
                else:
                    # Create a grid layout for buttons
                    grid = box.grid_flow(columns=2, align=True)
                    if all(IKtoFK_LegR_Bones):
                        # Add the "Snap to FK" button and link it to the corresponding operator
                        armr_ikfk_oprator = grid.operator('opr.legr_ikfk', text='Snap to FK')
                    else:
                        box.label(text= "IK to FK Incomplete", icon= 'ERROR')
                    if all(FKtoIK_LegR_Bones):
                        # Add the "Snap to IK" button and link it to the corresponding operator
                        armr_fkik_oprator = grid.operator('opr.legr_fkik', text='Snap to IK')
                    else:
                        box.label(text= "FK to IK Incomplete", icon= 'ERROR')

            else:
                # If none of the bone sets have any bones (meaning the armature doesn't have the necessary bones for snapping)
                col.label(text="Active Armature has no similar bones", icon='ERROR')
        else:
            # If the active object is not an armature
            col.label(text="No active armature", icon='ERROR')

#━━━━━━━━━━━━━━━━━━━━━━━━
#     Armature Panel     
#━━━━━━━━━━━━━━━━━━━━━━━━

class Armature_MappingPanel(bpy.types.Panel):
    bl_idname = 'ARMATURE_MAPPING_PT_panel'
    bl_label = 'Armature Mapping'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'IK-FK Snap'
    
    # Draw the preset menu button in the panel header
    def draw_header_preset(self, _context):
        operators.PRESET_PT_Panel.draw_panel_header(self.layout)
    
    def draw(self, context):
        col = self.layout.column()
        # Add the "Open Preset Directory" button and link it to the corresponding operator
        col.operator("opr.open_preset_directory", icon="FILEBROWSER")

# ------------------------------
#     Panel for Arm L Bones     
# ------------------------------

class ArmL_MappingPanel(bpy.types.Panel):
    bl_idname = 'ARML_MAPPING_PT_panel'
    bl_label = 'Arm L'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'IK-FK Snap'
    bl_parent_id = "ARMATURE_MAPPING_PT_panel"
    
    def draw(self, context):
        obj = bpy.context.active_object
        col = self.layout.column()
        # Check if an armature is active
        if obj and obj.type == 'ARMATURE':
            # Create bone selection fields for each bone involved in Arm L snapping
            col.prop_search(context.scene, "FK_Arm_Upper_L", obj.data, "bones")
            col.prop_search(context.scene, "FK_Arm_Lower_L", obj.data, "bones")
            col.prop_search(context.scene, "FK_Arm_End_L", obj.data, "bones")
            col.prop_search(context.scene, "IK_Arm_Upper_L", obj.data, "bones")
            col.prop_search(context.scene, "IK_Arm_Lower_L", obj.data, "bones")
            col.prop_search(context.scene, "IK_Arm_End_L", obj.data, "bones")
            col.prop_search(context.scene, "IK_Arm_Control_L", obj.data, "bones")
            col.prop_search(context.scene, "IK_Arm_Pole_L", obj.data, "bones")
            col.prop_search(context.scene, "IK_Arm_Target_L", obj.data, "bones")
            col.prop_search(context.scene, "IK_Arm_Pole_Target_L", obj.data, "bones")
            return
        else:
            # Display error if no armature is active
            col.label(text= "No active armature", icon= 'ERROR')

# ------------------------------
#     Panel for Arm R Bones     
# ------------------------------

class ArmR_MappingPanel(bpy.types.Panel):
    bl_idname = 'ARMR_MAPPING_PT_panel'
    bl_label = 'Arm R'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'IK-FK Snap'
    bl_parent_id = "ARMATURE_MAPPING_PT_panel"
    
    def draw(self, context):
        obj = bpy.context.active_object
        col = self.layout.column()
        # Check if an armature is active
        if obj and obj.type == 'ARMATURE':
            # Create bone selection fields for each bone involved in Arm L snapping
            col.prop_search(context.scene, "FK_Arm_Upper_R", obj.data, "bones")
            col.prop_search(context.scene, "FK_Arm_Lower_R", obj.data, "bones")
            col.prop_search(context.scene, "FK_Arm_End_R", obj.data, "bones")
            col.prop_search(context.scene, "IK_Arm_Upper_R", obj.data, "bones")
            col.prop_search(context.scene, "IK_Arm_Lower_R", obj.data, "bones")
            col.prop_search(context.scene, "IK_Arm_End_R", obj.data, "bones")
            col.prop_search(context.scene, "IK_Arm_Control_R", obj.data, "bones")
            col.prop_search(context.scene, "IK_Arm_Pole_R", obj.data, "bones")
            col.prop_search(context.scene, "IK_Arm_Target_R", obj.data, "bones")
            col.prop_search(context.scene, "IK_Arm_Pole_Target_R", obj.data, "bones")
            return
        else:
            # Display error if no armature is active
            col.label(text= "No active armature", icon= 'ERROR')

# ------------------------------
#     Panel for Leg L Bones     
# ------------------------------

class LegL_MappingPanel(bpy.types.Panel):
    bl_idname = 'LEGL_MAPPING_PT_panel'
    bl_label = 'Leg L'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'IK-FK Snap'
    bl_parent_id = "ARMATURE_MAPPING_PT_panel"
    
    def draw(self, context):
        obj = bpy.context.active_object
        col = self.layout.column()
        # Check if an armature is active
        if obj and obj.type == 'ARMATURE':
            # Create bone selection fields for each bone involved in Arm L snapping
            col.prop_search(context.scene, "FK_Leg_Upper_L", obj.data, "bones")
            col.prop_search(context.scene, "FK_Leg_Knee_L", obj.data, "bones")
            col.prop_search(context.scene, "FK_Leg_Lower_L", obj.data, "bones")
            col.prop_search(context.scene, "FK_Leg_End_L", obj.data, "bones")
            col.prop_search(context.scene, "IK_Leg_Upper_L", obj.data, "bones")
            col.prop_search(context.scene, "IK_Leg_Knee_L", obj.data, "bones")
            col.prop_search(context.scene, "IK_Leg_Lower_L", obj.data, "bones")
            col.prop_search(context.scene, "IK_Leg_End_L", obj.data, "bones")
            col.prop_search(context.scene, "IK_Leg_Control_L", obj.data, "bones")
            col.prop_search(context.scene, "IK_Leg_Pole_L", obj.data, "bones")
            col.prop_search(context.scene, "IK_Leg_Target_L", obj.data, "bones")
            col.prop_search(context.scene, "IK_Leg_Pole_Target_L", obj.data, "bones")
            return
        else:
            # Display error if no armature is active
            col.label(text= "No active armature", icon= 'ERROR')

# ------------------------------
#     Panel for Leg R Bones     
# ------------------------------

class LegR_MappingPanel(bpy.types.Panel):
    bl_idname = 'LEGR_MAPPING_PT_panel'
    bl_label = 'Leg R'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'IK-FK Snap'
    bl_parent_id = "ARMATURE_MAPPING_PT_panel"
    
    def draw(self, context):
        obj = bpy.context.active_object
        col = self.layout.column()
        # Check if an armature is active
        if obj and obj.type == 'ARMATURE':
            # Create bone selection fields for each bone involved in Arm L snapping
            col.prop_search(context.scene, "FK_Leg_Upper_R", obj.data, "bones")
            col.prop_search(context.scene, "FK_Leg_Knee_R", obj.data, "bones")
            col.prop_search(context.scene, "FK_Leg_Lower_R", obj.data, "bones")
            col.prop_search(context.scene, "FK_Leg_End_R", obj.data, "bones")
            col.prop_search(context.scene, "IK_Leg_Upper_R", obj.data, "bones")
            col.prop_search(context.scene, "IK_Leg_Knee_R", obj.data, "bones")
            col.prop_search(context.scene, "IK_Leg_Lower_R", obj.data, "bones")
            col.prop_search(context.scene, "IK_Leg_End_R", obj.data, "bones")
            col.prop_search(context.scene, "IK_Leg_Control_R", obj.data, "bones")
            col.prop_search(context.scene, "IK_Leg_Pole_R", obj.data, "bones")
            col.prop_search(context.scene, "IK_Leg_Target_R", obj.data, "bones")
            col.prop_search(context.scene, "IK_Leg_Pole_Target_R", obj.data, "bones")
            return
        else:
            # Display error if no armature is active
            col.label(text= "No active armature", icon= 'ERROR')

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#     Register & Unregister     
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

classes = [
    ToolPanel,
    Armature_MappingPanel,
    ArmL_MappingPanel,
    ArmR_MappingPanel,
    LegL_MappingPanel,
    LegR_MappingPanel
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
