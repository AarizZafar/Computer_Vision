import pyautogui 
import time 
import keyboard 

while True:
    im = pyautogui.screenshot()
    screen = im.getpixel((31,154))
 
    t1 = im.getpixel((450,664))
    t2 = im.getpixel((450,650))
    t3 = im.getpixel((500,660))
    t4 = im.getpixel((440,671))   

#    b1 = im.getpixel((370, 551))     
#    b2 = im.getpixel((475,550))                           
#    b3 = im.getpixel((500,550))                 
#    b4 = im.getpixel((488,530))  
#    or b1[0]!=0 or b2[0]!=0 or b3[0]!=0 or b4[0]!=0                                

    c = (32,33,36)
    if screen == c:        
        if t1!=c or t2!=c or t3!=c or t4!=c:
            pyautogui.press("space")

#    else:
#        if t1[0]!=255   or t2[0]!=255 or t3[0]!=255 or t4[0]!=255:
#            pyautogui.press("space")                  
#            time.sleep(0.0001)

    if keyboard.is_pressed("s"):        
        break 
    else:
        pass





