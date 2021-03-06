import sys
import time

player_name = input("What is your name?:")

class Player:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

player = Player(player_name)

def start_game():

    def slowprint(s):
        for c in s + "\n":
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(1.0 / 60)

    def game_over():
        print("Game over!")
        play_again()

    def play_again():
        print("Would you like to try again, y/n?")
        answer = input().lower()
        if "y" in answer:
            start_game()
        elif "n" in answer:
            exit()
        else:
            print("Please enter y for yes or n for no")
            play_again()


    sections = {
        'front': {'text': f"{player_name}, it's finally the big day! Time to get your driver's license! You were so excited last night you hardly slept, but you've been preparing for this day all your life. As your older brother drives you up to the DMV, you notice that it says it opens at 8 am, but it's now 8:05 and the doors are still locked!\n You can choose to\n 1. Attempt to break in...\n 2. Wait patiently\n 3. Check the back door\n 4. Curse your luck and go home\n What do you do?"},

        'side': {'text': "You approach the side and see a window. You try and open it, but it appears to be locked. You look around for anything to help and you see a brick laying on the ground. You figure you have only 2 options.\n What do you do?\n 1. Pick up the brick and throw it through the window.\n 2. Try and pick the lock and open the window."},

        'brick': {'text': "You pick up the brick and hurl it with all your might through the window. As soon as the glass breaks, you hear a loud alarm go off. In an instance, you are swarmed by a SWAT team and forced to the ground. Have they just been waiting behind the building waiting for someone to try this? Their response time was impeccable. They put you in handcuffs and off to prison you go."},

        'pick_lock': {'text': "You approach the window and see a lockpick set laying on the sill. What a lucky break to advance the story! You pick it up and with nimble fingers and dexterity you never knew you had, you manage to get the window unlocked and open. You crawl your way in and see you're in a dark room. As your vision adjusts to the low light, you see a desk in front of you. On the desk there seems to be a stack of papers. When you look at the top page, it looks like you found the answer to the written driver's test! What a miracle! You scan the pages quickly and are able to retain all the information with your photo memory which seems like another convenient plot device. As you finish reading it, you hear the door begin to open! Do you\n 1. Hide under the desk\n 2. Stand firm and see what happens"},

        'hide': {'text': "Too late! The door opens as a woman sees you in the middle of the room. 'What are you doing in here? Looking for the bathroom I presume? Follow me right this way.' You follow the woman as she leads you to where the restrooms are. After she walks away, you find your way to the front. The kind lady at the desk escorts you back to take the written test which you ace no problem with all of the answers in your head. Great job! Save point reached! Now head outside for the driving portion of the test."},

        'stand': {'text': "The door opens as a woman sees you in the middle of the room. Before you can act, she says 'What are you doing in here? Looking for the bathroom I presume? Follow me right this way.' You follow the woman as she leads you to where the restrooms are. After she walks away, you find your way to the front. The kind lady at the desk escorts you back to take the written test which you ace no problem with all of the answers in your head. Great job! Save point reached! Now head outside for the driving portion of the test."},

        'line': {'text': 'You approach the front door, seeing no one else around, and take your place in front of the doors. After a minute of waiting, a man comes and unlocks the door. Thank goodness you didn\'t have to wait long! You walk inside and somehow, some way, there is a line of 20 people in front of you. Where did they come from? This is outrageous! Do you\n 1. Take your place in line and wait\n 2. Sneak your way up front and cut in line to be next'},

        'wait': {'text': "You accept your lot in life and take your place at the end of the line. After waiting for hours, you finally get to the front and the lady looks you dead in the eye and says 'I'm sorry, but we are now closing for the day. Gas leak. You'll have to come again tomorrow."},

        'sneak': {'text': "You sneak your way up front and do the old tap the person on the shoulder so they look the other way and slide on in to the line. It worked! You approach the lady behind the counter and she looks at your beaming face. 'Let me guess. Here for your drivers license test? Well you are in for a surprise. Follow me for the written part of your test' You follow her to a back room where she leads you to a computer. You sit down to take the test.\n Question 1:\n You pull up to a red light. A car pulls up next to you and revs it's engine, obviously looking for an impromptu race. How do you respond?\n 1. Put on your driving gloves and get ready to take off as soon as the light hits green\n 2. Ignore the car next to you and stick to driving according to the law\n 3. Slam the car in reverse and run!"},

        'race_car': {'text': "Doesn't matter if you win by an inch or a mile, winning is winning. And you are a winner! Next question. Pick the object that is not like the others?\n 1. Car\n 2. Truck\n 3. Dandelion"},

        'car_answer': {'text': "Really? You must be joking. If you can't take this seriously, no license for you!"},

        'truck_answer': {'text': "You must have clicked the wrong button. This was supposed to be easy!"},

        'dandelion_answer': {'text': "You passed! Were you expecting more questions? Save point reached! Now head outside for the driving portion of your test."},

        'ignore_car': {'text': "Good job! Next question. Pick the object that is not like the others?\n 1. Car\n 2. Truck\n 3. Dandelion"},

        'reverse_car': {'text': "You slammed into the car behind you. You fail."},

        'back': {'text': "You walk towards the back of the building, seeing no one in sight. As you turn the corner, you see a door at the rear entrance. Maybe it's unlocked! As you head towards the door, you hear a growl to your left. You turn to the source of the noise and see a pack of 5 wolves glaring at you.\n What do you do now?\n 1. Fight! Wolves are no match for you!\n 2. Run! You didn't sign up for this!"},

        'fight_wolves': {'text': "Seriously, you thought you could take on 5 wolves? You've severely overestimated your skills."},

        'run_wolves': {'text': "Some may call you a coward, but you survived. Good thing they decided not to chase you for reasons you'll never know because it wasn't written in the script. As you come back around to the front, you notice that the doors are open. Maybe waiting would have been the safer choice. As you walk into the building, the man at the front desk greets you with a warm smile. He leads you to the back and hands you a paper and pencil. You sit down and look at the test.\nQuestion 1:\n How many tires does a normal car have?\n 1. 2\n 2. 4\n 3. 3\n 4. 1"},

        'pass_test': {'text': "Great job! You passed! Save point reached! Now go outside for the driving portion of the test."},

        'fail_test': {'text': "Come on, this is basic knowledge anyone should know."},

        'give_up': {'text': "This must be a sign that you aren't ready. Better go back home and keep on practicing."},
        }

    choices = ['1', '2', '3', '4']
    current_section = sections['front']

    while True:
        slowprint(sections['front']['text'])

        choice = input()

        if choice == choices[0]:
            slowprint(sections['side']['text'])

            choice = input()

            if choice == choices[0]:
                slowprint(sections['brick']['text'])
                game_over()
                break

            elif choice == choices[1]:
                slowprint(sections['pick_lock']['text'])

                choice = input()

                if choice in choices[0]:
                    slowprint(sections['hide']['text'])
                    break

                elif choice in choices[1]:
                    slowprint(sections['stand']['text'])
                    break

                else:
                    slowprint("Please choose a choice provided")


        elif choice == choices[1]:
            slowprint(sections['line']['text'])

            choice = input()

            if choice == choices[0]:
                slowprint(sections['wait']['text'])
                game_over()
                break

            elif choice == choices[1]:
                slowprint(sections['sneak']['text'])

                choice = input()

                if choice == choices[0]:
                    slowprint(sections['race_car']['text'])

                    choice = input()

                    if choice == choices[0]:
                        slowprint(sections['car_answer']['text'])
                        game_over()
                        break

                    elif choice == choices[1]:
                        slowprint(sections['truck_answer']['text'])
                        game_over()
                        break

                    elif choice == choices[2]:
                        slowprint(sections['dandelion_answer']['text'])
                        break

                elif choice == choices[1]:
                    slowprint(sections['ignore_car']['text'])

                    choice = input()

                    if choice == choices[0]:
                        slowprint(sections['car_answer']['text'])
                        game_over()
                        break

                    elif choice == choices[1]:
                        slowprint(sections['truck_answer']['text'])
                        game_over()
                        break

                    elif choice == choices[2]:
                        slowprint(sections['dandelion_answer']['text'])
                        break

                elif choice == choices[2]:
                    slowprint(sections['reverse_car']['text'])
                    game_over()
                    break

        elif choice == choices[2]:
            slowprint(sections['back']['text'])

            choice = input()

            if choice == choices[0]:
                slowprint(sections['fight_wolves']['text'])
                game_over()
                break

            elif choice == choices[1]:
                slowprint(sections['run_wolves']['text'])

                choice = input()
                if choice == choices[1]:
                    slowprint(sections['pass_test']['text'])
                    break

                else:
                    slowprint(sections['fail_test']['text'])
                    game_over()
                    break




        elif choice == choices[3]:
            slowprint(sections['give_up']['text'])
            game_over()
            break

        else:
            print("Choose one of the options provided")

start_game()
