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

def register():
    for mod in modules:
        mod.register()

def unregister():
    for mod in reversed(modules):
        mod.unregister()