# IK-FK Snapping Tool ![Latest Release (latest SemVer)](https://img.shields.io/github/v/release/Endertainer/IK-FK_Snapping_Tool?color=important&label=Latest%20Release) ![License](https://img.shields.io/github/license/Endertainer/IK-FK_Snapping_Tool?color=informational) ![Downloads](https://img.shields.io/github/downloads/Endertainer/IK-FK_Snapping_Tool/total?color=lightgrey&label=Downloads)

## Introduction
IK-FK Snapping Tool is a Blender add-on that allows you to snap the IK and FK control from IK to FK and vice versa.

This version of the add-on is a forked version of the original IK-FK-Snapping-for-Blender add-on by [Mystfit](https://github.com/Mystfit). This forked version comes with some modifications and improvements over the original version. One of the improvement added in this version is the addition of IK Target and IK Pole Target fields.

## Instruction
- To start using the add-on, install the IK-FK_Snapping_Tool.py file.
- In the viewport, go to the Sidebar > IK-FK Snap tab.
- In the Armature & Bones panel, enter the name of the Armature you want to target in the Armature field (Note that your rig needs to have the same Armature and Object name. Otherwise, the add-on wouldn't work).
- Fill the rest of the Bone field. What you fill the field with depends on what you want to snap. For example, if you want to snap the Left Arm, then you'll fill it like this: FK Upper = Shoulder_FK_L, FK Lower = Elbow_FK_L, FK End = Wrist_FK_L, IK Upper = Shoulder_IK_L, IK Lower = Elbow_IK_L, IK End = Wrist_IK_L, IK Effector = Arm_IK_Control_L, IK Pole = Arm_IK_Pole_L, IK Target = Arm_IK_Target_L, IK Pole Target = Arm_IK_Pole_Target_L.
- Once you set up all of the bones, you can use the Limb presets button in the upper right corner of the FK & IK Bones panel to create another preset. You can also switch your presets here (Note that if you want to change a bone or rename a preset, you need to delete and remake it from scratch).
- To do the snapping, click Snap to FK to snap the IK control to FK, or Snap to IK to snap the FK control to IK.
- If you want the add-on to automatically snap and key your controls over a frame range, check the Key across frame range option on the IK-FK Snapping panel and enter a start and end frame.

If you need help, you can join my [Discord](https://discord.com/invite/vANwCrPPBu) server.
