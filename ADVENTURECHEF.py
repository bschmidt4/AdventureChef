import time
import random

# Player-----------


def Name():
    global name
    print('Whats your name?')

    valid = True
    if valid is True:
        response = input()
        name = response
        start()


def Player_Profile():
    global stamina
    global name
    print('        Character         ')
    print('|------------------------|')
    print('|                        |')
    print('|        ???????         |')
    print('|        |-  - |         |')
    print('|        | |   |         |')
    print("|        |  -  /         |")
    print("|        ''''''          |")
    print('|                        |')
    print('|  Name- '+str(name)+'               |')
    print('|  Class- Chef Traveler  |')
    print('|  Stamina- '+str(stamina)+'            |')
    print('|                        |')
    print('|------------------------|')


name = ' '

stamina = 4
Health = 10
Attack = 1
Gold = 5
Borest_REP = 0
Aldren_REP = 0
Calduin_REP = 0
Triteem_REP = 0

# Death-------------


def death():
    global Health
    global stamina
    global Attack
    global Gold

    global lost_boy
    global shadyfigure_instance
    global shadyfigureleave
    global sob_woman
    global beggar_instance
    global Rejuvination_Amulet
    global Gleaming_sword
    global Rabbits_Foot
    global Stamina_potion
    global gladiatorsword

    global Borest_REP
    global Aldren_REP
    global Calduin_REP
    global Triteem_REP

    global peachb
    global coco_beansb
    global dragon_eggb
    global trufflesb
    global bananasb
    global brackberriesb
    global juicylambb
    global expshroomsb
    global chesoystersb
    global weldfishb
    global noblefernb
    global trollfatb
    global legendfruitb

    global peach
    global dragon_egg
    global coco_beans
    global truffles
    global bananas
    global brackberries
    global juicylamb
    global expshrooms
    global chesoysters
    global weldfish
    global noblefern
    global trollfat
    global legendfruit

    global raging_centipedes
    global bonewalkers
    global rats

    if Health < 1:
        Health -= Health
        Health += 10
        stamina -= stamina
        stamina += 4
        Attack -= Attack
        Attack += 1
        Gold -= Gold
        Gold += 5

        Borest_REP = 0
        Aldren_REP = 0
        Calduin_REP = 0
        Triteem_REP = 0

        lost_boy = True
        shadyfigure_instance = True
        shadyfigureleave = True
        sob_woman = True
        beggar_instance = True
        Rejuvination_Amulet = True
        Gleaming_sword = True
        Rabbits_Foot = True
        Stamina_potion = True
        gladiatorsword = True

        peachb = 0
        coco_beansb = 0
        dragon_eggb = 0
        trufflesb = 0
        bananasb = 0
        brackberriesb = 0
        juicylambb = 0
        expshroomsb = 0
        chesoystersb = 0
        weldfishb = 0
        noblefernb = 0
        trollfatb = 0
        legendfruitb = 0

        peach = 2
        dragon_egg = 1
        coco_beans = 3
        truffles = 1
        bananas = 3
        brackberries = 2
        juicylamb = 0
        expshrooms = 0
        chesoysters = 0
        weldfish = 0
        noblefern = 0
        trollfat = 0
        legendfruit = 1

        print('You DIE')
        time.sleep(2)
        print("Try Again(1)")
        valid = True
        if valid is True:
            response = input()
            if response == '1':

                start()
    else:
        print("")
# ------------------

# Backpack----------


peachb = 0
coco_beansb = 0
dragon_eggb = 0

trufflesb = 0
bananasb = 0
brackberriesb = 0

juicylambb = 0
expshroomsb = 0
chesoystersb = 0

weldfishb = 0
noblefernb = 0
trollfatb = 0

legendfruitb = 0
# ------------------

# Amount-IN-World---
peach = 2
dragon_egg = 1
coco_beans = 3

truffles = 1
bananas = 3
brackberries = 2

juicylambb = 0
expshroomsb = 0
chesoystersb = 0

weldfishb = 0
noblefernb = 0
trollfatb = 0

legendfruit = 1
# -------------------

# Info---------------


def Stamina():
    global stamina
    if stamina <= 0:
        print("You ran out of stamina and die crawling on your knees")
        death()
    else:
        print(" ")


def gold():
    print("You have " + str(Gold) + " gold\n")


def Selling():
    global peachb
    global coco_beansb
    global dragon_eggb
    global trufflesb
    global bananasb
    global brackberriesb
    global juicylambb
    global expshroomsb
    global chesoystersb
    global weldfishb
    global noblefernb
    global trollfatb
    global Gold
    global INBorest
    global INAldren
    print("peachs "+str(peachb)+" (1)")
    print("coco beans "+str(coco_beansb)+" (2)")
    print("dragon eggs"+str(dragon_eggb)+" (3)")
    print("truffles "+str(trufflesb)+" (4)")
    print("bananas "+str(bananasb)+" (5)")
    print("brackberries "+str(brackberriesb)+" (6)")
    print('juicy lamb '+str(juicylambb)+" (7)")
    print('expshrooms '+str(expshroomsb)+" (8)")
    print('chesoysters '+str(chesoystersb)+" (9)")
    print('weldfishs '+str(weldfishb)+" (10)")
    print("noblefern "+str(noblefernb)+" (11)")
    print("trollfat "+str(trollfatb)+" (12)")
    print("Buy from the shop(13)")
    valid = True
    while valid is True:
        response = input()
        if response == '1':
            if peachb < 1:
                print("You dont have any more of this item")
                Selling()
            else:
                Gold += peachb * 2
                peachb -= peachb
                print("You now have "+str(Gold)+" gold")
                Selling()
            break
        elif response == '2':
            if coco_beansb < 1:
                print("You dont have any more of this item")
                Selling()
            else:
                Gold += coco_beansb * 2
                coco_beansb -= coco_beansb
                print("You now have "+str(Gold) + " gold")
                Selling()
            break
        elif response == '3':
            if dragon_eggb < 1:
                print("You dont have any more of this item")
                Selling()
            else:
                Gold += dragon_eggb * 3
                dragon_eggb -= dragon_eggb
                print("You now have "+str(Gold) + " gold")
                Selling()
            break
        elif response == '4':
            if trufflesb < 1:
                print("You dont have any more of this item")
                Selling()
            else:
                Gold += trufflesb * 2
                trufflesb -= trufflesb
                print("You now have "+str(Gold) + " gold")
                Selling()
            break
        elif response == '5':
            if bananasb < 1:
                print("You dont have any more of this item")
                Selling()
            else:
                Gold += bananasb * 2
                bananasb -= bananasb
                print("You now have "+str(Gold) + " gold")
                Selling()
            break
        elif response == '6':
            if brackberriesb < 1:
                print("You dont have any more of this item")
                Selling()
            else:
                Gold += brackberriesb * 2
                brackberriesb -= brackberriesb
                print("You now have "+str(Gold) + " gold")
                Selling()
            break
        elif response == '7':
            if juicylambb < 1:
                print("You dont have any more of this item")
                Selling()
            else:
                Gold += juicylambb * 4
                juicylambb -= juicylambb
                print("You now have "+str(Gold) + " gold")
                Selling()
            break
        elif response == '8':
            if expshroomsb < 1:
                print("You dont have any more of this item")
                Selling()
            else:
                Gold += expshroomsb * 2
                expshroomsb -= expshroomsb
                print("You now have "+str(Gold) + " gold")
                Selling()
            break
        elif response == '9':
            if chesoystersb < 1:
                print("You dont have any more of this item")
                Selling()
            else:
                Gold += chesoystersb * 2
                chesoystersb -= chesoystersb
                print("You now have "+str(Gold) + " gold")
                Selling()
            break
        elif response == '10':
            if weldfishb < 1:
                print("You dont have any more of this item")
                Selling()
            else:
                Gold += weldfishb * 2
                weldfishb -= weldfishb
                print("You now have "+str(Gold) + " gold")
                Selling()
            break
        elif response == '11':
            if noblefernb < 1:
                print("You dont have any more of this item")
                Selling()
            else:
                Gold += noblefernb * 2
                noblefernb -= noblefernb
                print("You now have "+str(Gold) + " gold")
                Selling()
            break
        elif response == '12':
            if trollfatb < 1:
                print("You dont have any more of this item")
                Selling()
            else:
                Gold += trollfatb * 2
                trollfatb -= trollfatb
                print("You now have "+str(Gold) + " gold")
                Selling()
            break
        elif response == '13':
            print("you decide to buy something from the shop")
            if INBorest is False:
                Grumpy_Merchant()
            elif INAldren is False:
                Goblen_Shaman()
            elif INCalduin is False:
                Eleven_Enchanter()
            else:
                print(" ")
        else:
            print("Invalid input")
            continue
# ------------------


ALDREN = True
# Items-------------
Rejuvination_Amulet = True
Gleaming_sword = True
Rabbits_Foot = True
Stamina_potion = True
gladiatorsword = True
# ------------------

# Rumors-Road-Instances-


def Plays():
    rand_num = random.randint(1, 5)

    rumour_one = "THE CURTAINS open and exitement builds in you body."
    rumour_two = 'THE CURTAINS open and exitement builds in you body'
    rumour_three = 'THE CURTAINS open and exitement builds in you body'
    rumour_four = 'THE CURTAINS open and exitement builds in you body'
    rumour_five = 'THE CURTAINS open and exitement builds in you body'

    total_rumours = []
    total_rumours.append(rumour_one)
    total_rumours.append(rumour_two)
    total_rumours.append(rumour_three)
    total_rumours.append(rumour_four)
    total_rumours.append(rumour_five)
    return total_rumours[rand_num - 1]


def rumours():
    rand_num = random.randint(1, 7)

    rumour_one = 'I hear there are expensive truffles in skaldar forest.'
    rumour_two = 'The skaldur forest is full of dangerous goblin natives'
    rumour_three = 'I heer triteem is forming a expidition group to kill the trolls'
    rumour_four = 'The enchantreess in Calduin can enchant your weapons'
    rumour_five = 'The runes of Mistick in Aldren are full of vualuable items and unique plants'
    rumour_six = 'People enter the Mistick runes and the bodies aret never found'
    rumour_seven = 'some say accursed skeletons rome the bold Cemetary mountain'
    rumour_eight = 'The dwarfs of triteem boiled the very rock they live on to shape it with now unkown tools'
    rumour_nine = 'The Alpha in Calduin was once a ferocious titan in the old wars'
    rumour_ten = 'The Master of Metal is rumored to be in Triteem'
    total_rumours = []
    total_rumours.append(rumour_one)
    total_rumours.append(rumour_two)
    total_rumours.append(rumour_three)
    total_rumours.append(rumour_four)
    total_rumours.append(rumour_five)
    total_rumours.append(rumour_six)
    total_rumours.append(rumour_seven)
    total_rumours.append(rumour_eight)
    total_rumours.append(rumour_nine)
    total_rumours.append(rumour_ten)

    return total_rumours[rand_num - 1]


def road_one():
    print("You travel the road unharmed.")
    return 0


def road_two():
    print("You enjoy the easy journey.")
    return 0


def road_three():
    print("You are caught unaware while traveling the road and bandits seek to destroy you")
    bandits()
    return 0


def road_four():
    global Gold
    print("A toll bridge had been set up(you pay 1 gold")
    if Gold < 1:
        print("If you cant pay then you cant live, they say grinning")
        if Health > 2:
            print("A battle insues and you finish them of but lose 1 health")
        else:
            print("They brutally chop off your head. it rolls into a ditch")
    else:
        Gold -= 1
        gold()
    return 0


def road_five():
    print("You pass by a traveling troup and they say if you pay 1 gold they will perform for you")
    print("1. You ask to watch the show")
    print("2. Politely decline their offer(2)")
    valid = True
    while valid is True:
        response = input()
        if response == '1':
            print('They get really exited and set up the show')
            Plays()
            break
        elif response == '2':
            print("The reflect thier disapointment and you leave")
            break
        else:
            print("Invalid input")
            continue
    return 0


def road_six():
    print("Your tired but exited for the coming adventures ahead")
    return 0


def road_seven():
    global Health
    print("You pass by a traveling troup and they say if you pay 1 gold they will perform for you")
    print("1. You ask to watch the show")
    print("2. Politely decline their offer(2)")
    valid = True
    while valid is True:
        response = input()
        if response == '1':
            print('You want to see a show they say, and pull out thier swords with a ring')
            if Health < 5:
                Health -= 4
                print("You finish them off but lose 4 health")
            else:
                print("They brutally chop off your head. it rolls into a ditch")
                death()
        elif response == '2':
            print("You leave but feel oddly disturebed when you see the look on thier faces as you decline,and  you run away from the scene suddenly hearing cruel luaghter")
            break
        else:
            print("Invalid input")
            continue
    return 0


def rand_road():
    global road_one
    global road_two
    global road_three
    global road_four
    global road_five
    global road_six
    global road_seven

    rand_num = random.randint(1, 7)

    if rand_num == 1:
        road_one()
    elif rand_num == 2:
        road_two()
    elif rand_num == 3:
        road_three()
    elif rand_num == 4:
        road_four()
    elif rand_num == 5:
        road_five()
    elif rand_num == 6:
        road_six()
    elif rand_num == 7:
        road_seven()

    return
# ----------------------

# Enemies-----------


raging_centipedes = 4
bandits_level = 3
bonewalkers = 3
rats = 7
Trolls = 2


def bandits():
    global Health
    global Attack
    bandits_level = 3
    if Attack >= 3:
        print("You slay them with ease")
    else:
        Health -= bandits_level
        print('Your health is now ' + str(Health))
        if Health <= 0:
            death()
# ------------------

# Quests------------


lost_boy = True
shadyfigure_instance = True
shadyfigureleave = True
sob_woman = True
beggar_instance = True


def Combination():
    global Calduin_REP
    global ALDREN
    print('')
    valid = True
    while valid is True:
        response = input()
        if response == '3425':
            print("the gate is closed and you run with the stranger to Aldren road. He declares you a member of the Dawnstar group and you part ways")
            print("Reputaion in Calduin and the Dawnstar group has raised by 4 ")
            Calduin_REP += 4
            ALDREN = False
            Aldren_road()
        elif response != '3425':
            print("You dont know the combination and the goblins have already killed the centipedes. They take you to prison and torture you throughly until you die")
            death()

        else:
            print("Invalid input")
            continue


def AttackAldren():
    global Aldren_REP
    global Health
    global ALDREN
    print ("The goblins search for cover as some get injured, centipedes drilling through thier bodies  ")
    print ("You run to the top of the gates and engage in combat with the gate overseer to seal the gates")
    print ("He is much more skilled then you would expect and lose health")
    Health -= 4
    if Health < 1:
        death()
    else:
        print ("You deal a powerful blow and he sinks to his knees ")
        print ("But before he dies he sinks his dagger into your gut and deals damge again")
        Health -= 4
        if Health < 1:
            death()
        else:
            print ("You go up to the gate lever and see a combination to close it. Whats the combination")
            Combination()


def shadyfigure():
    global shadyfigure_instance
    global shadyfigurecon
    print ("Hello traveler can you keep a secret\n")
    print("Listen to his secret(1)")
    print ("Walk away(2)")
    valid = True
    while valid == True:
        response = input()
        if response == '1':
            if shadyfigure_instance == True:
                shadyfigurecon()
            else:
                print ("The man is waiting for you")
                Aldren()
        elif response == '2':
            print ("You Leave the shady figure")
            Aldren()
            break
        else:
            print("Invalid input")
            continue


def shadyfigurecon():
    global shadyfigure_instance
    print ('He leans in and says Im from a group called the Dawnstar, We purge the world from unholy creatures such as goblins.')
    print ("I might even consider you joining if you help me with a little something")
    print ("You see that Ancient oak over there, if you let out the centipedes and cuase a distraction I can light this place on fire. Then me and you will kill the gate overseer and trap them in their own city.")
    print( 'What do you say?\n')
    print('Accept the challenge(1)')
    print('Decline and say your crazy(2)')


    valid = True
    while valid == True:
        response = input()
        if response == '1':
            print ('Your looked like a smart fellow he says')
            shadyfigure_instance = False
            Aldren()
            break
        elif response == '2':
            print ("The man just shakes his head")
            Aldren()
            break
        else:
            print("Invalid input")
            continue


def Sobbing_Woman():
    global lost_boy
    global Gold
    global Borest_REP
    global sob_woman
    global Health
    if Borest_REP < -1:
        print("the womans eyes squint and and she starts yelling for guards. The guards lock you up in prison till you rot")
        Health -= 20
        death()
    if lost_boy is False:
        print("She says 'Im so grateful, please tak this as a reward'")
        Borest_REP += 3
        print("Your reputation is now "+str(Borest_REP))
        Gold += 15
        gold()
        Borest()
        sob_woman = False
    if sob_woman is True:
        print('Please travler help me she exclaims, my boy is lost and I cant find him!')
    else:
        print("Are you looking for him!")
        Borest()

    print("She looks to you\n")
    print('Say you will help the Lady(1)')
    print('Say keep track of your own kid(2)')
    print('Leave the sobbing woman(3)')
    valid = True
    while valid is True:
        response = input()
        if response == '1':
            print('The lady is so grateful and gives you a hug')
            Borest_REP += 1
            print('Your reputation is now ' + str(Borest_REP))
            sob_woman = False
            Borest()
            break
        elif response == '2':
            print("You tell her off and she yells and spits in your face while everyone watches")
            Borest_REP -= 1
            print("Your reputation went down 1")
            print("Your reputation is " + str(Borest_REP))
            break
        elif response == '3':
            print("You leave the woman to her own misery ")
            Borest()
            break
        else:
            print("Invalid input")
            continue


def lostt_boy():
    global lost_boy
    global bananasb
    print("You ask him why he ran off without his mom")
    print ("He says 'mister I want my bananas and im not leaving without them\n")
    print('Say you will try to get a banana for him(1)')
    print('leave him(2)')
    print('give him a banana(3)')
    valid = True
    while valid == True:
        response = input()
        if response == '1':
            print ('Geez, thanks mister he says annoyling')
            Aldren()
            break
        elif response == '2':
            print ("You leave him there ")
            Aldren()
            break
        elif response == '3':
            if bananasb < 1:
                print ("you dont have a banana")
                Aldren()
            else:
                print ("you give him a banana and he runs home")
                bananasb -= 1
                lost_boy = False
                Aldren()
            break
        else:
            print("Invalid input")
            continue
# ------------------

# Kindom-Grinds----------


def Sewer_Choice():
    print('The beast is gone but you can hear more scraping\n')
    print('Enter Borest(1)')
    print('Leave to borest road(2)')
    print('Fight more rats(3)')

    valid = True
    while valid == True:
        response = input()
        if response == '1':
            print ('You are glad to leave the disgusting sewers')
            Borest()
            break
        elif response == '2':
            print ("You are glad to leave the disgusting sewers ")
            borest_road()
            break
        elif response == '3':
            print ("The rats stand no chance ")
            Sewers()
            break
        else:
            print("Invalid input")
            continue


def Sewers():
    global rats
    global Gold
    global Health
    global Attack
    print ("You hate these sewers and despise the smell, you can hear scraping noises from all over")
    print ("A RAT! you exclaim as a huge on tries to attack you")
    print ("The rat is level 2\n")
    if Attack > 2:
        if rats == 0:
            print ("There are no rats")
            Sewer_Choice()
        print ("You slay the beast with ease")
        Gold += 1
        rats -= 1
        print ("You earned 1 gold")
        Sewer_Choice()
    else:
        if rats == 0:
            print ("There are no rats")
            Sewer_Choice()
        else:
            print('You lost 2 health')
            Health -= 2
            death()
            print ('Your health is '+ str(Health))
            print ("You earned 1 gold")
            Gold += 1
            print ('You have '+str(Gold)+ " gold.")
            Sewer_Choice()


def Trunk():
    global raging_centipedes
    global Gold
    global Health
    global Attack
    print ("You creep through the trunk roots and despise the dust, you can hear scuttling noises from all over")
    print ("A Raging Centipede! you exclaim as a huge on tries to attack you")
    print ("The centipede is level 4\n")
    if Attack >= 4 :
        if raging_centipedes == 0:
            print ("There are no centipedes")
            Trunk_Choice()
        print ("You slay the beast with ease")
        Gold += 2
        raging_centipedes -= 1
        print ("You earned 2 gold")
        Trunk_Choice()
    else:
        if rats < 1:
            print ("There are no centipedes")
            Trunk_Choice()
        Health -= 4
        raging_centipedes -= 1
        if Health <= 0:
            death()
        else:
            print ('You lost 3 health')
            print ('Your health is '+ str(Health))
            print ("You earned 2 gold")
            Gold += 2
            print ('You have '+str(Gold)+ "gold.")
            Trunk_Choice()


def Trunk_Choice():
    print("The beast is gone but you can hear more scuttling\n")
    print("Enter Aldren(1)")
    print("Leave to Aldren road(2)")
    print("Fight more centipedes(3)")
    if shadyfigure_instance == False:
        print ("Hack open a space in the trunk for the centipedes to get out(4)")
    valid = True
    while valid == True:
        response = input()
        if response == '1':
            print ('You are glad to leave the dusty ancient tree')
            Aldren()
            break
        elif response == '2':
            print ("You are glad to leave the dusty ancient tree and filthy city behind ")
            Aldren_road()
            break
        elif response == '3':
            print ("The centipedes stand no chance ")
            Trunk()
            break
        elif response == '4':
            if shadyfigure_instance == False:
                print ("You create a space and the centipedes sense thier new freedom and swarm into the streets")
                AttackAldren()
            else:
                Trunk_Choice
        else:
            print("Invalid input")
            continue


def Cemetary():
    global bonewalkers
    global Gold
    global Health
    global Attack
    print ("You march to the top of the the beautiful but also dreadful mountain. The tombstones glow unnaturaly")
    print ("A Bonewalker! you exclaim as a lond dead warrior  tries to attack you")
    print ("The bonewalker is level 6\n")
    if Attack >= 6:
        if bonewalkers < 1:
            print ("There are no bonewalkers")
            Cemetary_Choice()
        print ("You slay the not quite alive man with ease")
        Gold += 7
        bonewalkers -= 1
        print ("You earned 7 gold")
        Cemetary_Choice()
    else:
        if bonewalkers < 1:
            print ("There are no bonewalkers")
            Cemetary_Choice()
        Health -= 6
        bonewalkers -= 1
        if Health <= 0:
            death()   
        else: 
            print ('You lost 6 health')
            print ('Your health is '+ str(Health))
            print ("You earned 7 gold")
            Gold += 7
            print ('You have '+str(Gold)+ "gold.")
            Cemetary_Choice()


def Cemetary_Choice():
    global INCalduin
    print("The bonewalker is gone but you can hear more scraping\n") 
    print("Hike back to Calduin(1)")
    print("Leave to Calduin road(2)") 
    print("Fight more bonewalkers(3)")
    valid = True
    while valid == True:
        response = input()
        if response == '1':
            print ('You are glad to leave the eery mountain')
            INCalduin = False
            Calduin()
            break
        elif response == '2':
            print ("You are glad to leave Cemetary Mountain but sad to leave the enchanting city behind ")
            Calduin_road()
            break
        elif response == '3':
            print ("The dead shall relive thier demise ")
            Cemetary()
            break
        else:
            print("Invalid input")
            continue
#-----------------------


#Kindom-Borest----------
INBorest = True


def BKeep():
    print ('The high ceiling and perfectly decorated hall makes you feel a little bit stuffy and go up to the king')
    print (' The friendly and jovial king says, "you have really made an name for yourself here, and im getting bored with the Hogs Heads plain "food"\n Will you become my personal chef? "  ')
    print ('1. Become his chef (1)')
    print ('2. Your real goal is to start your own resturant, politly decline (2)')


def BEnter_Keep():
    if Borest_REP < 4:
        print ("The guards simply look at you and luagh at the boldness of a stranger they dont even know and turn away(!You need better reputation!)\n")
        Borest()
    if Borest_REP >= 4:
        print ('the guards welcome you into the hold hearing of your good deeds\n')
        BKeep()


def beggar():
    global beggar_instance
    global Borest_REP
    if Borest_REP < -1:
        print ("the mans eyes squint and and he starts yelling for guards. The guards lock you up in prison till you rot")
        death()
    print('The beggar lifts his head and attempts a smile, "Can you spare a coin" he asks\n')
    print('give the poor man some coin(1)')
    print('KIll the begger(2)')
    print('Leave the beggar(3)')

    valid = True
    while valid == True:
        response = input()
        if response == '1':
            if Gold >= 1:
                print ('You give the man some coin and wish him the best, he seems very grateful')
                Borest_REP += 1
                print ("You have 1 better reputation in Borest")
                beggar_instance = False
                Borest()
                
            else:
                print("You dont have the money either")
                Borest()
            break
        elif response == '2':
            print ("The mans gutteral screams chill your bones ")
            print ("You have lost 2 reputation")
            Borest_REP -= 2
            print ("Your reputation in Borest is "+str(Borest_REP))
            beggar_instance = False
            if Borest_REP < -1:
                print ("You are now reconized as a bandit")
                print ("Borest ")
            Borest()
            break
        elif response == '3':
            print ("You leave the beggar to his own filth")
            Borest()
        else:
            print("Invalid input")
            continue


def Hogs_Head():
    global Health
    global stamina
    global Gold
    print ('You sit and eye the travelers around you\n')
    print ('1. Listen in on rumors(1)')
    print ('2. Ask bartender for some food(2)')
    print ('3. Ask bartender to stay the night(3)')
    print ("4. Leave the Hogs Head(4)")

    valid = True
    while valid == True:
        response = input()
        if response == '1':
            print ('You hear them say...' + rumours())
            Hogs_Head()
            break
        elif response == '2':
            if Gold > 0:
                print ("You ask the bartender for some some food but become astonished as he comes out with a pile of glop. You cant believe he calls it food, but you eat it anyway\n")
                Health += 1
                Gold -= 1
                print ("You health is now " + str(Health)+ "\n")
                Hogs_Head()
            else:
                print("Not enough gold")
                Hogs_Head()
            break
        elif response == '3':
            if Gold > 9:
                print ("You lay down in the comfy bed providede and drift off peacefully ")
                stamina += 1
                Gold -= 10
                print ("Your stamina is now "+ str(stamina)+ "\n")
                Hogs_Head()
            else:
                print("Not enough gold")
                Hogs_Head()
            break
        elif response == '4':
            print ("You exit the comfy inn into Borest \n")
            Borest()
        else:
            print("Invalid input")
            continue


def Grumpy_Merchant():
    global Gold
    global Attack
    global Health
    global Rejuvination_Amulet
    global Gleaming_sword
    if Borest_REP < -1:
        print ("the mans eyes squint and and he starts yelling for guards. The guards lock you up in prison till you rot")
        Health -= 20
        death() 
    print ('The Merchant opens a few chests and displays what he has.')
    gold()
    if Gleaming_sword is True:
        print ('A gleaming sword (+ 3 damage (- 7 gold) (1)')
    else:
        print ('SOLD')
        
    if Rejuvination_Amulet is True:
        print ('A Rejuvination amulet (gives back 3 health after a fight(50 gold) (2)')
    else: 
        print ('SOLD')
    print ('A tasty looking glowing pear from the Lumin Forest (gives 2 health(1 gold) (3)')
    print ("SEll your ingredients(4)\n")
    print ('Leave the merchant(5)')
    
    valid = True
    while valid == True:
        response = input()
        if response == '1':
            if Gold >= 7:
                print ("When you pick up the sword you feel more sturdy and menacing\n")
                Gold -= 7
                Attack += 3
                Gleaming_sword = False
                
                Grumpy_Merchant()
            else:
                print ('!You dont have enought gold!\n')
                Grumpy_Merchant()
            break
        elif response == '2':
            print ("The expensive amulet must be very magical, it teems with energy")
            if Gold >= 50:
                print ('You place the amulet around your neck and feeled reassured with its protection\n')
                Gold -= 50
                Rejuvination_Amulet = False
                Grumpy_Merchant()
            else:
                print ('!Not enough gold!\n')
                Grumpy_Merchant()
            break
        elif response == '3':
            print ("You pick up the glowing pear and salivate wondering the amazing tast might be..")
            if Gold > 0:
                Gold -= 1
                print ('You eat the pear and fireworks of flavor burst into existence, you savor the sweet inside\n')
                Health += 2
                print ('Your Health is now ' + str(Health))
                Grumpy_Merchant()
            else:
                print ('!Not enough gold!\n')
                Grumpy_Merchant()
            break
            
        elif response == '5':
            print ("You turn away and walk towards- \n")
            Borest()
            break
        elif response == '4':
            print ("You show him what youve been collecting\n")
            Selling()

        else:
            print("Invalid input")
            continue


def borest_road():
    global INBorest
    global INAldren
    global INCalduin
    
    print ('You are on the Borest road (kindom roads allow you to travel to other kindoms) and can travel to..\n')
    print ('Lumin Forest (1)')
    print ('Darqthaal Cave(2)')
    print ('Aldren Kindom(3)')
    print ('Calduin Kindom(4)')
    print ('Triteem Kindom(5)')
    print ("Borest Kindom(6)")

    valid = True
    while valid == True:
        response = input()
        if response == '1':
            print (' You travel to the Lumin Forest in search of some new ingredients!')
            rand_road()
            Lumin_Forest()
            break
        elif response == '2':
            print ("You travel to Darqthaal Cave and see a fimiliar glow emitting from its gaping maw")
            rand_road()
            Darqthaal()
            break
        elif response == '3':
            print ("You travel to Aldren and the citys spiked roofs, warding feathers and, bone roofs remind of you of when you were a captive in the untamed forest there")
            rand_road()
            INAldren = False
            Aldren()
            break
        elif response == '4':
            print ("You travel to Calduin and are rewarded with a magical and alive city")
            rand_road()
            INCalduin = False
            Calduin()
            break
        elif response == '5':
            print ("You travel to the noble city of triteem. Misty mountains that soar through the sky create a stirring of adventure inside you.")
            rand_road()
            Triteem()
            break
        elif response == '6':
            print ("You go back into Borest ")
            INBorest = False
            Borest()
        else:
            print("Invalid input")
            continue


def Enter_Borest():
    global INBorest
    INBorest = False
    print ('You enter Borest and are exited to see Hogs Head(Tavern), a merchant, and the Kings Keep. \nYou also see lonely beggar, a sobbing woman and the accursed sewers.\n')


def Borest():
    global rats
    global beggar_instance
    global sob_woman
    global lost_boy
    global INBorest
    print ('Enter the Hogs Head(1)')
    print ('Talk to Merchant(2)')
    print ('Request a audience for the king(3)')
    if sob_woman == True:
        print ('Talk to sobbing woman(4)')
    else:
        print ('The woman is waiting(4)')
    if beggar_instance == True:
        print ('Talk to lonely beggar(5)')
    else:
        print ("The beggar has left(5)")
    print ('Enter the sewers(6)')
    print ('Leave Borest(7)')

    valid = True
    while valid == True:
        response = input()
        if response == '1':
            print ('You enter the Hogs Head Tavern and the warm glow of the fire welcomes you. the bartender announces that to stay the night is 10 gold and food is 1 gold.\nThere are also groups of people saying rumors.')
            Hogs_Head()
            break
        elif response == '2':
            print ("You walk up to the grumpy looking merchant and ask to browse his wares. He flashes a greedy grin ")
            Grumpy_Merchant()
            break
        elif response == '3':
            print ("You go up to the guards and ask for a audience with the king.")
            BEnter_Keep()
            break
        elif response == '4':
            if lost_boy == False:
                Sobbing_Woman()
            elif sob_woman == False:
                print ("The woman is waiting")
                Borest()
            else:
                print ("You walk up to the sobbing woman and gently coax her into telling you what happened")
                Sobbing_Woman()
                break
        elif response == '5':
            if beggar_instance == True:
                print ("You walk up to the lonely beggar and feel sorry for the knarled old man")
                beggar()
            else:
                print ("The beggar is gone")
                Borest()
            break
        elif response == '6':
            print ("You go to the sewers and a disgusting stench fills your nostrils ")
            Sewers()
            break
        elif response == '7':
            print ("You walk out onto Borest Road ready for more adventure and especially food! ")
            rats +=  2
            INBorest = True
            borest_road()
            break
        else:
            print("Invalid input")
            continue
#-----------------------


#Kindom-Aldren----------
INAldren = True
def AKeep():
    print ('The high ceiling and perfectly decorated hall makes you feel a little bit stuffy and go up to the king')
    print ('The friendly and jovial king says, "you have really made an name for yourself here, and im getting bored with the Hogs Heads plain "food"\n Will you become my personal chef?\n')
    print ('Become his chef (1)')
    print ('Your real goal is to start your own resturant, politly decline (2)')


def AEnter_Keep():
    if Borest_REP < 4:
        print ("The goblins simply look at you and cackle at the boldness of a stranger they dont even know and turn away(!You need better reputation!)")
        Aldren()
    if Borest_REP >= 4:
        print ('the goblins welcome you into the hold hearing of your good deeds')
        AKeep()


def Goble_Hut():
    global Health
    global stamina
    global Gold
    print ('You sit and eye the travelers around you very jumpily\n')
    print ('1. Listen in on rumors(1)')
    print ('2. Ask bartender for some food(1 gold(2)')
    print ('3. Ask bartender to stay the night(5 gold(3)')
    print ("4. Leave the Goble Hut(4)")

    valid = True
    while valid == True:
        response = input()
        if response == '1':
            print ('You hear them say... ' + rumours())
            Goble_Hut()
            break
        elif response == '2':
            if Gold > 0:
                print ("You ask the bartender for some some food but become astonished as he comes out with a pile of eyes uncooked. You cant believe he calls it food, but you eat it anyway\n")
                Health += 1
                Gold -= 1
                print ("You health is now " + str(Health)+ "\n")
                Goble_Hut()
            else:
                print ("Not enough gold")
                Goble_Hut()
            break
        elif response == '3':
            if Gold > 9:
                print ("You lay down in the uncomfortable bed provided and drift off to horrifying dreams\n")
                stamina += 1
                Gold -= 10
                print ("Your stamina is now "+ str(stamina)+ "\n")
                Goble_Hut()
            else:
                print ("Not enough gold")
                Goble_Hut()
            break
        elif response == '4':
            print ("You exit the filthy inn into Aldren \n")
            Aldren()
        else:
            print("Invalid input")
            continue


def Goblen_Shaman():
    global Gold
    global Attack
    global Health
    global stamina
    global Rabbits_Foot
    global Stamina_potion
    global trufflesb
    if Aldren_REP < -1:
        print ("the goblin shaman starts yelling for guards. The guards lock you up in prison till you rot")
        death() 
    print ('The Shaman opens a few chests and displays what he has.')
    gold()
    if Stamina_potion is True:
        print ('A Stamina Potion (+ 2 stamina (10 gold) (1)')
    else:
        print ('SOLD')
        
    if Rabbits_Foot is True:
        print ('A Rabbits_Foot (+ 1 damage(30 gold) (2)')
    else: 
        print ('SOLD')
    print ('A marvelous looking truffle that makes you almost faint at the sight of it (50 gold) (3)')
    print ("SEll your ingredients(4)")
    print ('Leave the merchant(5)')
    
    valid = True
    while valid == True:
        response = input()
        if response == '1':
            if Gold >= 7:
                print ("When you pick up the potion you feel rejuvinated")
                Gold -= 10
                stamina += 2
                Rabbits_Foot = False
                gold()
                Goblen_Shaman()
            else:
                print ('!You dont have enought gold\n')
                Goblen_Shaman()
            break
        elif response == '2':
            print ("The rabbit foot must be very magical, it teems with energy")
            if Gold >= 30:
                print ('You place the rabbit foot on astring around your neck and feeled reassured with its protection\n')
                Gold -= 30
                Rabbits_Foot = False
                gold()
                Goblen_Shaman()
            else:
                print ('!Not enough gold!\n')
                Goblen_Shaman()
            break
        elif response == '3':
            if Gold >= 30:
                print ("You pick up the completely amazing truffle and salivate wondering what the amazing tast might be..\n")
                Gold -= 50
                trufflesb += 1
                gold()
                Goblen_Shaman()
            else:
                print ('!You dont have enought gold!\n')
                Goblen_Shaman()
            break
        elif response == '5':
            print ("You turn away and walk towards- \n")
            Aldren()
            break
        elif response == '4':
            print ("You show him what youve been collecting\n")
            Selling()
            Goblen_Shaman()
        else:
            print("Invalid input")
            continue


def Aldren_road():
    global ALDREN
    global INBorest
    global INAldren
    print ('You are on the Aldren road (kindom roads allow you to travel to other kindoms) and can travel to..\n')
    print ('Skaldur Forest (1)')
    print ('Mistock Cave(2)')
    print ('Calduin Kindom(3)')
    print ('Triteem Kindom(4)')
    print ('Borest KIndom(5)')
    if ALDREN == False:
        print ("Aldren still burns its flames sky high")
    else:
        print ('Aldren Kindom(6)')

    valid = True
    while valid == True:
        response = input()
        if response == '1':
            print (' You travel to the Skaldur Forest dread filling your stomach')
            rand_road()
            Skaldur_Forest()
            break
        elif response == '2':
            print ("You travel the Mistick and see many standing stones of a lost civilization\nYou venture through the runes whilst brushing long strands of vines out of your face. The runes had amazing architecture and as you go around a corner you gasp in amazement when you see a waterfall\ncrashiong down misting across the runes and catching the sunlight ")
            rand_road()
            Mistick()
            break
        elif response == '3':
            print ("You travel to Calduin exited for the adventures ahead")
            rand_road()
            Calduin()
            break
        elif response == '4':
            print ("You travel to Triteem exited for the adventure ahead")
            rand_road()
            Darqthaal()
            break
        elif response == '5':
            print ("You travel to Borest exited for the adventure ahead")
            rand_road()
            INBorest = False
            Borest()
            break
        elif response == '6':
            if ALDREN == False:
                print ("ALDREN is destroyed")
                Aldren_road()
            else:
                print ("You travel back into Aldren")
                INAldren = False
                Aldren()
        else:
            print("Invalid input")
            continue


def Enter_Aldren():
     print ('You enter Borest and are exited to see Hogs Head(Tavern), a merchant, and the Kings Keep. \n You also see lonely beggar, a sobbing woman and the accursed sewers.\n')


def Aldren():
    global INAldren
    global raging_centipedes
    print ('Enter the Goble Hut(1)')
    print ('Talk to Goblen Shaman(2)')
    print ('Request a audience for the Chief(3)')
    if lost_boy == True:
        print ('Talk to the little boy(4)')
    else:
        print ('The boy has returned to his mother(4)')
    if shadyfigure_instance == True:
        print ('Talk to the shady figure(5)')
    else:
        print ("The shady figure has left(5)")
    print ('Enter the Ancient Trunk(6)')
    print ('Leave Aldren(7)\n')

    valid = True
    while valid == True:
        response = input()
        if response == '1':
            print ('You enter the Goble Hut Tavern and the warm glow of the fire welcomes you. the bartender announces that to stay the night is 10 gold and food is 1 gold.\nThere are also groups of goblins spouting rumors.')
            Goble_Hut()
            break
        elif response == '2':
            print ("You walk up to the mysterious looking shaman and ask to browse his wares. He flashes a thin smile ")
            Goblen_Shaman()
            break
        elif response == '3':
            print ("You go up to the guards and ask for a audience with the Chief.")
            AEnter_Keep()
            break
        elif response == '4':
            if lost_boy == False:
                print ("The infuriating boy is waiting for his banana")
                Borest()
            else:
                print ("You walk up to the boy and ask him what he is doing here")
                lostt_boy()
            break
        elif response == '5':
            if shadyfigureleave == True:
                print ("You walk up to the shady figure and notice his very cunning look and elvish ears")
                shadyfigure()
            else:
                print ("The shady figure is gone")
                Aldren()
            break
        elif response == '6':
            print ("You go to the Ancient Trunk and dust fills your eyes ")
            Trunk()
            break
        elif response == '7':
            print ("You walk out onto Aldren Road ready for more adventure and especially food! ")
            raging_centipedes +=  2
            INAldren = True
            Aldren_road()
            break
        else:
            print("Invalid input")
            continue
#-----------------------

#Kindom-Calduin----------
INCalduin = True
def CKeep():
    print ('The chamber is entertwined with nature and waterfalls pool into a large lake')
    print ('Admist the roar of the water emerges the alpha clad in plate and standing as a colloses, intimidating to say the least "you are a aid to my people and  a powerful ally, Is there any thing you desire?\n I will try to make it available to you\n')
    print ('Start a new resteruant(1)')
    print ('Enter any fruit name other than the ones of myth')


def CEnter_Keep():
    if Calduin_REP < 4:
        print ("The Proud elves hardly glance in your derection !You need better reputation!)")
        Calduin()
    if Calduin_REP >= 4:
        print ('the elves bow in respect while welcoming you into the chamber')
        CKeep()


def The_Garnished_Platter():
    global Health
    global stamina
    global Gold
    print ('You sit and eye the travelers around you very relaxed\n')
    print ('1. Listen in on rumors(1)')
    print ('2. Ask chef for some food(1 gold(2)')
    print ('3. Ask chef to stay the night(5 gold(3)')
    print ("4. Leave the Garnished Platter(4)")

    valid = True
    while valid == True:
        response = input()
        if response == '1':
            print ('You hear them say... ' + rumours())
            The_Garnished_Platter()
            break
        elif response == '2':
            if Gold > 0:
                print ("You ask the chef for some food and are rewarded with perfectly cooked and seasoned lamb with apple cider \n")
                Health += 1
                Gold -= 1
                print ("You health is now " + str(Health)+ "\n")
                The_Garnished_Platter()
            else:
                print ("Not enough gold")
                The_Garnished_Platter()
            break
        elif response == '3':
            if Gold > 9:
                print ("You lay down in the fancy bed provided and drift off to comfortable dreams\n")
                stamina += 1
                Gold -= 10
                print ("Your stamina is now "+ str(stamina)+ "\n")
                The_Garnished_Platter()
            else:
                print ("Not enough gold")
                The_Garnished_Platter()
            break
        elif response == '4':
            print ("You exit the tidy inn into the streets of Calduin \n")
            Calduin()
        else:
            print("Invalid input")
            continue


def Eleven_Enchanter():
    global Gold
    global Attack
    global Health
    global stamina
    global Calduin_REP
    if Calduin_REP < -1:
        print ("the elve starts signalling for guards. The guards lock you up in prison till you rot")
        death() 
    print ('The Enchanter lays down a table of elements asking what to enchant')
    gold()
    print ('Enchant Attack (+ 2 attack (100 gold) (1)')
    print ('Enchant Charisma (+ 1 Calduin REP (100 gold) (2)')
    print ('Accelerated Regineration (+ 4 stamina (45 gold) (3)')
    print ("SEll your ingredients(4)")
    print ('Leave the Enchanter(5)')
    
    valid = True
    while valid == True:
        response = input()
        if response == '1':
            if Gold >= 100:
                print ("Your fists suddenly harden at the transformation within them, becoming brass and menacing")
                Gold -= 100
                Attack += 2
                gold()
                Eleven_Enchanter()
            else:
                print ('!You dont have enought gold\n')
                Eleven_Enchanter()
            break
        elif response == '2':
            print ("The enchantress blows a mist in your direction and suddenly everyone seems more friendly towards you")
            if Gold >= 100:
                Gold -= 100
                Calduin_REP += 1
                gold()
                Eleven_Enchanter()
            else:
                print ('!Not enough gold!\n')
                Eleven_Enchanter()
            break
        elif response == '3':
            if Gold >= 45:
                print ("The enchanter places her hand on your chest and a welcoming wrmth envelops your body, you feel... refreshed\n")
                Gold -= 45
                stamina += 4
                gold()
                Eleven_Enchanter()
            else:
                print ('!You dont have enought gold!\n')
                Eleven_Enchanter()
            break
        elif response == '5':
            print ("You turn away and walk towards- \n")
            Calduin()
            break
        elif response == '4':
            print ("You show her what youve been collecting\n")
            Selling()
            Eleven_Enchanter()
        else:
            print("Invalid input")
            continue


def Calduin_road():
    global ALDREN
    global INBorest
    global INAldren
    global INCalduin
    print ('You are on the Calduin road (kindom roads allow you to travel to other kindoms) and can travel to..\n')
    print ('Norecast Palace (1)')
    print ('Dovenhiem Sea(2)')
    print ('Calduin Kindom(3)')
    print ('Triteem Kindom(4)')
    print ('Borest KIndom(5)')
    if ALDREN == False:
        print ("Aldren still burns its flames sky high")
    else:
        print ('Aldren Kindom(6)')

    valid = True
    while valid == True:
        response = input()
        if response == '1':
            print ('The Norecast palace has a mysterious aura that creates a magical feel to the mossy but stll snowy white rock that supports it ')
            rand_road()
            Norecast_Palace()
            break
        elif response == '2':
            print (" You travel to the very outskirts of calduin and are blinded by the briliant spakling life of the Dovenheim sea. A small port city standing there.")
            rand_road()
            Dovenhiem()
            break
        elif response == '3':
            print ("You travel to Calduin exited for the adventures ahead")
            rand_road()
            INCalduin = False
            Calduin()
            break
        elif response == '4':
            print ("You travel to Triteem exited for the adventure ahead")
            rand_road()
            Triteem()
            break
        elif response == '5':
            print ("You travel to Borest exited for the adventure ahead")
            rand_road()
            INBorest = False
            Borest()
            break
        elif response == '6':
            if ALDREN == False:
                print ("ALDREN is destroyed")
                Aldren_road()
            else:
                print ("You travel back into Aldren")
                INAldren = False
                Aldren()
        else:
            print("Invalid input")
            continue


def Enter_Calduin():
    global INCalduin
    INCalduin = False
    print ("You enter Calduin and are astonished by the architecture you see The Garnished Platter(Tavern), a Enchanter, the Alpha's Keep. \n You also see lonely beggar, a eleven maid and the accursed Cemetary Mountain.\n")


def Calduin():
    global INCalduin
    global bonewalkers
    print ('Enter the Garnished PLatter(1)')
    print ('Talk to the Enchantress(2)')
    print ('Request a audience for the Alpha(3)')
    print ('Climb up to Cemetary Mountain(4)')
    print ('Leave the fair city of Calduin(5)\n')

    valid = True
    while valid == True:
        response = input()
        if response == '1':
            print ('You enter the Garnished Platter and the warm glow of the fire welcomes you. the chef announces that to stay the night is 10 gold and food is 1 gold.\nThere are also groups of travelers spouting rumors.')
            The_Garnished_Platter()
            break
        elif response == '2':
            print ("You walk up to the mystical looking elve and ask to browse her wares. Her face is hidden inside a cowl")
            Eleven_Enchanter()
            break
        elif response == '3':
            print ("You go up to the guards and ask for a audience with the Alpha.")
            CEnter_Keep()
            break
        elif response == '4':
            print ("You travel towards the lonely bluff ")
            Cemetary()
            break
        elif response == '5':
            print ("You walk out onto CAlduin Road ready for more adventure and especially food! ")
            bonewalkers +=  1
            INCalduin = True
            Calduin_road()
            break
        else:
            print("Invalid input")
            continue
#-----------------------


#Kindom-Triteem---------
INTriteem = True


def TKeep():
    print ('The HAll has humble decorations but the blue and fiery orange fires cast a comfortable glow on the hall. Thick oak beams stretch into the cieling above')
    print ('Alone sitting on a guilded throne sat the Dwarf Warden , intimidating with his masked steel helmet and blunderbuss "you have aided the dwarfs in vanquishing foes and much more, Is there any thing you desire?\n I will try to make it available to you\n')
    print ('Start a new resteruant(1)')
    print ('Enter any fruit name -')


def TEnter_Keep():
    if Triteem_REP < 4:
        print ("The ancient dwarfs gaze on you with searching looks, They turn away from the unworthy(!You need better reputation!)")
        Calduin()
    if Triteem_REP >= 4:
        print ('the dwarfs slam their chest with one hand in custom form of respect while welcoming you into the hall')
        CKeep()


def The_Boiled_Rock():
    global Health
    global stamina
    global Gold
    print ('You sit and eye the travelers around you \n')
    print ('1. Listen in on rumors(1)')
    print ('2. Ask bartender for some food(1 gold(2)')
    print ('3. Ask bartender to stay the night(10 gold(3)')
    print ("4. Leave the Boiled Rock(4)")

    valid = True
    while valid == True:
        response = input()
        if response == '1':
            print ('You hear them say... ' + rumours())
            The_Boiled_Rock()
            break
        elif response == '2':
            if Gold > 0:
                print ("You ask the sturdy bartender for some food and are rewarded with steamed weldfish and rich hot cocoa \n")
                Health += 1
                Gold -= 1
                print ("You health is now " + str(Health)+ "\n")
                The_Boiled_Rock()
            else:
                print ("Not enough gold")
                The_Boiled_Rock()
            break
        elif response == '3':
            if Gold > 9:
                print ("You lay down in the sturdy bed provided and drift off to comfortable dreams\n")
                stamina += 1
                Gold -= 10
                print ("Your stamina is now "+ str(stamina)+ "\n")
                The_Boiled_Rock()
            else:
                print ("Not enough gold")
                The_Boiled_Rock()
            break
        elif response == '4':
            print ("You exit the comfy tavern into the bridges and beam supported outcroppings of Triteem\n")
            Triteem()
        else:
            print("Invalid input")
            continue


def Master_of_Metal():
    global Gold
    global Attack
    global Health
    global stamina
    global Triteem_REP
    if Triteem_REP < -1:
        print ("the dwarf starts signals for guards. The guards lock you up in prison till you rot")
        death() 
    print ('The Master of Metal has groups of people crowded around him examing and in marveling at his work ')
    gold()
    print ('Inforced dagger (+ 1 attack (50 gold) (1)')
    print ('Friendly Helm (+ 1 Triteem REP (100 gold) (2)')
    print ('Metal Infused Muscle(+ 3 stamina (40 gold) (3)')
    print ("SEll your ingredients(4)")
    print ('Leave the Master of Metal(5)')
    
    valid = True
    while valid == True:
        response = input()
        if response == '1':
            if Gold >= 50:
                print ("You clasp the dagger to your belt, its weight carries some comfort with it")
                Gold -= 50
                Attack += 2
                gold()
                Master_of_Metal()
            else:
                print ('!You dont have enought gold\n')
                Master_of_Metal()
            break
        elif response == '2':
            print ("The instant the helm is placed on your head a wave seems to spread from your body. People give respectful glances and smiles your way.")
            if Gold >= 100:
                Gold -= 100
                Triteem_REP += 1
                gold()
                Master_of_Metal()
            else:
                print ('!Not enough gold!\n')
                Master_of_Metal()
            break
        elif response == '3':
            if Gold >= 40:
                print ("The initial puncture stings but after you feel fortified and strong\n")
                Gold -= 40
                stamina += 3
                gold()
                Master_of_Metal()
            else:
                print ('!You dont have enought gold!\n')
                Master_of_Metal()
            break
        elif response == '5':
            print ("You turn away and walk towards- \n")
            Triteem()
            break
        elif response == '4':
            print ("You show him what youve been collecting\n")
            Selling()
            Master_of_Metal
        else:
            print("Invalid input")
            continue


def Triteem_road():
    global ALDREN
    global INBorest
    global INAldren
    global INCalduin
    global INTriteem
    print ('You are on the Triteem road (kindom roads allow you to travel to other kindoms) and can travel to..\n')
    print ('Folly(Dwarfs Bane)(1)')
    print ('Duvelden Crags(2)')
    print ('Calduin Kindom(3)')
    print ('Triteem Kindom(4)')
    print ('Borest KIndom(5)')
    if ALDREN == False:
        print ("Aldren still burns its flames sky high")
    else:
        print ('Aldren Kindom(6)')

    valid = True
    while valid == True:
        response = input()
        if response == '1':
            rand_road()
            Folly()
            break
        elif response == '2':
            print ("You travel to Folly, your weapons faithfully girded at your hip and a grim expression")
            rand_road()
            Folly()
            break
        elif response == '3':
            print ("You travel to Calduin exited for the adventures ahead")
            rand_road()
            INCalduin = False
            Calduin()
            break
        elif response == '4':
            print ("You travel back into Triteem")
            rand_road()
            Triteem()
            break
        elif response == '5':
            print ("You travel to Borest exited for the adventure ahead")
            rand_road()
            INBorest = False
            Borest()
            break
        elif response == '6':
            if ALDREN == False:
                print ("ALDREN is destroyed")
                Aldren_road()
            else:
                print ("You travel to Aldren exited for the adventure ahead")
                INAldren = False
                rand_road()
                Aldren()
        else:
            print("Invalid input")
            continue


def Enter_Triteem():
    global INCalduin
    INCalduin = False
    print ("You enter Triteem and instantly feel comforted by the warm glow huge brazers cast on vast bridges stretching across the snowy cliffs to other outcroppings\n you see The Boiled Rock(Tavern), The Master of Metal,and the Wardens Keep. \n You also see a lonely beggar, a dwarven statue and the accursed Folly cavern.\n")


def Triteem():
    global INTriteem
    global Trolls
    print ('Enter the Boiled Rock(1)')
    print ('Talk to the Master of Metal(2)')
    print ('Request a audience with the Warden(3)')
    print ('Descend into the Folly Cavern(4)')
    print ('Leave the noble city of Triteem(5)\n')

    valid = True
    while valid == True:
        response = input()
        if response == '1':
            print ('You enter the Boiled Rock and the warm glow of the fire welcomes you. the bartender announces that to stay the night is 10 gold and food is 1 gold.\nThere are also groups of travelers spouting rumors.')
            The_Boiled_Rock()
            break
        elif response == '2':
            print ("You walk up to the esteemed metal worker")
            Master_of_Metal()
            break
        elif response == '3':
            print ("You go up to the guards and ask for a audience with the Warden.")
            TEnter_Keep()
            break
        elif response == '4':
            print ("You travel to the bone dry and ghastly smelling cavern opening, knowing that trouble awaits. Frigid air bites your nose and chills your bones ")
            Folly()
            break
        elif response == '5':
            print ("You walk out onto Triteem Road ready for more adventure and especially food! ")
            Trolls +=  1
            INTriteem = True
            Triteem_road()
            break
        else:
            print("Invalid input")
            continue
#-----------------------


#Forests----------------
def Lumin_Forest():
    global Health
    global peach 
    global dragon_egg
    global coco_beans
    global peachb
    global coco_beansb
    global dragon_eggb
    print ('By looking around you can see a shadowed section, a cove on top of a hill, and  some stumps\n')
    print ('1. Examine shaded trees(1)')
    print ('2. Look in cove(2)')
    print ('3. Examine the stumps(3)')
    print ('4. Leave the Lumin Forest(4)')
    valid = True
    while valid == True:
        response = input()
        if response == '1':
            if peach > 0:
                print ('By looking in the trees you discover some Glowing Peaches!')
                print ('You got ' + str(peach) +' glowing peaches!')
                peach -= 2
                peachb += 2
                Lumin_Forest()
            else:
                print ("There are no peaches growing")
                Lumin_Forest()
            break
        elif response == '3':
            if coco_beans > 0:
                print ("You found some rich coco beans! ")
                print ("You got "+str(coco_beans)+' coco beans')
                coco_beans -= 3
                coco_beansb += 3
                Lumin_Forest()
            else:
                print ("there are no coco_beans right now")
                Lumin_Forest()
            break
        elif response == '2':
            if dragon_egg > 0:
                print ("The cove suddenly illuminates with dragons fire! You run to a dragon egg pick it up and run out as fast as you can\n you are skimmed however and lose 4 health  ")
                print ("You got "+ str(dragon_egg)+" dragon egg")
                Health -= 4
                dragon_eggb += 1
                death()
                Lumin_Forest()
            else:
                print ("There arent any dragon eggs right now")
                Lumin_Forest()
            break
        elif response == '4':
            print ("You leave the peaceful forest behind")
            coco_beans +=3
            peach += 2
            dragon_egg += 1
            lumin_road()
        else:
            print("Invalid input")
            continue


def lumin_road():
    global INBorest
    print('You are on the Lumin road and can travel to..\n')
    print('Borest (1)')
    print('Darqthaal Cave(2)')
    print('Go back into the Lumin forest(3)')

    valid = True
    while valid == True:
        response = input()
        if response == '1':
            print (' You travel on to Borest and see a sprawling city of pure white spires with a navy blue pointed roofs. Its majesticness leaves you in awe')
            INBorest = False
            Borest()
            break
        elif response == '2':
            print ("You travel to Darqthaal Cave and see a fimiliar glow emitting from its gaping maw")
            Darqthaal()
            break
        elif response == '3':
            print ("You back into the Lumin forest")
            Lumin_Forest()
            break
        else:
            print("Invalid input")
            continue


def Skaldur_Forest():
    global Health
    global truffles
    global bananas
    global brackberries
    global trufflesb
    global bananasb
    global brackberriesb
    print ('You warily look around you can see a cliff overhang, a gove on top of a hill, and a glowing campfire in the distanse\n')
    print ('1. Examine cliff overhang(1)')
    print ('2. Look in grove(2)')
    print ('3. Examine the campfire(3)')
    print ('4. Leave the accursed Skaldur Forest(4)')
    valid = True
    while valid == True:
        response = input()
        if response == '1':
            if peach > 0:
                print ('By looking in the trees you discover some Brackberries!')
                print ('You got ' + str(brackberries) +' glowing peaches!')
                brackberries -= 2
                brackberriesb += 2
                Skaldur_Forest()
            else:
                print ("There are no brackberries growing")
                Skaldur_Forest()
            break
        elif response == '2':
            if bananas > 0:
                print ("You found some ripe bananas! ")
                print ("You got "+str(bananas)+' bananas')
                bananas -= 3
                bananasb += 3
                Skaldur_Forest()
            else:
                print ("there are no bananas right now")
                Skaldur_Forest()
            break
        elif response == '3':
            if truffles > 0:
                print ("The fire is a NATIVE CAMP, there is a truffel sitting on a pedastool, Then the natives pounce on you with feral aggresiveness ")
                print ("You got "+ str(truffles)+" truffel")
                print ("You lost 10 health")
                Health -= 10
                trufflesb += 1
                if Health <= 0:
                    print("However The natives brutally ravage your body and your last moments are spent in extruciating pain")
                    death()
            else:
                print ("The camp is destroyed and there are no truffles")
                Skaldur_Forest()
            break
        elif response == '4':
            print ("You leave the horrific forest behind")
            brackberries +=3
            bananas += 2
            truffles += 1
            skaldur_road()
        else:
            print("Invalid input")
            continue


def skaldur_road(): 
    global INAldren
    print('You are on the skaldur road and can travel to..\n')
    print('Aldren (1)')
    print('Mistick Runes(2)')
    print('Go back into the Skaldur forest(3)')

    valid = True
    while valid == True:
        response = input()
        if response == '1':
            print (' You travel on to Aldren exited for the adventures ahead')
            INAldren = False
            Aldren()
            break
        elif response == '2':
            print ("You travel the Mistick and see many standing stones of a lost civilization\nYou venture through the runes whilst brushing long strands of vines out of your face. The runes had amazing architecture and as you go around a corner you gasp in amazement when you see a waterfall\n crashiong down misting across the runes and catching the sunlight ")
            Mistick()
            break
        elif response == '3':
            print ("You back into the Skaldur forest")
            Skaldur_Forest()
            break
        else:
            print("Invalid input")
            continue


def Duvelden():
    print('unfinished')


def duvelden_road():
    print('unfinished')


def Norecast_Palace():
    print('unfinished')


def norecast_palace_road():
    print('unfinished')
#----------------------

#Caves------------------
def Darqthaal():
    global bandits_level
    global Gold
    print ('You stride down the cave and suddenly hear voices and a glow coming down the passage. You know this is a bandit hideout \nbecuase of the grim voices, you huddle behind a rock decide what you should do\n')
    print ('The bandits are level ' + str(bandits_level) + '(level coincides with damage)')
    print ('1. Attack the bandits!(1)')
    print ('2. Retreat from the cave(2)\n')
   
    valid = True
    while valid == True:
        response = input()
        if response == '1':
            print ('You approach the bandits, ready for the fight and they give you a ferocious growl underneath their bandanas and begin THE CONFLICT')
            bandits()
            print ('You finish the fight and exit proud to rid the world of those cruel fellows')
            Gold += 5
            gold()
            darqthaal_road()
            break
        elif response == '2':
            print ("You retreat from the cave glad to escape the conflict that could of arisen. ")
            darqthaal_road()
            break
        else:
            print("Invalid input")
            continue


def darqthaal_road():
    global INBorest
    print ('You are on the Darthaal road and can travel to..\n')
    print ('Borest (1)')
    print ('Lumin forest(2)')
    print ('Back into the cave(3)')

    valid = True
    while valid == True:
        response = input()
        if response == '1':
            print ('You travel on to Borest and see a sprawling city of pure white spires with a navy blue pointed roofs. Its majesticness leaves you in awe')
            INBorest = False
            Enter_Borest()
            Borest()
            break
        elif response == '2':
            print ("You travel to Lumin Forest and find enjoyement in the lush undergrowth fantasizing about the delectible ingredients you might find ")
            Lumin_Forest()
            break
        elif response == '3':
            print ("You travel back into the dank cave ")
            Darqthaal()
            break
        else:
            print("Invalid input")
            continue


def Mistick():
    global legendfruitb
    global legendfruit
    global Health
    global gladiatorsword
    global stamina
    print ("Three things stand out to you\n") 
    print ("the waterfall of course(1)")
    print(" a cracked temple(2)") 
    print(" a huge coliseum which by the looks of it will consume 4 stamina(3)\n")
    valid = True
    while valid == True:
        response = input()
        if response == '1':
            print (' You examine the waterfall and slowly start to see a peculiar glint behind it and find a lock covering a steel inforced door')
            print ('There are three sliders on the lock with numbers ')
            print('What three numbers unlock this ')

            Mistick()
            break
        elif response == '2':
            print ("You walk under a broken door and are creeped out by the stone masks littered about the open space and also see light down one passage ")
            print ("Should you explore it(1) or play it safe and leave(2)")
            okay = True
            while okay == True:
                answer = input()
                if answer == '1':
                    print (' You walk down the passage and are suddenly attacked by a undead priest, some evil magic keeping it alive long past death')
                    print ('You lose 20 health from the savage druagr')
                    Health -= 20
                    death()
                    if legendfruit == 0:
                        print ("You are weakened and leave the temple")
                        Mistick()
                    else:
                        print ("The beast has weakened you but you are magnificintly rewarded by a fruit you thought was a myth... THE LEGENDFRUIT.\neverything you ever seen pales in comparrisen to its beautiful golden glow, and its warm the touch")
                        legendfruitb += 1
                        legendfruit -= 1
                        Mistick()
                    break
                elif answer == '2':
                    print ("You run from the temple")
                    Mistick()
                    break
                else:
                    print("Invalid input")
            continue
        elif response == '3':
            global Attack
            global gladiatorsword
            if gladiatorsword == True:
                stamina -= 4
                Stamina()
                print ("It takes hours to travel down into the pit of the massive coliseum and when you explore around find a old gladiators sword with the words NEVER DEMUR engraved in its blade.\nits suprising well kept and  you draw it from the fine sand ")
                Attack += 2
                print ("Your attack has increased 2")
                gladiatorsword = False
                Mistick()
            else:
                ("You have already explored here so you dont venture down the tedious steps")
                Mistick()
            break
        else:
            print("Invalid input")
            continue


def mistick_road():
    global INAldren
    print ('You are on the Mistick road and can travel to..\n')
    print ('Aldren (1)')
    print ('Skaldur forest(2)')
    print ('Back into the runes(3)')
    
    valid = True
    while valid == True:
        response = input()
        if response == '1':
            print (' You travel on to Aldren and keep your eyes open for natives')
            INAldren = False
            Enter_Aldren()
            Aldren()
            break
        elif response == '2':
            print ("You travel to Skaldur Forest and dread what awaits in the shadows ")
            Skaldur_Forest()
            break
        elif response == '3':
            print ("You go back to the time weatherd runes ")
            Mistick()
            break
        else:
            print("Invalid input")
            continue


def Dovenhiem():
    print('unfinished')


def dovenhiem_road():
    print('unfinished')


def Folly():
    print('unfinished')


def folly_road():
    print('unfinished')
#-----------------------
    print('unfinished')


#Starting-------
def VistiBorest():
    global Health
    print('You arrive in Borest but as you begin to enter through the gates the guards start to question you\n')
    print('Try to persuade them that you mean no harm (1)')
    print('Walk around the walls and try to find a way in (2)')
    print('Demand entrance to the city(3)')

    valid = True
    while valid == True:
        response = input()
        if response == '1':
            print ('You explain were youve come from and they thank you for the native tribes info. You pass through')
            Enter_Borest()
            Borest()
            break
        elif response == '2':
            print ("As you walk you find a sketchy sewer drain that has broken bars and enter ")
            Sewers()
            break
        elif response == '3':
            Health -= 20
            death()
            break
        else:
            print("Invalid input")
            continue


def VisitLumin():
    Lumin_Forest()


def VisitDarqthaal():
    Darqthaal()


def Escape():  
    global stamina
    print ('You run away and stumble apon a high bluff and can see the entire island your on. However travel is limited\n')
    print ('Closest to you is the kindom Borest(1)')
    print ('Medium distance is a lush forest(2)')
    print ('Farthest is a mysterious cave(3)')

    valid = True
    while valid == True:
        response = input()
        if response == '1':
            print ('You travel on to Borest and see a sprawling city of pure white spires with a navy blue pointed roofs. Its majesty leaves you in awe.')
            stamina -= 1
            print ("Your stamina is now " + str(stamina)) 
            VistiBorest()
            break
        elif response == '2':
            print ("You travel to the lush forest known as the Lumin Forest and are exited to see what sort of delectible ingredients you could find!")
            stamina -= 2
            print ("Your stamina is now " + str(stamina)) 
            VisitLumin()
            break 
        elif response == '3':
            print ("You run to the cave known as Darqthaal and notice a suprising amount of light emitted from its maw as night falls. ")
            stamina -= 3
            print ("Your stamina is now " + str(stamina))
            VisitDarqthaal()
            break
        else:
            print("Invalid input")
            continue


def Begin():
    global Health
    print ('These shrooms could flatten the natives around you but you are unsure about the risk it could put you in\n')
    print ('Throw it at the natives in hopes to destroy them (1)')
    print ('slowly tear apart the shroom and pull out the flammable goo and burn your bonds (2)')
    print ('threaten the natives and force them to let you go(3)')


    valid = True
    while valid == True:
        response = input()
        if response == '1':
            print ('Your attempts are foolish, as you throw the mushroom it explodes and you die with the natives')
            Health -= 10
            death()
            break
        elif response == '2':
            print (" Your bonds burn away and you slowly creep away into the darkness")
            Escape()
            break
        elif response == '3':
            print ("The natives are frightened and you feel powerful as you exit the camp unharmed")
            Escape()
            break
        else:
            print("Invalid input")
            continue


def start():
    global Health
    Player_Profile()
    print ('You awake to the sound of continious drumming from the ferocious natives \nand wonder how everything couldve gone so wrong. Your group of traveling chefs had \nonly been scouting for delicious mushrooms after all. Everything you have is gone \nexept your most favorite forest green cloke that had many pockets. As you survey\nthe sourrounding area you realize you only have a couple options.\n')
    print ('You challenge the natives(1)')
    print ('You reach into your cloak(2)')
    print ('You try to loosen your bonds(3)' )   

    valid = True
    while valid == True:
        response = input()
        if response == '1':
            print ('The natives are so offended they chop your head of and ironically being a chef serve you to their king on a silver plater')
            Health -= 10
            death()
            break
        elif response == '2':
            print ("you feel around in the cloak and to your astonishment find your beloved exploding shrooms. The natives thought they were harmless but you know the truth")
            Begin()
            break
        elif response == '3':
            print ("You will find that they weren't as tight as you expected. You slowly creep into the darkness.")
            Escape()
            break
        else:
            print("Invalid input")
            continue


def Palyerinfo():
    print ('Start Game (1)' )   

    valid = True
    while valid == True:
        response = input()
        if response == '1':
            Name()
        else:
            exit
    
#---------------

Palyerinfo()