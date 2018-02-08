# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# Comment is the PICTURE NAME corresponding to the character
define y = Character("You") # sylvie blue normal
                            # sylvie blue overdose
define f = Character("Friend") # lucy happy
define mom = Character("Mom") # mom
define dad = Character("Dad") # dad
define judge = Character("Judge") # morty
define police = Character("Police Officer") # police
define bae = Character("Boyfriend") # bae normal
define doc = Character("Doctor") # doctor
define dealer = Character("Drug Dealer")

# PICTURE NAMEs of the backgrounds
# bg courtroom
# bg doctor
# bg house
# bg uni
# bg all black
# bg all red
# bg jail

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg house

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show dad

    # These display lines of dialogue.
    
    "Honey, I finally got the painkillers for my knee pain."  

    hide dad
    show mom
    "That’s great sweetie! Now you can go to work without worrying about pain."
    hide mom

    show lucy happy
    f "Hey I heard your parents talking and your dad got painkillers. I’ve heard that they’re super fun. Let's steal your dad's drugs and get high."

    menu:
        "Do you want to steal drugs?"
        "Yes":
            jump high

        "No... I'm good":
            jump cmon
            
label cmon:
    scene bg house
    show lucy happy
    menu:
        f "C'mon, just take the drugs"
        "Yes":
            jump high

        "No... I'm good":
            jump cmon

label high:
    scene bg house
    show sylvie blue giggle
    y "I feel so good!"

label depressed:
    scene bg house
    show sylvie blue normal
    "Two weeks have passed since you used the painkillers."
    "You have been feeling depressed lately."
    menu:
        "Would you like to steal more drugs?"
        "Yes":
            jump highAgain
    
label highAgain:
    scene bg house
    show sylvie blue giggle
    y "These painkillers make life so much easier."
    "You decide to steal pills regularly"
    jump parentsConfront
    
    
label parentsConfront:
    scene bg house
    show mom at left
    show dad at right
    show sylvie blue normal
    
    dad "Sweetie, I've noticed that some of my pills have gone missing"
    menu:
        mom "Are you taking painkillers from your father"
        "I'm sorry. I have a problem.":
            mom "It's good to admit you have a problem. We'll get you help. We still love you"
            jump getHelp
        "I'm not that type of girl, mom.":
            jump lockUpDrugs

    
label lockUpDrugs: 
    scene bg house
    show sylvie blue normal
    "You sneak into your parents room to steal more painkillers."
    "You find out that your parents have locked up the painkillers"
    menu:
        "How will you get more drugs?"
        "Seek out a Drug Dealer":
            jump DrugDeal
        "Fake pain to get a prescription":
            jump DoctorsOffice

label DrugDeal:
    scene bg uni
    show shady
    dealer "Yo I have the drugs, give me your money."
    "You pay the drug dealer off and get the drugs."
    hide shady
    "But before you can make your get away, a police officer finds you!"
    jump policeScene

label policeScene:
    scene bg uni
    show police
    police "You’ve been caught in the middle of a drug deal young lady. We’re taking you to jail."
    jump jail

label jail:
    scene bg jail
    show sylvie blue surprised
    y "I can’t believe I got caught buying drugs. What are my parents going to think? How did I get like this?"
    jump courtScene

label courtScene:
    scene morty
    judge "You’ve been charged with possession of prescription drugs that were not prescribed to you. We are going to sentence you to one year of rehab so you can get the help you need."
    jump getHelp 


label  DoctorsOffice:
    scene bg doctor
    show sylvie blue normal
    y "Hey doc, I have severe back pain. Could you prescribe me some drugs to help with this?"
    hide sylvie blue normal
    show doctor
    doc "Sure, honey. Let me just write up a prescription. But be careful, it’s easy to get addicted to this medication."

label SOConfronts:
    scene bg house
    show bae normal
    bae "My love, we need to talk. You've been using painkillers and it's getting out of hand. You need to get help."
    
    hide bae
    show sylvie blue normal
    menu:
        bae "Will you let me get you help for your prescription drug problem"
        "Yes my love. Thank you for being so supportive.":
            jump getHelp

        "You need to mind your own business. I'm just using those drugs for fun. It's not a big deal.":
            jump SOLeaves
    
label SOLeaves:
    scene bg house
    show bae normal
    bae "I can't do this anymore. I've been so supportive of you, but if you don't want to get help then I'm leaving."
    hide bae
    
    show sylvie blue surprised
    menu:
        "Oh no, he left me! I love him so much and can't stand to be without him."
        "Do drugs to numb the pain.":
            jump OD

        "He was so right about everything. I need to get help.":
            jump getHelp

label OD: # Ethan
    # sylvie blue overdose
    # bg house
    # bg all black
    # bg all red

    # define y = Character("You") # sylvie blue normal
    # define mom = Character("Mom") # mom


    scene bg house

    show sylvie blue normal
    y "The love of my life has left me."
    y "..."
    y "......"
    y "........."

    menu:
        "Should I ...?"
        "Get help":
            jump getHelp
        "Just one to numb the pain":
            jump ODhaha

label ODhaha:
    scene bg house

    show sylvie blue normal
    y "Maybe another pill..."
    y "..."
    y "..."
    y "One more couldn't hurt"
    y "Oops.."
    hide sylvie blue normal

    show sylvie blue overdose
    y "hehe."
    y "hehehe."
    hide sylvie blue overdose

    scene bg all black
    y "hehehehehe."

    scene bg all red
    show sylvie blue overdose
    y "HEHEHEHEHEHE"
    hide sylvie blue overdose
    "Here's what could have happened if you got help."
    jump getHelp

label getHelp:

    scene bg doctor
    show doctor
    "Admitting that you have a problem is the first step to overcoming it."
    "Drug abuse is a complex problem. It requires the support of friends and family to overcome."
    "SAMHSA (Substance Abuse and Mental Health Services Administration) has a confidential, free, 24-hour-a-day, 365-day-a-year information service, for individuals and family members facing mental and/or substance use disorders."

    "Call 1-800-662-HELP"

    hide doctor
    return


