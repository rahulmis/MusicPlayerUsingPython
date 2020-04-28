def unmutemusic():
    global currentvol
    root.unmutebutton.grid_remove()
    root.mutebutton.grid()
    mixer.music.set_volume(currentvol)

def mutemusic():
    global currentvol
    root.mutebutton.grid_remove()
    root.unmutebutton.grid()
    currentvol = mixer.music.get_volume()
    mixer.music.set_volume(0)

def resumemusic():
    root.ResumeButton.grid_remove()
    root.PauseButton.grid()
    mixer.music.unpause()
    AudioStatusLabel.configure(text='playing......')


def volumeup():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol+0.05)
    ProgressbarVolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    ProgressbarVolume['value'] = mixer.music.get_volume()*100

def volumedown():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol-0.05)
    ProgressbarVolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    ProgressbarVolume['value'] = mixer.music.get_volume()*100

def stopmusic():
    mixer.music.stop()
    AudioStatusLabel.configure(text='Stopped......')

def pausemusic():
    mixer.music.pause()
    root.PauseButton.grid_remove()
    root.ResumeButton.grid()
    AudioStatusLabel.configure(text='Paused......')

def playmusic():
    ad = audiotrack.get()
    mixer.music.load(ad)
    ProgressbarLabel.grid()
    root.mutebutton.grid()
    ProgressbarMusicLabel.grid()
    mixer.music.set_volume(0.4)
    ProgressbarVolume['value'] = 40
    ProgressbarVolumeLabel['text'] = '40%'
    mixer.music.play()
    AudioStatusLabel.configure(text='playing......')

    Song = MP3(ad)
    totalsonglength = int(Song.info.length)
    ProgressbarMusic['maximum'] = totalsonglength
    ProgressbarMusicEndTimeLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=totalsonglength))))
    def Progresbarmusictick():
        CurrenSongLength = mixer.music.get_pos()//1000
        ProgressbarMusic['value'] = CurrenSongLength
        ProgressbarMusicStartTimeLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=CurrenSongLength))))
        ProgressbarMusic.after(2,Progresbarmusictick)
    Progresbarmusictick()

def musicurl():
    try:
        dd = filedialog.askopenfilename(initialdir='C:Users/ASUS/Desktop/codes',
                                        title='Select Audio File',
                                        filetype=(('MP3','*.mp3'),('WAV','*.wav')))
    except:
        dd = filedialog.askopenfilename(title='Select Audio File',
                                        filetype=(('MP3','*.mp3'),('WAV','*.wav')))
    # print(ff[-1])
    audiotrack.set(dd)
    ff = dd.split('/')
    audiotrack1.set(ff[-1])

def createwidthes():
    global implay,impause,imbrowse,imvolumeup,imvolumedown,imstop,imresume,immute,imunmute
    global AudioStatusLabel,ProgressbarVolumeLabel,ProgressbarVolume,ProgressbarLabel,ProgressbarMusicLabel,ProgressbarMusic,ProgressbarMusicEndTimeLabel,ProgressbarMusicStartTimeLabel

    ########################################################################  Images Register
    implay = PhotoImage(file='play.png')
    impause = PhotoImage(file='pause.png')
    imbrowse = PhotoImage(file='browsing.png')
    imvolumeup = PhotoImage(file='volume-up.png')
    imvolumedown = PhotoImage(file='volume-down.png')
    imstop = PhotoImage(file='stop.png')
    imresume = PhotoImage(file='stop1.png')
    immute = PhotoImage(file='mute.png')
    imunmute = PhotoImage(file='muted.png')

    ################################################################ Change size of images
    implay = implay.subsample(2,2)
    impause = impause.subsample(2,2)
    imbrowse = imbrowse.subsample(2,2)
    imvolumeup = imvolumeup.subsample(2,2)
    imvolumedown = imvolumedown.subsample(2,2)
    imstop = imstop.subsample(2,2)
    imresume = imresume.subsample(2,2)
    immute = immute.subsample(2,2)
    imunmute = imunmute.subsample(2,2)

    #############################################################################################################  Labels
    TrackLabel = Label(root,text='Select Audio Track : ',background='lightskyblue',font=('arial',15,'italic bold'))
    TrackLabel.grid(row=0,column=0,padx=20,pady=20)

    AudioStatusLabel = Label(root,text='',background='lightskyblue',font=('arial',15,'italic bold'),width=20)
    AudioStatusLabel.grid(row=2,column=1)

    ############################################################################################################## Entry Box
    TrackLabelEntry = Entry(root,font=('arial',16,'italic bold'),width=35,textvariable=audiotrack1)
    TrackLabelEntry.grid(row=0,column=1,padx=20,pady=20)

    ############################################################################################################## Buttons
    BrowseButton = Button(root,text='Search',bg='deeppink',font=('arial',13,'italic bold'),width=200,bd=5,
                          activebackground='purple4',image=imbrowse,compound=RIGHT,command=musicurl)
    BrowseButton.grid(row=0,column=2,padx=20,pady=20)

    PlayButton = Button(root,text='Play',bg='green2',font=('arial',13,'italic bold'),width=200,bd=5,
                        activebackground='purple4',image=implay,compound=RIGHT,command=playmusic)
    PlayButton.grid(row=1,column=0,padx=20,pady=20)

    root.PauseButton = Button(root,text='Pause',bg='yellow',font=('arial',13,'italic bold'),width=200,bd=5,
                         activebackground='purple4',image=impause,compound=RIGHT,command=pausemusic)
    root.PauseButton.grid(row=1,column=1,padx=20,pady=20)

    root.ResumeButton = Button(root,text='Resume',bg='yellow',font=('arial',13,'italic bold'),width=200,bd=5,
                         activebackground='purple4',image=imresume,compound=RIGHT,command=resumemusic)
    root.ResumeButton.grid(row=1,column=1,padx=20,pady=20)
    root.ResumeButton.grid_remove()

    root.mutebutton = Button(root,text='Mute',width=100,bg='yellow',activebackground='purple4',bd=5,
                             image=immute,compound=RIGHT,command=mutemusic)
    root.mutebutton.grid(row=3,column=3)
    root.mutebutton.grid_remove()

    root.unmutebutton = Button(root,text='UnMute',width=100,bg='yellow',activebackground='purple4',bd=5,
                             image=imunmute,compound=RIGHT,command=unmutemusic)
    root.unmutebutton.grid(row=3,column=3)
    root.unmutebutton.grid_remove()

    VolumeUpButton = Button(root,text='VolumeUp',bg='blue',font=('arial',13,'italic bold'),width=200,bd=5,
                            activebackground='purple4',image=imvolumeup,compound=RIGHT,command=volumeup)
    VolumeUpButton.grid(row=1,column=2,padx=20,pady=20)

    StopButton = Button(root,text='Stop',bg='red',font=('arial',13,'italic bold'),width=200,bd=5,
                        activebackground='purple4',image=imstop,compound=RIGHT,command=stopmusic)
    StopButton.grid(row=2,column=0,padx=20,pady=20)

    VolumeDownButton = Button(root,text='VolumeDown',bg='blue',font=('arial',13,'italic bold'),width=200,bd=5,
                              activebackground='purple4',image=imvolumedown,compound=RIGHT,command=volumedown)
    VolumeDownButton.grid(row=2,column=2,padx=20,pady=20)
    #############################################################################################  Progressbar Volume
    ProgressbarLabel = Label(root,text='',bg='red')
    ProgressbarLabel.grid(row=0,column=3,rowspan=3,padx=20,pady=20)

    ProgressbarVolume = Progressbar(ProgressbarLabel,orient=VERTICAL,mode='determinate',
                                    value=0,length=190)
    ProgressbarVolume.grid(row=0,column=0,ipadx=5)

    ProgressbarVolumeLabel = Label(ProgressbarLabel,text='0%',bg='lightgray',width=3)
    ProgressbarVolumeLabel.grid(row=0,column=0)
    ProgressbarLabel.grid_remove()

    ##########################################################################################  ProgressBar Music
    ProgressbarMusicLabel = Label(root,text='',bg='red')
    ProgressbarMusicLabel.grid(row=3,column=0,columnspan=3,padx=20,pady=20)
    ProgressbarMusicLabel.grid_remove()

    ProgressbarMusicStartTimeLabel = Label(ProgressbarMusicLabel, text='0:00:0', bg='red',width=6)
    ProgressbarMusicStartTimeLabel.grid(row=0, column=0)

    ProgressbarMusic = Progressbar(ProgressbarMusicLabel,orient=HORIZONTAL,mode='determinate',value=0)
    ProgressbarMusic.grid(row=0,column=1,ipadx=370,ipady=3)

    ProgressbarMusicEndTimeLabel = Label(ProgressbarMusicLabel,text='0:00:0', bg='red')
    ProgressbarMusicEndTimeLabel.grid(row=0, column=2)


################################################################################
from tkinter import *
from tkinter import filedialog
from pygame import mixer
from tkinter.ttk import Progressbar
import datetime
from mutagen.mp3 import MP3
root = Tk()
root.geometry('1100x500+200+50')
root.title('Simple Music Player..')
root.iconbitmap('music.ico')
root.resizable(False,False)
root.configure(bg='lightskyblue')
############################################################################# Gloabl Vraiables
audiotrack = StringVar()
audiotrack1 = StringVar()
currentvol = 0
totalsonglength=0
count = 0
text = ''
##############################################################################   Create Slider
ss = 'Developed By Rahul Mishra'
SliderLabel = Label(root,text=ss,bg='lightskyblue',font=('arial',40,'italic bold'))
SliderLabel.grid(row=4,column=0,padx=20,pady=20,columnspan=3)
def IntroLabelTRick():
    global count,text
    if(count>=len(ss)):
        count = -1
        text = ''
        SliderLabel.configure(text=text)
    else:
        text = text+ss[count]
        SliderLabel.configure(text=text)
    count += 1
    SliderLabel.after(200,IntroLabelTRick)

IntroLabelTRick()
mixer.init()
createwidthes()
root.mainloop()


