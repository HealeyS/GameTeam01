#libraries <3
import os, time, vlc



#forces the screen to be ~90x40 <3
#os.system('mode con: cols=91 lines=43') #this was for testing <3

def transition_flash():
    transition = vlc.MediaPlayer("file:///D:/Dropbox/Cardiff/CM1101/Week_4/GameTeam01/transition.mp3")
    transition.play()
    
    os.system('cls')
    for x in range(0,40):
        print("##########################################################################################")
    time.sleep(0.2)

    for y in range(0,9):
        if y%2 == 0:
            os.system('cls')
            for z in range(0,40):
                print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ")
            time.sleep(0.2)
        else:
            os.system('cls')
            for z in range(0,40):
                print(" # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.2)

    transition.stop()
