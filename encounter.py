#https://books.google.co.uk/books?id=0deFa0SWTOkC&pg=PA242&lpg=PA242&dq=down+-+80,+up+%3D+72&source=bl&ots=yhd3kA7g92&sig=y_D-B3Qw0dRprDZmvad6xGwozd0&hl=en&sa=X&ved=0ahUKEwjN39y6sNfPAhUhD8AKHeyaAVUQ6AEIIzAA#v=onepage&q=down%20-%2080%2C%20up%20%3D%2072&f=false
#if anything dies in this module throw me a message <3

#libraries <3
import os, time, random, sys, msvcrt, vlc

#local variables <3
beat_counter = 0
beat = 10
counter = 0
random_value = 0
wait_time = 0.1
last_score = "       "
audio_on = False
audio = vlc.MediaPlayer("file:///D:/Dropbox/Cardiff/CM1101/Week_4/GameTeam01/beat.mp3")


#variables to be called <3
player_health = 5000
boss_health = 5000
multiplier = 1
win = False

#mapping for the gaphics of each key (final value is wait time for that direction) <3
active_left = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
active_down = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
active_up = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
active_right = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#dictionary that prints each line of the grades
dict_grades = {
    "       " : ["                                           ", "                                           ", "                                           ", "                                           "],
    "BAD" : ["             _____ _____ ____              ", "            | __  |  _  |    \             ", "            | __ -|     |  |  |            ", "            |_____|__|__|____/             "],
    "POOR" : ["          _____ _____ _____ _____          ", "         |  _  |     |     | __  |         ", "         |   __|  |  |  |  |    -|         ", "         |__|  |_____|_____|__|__|         "],
    "GOOD" : ["          _____ _____ _____ ____           ", "         |   __|     |     |    \          ", "         |  |  |  |  |  |  |  |  |         ", "         |_____|_____|_____|____/          "],
    "AMAZING" : [" _____ _____ _____ _____ _____ _____ _____ ", "|  _  |     |  _  |__   |     |   | |   __|", "|     | | | |     |   __|-   -| | | |  |  |", "|__|__|_|_|_|__|__|_____|_____|_|___|_____|"],
    "PERFECT" : [" _____ _____ _____ _____ _____ _____ _____ ", "|  _  |   __| __  |   __|   __|     |_   _|", "|   __|   __|    -|   __|   __|   --| | |  ", "|__|  |_____|__|__|__|  |_____|_____| |_|  "],
    "MISS" : ["          _____ _____ _____ _____          ", "         |     |     |   __|   __|         ", "         | | | |-   -|__   |__   |         ", "         |_|_|_|_____|_____|_____|         "]
}

#forces the screen to be ~90x40 <3
def formatting():
    os.system('mode con: cols=91 lines=43')

#prints testing information <3
def diagnostics():
    print("active_left[36] " + str(active_left[36]) + " active_down[36] " + str(active_down[36]) + " active_up[36] " + str(active_up[36]) + " active_right[36] " + str(active_right[36]) + " " + '"' + last_score + '"')

#keypress wait <3
def keypress():
    initial_time = time.time()
    keypressed = False
    user_input = None

    while True:
        if msvcrt.kbhit():
            user_input = msvcrt.getch()
            keypressed = True
            break
        elif time.time() - initial_time > wait_time:
            break

    #if the user has pressed a key <3
    if keypressed == True:

        user_key = active_left
        #left arrow key <3
        if ord(user_input) == 75:
            active_left[36] = scoring(active_left, active_left[36])
        #down arrow key <3
        if ord(user_input) == 80:
            active_down[36] = scoring(active_down, active_down[36])
        #up arrow key <3
        if ord(user_input) == 72:
            active_up[36] = scoring(active_up, active_up[36])
        #right arrow key <3
        if ord(user_input) == 77:
            active_right[36] = scoring(active_right, active_right[36])

        time.sleep((initial_time + wait_time) - time.time())

    else:
        pass

#grades based on positions <3
def scoring(user_key, waiting):
    global last_score
    global player_health
    global boss_health

    result = 0

    if waiting <= 0:
        for x in range(26,35):
            if user_key[x] == 1:
                result = 34 - x

        #grades based on position of arrow key <3
        if user_key[26] == 1 or user_key[34] == 1:
            last_score = "BAD"
            player_health -= 50
        if user_key[27] == 1 or user_key[33] == 1:
            last_score = "POOR"
        if user_key[28] == 1 or user_key[32] == 1:
            last_score = "GOOD"
            boss_health -= 10
        if user_key[29] == 1 or user_key[31] == 1:
            last_score = "AMAZING"
            boss_health -= 50
        if user_key[30] == 1:
            last_score = "PERFECT"
            boss_health -= 100

    return result

#prints a title card at top of screen <3
def title():
    print("                       |%s|                      " %dict_grades[last_score][0])
    print("      YOUR HEALTH      |%s|     BOSS HEALTH      "%dict_grades[last_score][1])
    print("          %05d        |%s|         %05d        " %(player_health, dict_grades[last_score][2], boss_health))
    print("                       |%s|                      " %dict_grades[last_score][3])
    print("__________________________________________________________________________________________")

#generates an arrow trail using characters -type of lengeth -length <3
def trail(type, length):
    return "".join(random.SystemRandom().choice(type) for _ in range(length))

#returns graphic for arrow line <3
def left(line):
    if line == 0:
        return "               "
    if line == 1:
        return "*   " + trail("." + ":", 1) + trail("." + ":" + " " + " " + " " + " ", 4) + ":    *"
    if line == 2:
        return "    " + trail("." + ":" + " " + " " + " " + " ", 2) + ".:::     "
    if line == 3:
        return "    .:::::     "
    if line == 4:
        return "     '::::     "
    if line == 5:
        return "*       ':    *"

#returns graphic for arrow line <3
def down(line):
    if line == 0:
        return "               "
    if line == 1:
        return "*   " + trail("." + ":" + " " + " " + " " + " ", 7) + "   *"
    if line == 2:
        return "   " + trail("." + ":" + " " + " " + " " + " ", 9) + "   "
    if line == 3:
        return "   ." + trail("." + ":", 7) + ".   "
    if line == 4:
        return "    ':::::'    "
    if line == 5:
        return "*     ':'     *"

#returns graphic for arrow line <3
def up(line):
    if line == 0:
        return "               "
    if line == 1:
        return "*     " + trail("." + ":" + " " + " " + " " + " ", 3) + "     *"
    if line == 2:
        return "     " + trail("." + ":" + " " + " " + " " + " ", 5) + "     "
    if line == 3:
        return "     " + trail("." + ":" + " " + " " + " " + " ", 2) + ":" + trail("." + ":" + " " + " " + " " + " ", 2) + "     "
    if line == 4:
        return "    " + trail("." + ":" + " " + " " + " " + " ", 1) + ".:::." + trail("." + ":" + " " + " " + " " + " ", 1) + "    "
    if line == 5:
        return "*  .:::::::.  *"

#returns graphic for arrow line <3
def right(line):
    if line == 0:
        return "               "
    if line == 1:
        return "*    :" + trail("." + ":", 1) + trail("." + ":" + " " + " " + " " + " ", 4) + "   *"
    if line == 2:
        return "     :::." + trail("." + ":" + " " + " " + " " + " ", 2) + "    "
    if line == 3:
        return "     :::::.    "
    if line == 4:
        return "     ::::'     "
    if line == 5:
        return "*    :'       *"

#returns graphic for arrow line <3
def none():
    return "               "

#function that is called in main loop <3
def an_encounter():

    #these just make sure everything is universally accepted <3
    global beat_counter
    global beat
    global counter
    global random_value
    global wait_time
    global last_score
    global audio_on
    global audio
    global player_health
    global boss_health
    global multiplier
    global win
    global loss

    #main combat loop <3
    while True:

        #move everything down <3
        for x in range(34,0,-1):
            active_left[x] = active_left[x-1]
            active_down[x] = active_down[x-1]
            active_up[x] = active_up[x-1]
            active_right[x] = active_right[x-1]

        #generate top row <3
        for z in range(1,6):
            if active_left[1] == z:
                active_left[0] = int(z-1)
            if active_down[1] == z:
                active_down[0] = int(z-1)
            if active_up[1] == z:
                active_up[0] = int(z-1)
            if active_right[1] == z:
                active_right[0] = int(z-1)

        #every beat; remove score, add new step, if miss -100 health <3
        if counter%beat == 0:
            audio.play()
            random_value = random.randint(1, 4)

            if random_value == 1:
                active_left[0] = 5
            if random_value == 2:
                active_down[0] = 5
            if random_value == 3:
                active_up[0] = 5
            if random_value == 4:
                active_right[0] = 5

            if last_score == "       " and counter - 40 >= 0:
                player_health -= 100
                last_score = "MISS"
            else:
                last_score = "       "

        #check for win/loss <3
        if boss_health <= 0:
            win = True
            break
        if player_health <= 0:
            break

        #clear screen <3
        os.system('cls')

        #print title <3
        title()

        #print body <3
        for x in range(0,36):
            if x == 29:
                print(none()[:-1] + "=" + str(left(active_left[x]) + down(active_down[x]) + up(active_up[x]) + right(active_right[x])).replace(" ", "=") + "=" + none()[2:])
            elif 29 < x < 35:
                print(none()[:-1] + "=" + left(active_left[x]) + down(active_down[x]) + up(active_up[x]) + right(active_right[x]) + "=" + none()[2:])
            elif  x == 35:
                print(none()[:-1] + "==============================================================" + none()[2:])
            else:
                print(none() + left(active_left[x]) + down(active_down[x]) + up(active_up[x]) + right(active_right[x]) + none())

        #prints testing information <3
        #diagnostics()

        #add to counter <3
        counter += 1
        active_left[36] -= 1
        active_down[36] -= 1
        active_up[36] -= 1
        active_right[36] -= 1

        #wait for 0.1 seconds <3
        keypress()

        #stop the audio beat <3
        audio.stop()


    os.system('cls')
    return win
