###image sizes are 990x1100
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

    show text "{size=+20} Team Murray"
    with Pause(3)

    hide text
    with Pause(2)

    scene black
    with Pause(0)

    show text "{size=+20}Presents..."
    with Pause(4)

    hide text
    with Pause(0.25)

    scene black
    with Pause(0)

    show text "{size=+30}Finding Myself"
    with Pause(7)

    hide text
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

    stop music

    play sound "schoolbell.mp3" volume 0.2

    scene classroomevening2
    t """
    Alright, class, listen up! For homework tonight, you'll have to read Chapters 5 and 6 of your history textbook.

    You will also need to complete the worksheet on the American Revolution that I handed out earlier.

    That's all. Have a good evening!
    """

    play sound "classroomnoise.mp3" volume 0.1 loop
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

    stop sound


### Insert transtion scene or smth idk...
    scene beachevening
    play sound "beachsound.mp3" volume 0.07 loop
    play music "冬の訪れ.mp3" volume 0.5 loop
    "At the shore"
    "My footsteps left imprints in the wet sand as I walk along the shoreline, the gentle lapping of the waves a somber accompaniment to my thoughts. "
    "I gazed out at the vast expanse of the ocean, a sense of emptiness gnawing at my chest."

    k "Remembering the first time I walked with you along these shores, I was unsure of everything."
    k "We've come so far since then, from me being a loner to... to this. To us, here in this world, of dreams and possibilities."
    k "But ever since I lost you, everything feels... different."
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

    play sound "beachsound.mp3" volume 0.07 loop
    k "I wonder if they really want me to play with them or if they just want to rank up faster... sigh, I wish I could just write like before."
    k "It's strange. I used to love playing with them, but now... everything feels different. Maybe I'm just not the same person I was before."
    k "We used to have so much fun together, but now it feels like I'm just going through the motions. Maybe it's because you're not here, Shiro. Without you, everything feels hollow."
    k "I miss our late-night gaming sessions, where we'd laugh and joke around for hours. It's not the same without you."
    k "Do they even realize I'm not the same anymore? That I'm struggling to find my place without you by my side?"
    k "I wish I could tell them how I feel, but... I don't even know how to put it into words. Everything feels so complicated now."
    k "I just want things to go back to how they were before, when life was simpler and we were together. But I know that's impossible now."
    k "Maybe I should just go back and join them. It might not be the same, but at least I won't be alone."

    "{color=#f00}Kuro hesitates, torn between his memories of the past and the uncertainty of the present."
    "A distant, bright light catches my attention, shimmering over the ocean like a beacon in the night."

    k "What is that bright light?"

    #Kuro sees the bright light
    "Could this be a sign? A sign that there is still hope, that there is still a chance for him to find himself and his place in this world?"
    init:
        define flash = Fade(.25, 0.0, .75, color="#000")
    stop music

    scene beachbrightlight:
        fit "fill"
        xysize (1920, 1080)
    with flash

    "It's Isekai Time"
    play music "寂しいジングル.mp3" volume 0.5 loop
    k "Where am I?"
    k "This place... it's familiar, yet different. It's like a dream."
    k "Where am I?"
    k "What happened? Why is everything black and white?!"

    play sound "phonevibrate.mp3"

    "Kuro tries to pull up his phone."

    e_nvl "..."
    kt_nvl "..."
    j_nvl "..."
    play sound "beachsound.mp3" volume 0.07 loop
    k "That's strange. My phone was working just a moment ago."
    k "Maybe there's no signal. What the hell just happened?"
    "Kuro looks around, taking in his surroundings. The world seems to shimmer with an otherworldly light, casting everything in a surreal glow."
    k "This place... it's beautiful, in a haunting sort of way. It's like something out of a fairy tale."
    k "I wonder if I'm dreaming. Or maybe I've gone completely mad."
    k "But if this is a dream, it feels so real. The sand beneath my feet, the gentle breeze, the distant sound of waves... it's all so vivid."
    "As Kuro walks along the shore, he notices something glimmering in the sand. He bends down and picks it up, revealing a small, intricately carved shell."
    ##Insert pick-up sound
    k "This shell... it's like something out of a story. It's beautiful."
    "Kuro gazes out at the ocean, watching as the waves crash against the shore. There's a sense of peace here, a tranquility he hasn't felt in a long time."
    k "I don't know where I am or how I got here, but... for now, I think I'll just enjoy the moment."

    show shirolaugh with dissolve
    "Suddenly, Shiro appears before Kuro, looking as confused as ever."

    play music "静かな夜長に.mp3" volume 0.5 loop

    s "How's it going!"
    k "!!!!!"
    k "Shiro, y--you're here?!"

    show shiroangry1 with dissolve
    hide shirolaugh with None

    s "What do you mean? I've been here with you all along!"
    k "I don't understand. I thought... I thought you were..."

    show shironeutral with dissolve
    hide shiroangry1 with None

    s "I thought I was?"
    k "..."
    k "..."
    k "(Dead...................)"

    show shirosmile1 with dissolve
    hide shironeutral with None

    s "Aaah I get it. Snap out of it! You're daydreaming again!"
    k "Sorry..."
    k "(Am I daydreaming again?)"
    show shirosmile3 with dissolve
    hide shirosmile1 with None

    s "You always daydream especially when we're at school. This is the first time I saw you daydreaming here."
    k "Never mind. It's not important. Let's ..."
    k "(I... I don't know. This place feels so real, yet...)"
    k "(He's here...right in front of me.)"

    show shirolaugh with dissolve
    hide shirosmile3 with None

    s "Going back to our old hangout places when we were kids! Seems like a great idea! It's been so long since we last went to those places!"
    k "Oh sure..."
    k "(Whatever is going on here. I'm just glad he's here;;;)"

    show shironeutral with dissolve
    hide shiroluagh with None

    s "What's wrong Kuro? Are you not feeling well?"
    k "Uuuuuh. Nothing"

    show shirosmile2 with dissolve
    hide shironeutral with None

    s "Kuro, tell me the truth."

    menu:
        "Yeah":
            $ clarity_stat +=1
            jump shore_yeah

        "It's just ... been a while since I saw you.":
            $ clarity_stat +=1
            jump been_a_while

        "But you're not supposed to be here...":
            $ obscurity_stat +=1
            jump silence

    label shore_yeah:
        k "Yeah, I'm sure. Let's keep going."
        show shironeutral with dissolve
        s "I thought you're sick or something. But are you REALLY sure you're okay?"
        k "Yeah I just miss this."
        jump been_a_while

    label been_a_while:
        show shiroangry1 with dissolve
        s "What are you saying my guy? We've been hanging out a lot."
        k "Oh, I. Forgot."

        show shirosmile1 with dissolve
        hide shiroangry with None
        s "You're so funny Kuro."
        jump shore_end

    label silence:
        show shirosurprised with dissolve
        s "???"
        s "Oh we really need to go somewhere else and rest, you look so pale."
        k "..."
        show shirosmile2 with dissolve
        hide shirosurprised with None
        s "Let's go!"
        jump treehouse

    label shore_end:
        show shirosmile3 with dissolve
        hide shirosmile2 with None

        s "Alright, let's get back to the old treehouse for a bit and rest then, okay?"
        k "Okay."

        stop sound
        stop music
        jump treehouse


#Chapter 2: Treehouse
label treehouse:
    scene treehouse:
        fit "fill"
        xysize (1920, 1080)

    play music "beautifuldreamer.mp3" volume 0.5 loop

    k "Shiro, look! It's our childhood treehouse!"
    show shirosurprised with dissolve

    s "I can't believe it's still here. This place holds so many memories."
    k "Let's go inside, Shiro. I want to see if everything is just as we left it."

    show shirosmile2 with dissolve
    hide shirosurprised with None

    s "Yeah, let's relive some of our old adventures!"
    "While exploring the treehouse, You pick up a notebook filled with memories."
    k "Hey Shiro, it's our old notebook. We used to write stories in this."

    show shirosurprised with dissolve
    hide shirosmile2 with None

    s "I remember! We had lots of big dreams back then."

    show shirosmirk with dissolve
    hide shirosurprised with None

    s "Remember how we used to read and write stories together?"
    "As you flip through the notebook, you see some ideas you had written with Shiro."
    play sound "pageflip.mp3"

    hide shirosmirk with None
    show canvasofdreams ##resize book

    k "(It's ... been a while huh)"
    menu:
        "Those were the best times.":
            $ clarity_stat +=1
            jump treehouse_menu_1

        "My writing was ... bad.":
            $ obscurity_stat +=1
            jump treehouse_menu_2

    label treehouse_menu_1:
        k "I enjoyed writing with you! Even though my writing style was so cringy sksksksk."
        hide canvasofdreams with None
        play sound "bookclose.mp3"
        show shirolaugh with dissolve

        s "I enjoyed it, too! Your style ain't that bad y'know."
        k "But not as good as yours."

        show shirosmile3 with dissolve
        hide shiroluagh with None

        s "To be fair, I got into writing earlier than you."
        k "Your style literally reads like a published book!"

        show shirosurprised with dissolve
        hide shirosmile3 with None

        s "Woah. I think you're overpraising me."
        k "No, really! You're a genius."

        show shirosmile3 with dissolve
        hide shirosurprised with None

        s "Well... I don't even know what to say. I'm just flattered."

        show shirosmile2 with dissolve
        hide shirosmile3 with None

        s "I think we both have our strengths when it comes to writing."
        k "Yeah, I guess so. It's just hard not to compare sometimes."
        show shirosmile1 with dissolve
        hide shirosmile2 with None

        s "It's natural. Just remember that we all have our own unique voice."
        s "That's what makes writing so special."
        k "You're right. Thanks for the reminder, Shiro."
        show shirolaugh with dissolve
        hide shirosmile1 with None

        s "Anytime, Kuro. Now, let's keep exploring our imaginations!"
        stop music
        if obscurity_stat < clarity_stat:
            jump abandoned_library
        if clarity_stat < obscurity_stat:
            jump secret_hideout
        else:
            jump abandoned_library


    label treehouse_menu_2:
        hide canvasofdreams with None
        play sound "bookclose.mp3"
        show shiroangry1 with dissolve

        s "What are you talking about? Your writing was good!"
        k "Just looking at my old writing makes me cringe."
        show shiroangry2 with dissolve
        hide sihroangry1 with None

        s "C'mon Kuro, don't say that. I think its great!"
        k "But its so bad..."
        s "Have some confidence will ya?"
        menu:
            "...":
                $ obscurity_stat +=1
                jump treehouse_menu_2a
            "But":
                $ obscurity_stat +=1
                jump treehouse_menu_2a
            "Okay":
                $ clarity_stat +=1
                jump treehouse_menu_2b

    label treehouse_menu_2a:
        show shiroangry2 with dissolve

        s "No buts! No silence from you!"
        s "What matters is that you wrote them and that you tried!"
        show shiroangry1 with dissolve
        hide shiroangry with None

        k "..."
        s "Cmon now don't be sad. Don't put yourself down like that."
        k "Okay then..."
        show shirosad with dissolve
        hide shiroangry with None

    jump treehouse_menu_2b

    label treehouse_menu_2b:
        s "Remember, writing is a process. You'll improve over time."
        k "I guess you're right. Thanks, Shiro."
        show shirosmile1 with dissolve
        hide shiroangry1 with None

        s "Of course! And I believe in you, Kuro. Your stories are unique and have potential."
        k "Do you really think so?"
        show shirosmile2 with dissolve
        hide shirosmile1 with None

        s "Absolutely! They have a certain charm that draw people in."
        show shirosmile3 with dissolve
        hide shirosmile2 with None

        s "With a little polishing, they'll be amazing!"
        k "I'll take your word for it. Thanks, Shiro. I feel a lot better now."
        show shirolaugh with dissolve
        hide shirosmile3 with None

        s "That's the spirit! Now, let's get back to visiting our hangout places!"

        stop music


        if obscurity_stat < clarity_stat:
            jump abandoned_library
        if clarity_stat < obscurity_stat:
            jump secret_hideout
        else:
            jump abandoned_library


#Chapter 3a: Abandoned Library
label abandoned_library:
    scene abandonedlibrary:
        fit "fill"
        xysize (1920, 1080)
    play music "初夏の風を感じて.mp3" volume 0.4 loop
    "The Abandoned Library"
    show shirosurprised with dissolve
    s "Oh wow the library didn't change that much. I guess people really are scared of it."
    k "No wonder it's abandoned."

    play sound "booksdrop.mp3"

    k "What was that?"
    show shirosad with dissolve
    hide shirosurprised with None

    s "Ghosts aren't rrr-real right?"
    k "Uuuuh, I don't know. I'm not sure."
    k "... What if ... they are?!"
    s "Hey don't scare me like that!"
    k "I'm not."
    s "Then what was that?!!!"
    k "*smiles*"
    show shiroangry2 with dissolve
    hide shirosad with None

    s "Ugh, I can't believe you've done this."
    k "Hehe"
    s "How did you do that? Are you secretly a wizard or something?"
    k "Huh, I didn't do anything"
    play sound "ratsqueek.mp3"

    k "It's just a fat rat."
    k "Look"

    show shirosad with dissolve
    hide shiroangry2 with None
    s "Eeeek!"
    s "Oh okay, I almost had a heart attack. Don't you ever do that again Kuro."
    k "What? Really, I didn't do anything."
    s "I feel like my lifespan decreased because of that."
    show shirosmirk with dissolve
    hide shirosad with None

    s "Anyway. Now that the rat is gone."
    show shirosurprised with dissolve
    hide shirosmirk with None

    s "It's funny how there's this nearby abandoned library, and yet we decided to make our treehouse look like a library."
    k "*laughs* Yeah, I guess we were really into books back then."
    k "I'm sorry for laughing. It's just... nostalgic, you know?"
    show shirosmile1 with dissolve
    hide shirosurprised with None

    s "No need to apologize. I feel the same way. Those were good times."
    show shirosmile3 with dissolve
    hide shirosmile1 with None

    s "Want to read a book while we're here?"
    k "Sure!"
    show shirosmile2 with dissolve
    hide shirosmile3 with None

    s "What book do you want to read?"

    menu:
        "No Longer Human":
            $ clarity_stat +=1
            jump no_longer_human_library
        "The Little Prince":
            $ obscurity_stat +=1
            jump the_little_prince_library

    label no_longer_human_library:
        play sound "pageflip.mp3"
        show nolongerhuman
        "..."
        k "Shiro, I've been thinking."
        show shironeutral with dissolve
        hide nolongerhuman with None
        play sound "bookclose.mp3"

        s "About what?"
        k "Our dream... of becoming writers."
        s "Yeah, what about it?"
        k "I don't think it's for me."
        show shiroangry1 with dissolve
        hide shironeutral with None

        s "What do you mean? You love writing."
        k "I did, but now... I don't know. It just doesn't feel right anymore."
        show shironeutral with dissolve
        hide shiroangry1 with None

        s "I see. Well, it's okay to change your mind, Kuro. Maybe you'll find something else that sparks your passion."
        k "Yeah, maybe. Thanks, Shiro."
        show shirosmile2 with dissolve
        hide shironeutral with None
        s "Of course, Kuro. I'll support you no matter what you decide."

        s "So, what do you say we do next?"
        show shirosmile3 with dissolve
        hide shirosmile2 with None

        k "Hmm. I'm not sure what to do next."

        s "You know, revisiting our old hangout spots might inspire us for you. What do you think?"
        show shirolaugh with dissolve
        hide shirosmile3 with None

        k "Up to you."

        s "Okay then. Let's go!"

        if obscurity_stat < clarity_stat:
            jump starry_night
        if clarity_stat < obscurity_stat:
            jump beach
        else:
            jump starry_night

    label the_little_prince_library:
        play sound "pageflip.mp3"
        show thelittleprince
        "..."
        k "Shiro, I've realized something."
        show shirosmile2 with dissolve
        hide thelittleprince with None
        play sound "bookclose.mp3"

        s "What is it?"
        k "Our dream... of becoming writers one day."
        show shirolaugh with dissolve
        hide shirosmile2 with None

        s "Ah, yes. I remember that dream. We used to spend hours talking about the stories we would write."
        k "Exactly. And now, I want to make that dream a reality. I want to become a writer."
        show shirosurprised with dissolve
        hide shirolaugh with None
        s "That's amazing, Kuro! I believe you can do it. Your stories have always had a special magic to them."
        k "Thank you, Shiro. Your support means everything to me."
        show shirosmile2 with dissolve
        hide shirosurprised with None

        s "So, what do you say we do next?"
        show shirosmile3 with dissolve
        hide shirosmile2 with None

        k "Hmm. I'm not sure what to do next."

        s "You know, revisiting our old hangout spots might inspire us for your stories. What do you think?"
        show shirolaugh with dissolve
        hide shirosmile3 with None

        k "Sure."

        s "Okay then. Let's go!"
        stop music
        if obscurity_stat < clarity_stat:
            jump starry_night
        if clarity_stat < obscurity_stat:
            jump beach
        else:
            jump starry_night

#Chapter 3b: Secret Hideout
label secret_hideout:
    scene secrethideoutexterior:
        fit "fill"
        xysize (1920, 1080)
    play music "初夏の風を感じて.mp3" volume 0.5 loop
    "The Secret Hideout"
    show shirolaugh with dissolve
    s "Ah, it feels good to be back here."
    k "Yeah, being here makes me feel at peace."
    show shirosmile2 with dissolve
    hide shirolaugh with None

    s "Let's enjoy our time here now."
    show shirosmile1 with dissolve
    hide shirosmile2 with None

    s "Hey, do you remember the time we found that old treasure map?"
    k "Oh yeah, and we spent the whole summer searching for the treasure."
    show shirosmile3 with dissolve
    hide shirosmile1 with None

    s "We never did find it, did we?"
    k "No, but we had a lot of fun trying."

    k "*sigh* a lot has happened huh..."
    show shirosmile1 with dissolve
    hide shirosmile3 with None
    s "Yeah."

    k "Shiro, being here... it just reminds me of how much I miss our old life."
    show shironeutral with dissolve
    hide shirosmile1 with None

    s "I know what you mean, Kuro. School must've been hard for you huh."
    k "Yeah and ... life recently It's not the same, though. Everything feels... empty without the life we used to have."
    show shiroangry1 with dissolve
    hide shironeutral with None

    s "I understand, Kuro. It's a big change, but we can still all we can do is move forward."


    k "Sometimes I wonder if things would have been different if I didn't."
    s "I don't know what you're going through. But maybe, but we can't change the past. We can only cherish the moments we have now."
    k "I just... I just wish things were different. Maybe then, I wouldn't feel so lost."
    s "Kuro, we can't dwell on what we've lost. We have to focus on the present and the future."
    k "I know, but it's hard not to think about it. I miss our old life so much, Shiro."
    s "I miss it too, Kuro. But we're here now, together. And we can make new memories, even if it's not the same as before."
    show shirosmirk with dissolve
    hide shiroangry1 with None

    s "Try reading a book! Maybe it'll help you!"
    k "Okay;;"
    show shirosmile2 with dissolve
    hide shirosmirk with None

    s "What book do you want to read?"

    label choose_book_hideout:
        menu:
            "No Longer Human":
                $ clarity_stat +=1
                jump no_longer_human_hideout
            "The Little Prince":
                $ obscurity_stat +=1
                jump the_little_prince_hideout

    label no_longer_human_hideout:
        show shiroangry1 with dissolve
        s "Are you sure about that? I wouldn't recommend that book to you right now. "
        menu:
            "Yes":
                jump no_longer_human_hideout_continue
            "Oh...give me the other book then":
                jump the_little_prince_hideout

    label no_longer_human_hideout_continue:
        show shirosad with dissolve
        s "Okay. If you say so"
        show nolongerhuman
        play sound "pageflip.mp3"
        hide shirosad with None

        "..."
        k "Shiro, I've been thinking."
        show shirosmile1 with dissolve
        hide nolongerhuman with None
        play sound "bookclose.mp3"

        s "About what?"
        k "Our dream... of becoming writers."
        show shirosurprised with dissolve
        hide shirosmile1 with None

        s "Yeah, what about it?!!"
        k "I don't think it's for me."
        show shiroangry2 with dissolve
        hide shirosurprised with None

        s "What do you mean? You love writing!"
        k "I did, but now... I don't know. It just doesn't feel right anymore."
        show shirosad with dissolve
        hide shiroangry2 with None

        s "I see. Well, it's okay to change your mind, Kuro. Maybe you'll find something else that sparks your passion."
        k "Yeah, maybe. Thanks, Shiro."
        s "Of course, Kuro. I'll support you no matter what you decide."
        s "I'll...head back to the beach get some fresh air..."
        k "I'll go with you"
        s "..."

        if obscurity_stat < clarity_stat:
            jump starry_night
        if clarity_stat < obscurity_stat:
            jump beach
        else:
            jump starry_night

    label the_little_prince_hideout:
        show shirolaugh with dissolve
        s "The Little Prince coming right up!"
        show thelittleprince
        play sound "pageflip.mp3"
        "..."
        k "Shiro, I've realized something."
        hide thelittleprince with None
        play sound "bookclose.mp3"

        s "What is it?"
        k "Our dream... of becoming writers one day."
        s "Ah, yes. I remember that dream. We used to spend hours talking about the stories we would write."
        k "Exactly. And now, I want to make that dream a reality. I want to become a writer."
        s "That's amazing, Kuro! I believe you can do it. Your stories have always had a special magic to them."
        k "Thank you, Shiro. Your support means everything to me."
        stop music
        if obscurity_stat < clarity_stat:
            jump starry_night
        if clarity_stat < obscurity_stat:
            jump beach
        else:
            jump starry_night



#Chapter 4: Starry Night - Good Ending
label starry_night:
    scene beach1:
        fit "fill"
        xysize (1920, 1080)
    with fade

    play sound "night.mp3" volume 0.1 loop
    play music "poemoftheclouds.mp3" volume 0.4 loop

    "The Starry Night"
    k "Shiro, it's a beautiful night, isn't it?"
    show shirosmile2
    s "It really is, Kuro. The stars are so bright, and the sound of the crickets are so calming."
    k "It's moments like these that make me appreciate life, you know? Just being here with you, it feels like everything is right in the world."
    s "I feel the same way, Kuro. It's like all the worries and troubles just fade away."
    k "I wish we could stay like this forever, just enjoying each other's company."
    s "Me too, Kuro. But we have to cherish these moments, even if they're fleeting."
    k "You're right, Shiro. We should make the most of every moment we have together."
    s "Absolutely. Let's enjoy the peace and tranquility of this night."
    k "Hey, do you remember that time we got lost in the woods and had to find our way back using the stars?"
    s "Of course I do! It was a fun adventure, even though we were scared at first."
    k "Yeah, but we made it back safely, thanks to your sense of direction."
    s "And your ability to stay calm under pressure. We make a great team, don't we?"
    k "The best team. I'm grateful to have you as my friend, Shiro."
    s "I feel the same way, Kuro. You've always been there for me, through thick and thin."
    k "And I always will be. No matter what happens, you can count on me."
    s "I know, Kuro. And you can count on me too. We'll always have each other's backs."
    k"..."
    k"..."
    s "What is it, Kuro? You seem troubled."
    k "Shiro... there's something I've been meaning to tell you. It's... it's not easy, but I think you deserve to know."
    stop music

    play music "depression.mp3" volume 0.5 loop
    show shirosmile1 with dissolve
    hide shirosmile2 with None

    k "It's about this world we're in... It's beautiful and peaceful, but... sometimes I wonder if it's all real."
    s "What do you mean, Kuro?"
    k "I don't know... It's just a feeling I get sometimes, like there's something missing, something not quite right."

    show shironeutral with dissolve
    hide shirosmile1 with None

    s "You're overthinking things, Kuro. This world is as real as we make it. It's our sanctuary, our escape from the harshness of reality."
    k "I know, Shiro, but... What if this world is just an illusion? What if we're not really here?"
    s "Kuro, you're letting your imagination run wild. This world is as real as our dreams and our memories. It's a part of us."
    k "In the real world... you're not there anymore. You... you drowned, Shiro."

    show shiroangry1 with dissolve
    hide shironeutral with None

    s "..."
    k "I've been living in this illusion, this world we created together, because I can't bear to face the reality without you. I've been running away from the pain, pretending that everything is fine here."
    s "Kuro, I understand. It's not easy to lose someone you care about."
    k "But it's not fair to you, Shiro. You deserve to be remembered and honored in the real world, not trapped in this fantasy with me."
    s "Kuro, it's okay. I don't want you to blame yourself. We created this world together, as a place of comfort and solace. But it's time for you to let go and face the real world."
    k "I can't, Shiro. I can't face a world without you in it. Everything feels so empty and meaningless without you by my side."
    s "You're stronger than you think, Kuro. You have the strength to face whatever comes your way, even if it's difficult and painful."
    k "I... I don't want to say goodbye, Shiro. I don't want to lose you again."
    stop music

    show shirosmile1 with dissolve
    hide shiroangry1 with None
    play music "moon.mp3" volume 0.5 loop

    s "You're not losing me, Kuro. I'll always be a part of you, no matter where you go. Our memories, our dreams, they'll always be with you."
    k "I'll miss you, Shiro. I'll miss this world we created together."
    s "I'll miss you too, Kuro. But it's time for you to wake up and face the real world. I'll be waiting for you there, in your heart."
    k "Goodbye, Shiro. I'll never forget you."

    show shirosmile2 with dissolve
    hide shirosmile1 with None

    s "Goodbye, Kuro. Keep our dreams alive."

    show shirolaugh with dissolve
    hide shirosmile2 with None

    s "Also!"
    k "Yes?"

    show shirosmile3 with dissolve
    hide shirolaugh with None

    s "All along I knew this world was just an illusion!"
    k "Wait you knew?!"
    show shirolaugh with dissolve
    hide shirosmile3 with None
    s "Yes!!!"
    k "What if I fail? What if it's not going to be okay?"
    s "Kuro, you're stronger than you think. Even if things don't go as planned, even if you face challenges and obstacles, remember that I believe in you. Our dream is not just about success, it's about resilience, about never giving up no matter what."
    k "But what if I can't do it without you, Shiro? What if I'm not strong enough?"
    s "You are, Kuro. You've always been strong, even when you didn't realize it. And you're not alone. You have friends who care about you, who will support you every step of the way."
    k "Thank you, Shiro. I'll do my best to keep our dream alive, to honor your memory."
    s "I know you will, Kuro. And I'll always be watching over you, cheering you on from wherever I am. Our dream is yours now. Make it shine brighter than ever before."
    k "I will, Shiro. I promise."
    stop music
    stop sound

    jump good_game_end

#Chapter 4: Beach - Bad Ending
label beach:
    scene beach2:
        fit "fill"
        xysize (1920, 1080)
    with dissolve
    play sound "beachsound.mp3" volume 0.07 loop
    play music "poemoftheclouds.mp3" volume 0.5 loop
    "The Beach"
    s "sigh This place never fails to calm me down. Even though the clouds are dark. It's nice."
    show shirosmile1 with dissolve

    k "Yeah, it's like our own little slice of paradise."
    s "I'm glad we found this spot. It's nice to get away from everything for a while."
    show shirolaugh with dissolve
    hide shirosmile1 with None

    k "Definitely. It's important to take a break and just enjoy the moment."
    k "Also, I'm sorry for a while ago."
    s "What? It's fine! You're so stressed out so it's understandable!"
    show shiroangry2 with dissolve
    hide shirolaugh with None

    k "Oh...okay then."
    k "Man I wish we could stay here forever, just walking along the beach, watching the waves."

    show shirosmile2 with dissolve
    hide shiroangry2 with None

    s "Me too, Kuro. It's so peaceful here, just the sound of the ocean and the feel of the sand under our feet."
    k "Yeah, it's perfect. Sometimes I wish we could just escape from everything and live here, just the two of us."

    show shirosurprised with dissolve
    hide shirosmile2 with None

    s "That would be nice, wouldn't it? No worries, no responsibilities, just us and the beach."
    k "Exactly. We could build a little hut, fish for our food, live off the land. It would be a simple life, but a happy one."

    show shirolaugh with dissolve
    hide shirosurprised with None

    s "It sounds like a dream come true. Maybe one day we can make it happen, find our own little piece of paradise."
    k "I hope so, Shiro. I hope we can always find a way to be together, no matter what life throws at us."

    show shirosmile2 with dissolve
    hide shirosurprised with None

    s "We will, Kuro. We'll always find a way. As long as we have each other, we can face anything."
    k "Thanks, Shiro. I don't know what I'd do without you."

    show shirosmile1 with dissolve
    hide shirosmile2 with None

    s "You'll never have to find out, Kuro. I'll always be here for you, no matter what."
    k "I'm grateful for that, Shiro. Let's make the most of our time here, okay?"

    show shirosmile2 with dissolve
    hide shirosmile1 with None

    s "Absolutely. Let's enjoy every moment, together."
    k "Shiro... there's something I've been meaning to tell you. It's... it's not easy, but I think you deserve to know."

    show shirosmile1 with dissolve
    hide shirosmile2 with None

    play music "depression.mp3" volume 0.75 loop

    s "What is it, Kuro? You seem troubled."
    k "It's about this world we're in... It's beautiful and peaceful, but... sometimes I wonder if it's all real."

    show shironeutral with dissolve
    hide shirosmile1 with None

    s "What do you mean, Kuro?"
    k "I don't know... It's just a feeling I get sometimes, like there's something missing, something not quite right."

    show shiroangry1 with dissolve
    hide shironeutral with None

    s "You're overthinking things, Kuro. This world is as real as we make it. It's our sanctuary, our escape from the harshness of reality."
    k "I know, Shiro, but... What if this world is just an illusion? What if we're not really here?"
    s "Kuro, you're letting your imagination run wild. This world is as real as our dreams and our memories. It's a part of us."
    stop music

    play music "brokenpiano.mp3" loop volume 0.75 fadein 1.0

    k "In the real world... you're not there anymore. You... you died, Shiro."

    show shironeutral with dissolve
    hide shiroangry1 with None

    s "..."
    k "I've been living in this illusion, this world we created together, because I can't bear to face the reality without you. I've been running away from the pain, pretending that everything is fine here."
    s "Kuro, I understand. It's not easy to lose someone you care about."
    k "But it's not fair to you, Shiro. You deserve to be remembered and honored in the real world, not trapped in this fantasy with me."
    s "Kuro, it's okay. I don't want you to blame yourself. We created this world together, as a place of comfort and solace. But it's time for you to let go and face the real world."
    k "I can't, Shiro. I can't face a world without you in it. Everything feels so empty and meaningless without you by my side."
    s "I understand how you feel, Kuro. But you can't hide in this illusion forever. You have to find a way to move forward, to honor our memories and our dreams in the real world."
    k "I don't know if I can, Shiro. I don't know if I have the strength to face the pain and the loneliness."
    s "You're stronger than you think, Kuro. You have the strength to face whatever comes your way, even if it's difficult and painful."
    k "I... I don't want to say goodbye, Shiro. I don't want to lose you again."

    show shirosmile1 with dissolve
    hide shironeutral with None

    s "You're not losing me, Kuro. I'll always be a part of you, no matter where you go. Our memories, our dreams, they'll always be with you."
    k "I'll miss you, Shiro. I'll miss this world we created together."

    show shirosmile2 with dissolve
    hide shirosmile1 with None

    s "I'll miss you too, Kuro. But it's time for you to wake up and face the real world. I'll be waiting for you there, in your heart."
    k "Goodbye, Shiro. I'll never forget you."

    show shirosmile1 with dissolve
    hide shirosmile2 with None

    s "Goodbye, Kuro. Keep our dreams alive."
    "..."
    k "I can't do it, Shiro. I can't leave you behind. I'd rather stay here, in this illusion, with you."

    show shiroangry1 with dissolve
    hide shirosmile1 with None

    s "Kuro, listen to me. Our dream was never meant to be trapped in a fantasy. It was meant to be lived in the real world, where it can make a difference."
    k "But without you, Shiro, I... I don't know if I can."

    show shiroangry2 with dissolve
    hide shiroangry1 with None

    s "You're stronger than you think, Kuro. You have the strength to carry our dream forward, even without me. Promise me you'll try."
    k "I'll try."

    show shirosad with dissolve
    hide shiroangry1 with None

    s "That's all I ask, Kuro. Now, wake up. It's time to face the real world, with our dream guiding you."
    k "No, Shiro. I can't do it. I can't live without you."
    s "Kuro, please. You have to go back. You have to face reality."
    k "I'm sorry, Shiro. I can't. I won't."
    s "Kuro, please... you have to go..."
    k "I'm staying here with you, Shiro. I can't leave you."
    s "Kuro, it's not right. You have to go back. You have to live your life."
    k "I won't leave you, Shiro. I can't."
    s "Kuro, please... you have to go..."
    k "I'm sorry, Shiro. I'm so sorry..."
    s "..."
    k "..."
    stop sound
    stop music

    jump bad_game_end

label good_game_end:
    init:
        define flash = Fade(.25, 0.0, .75, color="#fff")
    show black
    with flash

    centered """
    {size=+10}But then, a new chapter began...

    {size=+10}I found strength in our memories, in the dreams we shared.

    {size=+10}I took those colors he showed me and painted my own story.

    {size=+10}I wrote with passion, with love, with the spirit of our friendship guiding me.

    {size=+10}And slowly, the colors returned to my world.

    {size=+10}I became a literary artist, weaving tales that touched hearts and inspired minds.

    {size=+10}In every word, in every sentence, he lived on, his legacy shining bright.

    {size=+10}And as I looked up at the starry night sky, I knew...

    {size=+10}I had found myself.
    """

    centered """
    {size=+20}{color=#f00}Find Myself
    """

    return
label bad_game_end:
    init:
        define flash = Fade(.25, 0.0, .75, color="#000")
    show black
    with flash

    centered """
    {size=+10}Life remained trapped in darkness...

    {size=+10}After Shiro disappeared, I was lost.

    {size=+10}I tried to write, to create, to find solace in my art.

    {size=+10}But the colors never returned.

    {size=+10}Shiro's absence weighed heavy on my heart, a constant reminder of what I had lost.

    {size=+10}I couldn't find myself, couldn't find meaning in a world without him.

    {size=+10}Days turned into nights, and nights turned into endless despair.

    {size=+10}And as I stared into the void, I knew...

    {size=+10}I was lost in the illusion, trapped forever in a world devoid of color, of hope, of him.
    """

    centered """
    {size=+20}{color=#f00}Lost in Illusion
    """
    return

    






