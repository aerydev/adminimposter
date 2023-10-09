import os, time
import pyautogui as pya
#######################################################################################################################################################################
#######################################################################################################################################################################
#######################################################################################################################################################################
os.system("title admin impostor by huhvzi on github")
title = input("title of window: ")
cn = input("company name: ")
def say(txt):
    print(f"[{cn}]:", txt)
os.system("cls")
os.system(f"title {title}")
print(f"[{cn}]: Loading command line . . . ")
time.sleep(2)
say("Loaded!")
say("Loading Ban Panel . . . ")
time.sleep(4)
say("Loaded!")
os.system("color 02")
while True:
    name = input(f"[{cn}]: Enter user of suspect: ")
    say("Loading user data . . . ")
    time.sleep(3)
    say("Loaded! \nReports: 14 \nSuspecious Account: TRUE \nReport Legitimacy: 89")
    ban = input(f"[{cn}]: Ban User? [y/n/s]: ")
    if ban == "y":
        say(f"Banning user {name} . . . ")
        say("Banned User! ")
        say("Loading ban panel again . . . ")
        time.sleep(3)
        say("Loaded! ")
    elif ban == "n":
        say(f"Marked user {name} as innocent! ")
        say("Loading ban panel again . . . ")
        time.sleep(3)
        say("Loaded! ")
    elif ban=="s":
        say(f"Skipped user {name}! ")
        say("Loading ban panel again . . . ")
        time.sleep(3)
        say("Loaded! ")
time.sleep(999999)
c=input("")
