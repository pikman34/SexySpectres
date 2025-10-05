# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("Jamie Quinn", color,"#ffff7d")
define m = Character("Morrigan", color,"#256f00")
define e = Character("Erasmos", color,"#ae4927")
define c = Character("Clara", color,"#77b3fe")
define l = Character("Lady Jane of Boyne Manor", color,"")
define g = Character("[name]", color,"#b8234f")

define J = Character("???", color,"#ffff7d")
define M = Character("???", color,"#256f00")
define E = Character("???", color,"#ae4927")
define C = Character("???", color,"#77b3fe")
define L = Character("???", color,"#b8234f")

define fadehold= Fade(0.5, 2.0, 0.5)

transform slightleft:
    yalign 1.0
    linear 1.0 xalign 0.25
    

transform fullleft:
    yalign 1.0
    linear 1.0 xalign 0.0
    

transform fullright:
    yalign 1.0
    linear 1.0 xalign 1.0


transform slightright:
    yalign 1.0
    linear 1.0 xalign 0.75

transform center:
    yalign 1.0
    linear 1.0 xalign 0.5
    

# The game starts here.

label start:

    play sound "<from 0 to 3.5>alarmclock.mp3" volume 2.0
    scene bg srday
    with fadehold

    "As usual, I’m woken by my harsh, blaring alarm."
    "I slam down on the snooze button, curling back up in my thin sheets."
    "It’s freezing, I don’t have work, so I’ll be good to get another few minutes, right?"
    
    " "
    
    "Shit, is it really 1pm already…?" 
    "I sigh, begrudgingly tossing my blanket aside as I try in vain to comb back my bedhead."
    "\“I’m getting too damn old for this...\”"
    "I stretch, wincing as my bones creak in ways they definitely shouldn’t for someone my age."

    scene black
    with fade

    "The taste of familiar clinical mint is sobering."
    "I grimace at the sight of my sleep-addled face in the mirror."
    "Come on, get it together..."

    python:
        name = renpy.input("What is your name?")

        name = name.strip() or "Mystery Guy"

    define mc = Character("[name]")

    "I rinse my face off, sighing. Another day alone at home."
    scene bg srday
    with fade

    "I scroll through my phone, settling down on the couch."
    "An hour slips away."
    "Then another."
    "How long has it been?"
    "I remain stationary."

    "..."

    "An unfamiliar aura permeates my living room."
    "I sit hesitantly on the couch, feeling a vague sense of anticipation."
    "Awkwardly shifting, I call out into the empty room."

    mc "Is someone… there?"

    J "Someone?!"

    "The voice that replies to me is foreign, almost unsettling if not for the abundant enthusiasm it carries."

    J "Don’t tell me… you don’t recognise your favorite host?"
    
    J "That just won’t do, not at all! Surely you’re camera-ready, right?!"

    mc "... what?"

    "I find myself speechless. There's that voice again, echoing around the room like it's empty."

    J "I could've sworn you signed up for the show..."

    J "Hah, you're too funny, [name]! Surely you didn't forget your starring role on season fifteen of Sexy Spectres?!"

    mc "Sexy Spectres-?"

    J "Moving along! Time's a-tickin', y'know! Our eligible bachelors don't have forever... at least, our star sure doesn't!"

    mc "Star? Bachelors?"

    show clara neutral:
        yalign 1.0
        xalign 0.0
    with dissolve 

    C "{color=#ffff7d}Jamie{/color}, when do we get to speak?"

    mc "What?!"

    "I turn to the source of the noise - lo and behold, an unimpressed woman that I’ve never seen before is standing by the door."

    j "Aw, {color=#77b3fe}Clara{/color}, don't you care for suspense...?"

    show jane neutral at slightleft
    with dissolve
    show erasmos neutral at slightright
    with dissolve
    show mori neutral at fullright
    with dissolve
    
    "I blink, looking around the room - one by one, figures seem to materialise out of thin air in various parts of the living room."

    "The woman, {color=#77b3fe}\"Clara,\"{/color} is staring at the center of the room. There doesn’t appear to be anyone there, but the nothingness responds regardless."

    j "Heh, guess not, folks! Just gotta run through some legal stuff with the contestant and then we’ll get-"

    mc "Hold on!!"

    "I interject, fumbling with my thoughts - contestant? Show?"

    mc "Who are you people?! What’s happening?"

    j "You signed up for… no, no. Roll the intro!"

    "The room falls silent, and nothing happens. The odd energy in the room seems almost embarrassed."

    j "Whoops, forgot about the budget cuts..."
    play sound "laughtrack.mp3" volume 0.8

    j "Aaaaanyway, welcome to a brand new season of the HIT show… Sexy Spectres!!"

    j "I’m your host, Jamie Quinn. How are we feelin’ about tonight’s episode?"

    mc "... I signed up for this?"

    "I ask the question hesitantly, sensing the mix of frustration and disappointment in the room."

    j "... how about we cut to a commercial break?"

    "Their tone is still pleasant. I brace for their frustration."

    j "Hey, uh… sport. Do you really not know what’s happenin’?"

    "I shake my head silently. They hum in response."

    j "'Kay, lemme sum it up. This is Sexy Spectres, a speed dating show with residents of the afterlife looking for love."

    j "You’re the only eligible bachelor that doesn’t, y’know, have a roommate, so your application was successful!"

    mc "S-So, you’re the host of… what, a TV show? Nobody watches-"

    j "Yessir! All you need to do is chat with our beguiling ghouls and pick someone you’re interested in datin’!"

    mc "What if I don’t like anyone?"

    "The host, seemingly the only spirit without a physical form, falls silent."

    j "No, that’s not possible! You’ll love our bachelors, okay? Y’don’t have to worry, just do what your heart tells you!"

    "I want to protest, but something in me refuses to pester poor Jamie."

    mc "... sure, I’ll play along."

    "I don’t need to tell them that a part of me is excited. I’m sure they can tell..."

    j "BRILLIANT! So, here’s the rules."

    j "{b}ONE!{/b} You may speak to two of our lovely guests per day - once in the morning and once at night."

    j "{b}TWO!{/b} You get to ask one question per ghost! And, {b}THREE…{/b}"

    j "... you can’t speak to the same ghost twice in one day."

    mc "Huh? Why?"

    j "Oh, y’know… budget… besides, you should try and get to know everyone, right?"

    mc "I… guess so."

    j "Wonderful! So, without further ado..."

    j "... let’s get to know our four LOVELY spectres!!"

    hide jane
    with dissolve
    hide mori
    with dissolve
    hide erasmos
    with dissolve
    show clara neutral at center

    j "For our first contestant, our most recently deceased, ready to get into the game..."

    j "Meet the incredibly enchanting... CLARA!"

    c "{cps=15}...hello, there...{/cps}"

    "Clara, despite her sharp dress and harsh stare, seems… awkward, almost."
    "She looks over me, refusing to make eye contact."

    mc "It's... nice to meet you, Clara. I'm, uh, [name]."