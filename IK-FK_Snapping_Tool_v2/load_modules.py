import importlib

#━━━━━━━━━━━━━━━━━━━━━━
#     Load Modules     
#━━━━━━━━━━━━━━━━━━━━━━

if "bpy" in locals():
    importlib.reload(ui)
    importlib.reload(operators)
    importlib.reload(utilities)
else:
    from . import (
        ui,
        operators,
        utilities
    )

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#     Register & Unregister     
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

modules = (
    ui,
    operators,
    utilities
)

def register(bl_info):
    for mod in modules:
        mod.register()

def unregister(bl_info):
    for mod in reversed(modules):
        mod.unregister()