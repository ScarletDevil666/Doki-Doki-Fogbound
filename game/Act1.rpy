init python:
    renpy.music.register_channel("ambient", "ambient", True)
label Act1:
    scene bg morvaynsroom
    with dissolve
    with flash
    pause 0.1
    play sound "mod_assets/sfx/Dying Fire.ogg"
    "Silence lingers, broken only by the faint crackle of a dying fire" 
    "I’ve never been fond of silence, but moments alone have their weight" 
    "Ruling over thousands wears even the strongest down" 
    "Mm, maybe I should play a record."  
    # TODO: import sounds from drive
    play sound "mod_assets/sfx/Vinyl (1600).ogg"
    play music "mod_assets/music/Heart Shaped Box (Vinyl 1600-Prologue-Cover).ogg" fadein 2.0
    queue sound "mod_assets/sfx/male sigh.ogg"
    "Better."
    play sound "mod_assets/sfx/Faint Footsteps (Int).ogg"
    pause 1.5
    "Before I can fully relax, my quiet is cut off by the faint sound of footsteps." 
    "Even without looking, I can tell their rhythm." 
    mo "Heh..." 
    "Goro. My adviser. Always watching, always waiting." 
    "He walks like he fears waking ghosts" 
    #play sound "mod_assets/sfx/scoff.ogg"
    "I scoff."
    "If anyone should fear the dead, it is me" 
    "Goro pauses at my side, head bowed"
    show goro neut fire at l21  
    g "Sire, forgive the intrusion. I bring troubling news" 
    mo "Another matter demanding my judgment?" 
    g "It is troubling, sire. The people are losing their magic one by one." 
    pause 0.75
    "H-Huh?" 
    mo "L-Losing Magic?" 
    mo "Ah. So the kingdom aches and you think it is my fault." 
    mo "I suppose that is what happens when you leave an old king alone with his thoughts too long." 
    g "I did not say it was your fault, sire. I only—{nw}" 
    mo "I jest, Goro. You know I trust your counsel." 
    mo "Speak"
    mo "I’m sure it’s not as terrible as you are making it out to be..." 
    g "Morvayn, spells are failing." 
    g "Rituals are collapsing." 
    g "Sparks that danced yesterday are gone today." 
    g "Even the healers cannot maintain a flicker" 
    mo "A-Ah."  
    mo "I see." 
    mo "Do you remember the festival of the Last Flame?" 
    mo "The year we almost lost half the apprentices to overconfidence?" 
    mo "You were there. I nearly had to rescue them from the river." 
    g "Haah, I remember. You swore we would never see such carelessness again."
    g "And yet, here we are.." 
    mo "Carelessness is contagious, apparently." 
    pause 1.5
    mo "Or perhaps it is the curse we did not see coming." 
    mo "Do you have any idea what caused this?" 
    g "I… I have no clue, sire." 
    g "I hoped you might have a lead, something I’ve missed?" 
    mo "Aren’t you supposed to be the adviser, boy?" 
    mo "Surely you must have noticed something?" 
    g "I wish I could say I have, sire." 
    g "Everything seems to slip through my grasp." 
    g "I, myself, have only just discovered it." 
    pause 1.5
    mo "Tell me, Goro, do you ever rest even for a moment?" 
    g "Rarely, sire. Not while the kingdom still breathes. You taught me that."  
    mo "...Yes, I suppose I did." 
    mo "Even so, this question must be asked." 
    mo "Now tell me plainly, are there any who can still cast spells?" 
    mo "Even if it shows only the slightest trace?" 
    g "A few weak sparks linger. Fading fast. Like a sickness, sire." 
    mo "A powerless kingdom. And yet, here we are." 
    mo "You and I, still breathing." 
    pause 0.75
    mo "Fear wants to rise, Goro, but we cannot let it. Calm is a weapon even if I'd like to lie to myself." 
    g "Yes, sire. Calm is the weapon that keeps us alive. Even now, I see it in your eyes." 
    mo "Then, how about we move forward?" 
    mo "You will gather the healers. Every mage who can still conjure a flame."
    mo "Search the archives."
    mo "I need answers very soon.."  
    mo "And Goro.." 
    mo "Do not scold me if I am slow. You know I prefer action over hesitation." 
    g "Yes, sire. At once."
    g "And I will hold my tongue mostly." 
    mo "I will see it for myself. Carry on, old friend." 
    show goro at lhide
    hide goro
    "He bows and retreats."
    play sound "mod_assets/sfx/male sigh.ogg"
    pause 1.0
    "I sigh quietly, alone once more." 
    "A ruler cannot falter, not for them, not even for himself."
    "This must be fixed. I will fix it." 

    scene black
    with dissolve
    stop music fadeout 2.0
    pause
    "3 Days Later"
    scene bg EntLibitinaRoom
    with dissolve
    play sound "mod_assets/sfx/crackling fire.ogg"
    play music "mod_assets/music/entrance to libitina's room.ogg" fadein 2.0
    pause 1.5

    "It’s been about two minutes since I stopped outside my daughter, Libitina's door."
    "The hinges are splintered. I should have fixed them weeks ago."
    "Didn’t find the time. And now maybe I never will."
    "Now even the wind feels wary, like it knows we’re running out of time."
    "Colder in the mornings, and heavier at night."
    "Three days ago, the sky was still clear."
    "The air had a spark in it, like the world was still breathing easily."
    "A spark that promised something simple, and ordinary."
    "A normal winter. Or, well… as normal as it could be."
    "But now that spark feels distant, like a memory fading before my eyes."

    "For the past three days, I’ve hardly slept."
    "I’ve been in the archives, reading through every ritual, every old scroll."
    "Chasing whispers of magic that might still work."
    "Poring over old battle plans, testing spells that should have died with me years ago."
    "I’ve even spoken to healers, begged for reports, and yet… here we are."
    "I’ve watched the kingdom falter while pretending I’m fine. Pretending I can still fix it all."
    "And, maybe I can."
    "Maybe I can’t."
    "That’s the burden of being a king."
    "But, of course my men started faltering, just like Goro warned."
    "At first, it was just the small things. A fizzled spell. A torch that wouldn’t light."
    "Then it all went dark."
    "The glow, the fire in their eyes snuffed out."
    "I told myself it was fatigue."
    "I told myself it would pass."
    "I told myself to keep quiet. Maybe I did not want to see the fear in their faces."

    show l base neutral at t11
    mo "Fuck."

    "I didn’t tell Libitina."
    "She would ask questions I cannot answer."
    "‘Who did this? Why is it happening?’"
    "I do not know. That is the bloody truth."
    "Perhaps it could have been deliberate."
    "Perhaps another kingdom has done this."
    "Every falter, every spark that died… maybe it was planned."
    "But for now, it is only a theory."

    pause 1.5

    "So I stayed quiet. Pretended I had control."
    "But hiding rot doesn’t work forever."
    "She knows something is off. I can feel it."
    "I do not know what I will say when I open the door."
    "But she deserves the truth."
    "I push it open."

    play sound "mod_assets/sfx/door opening.ogg"
    scene bg LibitinaRoom with fade
    show libitina base neut fire regalia at t11

    "Libitina sits cross-legged on the floor, head down."
    "Christ… how will she take this?"
    "I step inside, hesitantly."

    mo "Libitina… we need to talk."

    pause 1.5

    show libitina conc
    l "You sound different, Father. Is something wrong?"

    mo "Different? Maybe."
    mo "I’m tired, yes. But it’s not just that."

    l "Don’t worry, Father. You can tell me."

    pause 1.5

    mo "There’s no easy way to say this."
    mo "The people… they’re losing their magic."
    mo "One by one, it’s fading."

    pause 0.75

    show libitina lsca
    l "Gone?"
    l "Father, that’s impossible?"
    l "Three days ago, I felt it. The power was still there?"
    l "Well and alive?"

    mo "Alive enough to fool the vessel, perhaps."
    mo "But fools rarely last long."

    pause 0.75

    mo "The Festival of the Last Flame."
    mo "Do you remember that chaos?"
    mo "Half the apprentices nearly died because of overconfidence?"

    show libitina worr
    l "I remember. I was just a child, but I can’t forget the panic, the screams…"
    l "Is it like that again?"

    mo "Worse. It’s not overconfident this time."

    pause 1.5

    mo "I have a theory, Libitina."
    mo "That this was intentional, carefully planned."
    mo "Every falter, every spark that died. It was meant to happen."
    mo "Another kingdom, a rival, could be behind this."
    mo "Watching us, probing our weaknesses, wearing us down before they strike."

    show libitina worr at t11
    l "W-Who would do that?"
    l "How could they take something so… essential?"

    mo "I do not know, and that is the goddamn truth."
    mo "I’ve spent three days hunting answers, testing old spells, reading every scroll I could."
    mo "And still… here we are."

    show libitina worr
    l "Then we’re defenseless?"
    l "Father… I’m not afraid of dying. I’m afraid of watching the kingdom fall while we stand here and do nothing."

    mo "Defenseless? Hardly. We are alive, aren’t we? That counts for something."
    mo "Though, you aren’t completely wrong."
    mo "There’s nothing we can do right now to stop it. Not yet."
    mo "But that doesn’t mean we wait helplessly. Every moment we survive, we learn, we prepare."
    mo "When they strike, we will be ready. That is the only power we have at the moment."

    show libitina sad
    l "I… I wish I could help now. I feel useless."
    l "But I remember the festival of the last flame, Father. I remember the panic and how you saved us all then."

    mo "Saved? That’s a flattering way to put it."
    mo "I barely stopped them from killing themselves."
    mo "Magic or no magic, even kings can barely hold back chaos."
    mo "But you… you’ve grown since then."
    mo "You see fear, and you don’t fold. That’s why I trust you."

    show libitina sad ce
    l "I trust you too, Father… but it’s heavy."
    l "This weight… I can feel it."
    l "Even if we survive, how do we protect everyone else?"

    mo "Protect? Heh, maybe we can, maybe we can’t."
    mo "The truth is, I don’t know."
    mo "Not fully. That’s the burden we carry."

    show libitina unsu
    l "Then how about we carry it together?"
    l "You and me?"

    mo "Of course, Libitina."
    mo "We do what we can. We fight. We survive."
    mo "And when the time comes, we burn brighter than they think possible."

    l "Yes, Father."
    l "But what if we don’t succeed?"

    mo "Then you’ll learn the hard way, like I did."
    mo "But hear me. Today we will not fail."
    mo "Not while I draw breath."
    mo "I will keep you alive, Libitina."

    show libitina 
    l "…I trust you. I’ll follow."

    mo "Good. Then let’s breathe while we can."
    mo "Moments of calm… then action when it matters."
    "We step forward, together, and move outside."

    stop sound fadeout 2.0
    scene black with dissolve
    scene bg Village 
    show fog
    with dissolve
    play music "mod_assets/music/King Morvayn.ogg"
    play ambient "mod_assets/ambience/ext_day.ogg"
    show libitina base neut regalia evening at t31

    # SLIDE: BG: Calm B4 The Storm Village
    scene bg calm_b4_the_storm_village
    show fog
    with dissolve

    play sound "sfx_wind.ogg"
    play music "king_morvayn.ogg"
    # Sprite Hue: Grey (Rainy Colored Hue)

    "The wind hits us like a tank, fog curling in from the edges of my vision."

    mo "Shit, I swear, if this is just a calm before the storm, I’ll lose what’s left of my patience."

    show libitina base neut regalia evening at t11
    l "It feels… heavy. Everywhere."

    "We move toward the railing, stepping carefully up the worn stone steps."

    mo "Follow me, Libitina."

    l "Why? Where are we going?"

    mo "Up here, we can see better. Watch the men below, if the possibility of this being intentional really is true."
    mo "Anticipate every move before they make it."

    l "Will that be enough?"

    mo "Enough? No. But it gives us a chance. That’s all we need for now."

    # BG: BLACK SCREEN: Slowly Fade In:
    # DO NOT SHOW LIB SPRITES!!!
    scene black with fade
    "She nods, silently, gripping the railing."
    "I can feel her tension, tight as a wire, matching mine step for step as we finally reach the top."

    # Slowly Fade In: BG: RAILING (visuals sway)
    scene bg railing
    show fog
    with dissolve
    # (Do not show libitina sprites on railing)

    mo "Eyes forward. Watch the stairs."
    mo "Watch the shadows. We wait until we know exactly what we’re facing."

    l "I’m right here, Father."

    mo "Good. That’s all I need."

    pause 0.75

    # QUICK FADE IN + FADE OUT: MUSIC fades out, SFX wind continues
    stop music fadeout 1.5
    play sound "sfx_wind.ogg"

    "A couple hours have passed since Libitina and I stepped out onto the railing."
    "The fog hasn’t lifted at all."
    "But that’s the least of our worries."
    "They could strike at any given moment."
    "But throughout all the worry, we’ve stayed low, our eyes on the kingdom below."

    fadeout 1.5
    scene black

    mo "Ya know, Lib."
    mo "It’s been a while. Maybe we should check on the others."
    mo "See if anyone’s still holding the walls."

    l "You aren’t wrong."
    l "We can’t stay up here forever."
    l "Let’s go."

    "We edge toward the stairs, carefully."

    mo "Follow my lead. Keep low, and don’t speak unless you have to."

    l "I-I will."

    "As we make our way down, a familiar face blocks our path before we reach the bottom."

    play sound "sfx_footsteps.ogg"

    # FAST SLIDE to Morvayns Territory (outdoor)
    scene bg morvayns_territory_1600
    show fog
    with wipeleft_scene

    # (you can show lib sprites now - just not on railings or black/white screens)
    show goro base neut at t11
    goro "Morvayn, Libitina!"
    goro "I’ve been looking for you. Thought I’d find you here."
    goro "Today has been… rough. But we’ll get through it. We always do."

    mo "Damn straight, Goro."
    mo "How have you been holding up through everything?"

    goro "Ah… I’ve been—"

    # Visuals - Zooms In To Goro's Forehead
    play sound "sfx_goro_gunshot.ogg"
    show screen shake
    play ambience "ambience_war_fadein.ogg"
    play sound "sfx_collapse.ogg"

    "Suddenly his head snaps back."
    "He collapses onto the steps."
    "Blood stains the stairs instantly."

    play music "your_sweet_six_six_six_cover.ogg"

    mo "What the fuck!"
    mo "Libitina, run back up the steps!"

    "We sprint up the stairs instantly, blocking the enemy’s shots."

    # FASTLY FADE IN BLACK SCREEN
    scene black with fade
    "They’ve finally struck, and this is their way of saying hello."
    "God, Goro…"
    "I’ll sulk later."
    "I have a kingdom I need to protect."
    "The fog hides them, whoever they are."

    # Fast Slide to Railing (do not show libitina sprites)
    scene bg railing
    show fog
    with slide

    # DO NOT SHOW LIBATINA’S SPRITES!!
    l "Fucking hell!"
    l "Father, what do we do?"

    mo "Stay down! Don’t move unless I say!"
    mo "They knew we’d be here."
    mo "I was right."
    mo "These bastards planned this!"

    "Libitina curls closer to me. I can feel her shaking."
    "I’m barely keeping it together myself!"
    "Every shadow in the fog feels alive."
    "Every sound is a threat."

    mo "It’ll be okay, Libitina, just…"
    mo "Stay low. Watch the steps. Watch the fog."
    mo "And for fuck’s sake, don’t let them see us panic!"

    "The kingdom suddenly feels small, and reckless. And we’re right in the middle of it."
    "But we have each other."
    "We can face this."
    "I shift my gaze to another nearby wall."
    "That’s when I see it."

    # SLOWLY FADE IN: Armed Guards #1 (outdoor)
    scene bg armed_guards_1
    show fog
    with dissolve

    "Their armor, their stance…"
    "They aren’t here to talk."
    "I can feel the weight of their weapons from here. They’re coming for blood."

    # FAST SLIDE back to Railing (do not show lib sprites)
    scene bg railing
    show fog
    with slide

    l "What’s our next move?"

    mo "I-I should have guns. Stored in my room for emergencies."
    mo "Follow me, fast. Now!"

    "I grab her hand, yank her close, and we bolt."

    scene black
    "Smoke, fog, wind, everything presses against us, thick, and suffocating."
    "I can hear their shots lingering before us."
    "We don’t have much time."
    "Finally, we make it to the bottom."

    # FAST SLIDE - BG: Morvayns Territory (outdoor)
    scene bg morvayns_territory_1600
    show fog
    with slide

    mo "Down into my territory. Keep close. Don’t even think about looking back."
    mo "We’ll make a stand where we have the advantage."

    show libitina base lsca regalia evening at t11
    l "I’m scared, Father."
    l "I don’t know if I can—"

    mo "You have to focus, Libitina."
    mo "That’s it. You survive by focusing."

    "Her fingers squeeze mine."
    "She’s scared, yes, but she’s still moving."
    "She’s not frozen. Not entirely."
    "I can feel the panic rising in me, too. I taste it in my mouth, bitterly."
    "But I force it down. I need her to move, I need her to trust me."

    mo "Almost there…"
    mo "The room is just ahead."
    mo "Lib, stay tight. One misstep and we’re dead."
    mo "Guns…"
    mo "We get the guns, then we decide."

    l "I-Im holding on, Father."
    l "I trust you."

    # Slide to Morvayns Room (indoor)
    scene bg morvayns_room
    with slide
    play sound "sfx_muffled_rain.ogg"
    play ambience "ambience_muffled_war.ogg"

    # NARRATION: Sfx: Door Opening
    play sound "sfx_door_open.ogg"
    "I fling open the door to my territory."
    "We immediately run to the shelves."

    pause 0.75
    scene bg morvayns_room_zoomed
    with fade
    "W-What?"
    "The shelves should be lined with weapons, old but reliable."
    "But… nothing."

    stop music fadeout 1.5
    play ambience "ambience_muffled_war.ogg"
    "Every gun is gone."
    "Not a single sword or dagger left untouched."
    "The bastards knew exactly what to take."
    "I grip the edge of the nearest shelf, trying not to show panic."
    "Every heartbeat thrums in my chest like a drum."

    scene bg morvayns_room
    with fade
    show libitina base upse regalia at t11
    l "They… they took them all?"

    mo "Y-Yes."
    mo "And that means we have no fallback."
    mo "No comfort. Nothing to buy us time if they come for us again."

    pause 1.5

    mo "We have to use the last of it. The magic that still lingers. Every bit we have left."

    show libitina unsu at t11
    l "Father… you mean?"

    mo "Yes. Every ounce."
    mo "Libitina, listen. This isn’t a parlor trick."
    mo "This is life or death. If we fail here, the kingdom fails."
    mo "Look at me. Keep your focus. Do not flinch, do not doubt."

    pause 0.75

    "The power is faint, but I feel it stirring."
    "I can barely reach it, but it’s enough if we move fast."
    "If we move together…"

    l "I-I can feel it too, Father. It’s weak…"
    l "But it’s there."

    mo "Good. That’s all we need for now."
    mo "It’s enough."
    mo "They might have taken our guns, but they haven’t taken our fight."
    mo "Magic or no magic, we make them regret ever thinking this would be easy."

    pause 0.75

    mo "Now focus, Libitina."
    mo "Every flicker, every spark counts. We do this right, or nothing else matters."

    # Nothing Else Matters (Cover) fades in
    play music "nothing_else_matters_cover.ogg" fadein 1.5
    show libitina base conc regalia at t11
    l "I’ll stay with you, Father. I’ll do it."

    mo "Together. Always together."
    mo "Now, let’s make this count."
    mo "Once we’re out there, we hit the railing and draw every ounce of power we’ve got left."

    l "O-Okay…"

    "We step out into the storm, and make a run for it."

    # longer slide to Railing (outdoor)
    scene bg railing
    show fog
    with slide

    "We eventually reach the railing, ducking and dodging every shot that came our way."

    mo "Do you see them, Libitina?"

    # DO NOT SHOW Libitina SPRITES!!
    l "Y-Yes."
    l "Let’s finish what they started."

    mo "Damn right we will."

    # Fast Fade In - BG: Armed Soldier (outdoor)
    scene bg armed_soldier_1600
    show fog
    with fade

    # Visuals: Screen sways back and forth if possible
    #TODO: Scarlet, can you make the screen shake here?
    "My eyes dart to the soldiers, gunning down innocent mages."
    "Magic hums weakly in my veins, barely enough to hold a spark."
    "I draw in a shaky breath, preparing to push the last of it into one strike."

    mo "Let’s see what you’ve got."

    "I thrust my hands forward, pouring every ounce of remaining power into a single hit."

    play sound "sfx_whimper.ogg"
    play sound "sfx_falter.ogg"

    "The air cracks with energy. A guard nearest to me goes flying, slamming against the stone floor."
    
    # Armed Guards #1 (outdoor)
    scene bg armed_guards_1
    show fog
    with fade

    "HA!"
    "Too easy."
    "I glance back, ready to crush the next one."
    "And then it hits me…"
    "My power isn’t what I thought it was."
    "That’s when I realize how weak it truly is."

    mo "Shit."

    "The guard slowly lifts his weapon, eyes wide, smiling at me cheekily."

    play sound "sfx_goro_gunshot.ogg"
    show screen shake
    "Before I can react, a shot tears through the air, grazing my shoulder."

    "Pain flares, sharp and burning, but I grit my teeth and push through it."

    # Fast slide to Railing (do not show libitina sprites on railing)
    scene bg railing
    show fog
    with slide

    mo "Lib! Downstairs! Now! I’ll meet you there!"

    "Libitina hesitates for a split second, fear written across her face."
    "I grab her arm, yanking her toward the stairs. Every step is a gamble."
    "The storm howls around us, mixing with gunfire and desperate screams."
    "I know if I stay too long, we both die."
    "Every ounce of strength in my body focuses on keeping her alive."

    mo "Move, Libitina! Don’t stop!"

    "As she vanishes down the stairs, the last sparks of magic curl around my hands, fading fast."
    "Suddenly, a thought I’ve shoved to the back of my mind for years hits me."

    pause 0.75

    "There’s one path I’ve kept buried, a spell I swore never to touch."
    "Forbidden, dangerous, old as the kingdom itself."
    "Only for the darkest hour. And that hour is here."
    "It kills the caster. Rips the soul clean out and forces it into the nearest corpse."
    "The spell depends on voluntary sacrifice. you have to kill yourself for it to work."
    "Then, you receive a second life, trapped in borrowed flesh. A desperate man’s trick."
    "Apparently, it saved generals centuries ago, but none of them stayed the same. Some came back barely human."
    "This is my last ounce of power. If everything falls apart, if there’s no other way…"
    "This is what I’ll throw at them."
    "I’ll use it. Even if it turns me into something she won’t recognize."
    "But not now. Not here."
    "She must not see. She must not know."
    "She needs her father… not the monster I might become."

    "Finally, I make it downstairs to her."

    mo "Libitina, follow me. Don’t fall behind."
    mo "There’s a forest not far from here."
    mo "A place even most of our own people don’t remember."
    mo "They won’t find us if we move fast."
    mo "Let’s get the hell out of here!"

    # Away Path (outdoor)
    scene bg away_path
    show fog
    with slide

    play sound "sfx_running_ext.ogg"

    "There is no time. I grab Libatina’s hand, and we begin to flee."
    "Arrows and bullets streak past us, embedding in the ground near our feet."
    "Libitina clutches my hand, tightly, panting heavily."
    "We have to survive."
    "We have to!"
    "I’m not giving it up, dammit!"

    "Finally, we spot the forest."
    "Its entrance lies open and unguarded."
    "A haven for cover."

    # show libitina now (outdoor) - she is frightened/scared
    show libitina base vsca regalia evening at t11

    "We make a break for the trees."

    scene bg forest_1600
    show fog
    with fade

    play sound "sfx_wind.ogg"
    play ambience "ambience_war_quiet.ogg"
    stop sound "sfx_running.ogg" fadeout 1.0
    play sound "sfx_branches.ogg"

    "Branches tear at our faces the moment we hit the forest."
    "I hear them behind us."
    "Shouts. Orders barked over the chaos."
    "I let out a shaky sigh."

    pause 0.75
    play sound "sfx_male_sigh.ogg"

    "The forest swallows the sounds, thick and foggy."
    "For a few precious seconds, the world holds its breath."
    "Just enough for us to catch a heartbeat."

    play sound "sfx_female_sigh.ogg"

    show libitina base worr regalia evening at t11
    l "Maybe… maybe we’re safe…"

    pause 0.75

    show libitina base lsca regalia evening at t11
    "She presses close, trembling."
    "I grip her hand tighter, feeling her pulse race against mine."

    pause 0.75

    "But, I should know better. Safety is an illusion, in our circumstances."
    "The moment we stop, even if only for a second, the world will find us again."

    play music "nothing_else_matters_cover.ogg" fadein 2.0
    play sound "sfx_footsteps_faint.ogg"

    # Zoomed-in forest (outdoor)
    scene bg forest_1600_zoomed
    show fog
    with fade
    # Visuals: screen sways back and forth (if possible)

    "Movement in the shadows. Figures crouched behind thick trees, silent, and waiting."
    "Only seconds. That’s all we’ve got."

    # Screen stops swaying
    scene bg forest_1600
    show fog
    with fade

    mo "Libitina! RUN!"

    play sound "sfx_running_ext.ogg"

    # Gunshots and screen shakes
    play sound "sfx_goro_gunshot.ogg"
    show screen shake
    pause 0.2
    play sound "sfx_goro_gunshot.ogg"
    show screen shake
    pause 0.2
    play sound "sfx_goro_gunshot.ogg"
    show screen shake

    show libitina base vsca regalia evening at t11
    "She doesn’t even think. She bolts, her feet slamming the dirt as she vanishes down a narrow path I can’t follow."
    "Gunfire and arrows slam into the dirt at her feet, missing her ankles by inches."
    "But she slips away."
    "That’s all that matters."
    "The guards bolt after her, but the forest takes her before they reach her."
    "She’s got this."
    "Shit, do I?"
    "My chest tightens, nerves twisting inside me."
    "God, this is it."
    "The spell… the one I swore I’d never touch."
    "This is why I kept it hidden. Because it kills the caster."
    "But what choice do I have?"
    "No time to think. Hesitation gets you dead."
    "And me? I’m not going out without making it count."
    "She dies if I stall. Every last damn life in my hands. And I’ll be a corpse if I don’t do this."

    pause 1.5
    play sound "sfx_slash.ogg"

    "My throat opens in a single, straight cut."

    # Visuals: blood fades in

    "Hot blood surges, and burns, as my vision tilts."

    play sound "sfx_collapse.ogg"
    play sound "sfx_thud.ogg"

    # Black screen with blood overlay
    scene black
    with fade

    "The enemy freezes."
    "Silence hangs for the briefest second before panic hits them."

    pause 2.5
    play sound "sfx_the_king_is_dead.ogg"

    "They have no idea."
    "They think we’ve lost."
    "They think the king is dead."
    "But I’m not. Not yet. Not even close."

    stop music fadeout 2.0
    stop sound "sfx_wind.ogg" fadeout 2.0
    stop ambience fadeout 2.0

    scene bg Fire_Village
    show fog
    show eff_rain_l
    with dissolve_scene_full
    play sound "mod_assets/sfx/gasp.ogg"
    play ambient "mod_assets/ambience/rain_ext.ogg"

    pause 1.5
    "I awaken slowly, in another soldier's vessel."
    "Limbs that once were strong, now feel brittle and foreign, weighed down by the shell of someone else."
    stop ambient fadeout 2.0
    pause 1.5
    "This."
    "This is the cost."
    "The body dies, but the mind endures."
    "The shell is borrowed, broken, but the king remains."
    "I have cheated death, but the world has not cheated me."
    # The script says to hide Morvayn, but it never said to show him in the first place? Confusion.
    
    "I rise on unsteady legs."
    "Every motion is a reminder this is not my form, not my strength."
    "And yet, I am here."
    "Dead soldiers around me."
    "I can think, plan, breathe."
    "I take in the empty, silent aura of the once full and spirited kingdom, letting the breeze cool over me."
    "I take it in slowly, savoring each sense."
    "My mind reaches for Libitina."
    "I picture her small, brave, running ahead, untouched by the enemy."

    mo "She is safe, for now."
    mo "And that is all that matters."
    mo "For her, I have endured the unbearable."
    mo "For her, I cast the spell no king should ever wield."
    pause 1.5
    "They think the king is dead."
    "They celebrate as if they have claimed everything."
    "They do not know the truth. They do not know that the ruler remains."
    "That I remain."
    "That the game is not over."
    "They are all by the forest."
    "I must move fast."
    "I take a step forward, then another."
    "Each movement, each breath, each heartbeat is proof."
    "Proof that the impossible has happened."

    mo "The king is dead... But the ruler lives on..."
    mo "Bound by the fog."
    mo "I will find Libitina. She will not be left behind."
    
    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    pause 1.5
    scene bg 1700Forest
    show fog
    with dissolve_scene_full
    play ambient "mod_assets/ambience/wind.ogg"
    "Nearly a hundred years have passed since the fall of Blackbriar."
    "Years carried in exile, walking in shadows, wearing a face that’s not my own."
    "Yet through all of it, Libitina has remained at my side."
    pause 1.5
    "We have crossed kingdoms, seas, mountains... all searching."
    "Always searching."

    play sound "mod_assets/sfx/crackling fire.ogg"
    "We rest by the fire, the forest around us quiet."

    show libitina base regalia neut fire at t11 with dissolve
    l "Father... how long will this go on?"
    pause 1.5
    mo "What do you mean, Libitina?"
    show libitina sad

    l "We leave one place, find another."
    l "And every time, they drive us out."
    l "It’s been nearly a century."
    show libitina unsu
    l "War, suspicion, curses."
    l "Running.."
    l "Always something."
    l "Always someone watching."
    pause 1.5
    show libitina eyes_a
    l "When will we have a home again?"
    "Her voice is not the frightened whisper of the girl she once was."
    "It carries weight now."
    "Patience, tempered by years I cannot deny her."
    mo "Heh.."
    mo "I have asked myself the same question."
    mo "More times than you know."
    show libitina unim
    l "We survive, yes."
    l "We endure. But what life is this?"
    l "Running from one shadow to the next?"
    "Her eyes meet mine in the firelight."
    mo "Home is not found, Libitina."
    mo "It is made. And it cannot be made yet."
    mo "Not until the prophecy is fulfilled."
    show libitina neut
    l "What the hell kind of prophecy are we looking for?"
    l "And if we never find it?"
    mo "Then we keep walking."
    mo "Because if we stop, all of this-"
    pause 0.75
    mo "All of us... ends."
    show libitina neut mouth_c eyes_d
    "She exhales, looking into the flames."
    "Not content, but not broken either."
    "Her strength humbles me"
    "In her voice I hear the echo of her mother.."
    "And in her silence, the weight of every year I’ve stolen from her."
    "Dammit.."
    show libitina base regalia conc fire
    l "Then I will walk with you, Father."
    play sound "mod_assets/sfx/Dying Fire.ogg"
    "The fire fades away, the smell lingering around us."
    show libitina base regalia neut evening with dissolve
    l "The fire’s gone, Father."
    l "Do we keep moving?"
    mo "Yes. We cannot stay where the light dies."
    mo "We move until we find shelter."
    scene bg 1700Path
    show fog
    with dissolve_scene_full
    "We’ve been walking for a while through an unfamiliar path."
    "The path is uneven, tangled with roots and shadow."
    "Each step feels heavier than the last, but we press on."
    "Hours blur, until the forest gives way to something vast."
    "Before us, the trees fall away as we move."
    "We approach a-"
    scene black
    "A-A crater."
    "Wide, deep, and black with shadow."
    "The space here is broken, as if struck by something ancient, something meant to be forgotten."
    show libitina base regalia unsu night at t11
    l "What is this place...?"
    mo "I-I do not know. I have never seen land shaped like this."
    show libitina at thide
    hide libitina
    "We step carefully to the edge."
    "Loose stones tumble downward, swallowed by the dark. Then, in the stillness, I see it."
    "A crack?"
    "No, an opening."
    "A cave.."
    "At first it seems natural, but as I look closer.."
    "The shape is too deliberate, the angles way too clean."
    "This is no accident of stone."
    show libitina base regalia worr night at t11
    l "Father... there’s something inside."
    "She’s right."
    "A passage, cut by hands long before ours."
    "A cave, hidden beneath the scar of the crater."
    "My heart beats faster. Not with certainty."
    "But with the weight of discovery."
    "Whatever this place is, it was meant to be found, or meant to be buried."
    mo "Come with me Lib."
    mo "We will see what waits in the dark."
    stop ambient fadeout 2.0
    "Together, we descend into the depths."
    play ambient "mod_assets/ambience/int_night.ogg"
    scene bg CaveInterior with wipeleft_scene
    "The stone narrows around us, pressing close, until at last the passage opens into a chamber."
    "Libitina and I walk by each side looking for some type of connection, or shelter inside the space."
    "But instead I'm met with something else."
    scene black with fade
    "Little lines of text are scattered around the cave, each one less reconcilable than the other."
    "The walls.."
    "They are not natural."
    "Carved by hand, etched with symbols that shimmer faintly against the dim light."
    "A language unknown, curling across the stone like roots of meaning I cannot yet grasp."
    "But, a couple of lines singled out, stand out to me."
    pause 0.5
    scene bg CaveText with dissolve
    mo "...Someone was here before us."
    show libitina base regalia unsu green at t11
    l "Father, can you read it?"
    "I reach out, fingers brushing against the ancient text."
    pause
    show libitina at thide
    hide libitina
    "I cannot read it yet."
    "But it feels familiar."
    "As though some echo of the words lives in my blood."
    pause 1.5
    "Then I hear it.."
    "Not from the walls, but from memory.."
    "A voice, deep and steady, carried from my childhood."
    "My grandfather’s voice."
    stop ambient fadeout 2.0
    play music "mod_assets/music/King Morvayn.ogg" fadein 3.0
    mo "...I know this text."
    show libitina base regalia unsu night at t11
    l "You do? But how?"
    mo "I never thought I would hear it again."
    mo "My grandfather spoke these words only once, long ago, by firelight on a winter’s night."
    mo "He said they were old, older than kings, and that I should remember them, though I never understood why."
    mo "And here they are, carved into stone beneath Blackbriar.."
    mo "The same warning he gave, inscribed by those who came before us."
    mo "'If the kingdom falls, if fire takes the throne, seek the scar where earth was broken.'"
    mo "'Beneath its wound, the words endure.'"
    mo "'Take them into your blood, carry them into the dark.'"
    mo "'And the line will not be severed.'"
    show libitina worr
    l "He told you this?"
    pause 1.5
    l "He knew?"
    "My chest tightens."
    "My grandfather had spoken of ruin before it came.."
    show libitina at thide
    hide libitina
    "He had left behind a path for us in the shadow of defeat."
    "I thought of them only as stories."
    "But now.."
    "I now see them for what they really were."
    mo "He knew the kingdom would fall."
    mo "He knew we would stand here, at the edge of its grave."
    mo "These words.."
    mo "They are meant for us, Libitina."
    pause 1.5
    mo "We must find out what this means."
    mo "If it takes us days, weeks, years.."
    mo "So be it."
    mo "We will find out."
    stop music fadeout 2.0
    scene black
    with dissolve_scene_full

    # Title Card: Three Years Later
    scene bg 1700Path
    show fog
    with dissolve_scene_full
    play music "mod_assets\music\Zombie (Cover).ogg" fadein 2.0
    "Three years passed within the stone belly of the crater."
    "Three years of dust and firelight, of words carved into parchment until my hands bled."
    "With many quests as-well along the way."
    "Three years of Libitina’s quiet voice, keeping me anchored when shadows pressed too close."
    "I love her."
    "We’ve gone through hell and back together."
    pause 1.5
    "At last, the language surrendered itself to me."
    "The meaning was not simple... but it was clear."
    "It’s time I tell Libitina."
    "It’s time we go."
    "I step into the cave"
    scene bg CaveText with wipeleft_scene
    mo "Libitina, It’s time." 
    show libitina base regalia unsu night at t11
    l "Oh my?"
    l "Father this is.."
    l "What does it say?"
    mo "It speaks of two paths."
    l "What do they say?"
    mo "The first is a way through."
    mo "A portal."
    mo "A passage to another world."
    mo "A place where our people’s power lies waiting."
    pause 1.5
    mo "The second is the spell I once used, long ago."
    mo "But perfected."
    mo "Refined, you could say."
    "It is not a simple transfer now, not the vessel I once forged for myself."
    "This is power without limit."
    mo "It speaks of a mass awakening."
    mo "A way to place thought, memory, soul into bodies already stilled by death."
    mo "An army, loyal and unbroken. Carved not of flesh, but of will."
    show libitina worr
    l "To wake the dead?"
    "Her voice trembles, not in fear of me, but of what these words demand. And yet she does not turn away."
    mo "Yes. To wake them."
    mo "To bring them back to us eventually."
    mo "These texts tell me the truth."
    mo "The portal will carry us to a world not unlike our own, yet steeped in what was lost."
    mo "There, we must find vessels."
    mo "Bodies left behind by death, waiting to be claimed."
    l "Vessels...?"
    mo"Yes. People."
    mo"Each one will hold more strength than the last."
    mo"We must claim them, master them, until at last we find the strongest vessel of all."
    mo"Even if it means we have to kill."
    pause 1.5
    mo"Only then can my power be restored."
    mo"Only then can we return to Blackbriar... and raise our kingdom from its grave."
    mo"Bring the people back."
    mo"And take what’s ours.."
    pause 1.5
    mo "Libitina, I need you to open the portal for me."
    show libitina awkw
    l "...Me?"
    mo "Yes. The blood that binds us is the key."
    mo "Alone, I cannot force the passage open."
    mo "But with your strength, our line united, the way will yield."
    l "I-I don’t know if I can."
    mo "You can. You must."
    mo "These words were left for us, not for others."
    mo "The path is ours to walk."
    pause 1.5
    mo "Without you, Libitina, the kingdom dies with me."
    show libitina conc
    l "...Tell me what to do."
    "I move over to the wall, fingers tracing the deepest lines of the script."
    "My voice takes the rhythm of the old tongue... words my grandfather once whispered by firelight, long ago."
    "The cave trembles."
    play sound "mod_assets/sfx/Low Hum.ogg"
    "A low hum grows in the stone, in the air, in their very blood."
    "The symbols ignite, faint at first, then brighter, as though the chamber itself remembers its purpose."
    mo "Place your hand here, Libitina. Feel the words. Do not fear them."
    "She steps closer, hesitation lingering in her breath."
    "Slowly, she presses her palm to the stone beside mine."
    scene bg CaveText
    with flash
    "Suddenly the wall splits."
    "Light spills forth, pale and shifting, a wound in the air where stone once stood."
    show libitina base regalia lsur night at t11
    l "...Father, it’s real."
    mo "More real than anything we have known."
    pause 1.5
    mo "This is our passage."
    mo "Our reckoning."
    mo "Beyond this rift, the vessels await."
    scene white with Dissolve(6.0)
    "The light of the portal washes over us, painting the chamber in ghostly hues."
    "The cave groans as if resisting, yet the path holds open, beckoning."
    "I look to my beloved daughter, for the last time."
    mo "Once we step through, there is no return."
    mo "Do you understand?"
    mo "No matter what happens."
    mo "We survive."
    mo "Do whatever it takes to restore Blackbriar."
    l "I understand."
    l "If it means the kingdom lives again... I will follow you."
    mo "...Then let us begin."
    "Together, we step into the rift."
    "The cavern vanishes, swallowed in white."
    "And with it, the last memory of Blackbriar falls away.."
    scene black
    with dissolve_scene_full
    stop music fadeout 2.0
    stop sfx fadeout 2.0


    return
