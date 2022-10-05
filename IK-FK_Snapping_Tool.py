import bpy
from mathutils import Matrix, Vector
from bl_ui.utils import PresetPanel
from bl_operators.presets import AddPresetBase

bl_info = {
    # required
    'name': 'IK-FK Snapping Tool',
    'blender': (3, 3, 0),
    'category': 'Animation',
    'location': 'View3D > Sidebar > IK-FK Snap',
    'version': (1, 0, 0),
    'author': 'Byron Mallett (Edited by Endertainer007)',
    'warning': '',
    'description': 'Tools to perform IK to FK and FK to IK snapping',
}

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


class MT_LimbPresets(bpy.types.Menu): 
    bl_label = 'Limb Presets' 
    bl_idname = 'MT_LimbPresets'
    preset_subdir = 'object/FKIKSnap_presets' 
    preset_operator = 'script.execute_preset' 
    draw = bpy.types.Menu.draw_preset
    
    
class MY_PT_presets(PresetPanel, bpy.types.Panel):
    bl_label = 'Limb Presets'
    preset_subdir = 'object/FKIKSnap_presets'
    preset_operator = 'script.execute_preset'
    preset_add_operator = 'my.add_preset'


class FKIKSnapPanel(bpy.types.Panel):
    bl_idname = 'VIEW3D_PT_fk_to_ik_snap'
    bl_label = 'IK-FK Snapping'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'IK-FK Snap'
    
    def draw_header_preset(self, _context): 
        MY_PT_presets.draw_panel_header(self.layout)
    
    def draw(self, context):
        col = self.layout.column()
        row = col.row()
        row.prop(context.scene, "use_frame_range")
        row = col.row()
        row.prop(context.scene, "start_frame")
        row.enabled = context.scene.use_frame_range
        row = row.row()
        row.prop(context.scene, "end_frame")
        row.enabled = context.scene.use_frame_range

        grid = self.layout.grid_flow(columns=2, align=True)
        if context.scene.FK_control_upper_name and context.scene.FK_control_lower_name:
            snap_ik_to_fk_operator = grid.operator('opr.snap_ik_to_fk_operator', text='Snap to FK')
        if context.scene.IK_control_upper_name and context.scene.IK_control_lower_name:
            snap_fk_to_ik_operator = grid.operator('opr.snap_fk_to_ik_operator', text='Snap to IK')
            

class FKIKMappingPanel(bpy.types.Panel):
    bl_idname = 'VIEW3D_PT_fk_to_ik_mapping'
    bl_label = 'Armature & Bones'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'IK-FK Snap'
    
    def draw_header_preset(self, _context): 
        MY_PT_presets.draw_panel_header(self.layout)
    
    def draw(self, context):
        col = self.layout.column()
        col.prop_search(context.scene, "armature_name", bpy.data, "armatures")
        arma = bpy.data.armatures.get(context.scene.armature_name)
        if arma is not None:
            col.prop_search(context.scene, "FK_control_upper_name", arma, "bones")
            col.prop_search(context.scene, "FK_control_lower_name", arma, "bones")
            col.prop_search(context.scene, "FK_control_end_name", arma, "bones")
            col.prop_search(context.scene, "IK_control_upper_name", arma, "bones")
            col.prop_search(context.scene, "IK_control_lower_name", arma, "bones")
            col.prop_search(context.scene, "IK_control_end_name", arma, "bones")
            col.prop_search(context.scene, "IK_control_name", arma, "bones")
            col.prop_search(context.scene, "IK_control_pole_name", arma, "bones")
            col.prop_search(context.scene, "IK_control_target_name", arma, "bones")
            col.prop_search(context.scene, "IK_control_pole_target_name", arma, "bones")


class SnapIKtoFKOperator(bpy.types.Operator):
    bl_idname = 'opr.snap_ik_to_fk_operator'
    bl_label = 'Snap to FK'

    def execute(self, context):
        arma = bpy.data.objects[context.scene.armature_name]
        start_frame = context.scene.start_frame if context.scene.use_frame_range else -1
        end_frame = context.scene.end_frame if context.scene.use_frame_range else -1
        
        if start_frame < 0 or end_frame < 0:
            start_frame = bpy.context.scene.frame_current
            end_frame = start_frame + 1
        
        for frame in range(start_frame, end_frame):
            bpy.context.scene.frame_set(frame)
            self.snap_IK_to_FK(
                arma.pose.bones[context.scene.IK_control_pole_target_name],
                arma.pose.bones[context.scene.IK_control_target_name],
                arma.pose.bones[context.scene.FK_control_end_name],
                arma.pose.bones[context.scene.IK_control_pole_name],
                arma.pose.bones[context.scene.IK_control_name],
                arma.pose.bones[context.scene.IK_control_end_name],
            )
            
            if context.scene.use_frame_range:
                arma.pose.bones[context.scene.IK_control_pole_name].keyframe_insert('location', frame=frame)
                arma.pose.bones[context.scene.IK_control_pole_name].keyframe_insert('rotation_quaternion', frame=frame)
                arma.pose.bones[context.scene.IK_control_name].keyframe_insert('location', frame=frame)
                arma.pose.bones[context.scene.IK_control_name].keyframe_insert('rotation_quaternion', frame=frame)
                arma.pose.bones[context.scene.IK_control_end_name].keyframe_insert('location', frame=frame)
                arma.pose.bones[context.scene.IK_control_end_name].keyframe_insert('rotation_quaternion', frame=frame)
            
        return {'FINISHED'}
    
    def snap_IK_to_FK(self, IK_pole_target, IK_target, FK_end, IK_pole, IK_effector, IK_end):
        IK_pole.matrix = IK_pole_target.matrix
        bpy.context.view_layer.update()
        
        IK_effector.matrix = IK_target.matrix
        bpy.context.view_layer.update()
        
        IK_relative_to_FK = FK_end.bone.matrix_local.inverted() @ IK_end.bone.matrix_local
        IK_end.matrix = FK_end.matrix @ IK_relative_to_FK


class SnapFKtoIKOperator(bpy.types.Operator):
    bl_idname = 'opr.snap_fk_to_ik_operator'
    bl_label = 'Snap to IK'

    def execute(self, context):
        arma = bpy.data.objects[context.scene.armature_name]
        start_frame = context.scene.start_frame if context.scene.use_frame_range else -1
        end_frame = context.scene.end_frame if context.scene.use_frame_range else -1
        
        if start_frame < 0 or end_frame < 0:
            start_frame = bpy.context.scene.frame_current
            end_frame = start_frame + 1
        
        for frame in range(start_frame, end_frame):
            bpy.context.scene.frame_set(frame)
            self.snap_FK_to_IK(
                arma.pose.bones[context.scene.IK_control_upper_name],
                arma.pose.bones[context.scene.IK_control_lower_name],
                arma.pose.bones[context.scene.IK_control_end_name],
                arma.pose.bones[context.scene.FK_control_upper_name],
                arma.pose.bones[context.scene.FK_control_lower_name],
                arma.pose.bones[context.scene.FK_control_end_name],
            )
            
            if context.scene.use_frame_range:
                arma.pose.bones[context.scene.FK_control_upper_name].keyframe_insert('location', frame=frame)
                arma.pose.bones[context.scene.FK_control_upper_name].keyframe_insert('rotation_quaternion', frame=frame)
                arma.pose.bones[context.scene.FK_control_lower_name].keyframe_insert('location', frame=frame)
                arma.pose.bones[context.scene.FK_control_lower_name].keyframe_insert('rotation_quaternion', frame=frame)
                arma.pose.bones[context.scene.FK_control_end_name].keyframe_insert('location', frame=frame)
                arma.pose.bones[context.scene.FK_control_end_name].keyframe_insert('rotation_quaternion', frame=frame)
            
        return {'FINISHED'}
    
    def snap_FK_to_IK(self, IK_upper, IK_lower, IK_end, FK_upper, FK_lower, FK_end):
        FK_upper.matrix = IK_upper.matrix
        bpy.context.view_layer.update()
        
        FK_lower.matrix = IK_lower.matrix
        bpy.context.view_layer.update()
        
        FK_relative_to_IK = IK_end.bone.matrix_local.inverted() @ FK_end.bone.matrix_local
        FK_end.matrix = IK_end.matrix @ FK_relative_to_IK
        

class AddLimbPresetOperator(AddPresetBase, bpy.types.Operator):
    bl_idname = 'my.add_preset'
    bl_label = 'Add A preset'
    preset_menu = 'MT_LimbPresets'

    # Common variable used for all preset values
    preset_defines = [
                        'obj = bpy.context.object',
                        'scene = bpy.context.scene'
                     ]

    # Properties to store in the preset
    preset_values = [
                        'scene.armature_name',
                        'scene.FK_control_upper_name',
                        'scene.FK_control_lower_name',
                        'scene.FK_control_end_name',
                        'scene.IK_control_upper_name',
                        'scene.IK_control_lower_name',
                        'scene.IK_control_end_name',
                        'scene.IK_control_name',
                        'scene.IK_control_pole_name',
                        'scene.IK_control_target_name',
                        'scene.IK_control_pole_target_name'
                    ]

    # Directory to store the presets
    preset_subdir = 'object/FKIKSnap_presets'
    

def register():
    for (prop_name, prop_value) in PROPS:
        setattr(bpy.types.Scene, prop_name, prop_value)
    
    for klass in CLASSES:
        bpy.utils.register_class(klass)


def unregister():
    for (prop_name, _) in PROPS:
        delattr(bpy.types.Scene, prop_name)

    for klass in CLASSES:
        bpy.utils.unregister_class(klass)
        

PROPS = [
    ('armature_search', bpy.props.EnumProperty(items=arma_items, update=arma_upd)),
    ('bone_collection', bpy.props.CollectionProperty(type=bpy.types.PropertyGroup)),
    ('armature_name', bpy.props.StringProperty(name='Armature')),
    ('FK_control_upper_name', bpy.props.StringProperty(name='FK Upper')),
    ('FK_control_lower_name', bpy.props.StringProperty(name='FK Lower')),
    ('FK_control_end_name', bpy.props.StringProperty(name='FK End')),
    ('IK_control_name', bpy.props.StringProperty(name='IK Effector')),
    ('IK_control_pole_name', bpy.props.StringProperty(name='IK Pole')),
    ('IK_control_upper_name', bpy.props.StringProperty(name='IK Upper')),
    ('IK_control_lower_name', bpy.props.StringProperty(name='IK Lower')),
    ('IK_control_end_name', bpy.props.StringProperty(name='IK End')),
    ('IK_control_target_name', bpy.props.StringProperty(name='IK Target')),
    ('IK_control_pole_target_name', bpy.props.StringProperty(name='IK Pole Target')),
    ('use_frame_range', bpy.props.BoolProperty(name='Key across frame range', default=False)),
    ('start_frame', bpy.props.IntProperty(name='Start frame', default=0)),
    ('end_frame', bpy.props.IntProperty(name='End frame', default=0)),
]

CLASSES = [
    SnapIKtoFKOperator,
    SnapFKtoIKOperator,
    AddLimbPresetOperator,
    FKIKSnapPanel,
    FKIKMappingPanel,
    MY_PT_presets, 
    MT_LimbPresets
]


if __name__ == '__main__':
    register()
