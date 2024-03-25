#Characters
define t = Character ("Teacher")
define kt = Character ("Kurt")
define j = Character ("Jerub")
define e = Character ("Engel")
define k = Character ("Kuro")
define s = Character ("Shiro")
#NVL characters are used for the phone texting

define kt_nvl = Character("Kurt", kind=nvl, callback=Phone_ReceiveSound)
define j_nvl = Character("Jerub", kind=nvl, callback=Phone_ReceiveSound)
define e_nvl = Character("Engel", kind=nvl, callback=Phone_ReceiveSound)

#defining stats for game flow
default clarity_stat = 0
default obscurity_stat = 0

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

label splashscreen:
    play music "intro.mp3" volume 2
    scene black
    with Pause(0.5)

    show text "{size=+20} Team Murray" with dissolve
    with Pause(3)

    hide text with dissolve
    with Pause(1)

    scene black
    with Pause(0)

    show text "{size=+20}Presents..." with dissolve
    with Pause(2.5)

    hide text with dissolve
    with Pause(0.25)

    scene black
    with Pause(0)

    show text "{size=+30}Finding Myself" with dissolve
    with Pause(7)

    hide text with dissolve
    with Pause(3)
    return
#The game starts here
label start:
#Chapter 1: Finding Myself

    play music "dearalice.mp3" volume 1 loop
    centered """
    {size=+10}Life was so dark back then...

	{size=+10}Then, one day... I lost him.

	{size=+10}My dreams, my moments with him...

	{size=+10}all taken away from me.

	{size=+10}He showed me colors of this world

	{size=+10}Vibrant and alive

	{size=+10}But those colors... they faded.

	{size=+10}Now I'm back to this bland world, all black and white.

	{size=+10}The waves swept him away with all the colors

	{size=+10}to a place I can't reach.

	{size=+10}Now that he's gone...

	{size=+10}will I ever be able to...

	{size=+20}{color=#f00}Find Myself
    """
    play music "classroomnoise.mp3" volume 1.5 loop
    scene classroomevening2

    t """
    Alright, class, listen up! For homework tonight, you'll have to read Chapters 5 and 6 of your history textbook.

    You will also need to complete the worksheet on the American Revolution that I handed out earlier.

    That's all. Have a good evening!
    """

    "The students immediately begin packing up their things, eager to leave."
    scene classroomevening
    kt "Ugh, more homework. I swear, this teacher never lets us have a break."
    j "Can't even play League with you guys after dismissal ;;"
    e "I know right! What if we ditch that assignment. What's your midterm grade again Kurt?"
    kt "Uhm, 85"
    e "How about you Jerub?"
    j "90"
    e "Damn son! We all got passing grades for midterms anyway, so I'm thinking... what if we don't do the homework?"
    j "Are you crazy?"
    kt "I mean. He's got a point. I'm in."
    e "What about you Jerub?"
    j "But the homework."
    e "C'mon we're only going to do this once. Let's go! Let's play, how are we gonna rank up without you?"
    kt "Yeah, we rack up wins when you're in the team! We'll get in Diamond rank in no time!"
    j "Sure but...(it'll be hard for me to carry them ;; and it's not gonna be worth it if we lose again.)"
    j "(Oh yeah there's Kuro! Game's gonna be so much easier when he's on our team)"
    j "Oiiiiiiiiiii! Kuro! You coming with us right?"
    "I looked at Jerub with a tired face"

    scene classroomevening3
    j "So are you coming?"

    menu:
        "Uuuuuuh yeah sure":
            jump go_with_them

        "No":
            jump dont_go_with_them


label go_with_them:
    k "Sure I want to go with you guys but isn't it a bit late for that?"
    e "A bit late?"
    e "What are you talking about? It's still 5:00 pm bro"
    j "Now that you mention it isn't Kurt's mom gonna call him again if he plays with us this late?"
    kt "Uhm...no"
    j "Remember the last time your mom picked you up while we're playing back then?"
    kt "Let's...not talk about that."
    e "Hey c'mon Jerub give Kurt a break."
    e "Surely this time his mom won't come and pick him up. Right Kurt?"
    kt "Yeah"
    j "I don't know about that one bro. What if his mom picks him up again?"
    e "Let's just hope his mom doesn't come xD."
    j "Are you guys sure about this?"
    kt "Yeah, I just want to play with you guys."
    j "... fine then."
    k "On second thought...I'm not coming with you guys"
    kt "Eeeeh? Why?"
    k "As I said it's already late. Also..."
    jump dont_go_with_them

label dont_go_with_them:
    k "... I gotta go somewhere."
    e "Where?"
    k "..."

    j "C'mon man at least one game ;;..."
    k "I really can't man I'm just too tired and we still got that requirement to do ..."
    e "Why? Don't you want to play with us?"
    kt "I'll buy you the new Irelia skin hehe ^^."
    k "I really can't today. Maybe next time."
    e "I see."
    kt "Looks like he doesn't want the new Irelia skin I suppose."
    "Kuro leaves the room"
    e "He's been like that ever since he lost his friend."
    kt "What was his name again?"
    j "Shiro"
    kt "Oh yeah! I remember him hanging out with Kuro multiple times back then."
    e "I never knew they were that close."
    j "They were, similar, in many ways but at the same time they're quite the opposite of each other."
    kt "You hanged out with them back then?"
    j "Not really but ... I was there when Shiro died." ##make the dialogue smoother or smth
    e "Damn."
    kt "Sorry for asking."
    j "It's fine."
    j "Let's just hope Kuro's okay."
    kt "Yeah."
    e "Yeah."


### Insert transtion scene or smth idk...
    scene beach:
        fit "fill"
        xysize (1920, 1080)
    play music "beachaudio.mp3" volume 0.1 loop
    "At the shore"
    "Kuro's footsteps left imprints in the wet sand as he walked along the shoreline, the gentle lapping of the waves a somber accompaniment to his thoughts. "
    "He gazed out at the vast expanse of the ocean, a sense of emptiness gnawing at his heart."
    k "Remembering the first time I walked with you along these shores, I was unsure of everything."
    k "We've come so far since then, from me being a loner to...to this. To us, here in this world, of dreams and possibilities."
    k "But ever since I lost you, everything feels...different."
    k "You were my silent companion, my confidante. And now, without you, I feel... lost"
    k "I wish you were here. To share this moment with me, to remind me that even in the darkest of times, there is still light."
    k "*sigh*"
    k "It's getting dark already."
    k "Gotta check out my phone and look what the boys are up to"

    e_nvl "Hey. Jerub where you at we're already here at the shop!"
    kt_nvl "We can't start without you bro."
    j_nvl "Can you guys just wait I'm still cleaning!"
    e_nvl "Aren't you guys taking long cleaning?"
    j_nvl "Look cleaning is easy. Not when Ma'am Heather's our adviser. She literally wants everything to be nice and tidy"
    e_nvl "Oh...yeah. My bad."
    kt_nvl "Yeah that's true."
    j_nvl "Just finished sweeping actually guess I can go now."
    e_nvl "Hell yeah!"

    k "What is that bright light?"
    "Kuro see's the bright light"

    scene beachbrightlight:
        fit "fill"
        xysize (1920, 1080)

    "It's Isekai Time"

    scene otherworld:
        fit "fill"
        xysize (1920, 1080)

    k "Where am I?"
    k "Let me pull up my phone real quick."

    e_nvl "asdlkfja;lsdf'kasdf;"
    kt_nvl "akdslfjaslkdfj;as;df"
    j_nvl "asfkjsdkflajadsflksdf"

    k "Wala imong signal whaaat?"


    "Kuro walks..."


    #Chapter 2: Treehouse
    scene treehouse:
        fit "fill"
        xysize (1920, 1080)
    k "Shiro, look! It's our treehouse from when we were kids."
    s "I can't believe it's still here. This place holds so many memories."
    k "Let's go inside, Shiro. I want to see if everything is just as we left it."
    s "Yeah, let's relive some of our old adventures!"
    "While exploring the treehouse, You pick up notebook filled with memories."
    k "Look, Shiro, it's our old notebook. We used to write stories in this."
    s "I remember! We had so many big dreams back then."
    s "Remember how we used to read books and write stories together? Those were good times"
    "As you flip through the notebook, you see ideas you had written together."
    menu:
        "Yeah!":
            $ clarity_stat +=1
            jump treehouse_menu_1
        "My writing was ... bad.":
            $ obscurity_stat +=1
            jump treehouse_menu_2

    label treehouse_menu_1:
        k "I enjoyed writing with you! Even though my writing style was so cringy sksksksk."
        s "I enjoyed writing with you too! Your writing style ain't that bad yknow."
        k "But not as good as you."
        s "To be fair. I got into writing earlier than you."
        k "You're writing style is literally as good as a publishable book what do you mean?"
        s "Woah. I think you're overpraising me."
        k "No but really! You're literally a genius."
        s "Well...I don't even know what to say i'm just flattered."


    label treehouse_menu_2:
        s "What are you talking about your writing was good!"
        k "Just looking at how I wrote makes me cringe."
        s "C'mon Kuro don't say that. I think they're great!"
        k "But they're so bad."
        s "Have some confidence will ya?"
        menu:
            "...":
                jump treehouse_menu_2a
            "But":
                jump treehouse_menu_2a
    label treehouse_menu_2a:
        s "No buts! No silence from you!"
        s "What matters is that you wrote them and that you tried!"
        s "Remember, writing is a process. You'll improve over time."
        k "I guess you're right. Thanks, Shiro."
        s "Of course! And I believe in you, Kuro. Your stories are unique and have potential."
        k "Do you really think so?"
        s "Absolutely! Your writing has a certain charm that draws people in."
        s "With a little polishing, they'll be amazing!"
        k "I'll take your word for it. Thanks, Shiro. I feel a lot better now."
        s "That's the spirit! Now, let's get back to our adventure!"
    jump secret_hideout




label abandoned_library:
    scene abandonedlibrary1
    "The Abandoned Library"
    scene abandonedlibrary

label secret_hideout:
    "The Secret Hideout"

label starry_night:
    scene stargazing
    "The Starry Night"

label beach:
    scene beach1
    "The Beach"


label game_end:

    return

    






