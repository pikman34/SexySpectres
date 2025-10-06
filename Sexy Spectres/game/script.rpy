define j = Character("Jamie Quinn", color="#ffff7d")
define m = Character("Mori", color="#256f00")
define e = Character("Erasmos", color="#ae4927")
define c = Character("Clara", color="#77b3fe")
define l = Character("Lady Jane", color="#b8234f")
define g = Character("[name]")

define J = Character("???", color="#ffff7d")
define C = Character("???", color="#77b3fe")
define M = Character("Morrigan", color="#256f00")

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

label start:

    play sound "alarmclock.mp3" volume 2.0
    scene bg bedroom
    with fadehold

    "As usual, I’m woken by my harsh, blaring alarm."
    stop sound
    "I slam down on the snooze button, curling back up in my thin sheets."
    "It’s freezing, I don’t have work, so I’ll be good to get another few minutes, right?"
    
    "..."
    
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
    scene bg srnight
    with fade
    play music "bgmusic.mp3" volume 1.5

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
    show clara neutral:
        yalign 1.0
        xalign 0.0
    show erasmos neutral at slightright
    with dissolve
    show mori neutral at fullright
    with dissolve
    
    "I blink, looking around the room - one by one, figures seem to materialise out of thin air in various parts of the living room."

    "The woman, \"Clara,\" is staring at the center of the room. There doesn’t appear to be anyone there, but the nothingness responds regardless."

    j "Heh, guess not, folks! Just gotta run through some legal stuff with the contestant and then we’ll get-"

    mc "Hold on!!"

    "I interject, fumbling with my thoughts - contestant? Show?"

    mc "Who are you people?! What’s happening?"

    j "You signed up for… no, no. Roll the intro!"

    "The room falls silent, and nothing happens. The odd energy in the room seems almost embarrassed."

    play sound "laughtrack.mp3" volume 0.8
    j "Whoops, forgot about the budget cuts..."

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

    j "Meet the incredibly enchanting... {b}{color=#77b3fe}CLARA!{/color}{/b}"

    c "{cps=15}...hello, there...{/cps}"

    "Clara, despite her sharp dress and harsh stare, seems… awkward, almost."
    "She looks over me, refusing to make eye contact."

    mc "It's... nice to meet you, Clara. I'm, uh, [name]."

    c "That’s nice. I’m Clara."

    mc "Uh, I know. Thank you."

    "The atmosphere is thick enough to send me to the grave, but thankfully Jamie seems to catch on."

    hide clara
    with dissolve
    j "Aaaaand for our second contestant, a godly man sculpted like Zeus himself..."

    j "All the way from Greece in search of companionship, meet the lovely {b}{color=#ae4927}ERASMOS!{/color}{/b}"
    
    show erasmos neutral
    with dissolve
    e "Ah, hello... it is nice to be here."

    "He falls silent, having little else to say. Jamie lets out an awkward cough."

    j "Ah, hah… that’s our Erasmos! Now, um..."

    play sound "laughtrack.mp3" volume 0.8
    "There’s a sound akin to shuffled paper, which is jarring from the formless Jamie."

    hide erasmos
    with dissolve
    j "Now... ah, yes! Let’s hope you don’t have low iron, 'cause our third contestant's got a thing for blood!"

    j "A real vampire, an expert at all things occult, meet the bewitching... {b}{color=#256f00}MORRIGAN!{/color}{/b}"

    show mori neutral
    with dissolve
    M "Jamie, for the last damn time, call me Mori..."

    "Morrigan- Mori, has a look I haven’t quite seen before. I notice her painted face, her fangs..."

    "The prominent hole in the middle of her chest. It doesn’t take detective work to figure out what happened to the poor soul."

    m "Ignore them. I’m Mori. Nice to meet you."

    mc "A-Ah, likewise. I’m [name]."

    m "Pleasure."

    "She reaches a hand out, presumably an attempt at a handshake."

    show mori neutral:
        xalign 0.5 yalign 1.0
        block:
            linear 1.0 yalign 0.8
            linear 1.0 yalign 1.2
            repeat
    "Her form phases through mine, but I do my best to match her motion."

    show mori neutral:
        xalign 0.5 yalign 1.0
    j "Hah, she’s a prickly one, folks!"

    "Jamie lets out a strikingly artificial laugh, one perfectly manufactured for TV."

    hide mori
    with dissolve
    j "Now, for our last guest… hailing from the Edwardian period, and a previous owner of this illustrious home"
    
    j "In search of real love, the beautiful {color=#b8234f}Lady {b}JANE!{/color}{/b}"

    show jane neutral
    with dissolve
    l "That’s \"Lady Jane of Boyne Manor\" to you, Quinn."

    "The woman before me commands presence, and her long title leads me to believe she was quite important in life."

    "She stares at me like I’ve already wronged her somehow."

    l "I cannot believe your nerve, Quinn. Did you truly have to host this wretched contest at my home?"

    "Y-Your home, ma’am?"

    l "{i}Lady Jane of Boyne Manor{/i} to you."

    mc "There isn’t a manor here, L… Lady Jane. This is my house."

    "I wince - her stare is mean."

    j "Folks, let’s not start the flirtin’ before we’ve finished the season premiere!"

    "I watch Lady Jane glare in the direction of Jamie’s voice. It’s hard to tell if it’s effective or not."

    hide jane
    with dissolve
    j "And that, ladies and gentleghouls, concludes our first episode. Episode two picks up tomorrow morning, so don’t forget to tune in!"

    "There are varying responses from around the room - relief, frustration, the like."

    j "See you bright and early for the next episode of… Sexy Spectres!!"

    "The other... contestants wave to each other with the exception of Lady Jane."

    "Jamie calls for my attention before I can slip off to bed."

    j "Hey, [name], got a second?"

    mc "Sure thing."

    j "You know what to do tomorrow, yeah?"

    mc "I just have to talk to two of the others, right?"

    j "Yep! Three days, six conversations. Think you can handle that?"

    mc "Sounds easy enough, yeah."

    j "Perfect! Goodnight, then!"

    mc "Night, Jamie"

    scene bg bedroom
    with fade
    "I slip back into my bedroom, partially relieved but mostly confused."
    "I still don’t recall signing up for any kind of game show, but it seems like too much hassle to fight it."
    "I put on pajamas and slip into my cold bed, wondering about what the next few days will entail."

    jump day1

label day1:
    $ not_talked_to_clara = True
    $ not_talked_to_mori = True
    $ not_talked_to_jamie = True
    $ not_talked_to_erasmos = True
    $ not_talked_to_jane = True

    $ is_day = True
    $ day_one = True
    $ day_two = False
    $ day_three = False

    $ clara_first = True
    $ mori_first = True 
    $ erasmos_first = True
    $ jamie_first = True
    $ jane_first = True

    $ q1_c_tbd = True
    $ q2_c_tbd = True
    $ q3_c_tbd = True

    $ q1_m_tbd = True
    $ q2_m_tbd = True
    $ q3_m_tbd = True

    $ q1_e_tbd = True
    $ q2_e_tbd = True
    $ q3_e_tbd = True

    $ q1_j_tbd = True
    $ q2_j_tbd = True
    $ q3_j_tbd = True

    $ q1_l_tbd = True
    $ q2_l_tbd = True
    $ q3_l_tbd = True

    scene bg bedroom
    with fade
    play sound "<from 0 to 3>alarmclock.mp3" volume 2.0
    j "Rise and shine! Ready to start chatting with everyone?"

    mc "Ready as I’ll ever be, Jamie!"

    j "That’s the “spirit”! Now, [name], choose your bachelor!"

    "Who should I talk to?"

    menu: 

        "Clara" if not_talked_to_clara:
            jump clara_conversations
        
        "Mori" if not_talked_to_mori:
            jump mori_conversations

        "Erasmos" if not_talked_to_erasmos:
            jump erasmos_conversations

        "Lady Jane" if not_talked_to_jane:
            jump jane_conversations

        "Jamie Quinn" if not_talked_to_jamie:
            jump jamie_conversations


label evening1:

    $ is_day = False    

    scene bg bedroom
    with fade
    "Who should I talk to tonight?"

    menu: 

        "Clara" if not_talked_to_clara:
            jump clara_conversations
        
        "Mori" if not_talked_to_mori:
            jump mori_conversations

        "Erasmos" if not_talked_to_erasmos:
            jump erasmos_conversations

        "Lady Jane" if not_talked_to_jane:
            jump jane_conversations

        "Jamie Quinn" if not_talked_to_jamie:
            jump jamie_conversations

label day2:
    $ not_talked_to_clara = True
    $ not_talked_to_mori = True
    $ not_talked_to_jamie = True
    $ not_talked_to_erasmos = True
    $ not_talked_to_jane = True

    $ day_one = False
    $ day_two = True

    $ is_day = True

    scene bg bedroom
    with fade
    j "Rise and shine, [name]!! Ready for another day getting to know these eligible bachelors?"

    mc "Sure am, Jamie!"

    j "Perfect! [name], choose your bachelor!"

    "Who should I talk to?"

    menu: 

        "Clara" if not_talked_to_clara:
            jump clara_conversations
        
        "Mori" if not_talked_to_mori:
            jump mori_conversations

        "Erasmos" if not_talked_to_erasmos:
            jump erasmos_conversations

        "Lady Jane" if not_talked_to_jane:
            jump jane_conversations

        "Jamie Quinn" if not_talked_to_jamie:
            jump jamie_conversations

label evening2:

    $ is_day = False    

    scene bg bedroom
    with fade
    "Who should I talk to tonight?"

    menu: 

        "Clara" if not_talked_to_clara:
            jump clara_conversations
        
        "Mori" if not_talked_to_mori:
            jump mori_conversations

        "Erasmos" if not_talked_to_erasmos:
            jump erasmos_conversations

        "Lady Jane" if not_talked_to_jane:
            jump jane_conversations

        "Jamie Quinn" if not_talked_to_jamie:
            jump jamie_conversations

label day3:
    $ not_talked_to_clara = True
    $ not_talked_to_mori = True
    $ not_talked_to_jamie = True
    $ not_talked_to_erasmos = True
    $ not_talked_to_jane = True

    $ day_two = False
    $ day_three = True

    $ is_day = True

    scene bg bedroom
    with fade
    j "Mornin’!! Are you ready for the home stretch?!"

    mc "Ready as I'll ever be."

    j "There's that enthusiasm!!"

    "Who should I talk to?"

    menu: 

        "Clara" if not_talked_to_clara:
            jump clara_conversations
        
        "Mori" if not_talked_to_mori:
            jump mori_conversations

        "Erasmos" if not_talked_to_erasmos:
            jump erasmos_conversations

        "Lady Jane" if not_talked_to_jane:
            jump jane_conversations

        "Jamie Quinn" if not_talked_to_jamie:
            jump jamie_conversations

label evening3:

    $ is_day = False    

    scene bg bedroom
    with fade
    "Who should I talk to tonight?"

    menu: 

        "Clara" if not_talked_to_clara:
            jump clara_conversations
        
        "Mori" if not_talked_to_mori:
            jump mori_conversations

        "Erasmos" if not_talked_to_erasmos:
            jump erasmos_conversations

        "Lady Jane" if not_talked_to_jane:
            jump jane_conversations

        "Jamie Quinn" if not_talked_to_jamie:
            jump jamie_conversations

label jamie_conversations:

    $ not_talked_to_jamie = False

    if is_day:
        scene bg srday 
        with dissolve
    
    else: 
        scene bg srnight
        with dissolve
    
    if jamie_first:
        $ jamie_first = False

        "I walk over to where Jamie’s voice seemed the loudest and call out their name."

        j "Hey! Do you have any questions about the game?!"

        mc "Not exactly... I had questions for you!"

        j "W-What?! No no no. I’m not one of the contestants! No need to talk to me."

        mc "But I have questions to ask you?"

        j "I- um-"

        "Jamies pauses for a moment. They almost seem lost."

        j "There's no need to speak to {i}me{/i} when we have all those lovely comprehensible ghosts over there just {i}waitin'{/i} to be spoken to!"

        mc "So, am I not {i}allowed{/i} to speak to you?"

        j "Oh, well... you can if you really want to."

    else:

        "I walk over to Jamie again, and against their best wishes inted to ask them another question."
    
    menu:

        "Why can't I see you?" if q1_j_tbd:
            
            j "I don't know!"

            mc "You don't know?"

            j "Yup!"

            mc "I don't believe you."

            j "Why not?"

            mc "You’re telling me that you’re, like, a floating voice and you know absolutely NOTHING about why?"

            j "Yes!"

            mc "Haven’t you maybe…. TRIED? To figure it out?"

            j "No!"

            mc "Why…?"

            j "Why should I! Whatever it is, I don't wanna worry about it."

            j "All I need to worry about is makin’ sure you five are having a good time!"

            mc "Well if it makes you feel any better, this is pretty entertaining for me."

            "Jamie, enthusiastic as ever, begins to squeal."

            j "YES!! That is exactly why I do this. If I had a physical form I would hug you right now, I swear!"

            mc "The thought of not having a physical form is… really interesting. I honestly can't even imagine what it must be like."

            mc "Do you remember what it was like to have a physical form?"

            j "Nope! To be honest, I don't remember much of anything from my past."

            mc "I see… then what makes you think you even want a physical form?"

            j "I mean, c'mon! I see people show affection for each other all the time, it would be nice to know what it actually feels like."

            mc "I get that, you can do a lot with words though. But I do hope one day you can learn what it feels like."

            j "T-Thanks…! For um, thanks for that. But… I really think you should just stick to talkin’ to the others! We have a great line up prepared, y'know?"

            mc "I’ll try."

            $ q1_j_tbd = False

            if day_one and is_day:
                jump evening1
            
            elif day_one:
                jump day2
            
            elif day_two and is_day:
                jump evening2

            elif day_two:
                jump day3
            
            elif day_three and is_day:
                jump evening3
            
            elif day_three:
                jump finalday
            
            else:
                "How did we get here?"
            
        "Why is this a... game show?" if q2_j_tbd:
           
            j "Why wouldn't it be?! Everyone deserves to see love unfold tonight!"
            
            mc "I guess? But there aren't any cameras, or anything you would need to make an ACTUAL game show?"
            
            j "We have a host, a stage, and five single and ready to mingle bachelors! We have MORE than enough!"
            
            mc "But why keep up the act of a gameshow? You keep referring to \"seasons,\" and an “audience,” but..."

            mc "If none of that actually exists, what's the point in keeping this whole shtick up?"
            
            "Jamie pauses for a moment. For a moment, it seems like they’ve stopped talking."

            j "I don't..." 

            "They struggle to find their words."

            j "To be honest, I don't really… know. I just have a strong urge to entertain others, I guess. Where that spark comes from is beyond me."
            
            j "You would be surprised to hear, but it's hard to actually host a TV show when you’re a ghost without a physical form."

            mc "I didn't think about it like that... I’d say you’re doing a pretty good job, Jamie."
            
            j "Thanks, [name]! That means more than you could know. You’re a real sweetheart."

            $ q2_j_tbd = False

            if day_one and is_day:
                jump evening1
            
            elif day_one:
                jump day2
            
            elif day_two and is_day:
                jump evening2

            elif day_two:
                jump day3
            
            elif day_three and is_day:
                jump evening3
            
            elif day_three:
                jump finalday
            
            else:
                "How did we get here?"

        "How did you die?" if q3_j_tbd:

            j "Jeez, at least take me out for a drink, first! Don't you know it's rude to ask someone how they died?"
            
            mc "I didn't-"

            j "Wait, how would you know… no, there’s literally no way you could know that. Sorry, [name], don't sweat it!"

            mc "I wasn’t-"

            mc "I’ll just explain anyway! It isn't really a big deal to me, y’know? Though for myself… I don't really know." 
            
            j "I’ve pondered it y'know? I feel relatively at peace, so maybe… old age? Or maybe it has something to do with why I don't have a physical form."
            
            j "But honestly, knowing how I died isn't really important for me to do what I want to do."
            
            mc "Which is?"
            
            j "Ensurin’ you all find the love of your afterlives! One way or another."
            
            mc "I mean my opinion is that I don’t think the cause was old age."
            
            j "Hm? What makes you say that?"
            
            mc "I mean, I don't think someone who died of old age would have the amount of energy you have. And you don't even sound sure of yourself when you say that?"
            
            j "Well I just assumed… I can't see myself, so I don't really know. You can usually tell how you died by looking at your body."
            
            mc "What made you assume it was old age then?"
            
            j "Apparently when you die of old age you feel at ease, or so I've been told! And I would like to believe that I lived a long life that ended with ease."
            
            mc "That does sound nice…"

            $ q3_j_tbd = False

            if day_one and is_day:
                jump evening1
            
            elif day_one:
                jump day2
            
            elif day_two and is_day:
                jump evening2

            elif day_two:
                jump day3
            
            elif day_three and is_day:
                jump evening3
            
            elif day_three:
                jump finalday
            
            else:
                "How did we get here?"

label mori_conversations:

    $ not_talked_to_mori = False

    if is_day:
        scene bg srday 
        with dissolve
    
    else: 
        scene bg srnight
        with dissolve
    
    if mori_first:
        $ mori_first = False

        show mori neutral
        with dissolve
        "I look around before approaching the fanged woman."
        
        m "Oh, huh. Me?"
        
        mc "Is there a reason I shouldn’t talk to you?"

        "Mori snorts, fidgeting with the cork on her bottle."
        
        m "Nah, I guess not. Just not real used to being approached."
        
        mc "Well, you’re interesting. Mind if I ask you something?"
        
        m "Fire away, [name]."

    else:
        show mori neutral
        with dissolve
        "I return to Mori, pep in my step as I approach her. It could be my imagination, but she seems to perk up ever so slightly."

    menu:

        "What’s with the… fangs? Jamie said that you’re a vampire?" if q1_m_tbd:

            m "What, are you scared?"

            "She seems to be mocking me, but there’s an inexplicable kindness to it."

            mc "Not scared, no. Just wondering."

            m "... right. Yeah, I’m a vampire."

            "She prods at one of her fangs, grinning."

            "I squint at them."

            mc "They’re not... like, plastic?"

            m "What?! Hell no. I can give you a demonstration if you’d like."

            mc "A-Ah, uh… I think I’m good for now."

            m "Suit yourself."

            "She saunters off, walking through my wooden door like it’s nothing but air."

            "Is she upset with me?"

            "I guess it {i}was{/i} kinda rude of me, though..."

            $ q1_m_tbd = False

            if day_one and is_day:
                jump evening1
            
            elif day_one:
                jump day2
            
            elif day_two and is_day:
                jump evening2

            elif day_two:
                jump day3
            
            elif day_three and is_day:
                jump evening3
            
            elif day_three:
                jump finalday
            
            else:
                "How did we get here?"

        "What brings you here?" if q2_m_tbd:

            m "To where? Your house, the afterlife, where?"

            mc "Uh… the game show, I guess?"

            m "Oh, that..."

            "She grimaces to herself, letting out a scoff."

            m "Dunno. Felt like I should start looking for someone, I guess?"

            mc "Ha, fair enough!"
            
            m "... what about you?"

            "Her voice softens ever so slightly, as though she fears the answer."

            mc "Me? Huh, I… don’t really know, I guess. Just looking for love, same as you."

            m "Is that so..?"

            mc "Are you judging?!"

            m "Me? Nah. You just, I’unno. Seems like you’ve got it all together."

            mc "Oh god no."

            "She laughs, not her usual snort. I can’t fight the grin etching itself across my face."

            mc "What? Just saying..."

            m "You’re funny. I like that."

            mc "Is that so?"

            "She nods, smiling back in turn."

            $ q2_m_tbd = False

            if day_one and is_day:
                jump evening1
            
            elif day_one:
                jump day2
            
            elif day_two and is_day:
                jump evening2

            elif day_two:
                jump day3
            
            elif day_three and is_day:
                jump evening3
            
            elif day_three:
                jump finalday
            
            else:
                "How did we get here?"
        
        "How did you die?" if q3_m_tbd:

            m "Y’know it’s rude to ask a lady how she died, don’t you?"
            
            mc "Oh, sorry. Uh, let me think of something else to..."

            m "Nah, all good. Everyone rots, yeah?"

            mc "I-I guess so."

            m "How I died, oh man..."

            "She lets out an unsettling giggle."

            m "Well, back when I was human, y’know..."

            mc "You were human? But I thought-"

            m "Shh! I’m getting to it."

            m "So, I had to do a ritual to properly transform, yeah?"

            mc "Is that where the..?"

            "I gesture vaguely to the hole in her chest, unsure how to phrase it politely."

            m "Yup. I had to put a stake through my heart."

            mc "... doesn't that kill vampires?"

            "I stare at her in disbelief, unsure how exactly to parse the information."

            m "I mean, yeah, but... whatever, [name]!"

            m "I’m a vampire now, so it all worked out, yeah?"

            "She stares expectantly at me, so I decide to nod."

            m "Yeah, see? All good."

            mc "Y-Yeah, all good."

            $ q3_m_tbd = False

            if day_one and is_day:
                jump evening1
            
            elif day_one:
                jump day2
            
            elif day_two and is_day:
                jump evening2

            elif day_two:
                jump day3
            
            elif day_three and is_day:
                jump evening3
            
            elif day_three:
                jump finalday
            
            else:
                "How did we get here?"

label erasmos_conversations:

    $ not_talked_to_erasmos = False

    if is_day:
        scene bg srday 
        with dissolve
    
    else: 
        scene bg srnight
        with dissolve
    
    if erasmos_first:
        $ erasmos_first = False

        show erasmos neutral
        with dissolve

        "I walk over to the man draped in cloth."

        mc "Hey. I'm [name]!"

        "I extend my hand toward him, trying to offer it."

        "He glances at my hand, then back to me. He seems uncertain, almost wary."

        e "Greetings."

        "He pauses, eyes flicking away for a moment. Silence fills the air."

        e "My name was already spoken. Your hand… is something wrong?"

        "A look of confusion crosses his face."

        mc "Oh right.. you probably wouldn't know about that..."

        "I retract my hand, letting it fall down by my side."

        "He clears his throat, fidgeting slightly with the edge of his cloth."

        e "Do you… do you wish to meet my Lissa?"

        mc "Who's Lissa? Another ghost?"

        e "Yes!"

        "He lowers his head slightly, his tone softening. He raises a single finger, toward a small insect resting on his chest. Then with care, he lets it crawl out onto his hand and holds it out toward me."

        e "She’s a Geotrupes stercorarius, an earth-boring dung beetle. Stronger than she seems. Patient… tireless… She turns what is dead into what feeds the living."

        e "I find her most marvellous. She's resourceful and, in her own way… beautiful."

        "He glances at me quickly, then back down at the beetle."

        "As he speaks, a faint smile crosses his face the first you’ve seen from him. But just as quickly as it appears, it fades, and he cuts himself off."

        e "I should stop. I’ve spoken to myself for far too long… I suppose you have questions to ask me?"

        "That you do."

    else:
        show erasmos neutral
        with dissolve

        e "Do you have something you want to say? Time isn't infinite you know."

    menu:

        "Tell me more about Lissa!" if q1_e_tbd:

            e "You care to know more? I… I am surprised."
            
            e "I have already spoken about her, what more information do you seek?"
            
            mc "How did you two become acquainted?"
            
            e "She was given to me… long ago, by someone dear to me. When I passed, she followed me. A small thing she is, yet… the greatest gift I could have asked for. She has been my companion ever since."

            mc "That's sweet, she seems to like you a lot too! Who gave her to you?"

            e "Someone I loved in life. But… I would rather not speak his name, if you would not mind. It is enough to say he gave Lissa to me. And for that, I am grateful."
            
            mc "She’s kinda cute. Does she help you feel less lonely?"

            e "I mean… I do sometimes feel the sting of loneliness. Lissa… she is quiet company, she does not ask much, and yet… she listens in her own way." 

            e "I can tell she appreciates me. She would not be here after all these years if that was not the case."

            "He pauses, looking hesitantly into my eyes."

            e "Would you… would you mind if I talked some more about her? It is rare that anyone wishes to hear me speak of my darling."

            "Sure thing! I’m all ears."

            "Erasmos brightens, a quiet excitement flickering across his face."

            e "Oh! Good! In my homeland, we used to say even the smallest creature can humble the great. Aesop wrote that a beetle once brought down an eagle. A tale often forgotten."
            
            e "When they look at her, they see filth, but I see strength. I do not think it wise to underestimate creatures like her. To make life from what is cast away… it is no small feat."

            mc "I think it’s unwise as well, Erasmos."

            e "You can hold her if you wish. She is quite friendly."
            
            mc "I don't know if that's possible… Lissa’s dead too, right?"

            e "Ah… yes. I forget myself, perhaps one day you will."

            e "Not that I wish misfortune upon you! Only that… when time has run its course, it would be nice to meet again."
            
            "Erasmos seems a bit panicked at his choice of words."
            
            mc "I understand what you mean, Erasmos." 
            
            "I chuckle, endeared."

            mc "I would like that, too."
            
            "Erasmos smiles, relieved."

            e "Ah. I’m glad."

            $ q1_e_tbd = False

            $ q2_e_tbd = False

            if day_one and is_day:
                jump evening1
            
            elif day_one:
                jump day2
            
            elif day_two and is_day:
                jump evening2

            elif day_two:
                jump day3
            
            elif day_three and is_day:
                jump evening3
            
            elif day_three:
                jump finalday
            
            else:
                "How did we get here?"
        
        "What were you before you came here?" if q2_e_tbd:

            e "I was in Greece, but it has been so long. The days blur together. All I can remember clearly is that I was… with him."

            e "I cannot speak his name… it pains me too much to even think of it. And I doubt you would have much care to hear of my past."

            "I don't want to pry, but… my curiosity gets the best of me."

            mc "I don't mind. We only have so much time to speak, right? And I want to get to know you."

            "He pauses for a moment."

            e "My past lover… in my time alive, he was who I spent my time with. We spent every waking moment together, I never felt like I belonged anywhere, except when I was with him."

            e "I passed before him and awaited his return. And in due time he came. But… by the time we were together again, he… had found someone new"

            "He trails off as he speaks."

            e "It pained me deeply. I… I did not know what to do without him. All my life I felt unwanted… and without him, I had to learn to find that belonging within myself."

            mc "I’m... sorry to hear that, Erasmos."

            "He quickly jolts his head up."

            e "You need not feel sorrow for me, [name]. Time has softened the grief. I... I can handle it now."

            e "I... I..."

            "Erasmos pauses, a quiet tension in his shoulders, his eyes distant and unblinking."

            e "I... I should stop. It seems that I am not used to sharing this much with others. My apologies, [name]."

            mc "Dont worry Erasmos! Please, it's fine."

            e "I should go now, I think I need a moment to myself. Farewell for now."

            $ q2_e_tbd = False

            if day_one and is_day:
                jump evening1
            
            elif day_one:
                jump day2
            
            elif day_two and is_day:
                jump evening2

            elif day_two:
                jump day3
            
            elif day_three and is_day:
                jump evening3
            
            elif day_three:
                jump finalday
            
            else:
                "How did we get here?"

        "What is that belt that you are wearing?" if q3_e_tbd:

            e "My belt? It is just a piece of fabric to hold my clothing together."
            
            mc "I mean the gem, mostly. It looks interesting!"

            e "Oh, it is a bug encased in amber."
            
            mc "Hm?"
            
            e "If you wish to know more about it, you must speak clearly about what you wish to know. I do not do well with assuming one's intentions."
            
            mc "What type of bug is it, why that bug specifically. That sort of thing, y’know?"
            
            "Erasmos looks surprised."

            e "Oh! I did not assume you wished to know all those details. In that case, I am happy to oblige."

            e "Encased in this amber is a moth. She was small… fragile. I remember her still. She was crushed beneath the heel of a fool who did not even notice her presence..." 
            
            "Erasmos sighs, pained at the thought."

            e "Most do not notice such things. They walk through life seeing only what shines, not what breathes quietly beneath their feet."

            "He pauses, his gaze distant."

            e "I found her after. Wings torn, body still warm. I could not bear to see her lost to the dust, so I preserved her."
        
            e "A small kindness for a small life. Perhaps it was foolish, but I like to remember what others forget."
            
            "He runs a thumb slowly over the amber, voice softening."

            e "People overlook the small things. The fragile things. Yet they are what make the world whole. I suppose that is why I keep her with me."

            e "As a reminder that even the smallest life deserves to be remembered."

            "I pause for a moment, unsure what to say."

            e "Oh forgive me! For rambling on too long, I did not mean to."
            
            mc "No no, it's alright, Erasmos. It's nice to hear your perspective on things, I mean, that's why we’re talking, isn't it?"
            
            e "I suppose so."

            "He gives a small, fleeting smile, the kind that fades before it has the chance to fully form."

            $ q3_e_tbd = False

            $ q2_e_tbd = False

            if day_one and is_day:
                jump evening1
            
            elif day_one:
                jump day2
            
            elif day_two and is_day:
                jump evening2

            elif day_two:
                jump day3
            
            elif day_three and is_day:
                jump evening3
            
            elif day_three:
                jump finalday
            
            else:
                "How did we get here?"

label finalday:

    scene bg srday 
    with fade
    j "Good morning, [name]! Get ready for tonight, because today’s the day you get to pick your perfect match!"

    j "Now, having spoken to our eligible bachelors... [name], who piqued your interest?!"

    j "Which of our four beautiful spectres will you choose to take on a date?!"

    "Who should I choose?"

    menu: 

        "Clara" if clara_once:
            jump choseclara

        "Mori" if mori_once:
            jump chosemori
        
        "Erasmos" if erasmos_once:
            jump choseerasmos

        "Lady Jane" if jane_once:
            jump chosejane
        
        "Jamie Quinn" if jamie_once:
            jump chosejamie
