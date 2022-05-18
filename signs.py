import random
from random import randint

name = ""
user_sign = ""
sign_readings = {
    "Aries": """The first sign of the zodiac, Aries loves to be number one. 
    Naturally, this dynamic fire sign is no stranger to competition. 
    Bold and ambitious. Aries dives headfirst into the most challenging situations...
    —and they'll make sure they always come out on top!""",

    "Taurus": """What sign is more likely to take a six-hour bath... 
    followed by a luxurious Swedish massage... 
    and decadent dessert spread?... 
    Why Taurus, of course! Taurus is an earth sign represented by the bull. 
    Like their celestial spirit animal: 
    Taureans enjoy relaxing in serene, bucolic environments surrounded by soft sounds, and succulent flavors.""",

    "Gemini": """Have you ever been so busy that you wished you could clone yourself just to get everything done? 
    That's the Gemini experience in a nutshell. Spontaneous, playful, and adorably erratic, Gemini is driven by its 
    insatiable curiosity. Appropriately symbolized by the celestial twins, this air sign was interested in so many 
    pursuits that it had to double itself. You know, NBD... """,

    "Cancer": """Represented by the crab, Cancer seamlessly weaves between the sea and shore representing Cancer’s 
    ability to exist in both emotional and material realms. Cancers are highly intuitive and their psychic abilities 
    manifest in tangible spaces. But—just like the hard-shelled crustaceans—this water sign is willing to do whatever 
    it takes to protect itself emotionally. In order to get to know this sign, you're going to need to establish 
    trust! """,

    "Leo": """Roll out the red carpet because Leo has arrived. Passionate, loyal, and infamously dramatic, 
    Leo is represented by the lion and these spirited fire signs are the kings and queens of the celestial jungle. 
    They're delighted to embrace their royal status: Vivacious, theatrical, and fiery, Leos love to bask in the 
    spotlight and celebrate… well, themselves. """,

    "Virgo": """You know the expression, "if you want something done, give it to a busy person?" Well, that definitely 
    is the Virgo anthem. Virgos are logical, practical, and systematic in their approach to life. Virgo is an earth 
    sign historically represented by the goddess of wheat and agriculture, an association that speaks to Virgo's 
    deep-rooted presence in the material world. This earth sign is a perfectionist at heart and isn’t afraid to 
    improve skills through diligent and consistent practice. """,

    "Libra": """Balance, harmony, and justice define Libra energy. As a cardinal air sign, Libra is represented by 
    the scales (interestingly, the only inanimate object of the zodiac), an association that reflects Libra's 
    fixation on establishing equilibrium. Libra is obsessed with symmetry and strives to create equilibrium in all 
    areas of life — especially when it comes to matters of the heart. """,

    "Scorpio": """Elusive and mysterious, Scorpio is one of the most misunderstood signs of the zodiac. Scorpio is a 
    water sign that uses emotional energy as fuel, cultivating powerful wisdom through both the physical and unseen 
    realms. In fact, Scorpio derives its extraordinary courage from its psychic abilities, which is what makes this 
    sign one of the most complicated, dynamic signs of the zodiac. """,

    "Sagittarius": """Oh, the places Sagittarius goes! But… actually. This fire sign knows no bounds. Represented by 
    the archer, Sagittarians are always on a quest for knowledge. The last fire sign of the zodiac, Sagittarius 
    launches its many pursuits like blazing arrows, chasing after geographical, intellectual, and spiritual 
    adventures. """
}

while True:
    user_sign = input("Please enter your star sign: ").title()
    while user_sign not in sign_readings:
        print("Ahh, I can not help you here... you do not have a sign under the stars, tell me again, now SERIOUSLY!!!")
        user_sign = input("Please enter your star sign: ").title()

    print("Welcome to the world of wonder, my precious, and who might you be... you are familiar?")
    name = input("ENTER YOUR NAME: ")
    while name == "":
        print("Try again... you left it empty...")
        name = input("ENTER YOUR NAME: ")

    print("Ahhh yes...." + name + " I knew you'd come in to seek the ways of the stars....")
    print("Something tells me, you're a " + user_sign + " is that right?")
    answer_1 = input("Enter 'Yes' or 'No'  followed by enter key: ")
    if answer_1.lower() == "yes":
        continue
    else:
        print("Hmmm... that's odd, the spirits normally don't do me wrong...")
        print("Tell me then, what are your stars?")
        user_sign = input("Please enter your star sign: ")
        while user_sign not in sign_readings:
            print("Ahh, I can not help you here... you do not have a sign under the stars, tell me again, now SERIOUSLY!!!")
            user_sign = input("Please enter your star sign: ").title()
        print("Right... a, " + user_sign + ".")