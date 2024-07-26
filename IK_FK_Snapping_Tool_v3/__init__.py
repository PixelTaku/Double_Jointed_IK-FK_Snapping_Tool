'''
  _____ _  __     ______ _  __   _____                         _               _______          _ 
 |_   _| |/ /    |  ____| |/ /  / ____|                       (_)             |__   __|        | |
   | | | ' /_____| |__  | ' /  | (___  _ __   __ _ _ __  _ __  _ _ __   __ _     | | ___   ___ | |
   | | |  <______|  __| |  <    \___ \| '_ \ / _` | '_ \| '_ \| | '_ \ / _` |    | |/ _ \ / _ \| |
  _| |_| . \     | |    | . \   ____) | | | | (_| | |_) | |_) | | | | | (_| |    | | (_) | (_) | |
 |_____|_|\_\    |_|    |_|\_\ |_____/|_| |_|\__,_| .__/| .__/|_|_| |_|\__, |    |_|\___/ \___/|_|
                                                  | |   | |             __/ |                     
                                                  |_|   |_|            |___/                      

                            [   MIT License   ]

 Copyright (c) 2022 Byron Mallett
 Copyright (c) 2024 Endertainer007
 
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
    load_modules.register()

def unregister():
    load_modules.unregister()

if __name__ == "__main__":
    register()