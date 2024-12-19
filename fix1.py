import random
import time
import pygame

pygame.init()


revolver_sound = pygame.mixer.Sound("revolver.mp3")
click_sound = pygame.mixer.Sound("click.mp3")
bgm = pygame.mixer.Sound("bgm.mp3")



def shoot(bullet):
    while True:
        pull_the_trigger = input("Type 's' to shoot: ").lower()

        if pull_the_trigger == 's':
            print("\nYou pull the trigger...")
            time.sleep(1)

            if bullet == 1:
                revolver_sound.play()
                time.sleep(1)
                print("\nYou are dead. Game over!")
                exit()
            else:
                click_sound.play()
                time.sleep(1)
                print("\nClick,\nyou lucky bastard. Go again\n")
                break
        else:
            print("You must type 's' to shoot")

while True:
    bullet = random.choice([0, 0, 0, 0, 0, 1])
    print("\nPlay Russian Roulette\n")
    bgm.play()
    bgm.fadeout(6000)
    shoot(bullet)

    while True:
        bullet = random.choice([0, 0, 0, 0, 1])    
        shoot(bullet)

        while True:
            bullet = random.choice([0, 0, 0, 1])  
            shoot(bullet)

            while True:
                bullet = random.choice([0, 0, 1])  
                shoot(bullet)

                while True:
                    bullet = random.choice([0, 1])  
                    shoot(bullet)

                    print("\nBullet left. You won!\n")
 
    while True:
        replay = input("Wanna play again? Type y/n:").lower()
        if replay == "y":
            print("Let's play again\n")
            break

        elif replay == "n":
            print("You left the table")
            exit()

        else:
            print("Please type y/n")