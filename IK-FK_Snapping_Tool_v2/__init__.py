'''
                            [   MIT License   ]

 Copyright (c) 2022 Byron Mallett
 
 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.
 '''

#━━━━━━━━━━━━━━
#     Info     
#━━━━━━━━━━━━━━

bl_info = {
    'name': 'IK-FK Snapping Tool',
    'blender': (3, 3, 1),
    'category': 'Animation',
    'location': 'View3D > Sidebar > IK-FK Snap',
    'version': (2, 0, 0),
    'author': 'Byron Mallett (Modified by Endertainer007)',
    'description': 'Tools to perform IK to FK and FK to IK snapping',
}

#━━━━━━━━━━━━━━━━━━━━━━
#     Load Modules     
#━━━━━━━━━━━━━━━━━━━━━━

if "load_modules" in locals():
    importlib.reload(load_modules)
else:
    from . import load_modules

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#     Register & Unregister     
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def register():
    load_modules.register(bl_info)

def unregister():
    load_modules.unregister(bl_info)

if __name__ == "__main__":
    register()