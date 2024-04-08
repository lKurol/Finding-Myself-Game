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
    with Pause(1)

    scene black
    with Pause(0)

    show text "{size=+20}Presents..."
    with Pause(2.5)

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

    k "There's no signal here?! What is going on?!"


    "Kuro walks..."


#Chapter 2: Treehouse
    scene treehouse:
        fit "fill"
        xysize (1920, 1080)
    play music "etudealone.mp3" loop
    k "Shiro, look! It's our childhood treehouse!"
    show shirosurprised

    s "I can't believe it's still here. This place holds so many memories."
    k "Let's go inside, Shiro. I want to see if everything is just as we left it."
    show shirosmile2

    s "Yeah, let's relive some of our old adventures!"
    "While exploring the treehouse, You pick up a notebook filled with memories."
    k "Hey Shiro, it's our old notebook. We used to write stories in this."
    show shirosurprised

    s "I remember! We had lots of big dreams back then."
    show shirosmirk

    s "Remember how we used to read and write stories together? Those were good times."
    "As you flip through the notebook, you see some ideas you had written with Shiro."
    play sound "pageflip.mp3" volume 2.0
    k "(It's ... been a while huh)"
    menu:
        "Yeah!":
            $ clarity_stat +=1
            jump treehouse_menu_1
        "My writing was ... bad.":
            $ obscurity_stat +=1
            jump treehouse_menu_2

    label treehouse_menu_1:
        k "I enjoyed writing with you! Even though my writing style was so cringy sksksksk."
        show shirolaugh

        s "I enjoyed it, too! Your style ain't that bad y'know."
        k "But not as good as yours."
        show shirosmile3

        s "To be fair, I got into writing earlier than you."
        k "Your style literally reads like a published book!"
        show shirosurprised

        s "Woah. I think you're overpraising me."
        k "No, really! You're a genius."
        show shirosmile3

        s "Well... I don't even know what to say. I'm just flattered."
        show shirosmile2

        s "I think we both have our strengths when it comes to writing."
        k "Yeah, I guess so. It's just hard not to compare sometimes."
        show shirosmile1

        s "It's natural. Just remember that we all have our own unique voice."
        s "That's what makes writing so special."
        k "You're right. Thanks for the reminder, Shiro."
        show shirolaugh

        s "Anytime, Kuro. Now, let's keep exploring our imaginations!"
    jump abandoned_library


    label treehouse_menu_2:
        show shiroangry1

        s "What are you talking about? Your writing was good!"
        k "Just looking at my old writing makes me cringe."
        show shiroangry2

        s "C'mon Kuro, don't say that. I think its great!"
        k "But its so bad..."
        s "Have some confidence will ya?"
        menu:
            "...":
                jump treehouse_menu_2a
            "But":
                jump treehouse_menu_2a
    label treehouse_menu_2a:
        show shiroangry2

        s "No buts! No silence from you!"
        s "What matters is that you wrote them and that you tried!"
        show shiroangry1

        s "Remember, writing is a process. You'll improve over time."
        k "I guess you're right. Thanks, Shiro."
        show shirosmile1

        s "Of course! And I believe in you, Kuro. Your stories are unique and have potential."
        k "Do you really think so?"
        show shirosmile2

        s "Absolutely! They have a certain charm that draw people in."
        show shirosmile3

        s "With a little polishing, they'll be amazing!"
        k "I'll take your word for it. Thanks, Shiro. I feel a lot better now."
        show shirolaugh

        s "That's the spirit! Now, let's get back to our adventure!"
    jump secret_hideout




label abandoned_library:
    scene abandonedlibrary1
    "The Abandoned Library"
    scene abandonedlibrary
    jump starry_night

label secret_hideout:
    "The Secret Hideout"
    jump beach

label starry_night:
    scene beach1:
        fit "fill"
        xysize (1920, 1080)
    "The Starry Night"
    k "Shiro, it's a beautiful night, isn't it?"
    show shirosmile2
    s "It really is, Kuro. The stars are so bright, and the sound of the waves is so calming."
    k "It's moments like these that make me appreciate life, you know? Just being here with you, it feels like everything is right in the world."
    s "I feel the same way, Kuro. It's like all the worries and troubles just fade away."
    k "I wish we could stay like this forever, just enjoying each other's company."
    s "Me too, Kuro. But we have to cherish these moments, even if they're fleeting."
    k "You're right, Shiro. We should make the most of every moment we have together."
    s "Absolutely. Let's enjoy the peace and tranquility of this night."
    k "Shiro... there's something I've been meaning to tell you. It's... it's not easy, but I think you deserve to know."
    show shirosmile1 with dissolve
    hide shirosmile2 with None
    s "What is it, Kuro? You seem troubled."
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
    show shirosmile1 with dissolve
    hide shiroangry1 with None
    s "You're not losing me, Kuro. I'll always be a part of you, no matter where you go. Our memories, our dreams, they'll always be with you."
    k "I'll miss you, Shiro. I'll miss this world we created together."
    show shirosmile2 with dissolve
    hide shirosmile1 with None
    s "I'll miss you too, Kuro. But it's time for you to wake up and face the real world. I'll be waiting for you there, in your heart."
    k "Goodbye, Shiro. I'll never forget you."
    show shirosmile1 with dissolve
    hide shirosmile2 with None
    s "Goodbye, Kuro. Keep our dreams alive."
    show shirolaugh with dissolve
    hide shirosmile1 with None
    s "Also!"
    k "Yes?"
    show shirosmile2 with dissolve
    hide shirolaugh with None
    s "All along I knew this world was just an illusion!"
    k "Wait you knew?!"
    show shirolaugh with dissolve
    hide shirosmile2 with None
    s "Yeah!!! Now go keep our dream alive Kuro!"

    jump game_end

label beach:
    scene beach2:
        fit "fill"
        xysize (1920, 1080)
    play music "beachaudio.mp3" volume 0.1 loop
    "The Beach"
    k "sigh This place never fails to calm me down. Even though the clouds are dark. It's nice."
    show shirosmile1 with dissolve

    s "Yeah, it's like our own little slice of paradise."
    k "I'm glad we found this spot. It's nice to get away from everything for a while."
    show shirolaugh with dissolve
    hide shirosmile1 with None

    s "Definitely. It's important to take a break and just enjoy the moment."
    k "I wish we could stay here forever, just walking along the beach, watching the waves."
    show shirosmile2 with dissolve
    hide shirolaugh with None
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
    jump game_end

label game_end:

    return

    






