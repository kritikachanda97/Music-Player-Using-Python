def unmutemusic():
    global currentvol
    root.UnmuteButton.grid_remove()
    root.MuteButton.grid()
    mixer.music.set_volume(currentvol)

def mutemusic():
    global currentvol
    root.MuteButton.grid_remove()
    root.UnmuteButton.grid()
    currentvol = mixer.music.get_volume()
    mixer.music.set_volume(0)

def resumemusic():
    root.ResumeButton.grid_remove()
    root.PauseButton.grid()
    mixer.music.unpause()
    ProgressbarLabel.grid()
    AudioStatusLabel.configure(text = 'Playing......')

def volumeup():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol+0.05)
    ProgressbarVolumeLabel.configure(text = '{}%'.format(int(mixer.music.get_volume()*100)))
    ProgressbarVolume['value'] = mixer.music.get_volume()*100

def volumedown():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol-0.05)
    ProgressbarVolumeLabel.configure(text = '{}%'.format(int(mixer.music.get_volume()*100)))
    ProgressbarVolume['value'] = mixer.music.get_volume()*100

def stopmusic():
    mixer.music.stop()
    ProgressbarLabel.grid_remove()
    ProgressbarMusicLabel.grid_remove()
    AudioStatusLabel.configure(text = 'Stopped......')

def pausemusic():
    mixer.music.pause()
    root.PauseButton.grid_remove()
    root.ResumeButton.grid()
    ProgressbarLabel.grid_remove()
    AudioStatusLabel.configure(text = 'Paused......')

def playmusic():
    audio = audiotrack.get()
    mixer.music.load(audio)
    ProgressbarLabel.grid()
    root.MuteButton.grid()
    ProgressbarMusicLabel.grid()
    mixer.music.set_volume(0.4)
    ProgressbarVolume['value'] = 40
    ProgressbarVolumeLabel['text'] = '40%'
    mixer.music.play()
    AudioStatusLabel.configure(text = 'Playing......')

    Song = MP3(audio)
    totalsonglength = int(Song.info.length)
    ProgressbarMusic['maximum'] = totalsonglength
    ProgressbarMusicEndTimeLabel.configure(text = '{}'.format(str(datetime.timedelta(seconds= totalsonglength))))
    def ProgressbarMusictick():
        CurrentSongLength = mixer.music.get_pos()//1000
        ProgressbarMusic['value'] = CurrentSongLength
        ProgressbarMusicStartTimeLabel.configure(text = '{}'.format(str(datetime.timedelta(seconds= CurrentSongLength))))
        ProgressbarMusic.after(2,ProgressbarMusictick)
    ProgressbarMusictick()

def musicurl():
    try:
        dd = filedialog.askopenfilename(initialdir = 'F:/Songs', title = 'Select audio file', filetype = (('.MP3','*.mp3'), ('WAV','*.wav')))

    except:
        dd = filedialog.askopenfilename(title = 'Select audio file', filetype = (('.MP3','*.mp3'), ('WAV','*.wav')))

    audiotrack.set(dd)

def createwidgets():
    global Imgbrowse
    global Imgplay
    global Imgstop
    global Imgvolumeup
    global Imgvolumedown
    global Imgpause
    global Imgresume
    global Imgmute
    global Imgunmute
    global AudioStatusLabel
    global ProgressbarVolumeLabel
    global ProgressbarVolume
    global ProgressbarLabel
    global ProgressbarMusicLabel
    global ProgressbarMusic
    global ProgressbarMusicEndTimeLabel
    global ProgressbarMusicStartTimeLabel

    ################################################################################################################  Image Icons
    Imgplay = PhotoImage(file = 'Play.png')
    Imgstop = PhotoImage(file = 'Stop.png')
    Imgbrowse = PhotoImage(file = 'Search.png')
    Imgvolumeup = PhotoImage(file = 'Vup.png')
    Imgvolumedown = PhotoImage(file = 'Vdown.png')
    Imgpause = PhotoImage(file = 'Pause.png')
    Imgresume = PhotoImage(file = 'Resume.png')
    Imgmute = PhotoImage(file = 'Mute.png')
    Imgunmute = PhotoImage(file = 'Unmute.png')

    ################################################################################################################  Image Icons Size
    Imgbrowse = Imgbrowse.subsample(15,15)
    Imgplay = Imgplay.subsample(15,15)
    Imgstop = Imgstop.subsample(15,15)
    Imgvolumeup = Imgvolumeup.subsample(15,15)
    Imgvolumedown = Imgvolumedown.subsample(15,15)
    Imgpause = Imgpause.subsample(15,15)
    Imgresume = Imgresume.subsample(15,15)
    Imgmute = Imgmute.subsample(15,15)
    Imgunmute = Imgunmute.subsample(15,15)

    ################################################################################################################ Labels
    TrackLabel = Label(root, text = 'Select audio : ', background = 'lightskyblue', font = ('arial', 15, 'italic bold'), width = 20)
    TrackLabel.grid(row =0, column =0, padx = 20, pady = 20)

    AudioStatusLabel = Label(root, text = '', background = 'lightskyblue', font = ('arial', 15, 'italic bold'))
    AudioStatusLabel.grid(row =2, column =1)

    ################################################################################################################ Entry Box
    TrackLabelEntry = Entry(root, font = ('arial', 16, 'italic bold'), width = 35, textvariable = audiotrack)
    TrackLabelEntry.grid(row =0, column = 1, padx = 20, pady = 20)

    ################################################################################################################ Buttons
    BrowseButton = Button(root, text = 'Search', background = 'deeppink', font = ('arial', 13, 'italic bold'), width = 200, bd = 5,
                          activebackground = 'purple4', image = Imgbrowse, compound = RIGHT, command = musicurl)
    BrowseButton.grid(row =0, column = 2, padx = 20, pady = 20)

    PlayButton = Button(root, text = 'Play', background = 'green2', font = ('arial', 13, 'italic bold'), width = 200, bd = 5,
                        activebackground = 'purple4', image = Imgplay, compound = RIGHT, command = playmusic)
    PlayButton.grid(row =1, column = 0, padx = 20, pady = 20)

    root.PauseButton = Button(root, text = 'Pause', background = 'yellow', font = ('arial', 13, 'italic bold'), width = 200, bd = 5,
                         activebackground = 'purple4', image = Imgpause, compound = RIGHT, command = pausemusic)
    root.PauseButton.grid(row =1, column = 1, padx = 20, pady = 20)

    root.ResumeButton = Button(root, text = 'Resume', background = 'yellow', font = ('arial', 13, 'italic bold'), width = 200, bd = 5,
                         activebackground = 'purple4', image = Imgresume, compound = RIGHT, command = resumemusic)
    root.ResumeButton.grid(row =1, column = 1, padx = 20, pady = 20)
    root.ResumeButton.grid_remove()

    root.MuteButton = Button(root, text = 'Mute', width = 100, bg = 'yellow', activebackground = 'purple4', bd = 5,
                             image = Imgmute, compound = RIGHT, command = mutemusic)
    root.MuteButton.grid(row =3, column = 3)
    root.MuteButton.grid_remove()

    root.UnmuteButton = Button(root, text = 'Unmute', width = 100, bg = 'yellow', activebackground = 'purple4', bd = 5,
                             image = Imgunmute, compound = RIGHT, command = unmutemusic)
    root.UnmuteButton.grid(row =3, column = 3)
    root.UnmuteButton.grid_remove()

    VolumeUpButton = Button(root, text = 'VolumeUp', background = 'blue', font = ('arial', 13, 'italic bold'), width = 200, bd = 5,
                            activebackground = 'purple4', image = Imgvolumeup, compound = RIGHT, command = volumeup)
    VolumeUpButton.grid(row =1, column = 2, padx = 20, pady = 20)

    StopButton = Button(root, text = 'Stop', background = 'red', font = ('arial', 13, 'italic bold'), width = 200, bd = 5,
                        activebackground = 'purple4', image = Imgstop, compound = RIGHT, command = stopmusic)
    StopButton.grid(row =2, column = 0, padx = 20, pady = 20)

    VolumeDownButton = Button(root, text = 'VolumeDown', background = 'blue', font = ('arial', 13, 'italic bold'), width = 200, bd = 5,
                              activebackground = 'purple4', image = Imgvolumedown, compound = RIGHT, command = volumedown)
    VolumeDownButton.grid(row =2, column = 2, padx = 20, pady = 20)

################################################################################################################## Progress Bar
    ProgressbarLabel = Label(root, text = '', bg = 'red')
    ProgressbarLabel.grid(row = 0, column = 3, rowspan = 3, padx = 20, pady = 20)
    ProgressbarLabel.grid_remove()

    ProgressbarVolume = Progressbar(ProgressbarLabel, orient = VERTICAL, mode = 'determinate', value = 0, length = 190)
    ProgressbarVolume.grid(row = 0, column = 0, ipadx = 5)

    ProgressbarVolumeLabel = Label(ProgressbarLabel, text = '0%', bg = 'lightgrey', width = 3)
    ProgressbarVolumeLabel.grid(row = 0, column = 0)
    ############################################################################################################# Progressbar Music
    ProgressbarMusicLabel = Label(root, text = '', bg = 'red')
    ProgressbarMusicLabel.grid(row = 3, column = 0, columnspan = 3, padx = 20, pady = 20)
    ProgressbarMusicLabel.grid_remove()

    ProgressbarMusicStartTimeLabel = Label(ProgressbarMusicLabel, text = '0:00:0', bg = 'red')
    ProgressbarMusicStartTimeLabel.grid(row = 0, column = 0)

    ProgressbarMusicEndTimeLabel = Label(ProgressbarMusicLabel, text = '0:00:0', bg = 'red')
    ProgressbarMusicEndTimeLabel.grid(row = 0, column = 2)

    ProgressbarMusic = Progressbar(ProgressbarMusicLabel, orient = HORIZONTAL, mode = 'determinate', value = 0)
    ProgressbarMusic.grid(row = 0, column = 1, ipadx = 370, ipady = 3)

##################################################################################################################
from tkinter import *
from tkinter import filedialog
from pygame import mixer
import datetime
from mutagen.mp3 import MP3
from tkinter.ttk import Progressbar
root = Tk()
root.geometry('1100x500+200+50')
root.title('Music Player')
root.resizable(False,False)
root.configure(bg = 'lightskyblue')

########################################################################################################### Global variables
audiotrack = StringVar()
currentvol = 0
totalsonglength = 0
count = 0
text = ""

############################################################################################################ Slider
ss = 'Developed By Kritika Chanda'
SliderLabel = Label(root, text = ss, bg = 'lightskyblue', font = ('arial', 40, 'italic bold'))
SliderLabel.grid(row =4, column = 0, padx = 20, pady = 20, columnspan = 3)
def Slide():
    global count,text
    if(count>=len(ss)):
        count = -1
        text = ''
        SliderLabel.configure(text=text)
    else:
        text = text+ss[count]
        SliderLabel.configure(text=text)
    count +=1
    SliderLabel.after(200,Slide)
Slide()
mixer.init()
createwidgets()
root.mainloop()