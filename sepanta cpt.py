
age = input("How old are you?")
age = int(age)

if age > 10:

    answer = input("You are a fugitive fleeing from prison. After many attempts, you finally escape. Which way do you "
                   "turn?")
    if answer == "right":
        answer = input("You turn right and begin walking onto a busy street. Should you run or should you purchase a "
                       "disguise?")

        if answer == "run":
            print("Wrong choice! You bring attention to yourself and the police are called. Try again!")

        elif answer == "disguise":
            answer = input("You enter a small store and want to buy a hat when you realize you're broke. "
                           "Do you leave the store recognizable or steal?")

            if answer == "steal":
                print("Wrong choice! The owner of the store notices you and calls the police! Try again!")

            else:
                answer = input("You leave the store with no disguise. You hear police sirens and assume they're for "
                               "you. Do you hide or wait for police to come and attack them?")

                if answer == "hide":
                    print("You hide out for the rest of the night without getting caught. You win!")

                elif answer == "attack":
                    print("You attack the police, bringing massive attention to yourself. Not only are you taken back "
                           "to jail, but the video of you fighting the police goes viral. Try again!")

    if answer == "left":
        answer = input("You turn left until someone begins asking you for directions. You want to avoid confrontation "
                       "but don't want to make a scene. Do you help the man or knock him out?")

        if answer == "knock him out":
            answer = input("You punch the man in the face, leaving him unconscious. You panic and run home. Do you ring" 
                           " the doorbell or break in?")

            if answer == "break in":
                print("Wrong choice! Someone calls in a breaking and entering. Try again!")

            elif answer == "ring the doorbell":
                answer = input("Your mom opens the door and lets you come inside. She says you have to clean the "
                               "house or she will snitch on you. Will you clean the house or disobey her?")

                if answer == "clean the house":
                    print("Your mom agrees to helping you stay hidden. You win!")

                elif answer == "disobey":
                    answer = input("You storm upstairs to your room. You unlock your old computer and turn on its "
                                   "monitor. You begin receiving pop ups about how there is nearly more plastic than "
                                   "fish in the ocean. Should you click on them?")

                    if answer == "click on them":
                        print("You should know better than to not have an antivirus. Your location is now tracked and "
                              "the police found you. Try again!")

                    else:
                        print("You stay away from location trackers, however, your mom has alerted authorities. "
                              "She says she's tired of you being so lazy and is still mad you did not go to "
                              "college. Try again.")

        if answer == "help":
            print("Wrong choice! The man recognizes you and calls the police! Try again!")

else:
    print("Access denied.")