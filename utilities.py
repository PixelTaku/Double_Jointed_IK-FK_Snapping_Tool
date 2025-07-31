import bpy

#━━━━━━━━━━━━━━━━━━━
#     Utilities     
#━━━━━━━━━━━━━━━━━━━

# -------------------------
#     Helper Functions     
# -------------------------

# Retrieves bone objects and perform error checking
def get_bones_with_check(context, bone_names):
    obj = context.active_object
    # Check if the active object is an armature
    if not obj or obj.type != 'ARMATURE':
        return None
    
    bones = []
    # Iterate over the provided bone names
    for name in bone_names:
        # Try to get the bone object by name
        bone = obj.pose.bones.get(name)
        if not bone:
            return None 
        # Add the bone object to the list
        bones.append(bone)
    return bones

# Check if any snapping action is possible
def any_snapping_possible(*bone_sets):
    return any(all(bone_set) for bone_set in bone_sets)

# Snaps IK bones to match the FK pose
def snap_IK_to_FK(IK_pole_target, IK_target, FK_end, IK_pole, IK_control, IK_end):
    # Match the IK control's matrix to the IK target's matrix
    IK_control.matrix = IK_target.matrix.copy()
    # Update the viewport to reflect the change
    bpy.context.view_layer.update()

    # Match the IK pole's matrix to the IK pole target's matrix
    IK_pole.matrix = IK_pole_target.matrix.copy()
    # Update the viewport to reflect the changes
    bpy.context.view_layer.update()

    # Match the IK end's matrix to the FK end's matrix
    IK_end.matrix = FK_end.matrix.copy()
    # Update the viewport to reflect the change
    bpy.context.view_layer.update()

# Snaps IK bones to match the FK pose with added Knee
def snap_IK_to_FK_knee(IK_pole_target, IK_target, FK_knee, TWEAK_knee, FK_lower, FK_end, IK_pole, IK_control, IK_knee, IK_end, IK_lower, TWEAK_lower):
    # Match the IK control's matrix to the IK target's matrix
    IK_control.matrix = IK_target.matrix.copy()
    # Update the viewport to reflect the change
    bpy.context.view_layer.update()
    # IK_control.keyframe_insert(KEYFRAME)

    # Match the IK pole's matrix to the IK pole target's matrix
    IK_pole.matrix = IK_pole_target.matrix.copy()
    # Update the viewport to reflect the changes
    bpy.context.view_layer.update()
    # IK_pole.keyframe_insert(KEYFRAME)
    
    # Match the IK end's matrix to the FK end's matrix
    IK_end.matrix = FK_end.matrix.copy()
    # Update the viewport to reflect the change
    bpy.context.view_layer.update()
    # IK_end.keyframe_insert(KEYFRAME)
    
    # Match the lower and end
    IK_lower.matrix = FK_lower.matrix.copy()
    # Update the viewport to reflect the change
    bpy.context.view_layer.update()
   
    # Match the IK knee's matrix to the FK knee's matrix
    IK_knee.matrix = FK_knee.matrix.copy()
    # Update the viewport to reflect the change
    bpy.context.view_layer.update()
    # IK_knee.keyframe_insert(KEYFRAME)
    
   
    # match the TWEAK knee and TWEAK lower to the FK Knee and FK lower respectively
    TWEAK_lower.matrix = FK_lower.matrix.copy()
    # Update the viewport to reflect the change
    bpy.context.view_layer.update()
    TWEAK_knee.matrix = FK_knee.matrix.copy()
    # Update the viewport to reflect the change
    bpy.context.view_layer.update()

# Snaps FK bones to match the IK pose
def snap_FK_to_IK(IK_upper, IK_lower, IK_end, FK_upper, FK_lower, FK_end):
    # Match the FK upper's matrix to the IK upper's matrix
    FK_upper.matrix = IK_upper.matrix.copy()
    # Update the viewport to reflect the change
    bpy.context.view_layer.update()
    
    # Match the FK lower's matrix to the IK lower's matrix
    FK_lower.matrix = IK_lower.matrix.copy()
    # Update the viewport to reflect the change
    bpy.context.view_layer.update()

    # Match the FK end's matrix to the IK end's matrix
    FK_end.matrix = IK_end.matrix.copy()
    # Update the viewport to reflect the change
    bpy.context.view_layer.update()

# Snaps FK bones to match the IK pose with added Knee
def snap_FK_to_IK_knee(IK_upper, IK_knee, TWEAK_knee, IK_lower, TWEAK_lower, IK_end, FK_upper, FK_knee, FK_lower, FK_end):
    # Match the FK upper's matrix to the IK upper's matrix
    FK_upper.matrix = IK_upper.matrix.copy()
    # Update the viewport to reflect the change
    bpy.context.view_layer.update()

    # Match the FK knee's matrix to the IK knee's matrix
    FK_knee.matrix = IK_knee.matrix.copy()
    FK_knee.matrix = TWEAK_knee.matrix.copy()
    # Update the viewport to reflect the change
    bpy.context.view_layer.update()
    
    # Match the FK lower's matrix to the IK lower's matrix
    FK_lower.matrix = IK_lower.matrix.copy()
    FK_lower.matrix = TWEAK_lower.matrix.copy()
    # Update the viewport to reflect the change
    bpy.context.view_layer.update()

    # Match the FK end's matrix to the IK end's matrix
    FK_end.matrix = IK_end.matrix.copy()
    # Update the viewport to reflect the change
    bpy.context.view_layer.update()

# --------------------------
#     Custom Properties     
# --------------------------

PROPS = [
    ('FK_Arm_Upper_L', bpy.props.StringProperty(name='FK Upper')),
    ('FK_Arm_Lower_L', bpy.props.StringProperty(name='FK Lower')),
    ('FK_Arm_End_L', bpy.props.StringProperty(name='FK End')),
    ('IK_Arm_Upper_L', bpy.props.StringProperty(name='IK Upper')),
    ('IK_Arm_Lower_L', bpy.props.StringProperty(name='IK Lower')),
    ('IK_Arm_End_L', bpy.props.StringProperty(name='IK End')),
    ('IK_Arm_Control_L', bpy.props.StringProperty(name='IK Control')),
    ('IK_Arm_Pole_L', bpy.props.StringProperty(name='IK Pole')),
    ('IK_Arm_Target_L', bpy.props.StringProperty(name='IK Target')),
    ('IK_Arm_Pole_Target_L', bpy.props.StringProperty(name='IK Pole Target')),
    ('FK_Arm_Upper_R', bpy.props.StringProperty(name='FK Upper')),
    ('FK_Arm_Lower_R', bpy.props.StringProperty(name='FK Lower')),
    ('FK_Arm_End_R', bpy.props.StringProperty(name='FK End')),
    ('IK_Arm_Upper_R', bpy.props.StringProperty(name='IK Upper')),
    ('IK_Arm_Lower_R', bpy.props.StringProperty(name='IK Lower')),
    ('IK_Arm_End_R', bpy.props.StringProperty(name='IK End')),
    ('IK_Arm_Control_R', bpy.props.StringProperty(name='IK Control')),
    ('IK_Arm_Pole_R', bpy.props.StringProperty(name='IK Pole')),
    ('IK_Arm_Target_R', bpy.props.StringProperty(name='IK Target')),
    ('IK_Arm_Pole_Target_R', bpy.props.StringProperty(name='IK Pole Target')),
    ('FK_Leg_Upper_L', bpy.props.StringProperty(name='FK Upper')),
    ('FK_Leg_Lower_L', bpy.props.StringProperty(name='FK Lower')),
    ('FK_Leg_End_L', bpy.props.StringProperty(name='FK End')),
    ('IK_Leg_Upper_L', bpy.props.StringProperty(name='IK Upper')),
    ('IK_Leg_Lower_L', bpy.props.StringProperty(name='IK Lower')),
    ('IK_Leg_End_L', bpy.props.StringProperty(name='IK End')),
    ('IK_Leg_Control_L', bpy.props.StringProperty(name='IK Control')),
    ('IK_Leg_Pole_L', bpy.props.StringProperty(name='IK Pole')),
    ('IK_Leg_Target_L', bpy.props.StringProperty(name='IK Target')),
    ('IK_Leg_Pole_Target_L', bpy.props.StringProperty(name='IK Pole Target')),
    ('FK_Leg_Upper_R', bpy.props.StringProperty(name='FK Upper')),
    ('FK_Leg_Lower_R', bpy.props.StringProperty(name='FK Lower')),
    ('FK_Leg_End_R', bpy.props.StringProperty(name='FK End')),
    ('IK_Leg_Upper_R', bpy.props.StringProperty(name='IK Upper')),
    ('IK_Leg_Lower_R', bpy.props.StringProperty(name='IK Lower')),
    ('IK_Leg_End_R', bpy.props.StringProperty(name='IK End')),
    ('IK_Leg_Control_R', bpy.props.StringProperty(name='IK Control')),
    ('IK_Leg_Pole_R', bpy.props.StringProperty(name='IK Pole')),
    ('IK_Leg_Target_R', bpy.props.StringProperty(name='IK Target')),
    ('IK_Leg_Pole_Target_R', bpy.props.StringProperty(name='IK Pole Target')),

    # Additional properties for double jointed legs
    ('FK_Leg_Knee_L', bpy.props.StringProperty(name='FK Knee')),
    ('FK_Leg_Knee_R', bpy.props.StringProperty(name='FK Knee')),
    ('IK_Leg_Knee_L', bpy.props.StringProperty(name='IK Knee')),
    ('IK_Leg_Knee_R', bpy.props.StringProperty(name='IK Knee')),

    ('TWEAK_Leg_Knee_R', bpy.props.StringProperty(name='TWEAK Knee')),
    ('TWEAK_Leg_Lower_R', bpy.props.StringProperty(name='TWEAK Lower')),
    ('TWEAK_Leg_Knee_L', bpy.props.StringProperty(name='TWEAK Knee')),
    ('TWEAK_Leg_Lower_L', bpy.props.StringProperty(name='TWEAK Lower'))
]

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#     Register & Unregister     
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def register():
    for (prop_name, prop_value) in PROPS:
        setattr(bpy.types.Scene, prop_name, prop_value)

def unregister():
    for (prop_name, _) in PROPS:
        delattr(bpy.types.Scene, prop_name)
