# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("You")
define f = Character("Friend")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg uni

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show sylvie blue normal

    # These display lines of dialogue.
    
    "Your parents have drugs"   
    "Your friend knows about drugs"
    hide sylvie blue normal
    show lucy happy
    f "Hey, let's steal drugs"
    menu:
        "Do you want to steal drugs?"
        "Yes":
            jump high

        "No... I'm good":
            jump cmon
label cmon:
    scene bg uni
    show lucy happy
    menu:
        f "C'mon, just take the drugs"
        "Yes":
            jump high

        "No... I'm good":
            jump cmon

label high:
    scene bg uni
    show sylvie blue normal
    y "I'm so high rn"
    "The End"

    # This ends the game.

    return
