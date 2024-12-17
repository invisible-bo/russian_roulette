import random
import time
import pygame

pygame.init()

revolver_sound = pygame.mixer.Sound("revolver.mp3")
click_sound = pygame.mixer.Sound("click.mp3")
bgm = pygame.mixer.Sound("bgm.mp3")

while True:
    bullet = random.choice([0,0,0,0,0,1])

    print("play russian roulette\n")     
    bgm.play()
    bgm.fadeout(6000)

    while True:
        pull_the_trigger = input("type 's' to shoot: ").lower()

        if pull_the_trigger == 's':
            print("You pull the trigger...")
            time.sleep(1)

            if bullet == 1:
                revolver_sound.play()
                time.sleep(1)
                print("you are dead. Game over!")
                exit()

            elif bullet == 0:
                click_sound.play()
                time.sleep(1)
                print("click,\nyou lucky bastard. Go again\n")
                break

        else:
            print("You must 's'to shoot") 

    while True:
        bullet = random.choice([0,0,0,0,1])

        pull_the_trigger = input("type 's' to shoot: ").lower()

        if pull_the_trigger == 's':
            print("You pull the trigger...")
            time.sleep(1)

            if bullet == 1:
                revolver_sound.play()
                time.sleep(1)
                print("you are dead. Game over!")
                exit()

            elif bullet == 0:
                click_sound.play()
                time.sleep(1)
                print("click,\nyou lucky bastard. Go again\n")
                break

        else:
            print("You must 's'to shoot") 

    while True:
        bullet = random.choice([0,0,0,1])

        pull_the_trigger = input("type 's' to shoot: ").lower()

        if pull_the_trigger == 's':
            print("You pull the trigger...")
            time.sleep(1)

            if bullet == 1:
                revolver_sound.play()
                time.sleep(1)
                print("you are dead. Game over!")
                exit()

            elif bullet == 0:
                click_sound.play()
                time.sleep(1)
                print("click,\nyou lucky bastard. Go again\n")
                break

            else:
                print("You must 's'to shoot") 

    while True:
        bullet = random.choice([0,0,1])

        pull_the_trigger = input("type 's' to shoot: ").lower()

        if pull_the_trigger == 's':
            print("You pull the trigger...")
            time.sleep(1)

            if bullet == 1:
                revolver_sound.play()
                time.sleep(1)
                print("you are dead. Game over!")
                exit()

            elif bullet == 0:
                click_sound.play()
                time.sleep(1)
                print("click,\nyou lucky bastard. Go again\n")
                break

            else:
                print("You must 's'to shoot") 

    while True:
        bullet = random.choice([0,1])

        pull_the_trigger = input("type 's' to shoot: ").lower()

        if pull_the_trigger == 's':
            print("You pull the trigger...")
            time.sleep(1)

            if bullet == 1:
                revolver_sound.play()
                time.sleep(1)
                print("you are dead. Game over!")
                exit()

            elif bullet == 0:
                click_sound.play()
                time.sleep(1)
                print("click,\nyou lucky bastard. Go again\n")
                break

            else:
                print("You must 's'to shoot") 


    print("bullet left. you won!")

    while True:
        replay = input("wanna play again? type y/n : ").lower()
        if replay == "y":
            print("Let's play again\n")
            break
    
        elif replay == "n":
            print("you left the table")
            exit()
    
        else:
            print("please type y/n")  
