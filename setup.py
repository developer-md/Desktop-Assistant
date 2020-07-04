from cx_Freeze import setup, Executable
import sys

base = None    
if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable("main.py", base=base)]

packages = ["idna","speech_recognition","os","random","time","datetime","webbrowser","wikipedia","pyttsx3","pyaudio","pywhatkit","keyboard","pyautogui","tkinter","PIL","smtplib"]
options = {
    'build_exe': {    
        'packages':packages,
        'includes':["tkinter"]
    },    
}

setup(
    name = "<Panda-the assistant app>",
    options = options,
    version = "1.0",
    description = '<This is a desktop application that assist his owner by speech. >',
    executables = executables
)