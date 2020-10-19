from cx_Freeze import *
includefiles = ['Mute.png', 'Pause.png', 'Play.png', 'Resume.png', 'Search.png', 'Stop.png', 'Unmute.png', 'Vdown.png', 'vup.png']
excludes = []
packages = []
base = None
if sys.platform == "win64":
    base = "Win64GUI"

shortcut_table = [
    ("DesktopShortcut", # Shortcut
     "DesktopFolder", # Directory_
     "Music Player", # Name
    "TARGETDIR", # Component
    "[TARGETDIR]\Music.exe",   # Target
        None,   # Arguments
        None,   # Description
        None,   #Hotkey
        None,   # Icon
        None,   # IconIndex
        None,   # Showcmd
        "TARGETDIR",   # WkDir
    )
]

msi_data = {"Shortcut": shortcut_table}

bdist_msi_options = {'data': msi_data}
setup(
    version = "0.1",
    description = "Music Player Developed By Kritika Chanda",
    author = "Kritika Chanda",
    name = "Music Player",
    options = {'build_exe': {'include_files': includefiles}, "bdist_msi": bdist_msi_options, },
    executables = [
        Executable(
            script="Music.py",
            base=base,
        )
    ]
)