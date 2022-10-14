import bpy

#━━━━━━━━━━━━━━━━━━━━━━━━━━━
#     Functions & Utils     
#━━━━━━━━━━━━━━━━━━━━━━━━━━━

def arma_items(self, context):
    obs = []
    for ob in context.scene.objects:
        if ob.type == 'ARMATURE':
            obs.append((ob.name, ob.name, ""))
    return obs

def arma_upd(self, context):
    self.arma_coll.clear()
    for ob in context.scene.objects:
        if ob.type == 'ARMATURE':
            item = self.arma_coll.add()
            item.name = ob.name

PROPS = [
    ('armature_search', bpy.props.EnumProperty(items=arma_items, update=arma_upd)),
    ('bone_collection', bpy.props.CollectionProperty(type=bpy.types.PropertyGroup)),
    ('armature_name', bpy.props.StringProperty(name='Armature')),
    ('FK_Arm_Upper_L', bpy.props.StringProperty(name='FK Upper')),
    ('FK_Arm_Lower_L', bpy.props.StringProperty(name='FK Lower')),
    ('FK_Arm_End_L', bpy.props.StringProperty(name='FK End')),
    ('IK_Arm_Upper_L', bpy.props.StringProperty(name='IK Upper')),
    ('IK_Arm_Lower_L', bpy.props.StringProperty(name='IK Lower')),
    ('IK_Arm_End_L', bpy.props.StringProperty(name='IK End')),
    ('IK_Arm_Effector_L', bpy.props.StringProperty(name='IK Effector')),
    ('IK_Arm_Pole_L', bpy.props.StringProperty(name='IK Pole')),
    ('IK_Arm_Target_L', bpy.props.StringProperty(name='IK Target')),
    ('IK_Arm_Pole_Target_L', bpy.props.StringProperty(name='IK Pole Target')),
    ('FK_Arm_Upper_R', bpy.props.StringProperty(name='FK Upper')),
    ('FK_Arm_Lower_R', bpy.props.StringProperty(name='FK Lower')),
    ('FK_Arm_End_R', bpy.props.StringProperty(name='FK End')),
    ('IK_Arm_Upper_R', bpy.props.StringProperty(name='IK Upper')),
    ('IK_Arm_Lower_R', bpy.props.StringProperty(name='IK Lower')),
    ('IK_Arm_End_R', bpy.props.StringProperty(name='IK End')),
    ('IK_Arm_Effector_R', bpy.props.StringProperty(name='IK Effector')),
    ('IK_Arm_Pole_R', bpy.props.StringProperty(name='IK Pole')),
    ('IK_Arm_Target_R', bpy.props.StringProperty(name='IK Target')),
    ('IK_Arm_Pole_Target_R', bpy.props.StringProperty(name='IK Pole Target')),
    ('FK_Leg_Upper_L', bpy.props.StringProperty(name='FK Upper')),
    ('FK_Leg_Lower_L', bpy.props.StringProperty(name='FK Lower')),
    ('FK_Leg_End_L', bpy.props.StringProperty(name='FK End')),
    ('IK_Leg_Upper_L', bpy.props.StringProperty(name='IK Upper')),
    ('IK_Leg_Lower_L', bpy.props.StringProperty(name='IK Lower')),
    ('IK_Leg_End_L', bpy.props.StringProperty(name='IK End')),
    ('IK_Leg_Effector_L', bpy.props.StringProperty(name='IK Effector')),
    ('IK_Leg_Pole_L', bpy.props.StringProperty(name='IK Pole')),
    ('IK_Leg_Target_L', bpy.props.StringProperty(name='IK Target')),
    ('IK_Leg_Pole_Target_L', bpy.props.StringProperty(name='IK Pole Target')),
    ('FK_Leg_Upper_R', bpy.props.StringProperty(name='FK Upper')),
    ('FK_Leg_Lower_R', bpy.props.StringProperty(name='FK Lower')),
    ('FK_Leg_End_R', bpy.props.StringProperty(name='FK End')),
    ('IK_Leg_Upper_R', bpy.props.StringProperty(name='IK Upper')),
    ('IK_Leg_Lower_R', bpy.props.StringProperty(name='IK Lower')),
    ('IK_Leg_End_R', bpy.props.StringProperty(name='IK End')),
    ('IK_Leg_Effector_R', bpy.props.StringProperty(name='IK Effector')),
    ('IK_Leg_Pole_R', bpy.props.StringProperty(name='IK Pole')),
    ('IK_Leg_Target_R', bpy.props.StringProperty(name='IK Target')),
    ('IK_Leg_Pole_Target_R', bpy.props.StringProperty(name='IK Pole Target'))
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