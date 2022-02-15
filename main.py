import keyboard


#Current position
season = 1
episode = 1

#Seans length for your series of choice
season_len = [26, 7, 11]


result = ""

def paste():
    global season
    global episode
    global season_len
    global result
    test = ""
    result = ""
    if season >= 10:
        result = result.join("s" + str(season))
    else:
        result = result.join("s0" + str(season))
    

    if episode >= 10: 
        test = result + "e" + str(episode)
    else:
        test = result + "e0" + str(episode)
        
    
    #print("result: "+ test)

    keyboard.press_and_release('right, space')
    keyboard.write(test)
    keyboard.press_and_release("enter, down")
    
    episode += 1
    if episode > season_len[season - 1]:
        episode = 1
        season += 1



keyboard.add_hotkey('F2', paste)
keyboard.add_hotkey('esc', quit)

keyboard.wait()
