init python:
    renpy.music.register_channel("ambient", "ambient", True)
label Act1:
    scene bg morvaynsroom
    with dissolve
    with flash
    pause 0.1
    play ambient muffled_rain_interior fadein 1.0
    "Silence lingers, broken only by the faint crackle of a dying fire" 
    "I’ve never been fond of silence, but moments alone have their weight" 
    "Ruling over thousands wears even the strongest down" 
    "Mm, maybe I should play a record."  
    # TODO: import sounds from drive
    play sound vinyl_1600
    play music heartshapedbox fadein 2.0
    queue sound male_sigh
    "Better."
    play sound faint_footsteps_int fadein 1.0
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
    g "Sire, forgive the intrusion. I bring troubling news." 
    mo "Another matter demanding my judgment?" 
    g "It is troubling, sire. The people are losing their magic one by one." 
    pause 1.0
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
    pause 1.25
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
    play sound male_sigh
    pause 1.5
    "I sigh quietly, alone once more." 
    "A ruler cannot falter, not for them, not even for himself."
    "This must be fixed. I will fix it." 

    scene black
    with dissolve_scene_full
    stop music fadeout 2.0
    stop ambient fadeout 2.0
    pause
    "3 Days Later"
    scene bg EntLibitinaRoom
    with dissolve
    play ambient crackling_fire fadein 2.0
    # play music  fadein 2.0
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

    show l base neut regalia at t11
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

    play sound door_opening
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

    pause 1.5

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
    scene bg CalmVillage 
    show fog
    with dissolve
    play music kingmorvayn fadein 2.0
    play ambient wind_fog fadein 2.0
    show libitina base neut regalia evening at t31

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

    scene black with Dissolve(3.0)
    "She nods, silently, gripping the railing."
    "I can feel her tension, tight as a wire, matching mine step for step as we finally reach the top."

    scene bg Railing
    show fog
    with dissolve_scene_full

    mo "Eyes forward. Watch the stairs."
    mo "Watch the shadows. We wait until we know exactly what we’re facing."

    l "I’m right here, Father."

    mo "Good. That’s all I need."

    pause 0.75

    stop music fadeout 1.5
    scene black with dissolve
    scene bg Railing
    show fog 
    with dissolve

    "A couple hours have passed since Libitina and I stepped out onto the railing."
    "The fog hasn’t lifted at all."
    "But that’s the least of our worries."
    "They could strike at any given moment."
    "But throughout all the worry, we’ve stayed low, our eyes on the kingdom below."

    scene black with dissolve_sceen_full

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

    play sound faint_footsteps_int

    # FAST SLIDE to Morvayns Territory (outdoor)
    scene bg MorvaynsTerritory
    show fog
    with wipeleft_scene

    # (you can show lib sprites now - just not on railings or black/white screens)
    show goro base neut evening at t11
    goro "Morvayn, Libitina!"
    goro "I’ve been looking for you. Thought I’d find you here."
    goro "Today has been… rough. But we’ll get through it. We always do."

    mo "Damn straight, Goro."
    mo "How have you been holding up through everything?"

    goro "Ah… I’ve been—"

    # TODO - Zooms In To Goro's Forehead
    play sound goro_gunshot
    # TODO - show screen shake
    play ambient war_sounds fadein 3.0
    play sound collapse

    "Suddenly his head snaps back."
    "He collapses onto the steps."
    "Blood stains the stairs instantly."

    play music sweet666 fadein 2.0

    mo "What the fuck!"
    mo "Libitina, run back up the steps!"

    "We sprint up the stairs instantly, blocking the enemy’s shots."

    scene black with Dissolve(0.5)
    "They’ve finally struck, and this is their way of saying hello."
    "God, Goro…"
    "I’ll sulk later."
    "I have a kingdom I need to protect."
    "The fog hides them, whoever they are."

    # Fast Slide to Railing (do not show libitina sprites)
    scene bg Railing
    show fog
    with wipeleft_scene

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
    scene bg ArmedGuards
    show fog
    with dissolve_scene_full

    "Their armor, their stance…"
    "They aren’t here to talk."
    "I can feel the weight of their weapons from here. They’re coming for blood."

    # FAST SLIDE back to Railing (do not show lib sprites)
    scene bg Railing
    show fog
    with wipeleft_scene

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
    scene bg MorvaynsTerritory
    show fog
    with wipeleft_scene

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
    stop ambient fadeout 1.5

    # Slide to Morvayns Room (indoor)
    scene bg morvaynsroom
    with wipeleft_scene
    play sound "sfx_muffled_rain.ogg"
    # This is a png file! play ambient "ambience_muffled_war.ogg"

    # NARRATION: Sfx: Door Opening
    play sound door_opening
    "I fling open the door to my territory."
    "We immediately run to the shelves."

    pause 0.75
    scene bg MorvaynsRoomZoom
    with Dissolve(0.75)
    "W-What?"
    "The shelves should be lined with weapons, old but reliable."
    "But… nothing."

    stop music fadeout 1.5
    "Every gun is gone."
    "Not a single sword or dagger left untouched."
    "The bastards knew exactly what to take."
    "I grip the edge of the nearest shelf, trying not to show panic."
    "Every heartbeat thrums in my chest like a drum."

    scene bg morvaynsroom
    with Dissolve(0.75)
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

    play music nothingelse fadein 1.5
    show libitina base conc regalia at t11
    l "I’ll stay with you, Father. I’ll do it."

    mo "Together. Always together."
    mo "Now, let’s make this count."
    mo "Once we’re out there, we hit the railing and draw every ounce of power we’ve got left."

    l "O-Okay…"

    "We step out into the storm, and make a run for it."

    # longer slide to Railing (outdoor)
    scene bg War Railing
    show fog
    with wipeleft_full

    "We eventually reach the railing, ducking and dodging every shot that came our way."

    mo "Do you see them, Libitina?"

    l "Y-Yes."
    l "Let’s finish what they started."

    mo "Damn right we will."

    # Fast Fade In - BG: Armed Soldier (outdoor)
    scene bg ArmedSoldier
    show fog
    with Dissolve(0.75)

    # Visuals: Screen sways back and forth if possible
    #TODO: Scarlet, can you make the screen shake here?
    "My eyes dart to the soldiers, gunning down innocent mages."
    "Magic hums weakly in my veins, barely enough to hold a spark."
    "I draw in a shaky breath, preparing to push the last of it into one strike."

    mo "Let’s see what you’ve got."

    "I thrust my hands forward, pouring every ounce of remaining power into a single hit."

    play sound small_whimper
    play sound falter

    "The air cracks with energy. A guard nearest to me goes flying, slamming against the stone floor."
    
    # Armed Guards #1 (outdoor)
    scene bg ArmedGuards
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

    play sound goro_gunshot
    show screen shake
    "Before I can react, a shot tears through the air, grazing my shoulder."

    "Pain flares, sharp and burning, but I grit my teeth and push through it."

    # Fast slide to Railing (do not show libitina sprites on railing)
    scene bg WarRailing
    show fog
    with wipeleft_scene

    mo "Lib! Downstairs! Now! I’ll meet you there!"

    "Libitina hesitates for a split second, fear written across her face."
    "I grab her arm, yanking her toward the stairs. Every step is a gamble."
    "The storm howls around us, mixing with gunfire and desperate screams."
    "I know if I stay too long, we both die."
    "Every ounce of strength in my body focuses on keeping her alive."

    mo "Move, Libitina! Don’t stop!"

    "As she vanishes down the stairs, the last sparks of magic curl around my hands, fading fast."
    "Suddenly, a thought I’ve shoved to the back of my mind for years hits me."

    pause 1.5

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
    scene bg Away_Path
    show fog
    with slide

    play sound running_1600

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
    show libitina base lsca regalia evening at t11

    "We make a break for the trees."

    scene bg forest_1600
    show fog
    with fade

    # TODO: Sort out the mess that is the sounds
    play ambience war_sounds volume 0.5 
    play sound branches

    "Branches tear at our faces the moment we hit the forest."
    "I hear them behind us."
    "Shouts. Orders barked over the chaos."
    "I let out a shaky sigh."

    pause 0.75
    play sound male_sigh

    "The forest swallows the sounds, thick and foggy."
    "For a few precious seconds, the world holds its breath."
    "Just enough for us to catch a heartbeat."

    play sound female_sigh

    show libitina base worr regalia evening at t11
    l "Maybe… maybe we’re safe…"

    pause 0.75

    show libitina base lsca regalia evening at t11
    "She presses close, trembling."
    "I grip her hand tighter, feeling her pulse race against mine."

    pause 0.75

    "But, I should know better. Safety is an illusion, in our circumstances."
    "The moment we stop, even if only for a second, the world will find us again."

    play music nothingelse fadein 2.0
    play sound faint_footsteps_ext fadein 0.5

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

    play sound running_1600
    pause 0.5
    # Gunshots and screen shakes
    play sound goro_gunshot
    show screen shake
    pause 0.3
    play sound goro_gunshot
    show screen shake
    pause 0.5
    play sound goro_gunshot
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
    play sound slast

    "My throat opens in a single, straight cut."

    # Visuals: blood fades in

    "Hot blood surges, and burns, as my vision tilts."

    play sound collapse

    # Black screen with blood overlay
    scene black
    with fade

    "The enemy freezes."
    "Silence hangs for the briefest second before panic hits them."

    pause 2.5
    play sound the_king_is_dead_voice

    "They have no idea."
    "They think we’ve lost."
    "They think the king is dead."
    "But I’m not. Not yet. Not even close."

    stop music fadeout 2.0
    stop ambience fadeout 2.0

    # Slow fade in with white flash
    scene bg fire_village
    show fog
    show eff_rain_r
    with fade

    play sound gasp
    pause 1.5
    play sound wind
    play ambient rain_ext
    # Rain effect + fog overlay

    "I wake, startled to find myself still alive, as if death itself miscalculated."
    "I-I’m not in my bed. Not in my body."
    "This thing I’m in is stiff, wrong, brittle."
    "Someone else’s skin, someone else’s bones."

    pause 1.5
    "Huh? That’s unpleasant."
    "Not the grandest entrance back to life, I’ll say that."

    pause 2.5
    play music "where_did_you_sleep_cover.ogg" fadein 2.0

    "Heh.."
    "This."
    "This is the cost."
    "The body dies, but the mind endures."
    "I have cheated death, but life has not cheated me."
    "It tried."
    "God knows it tried. But I’m still here."
    "My mind snaps to Libatina."
    "Confident, and brave."
    "She pushes forward."
    "Alive."

    mo "She’s fine."
    mo "I did what had to be done."

    "I rise on unsteady legs, nearly falling over in the process."

    pause 1.5
    "They think the king is dead."
    "Ha. Let them celebrate. Let them dance on the ashes like fools."
    "They think they’ve won. They think this ruin is theirs."
    "They do not know."
    "They do not know the ruler still breathes."
    "That I remain."
    "That the game is far from over."
    "Their path leads to the forest."
    "I must move fast. Every second counts. Every moment I hesitate is a moment wasted."

    # Fast fade in/out to Fire Path (outdoor)
    scene bg fire_path
    show fog
    with fade

    "I take a step forward, then another."
    "My limbs complain, my bones protest, but I don’t care."
    "Each step, each breath, each heartbeat… proof."
    "Proof that death can be cheated. Proof that the impossible is real."
    "That we still have strength even without power."

    pa "The king is dead… but the ruler? The ruler lives. Alive, angry, and ready."
    pa "Bound by fog, cloaked in the shadows."
    pa "I will find her."
    pa "She will not be left behind. Not today, not ever."
    pa "I will rebuild. I will fight."
    pa "Even if it takes 100 years.."
    pa "I will rise from this chaos, and they will learn who they just tried to destroy."

    # Slow fade out
    stop music fadeout 3.0
    stop ambient fadeout 2.0

    # Title card
    scene black with fade
    show text "Nearly a Century Later" with dissolve
    pause 2.0
    scene black with fade

    # Fade in game with white flash
    scene bg forest_1700
    show fog
    with fade

    play ambient wind
    #play music walkingforest

    pause 1.5

    pa "Hey, Lib?"
    pa "How are you holding up? Are you still hungry?"

    show libitina base unim regalia evening at t11
    l "Not for a dead squirrel."

    pa "Heh, Figures. Not exactly a five-star meal, but.."
    pa "I’ve eaten worse."
    pa "We both have.."

    show libitina at thide
    hide libitina 

    pause 1.5
    "For nearly a hundred years, it’s been the exact same damn thing."
    "A hundred years in this stolen body, and it still groans as if it hates me."

    pause 1.5
    "This spell isn’t pretty. It could ruin everything you were."
    "Once you slip into someone else’s flesh, you get more than just their body."
    "You inherit almost everything. Their memories, their habits, their dumb mistakes, their flaws."
    "Every prideful moment, every selfish impulse. All of it sticks like gum you can’t scrape off."
    "Prince Ale, for instance."
    "I wear his flesh, but it’s more than that."
    "His arrogance, his greed, his spectacularly poor decisions. Yeah, all of that is in me now. Fun, right?"
    "I won’t claim to be perfect, or the most charming guy, but this borrowed vessel definitely leans more toward the downside."
    "At least I came out human. Better than some poor earlobe clinging towards the corner of my mouth."
    "Even though we’ve spent a century together, my daughter still flinches at the sight of this borrowed body."
    "Even worse, those soldiers never let up on us."
    "We’ve been weak, and running, ever since our kingdom fell."
    "We’ve slept anywhere the world wouldn’t bother to touch us."
    "Caves, ruins, riverbanks, a hollowed tree or two when we got desperate."
    "Anywhere the fog couldn’t reach."
    "Rain, snow, hunger, fire."
    "We survived, just barely."
    "Libatina grew up in the middle of all this."
    "I tried to shield her, but she saw enough to understand everything."
    "She used to cling to me, scared of every shadow. Now she moves ahead like she’s the one keeping me alive."
    "I swear, sometimes she is braver than any of the bastards hunting us."
    "Every settlement we reach, Kingdom Mekus feels farther away."
    "Every night without danger feels like a trick. Like the world’s just catching its breath before it comes for us again."
    "Sometimes I wonder if we’re chasing a kingdom that doesn’t even exist anymore."
    "And yet, we still move. Step by step, shadow to shadow, year to year."
    "Even now, we’re trudging through the woods with a damn dead squirrel in hand!"
    "Not exactly a feast, but it will keep us alive. For now, at least."
    "Luckily, we’ve landed somewhere that isn’t trying to kill us, for now anyway."
    "I glance around, scanning the shadows, making sure nothing follows too closely."
    "I wouldn't want another 1600 situation.."

    pause 1.5
    "Clear."
    "I gesture to Libatina, pointing toward the open stretch of forest just ahead."
    "She nods, her eyes steady, and together we slip into the shelter of the trees, carefully."
    stop music fadeout 2.0
    # Medium slide to fiery forest
    scene bg fiery_forest_1700
    show fog
    with wipeleft_scene

    play music crackling_fire fadein 1.0
    # Sprite hue: reddish firey

    "We settle into the small forest. It’s quiet and empty. Just what we needed."
    "Our dinner hisses over the flames."
    "Rest easy, squirrel. This is messy, I know."

    show libitina base worr regalia fire at t11
    l "…Father?"

    pa "Mm?"

    l "You haven’t said a word in an hour."

    pa "I’m enjoying it. No one’s trying to stab me, and the fire’s been crackling for a while now."

    "A few glowing embers from that dead tree, some dry moss, a little coaxing, and here we are."

    pa "Flames don’t obey easily, but tonight they’re ours."

    l "You mean you just scraped sparks together?"

    pa "Heh. Something like that. Nothing super fancy, just enough to keep us alive tonight."

    l "…Father."

    pa "Eat first. Then talk. Don’t wear yourself out before you’ve even had a bite."

    l "I’m not—"

    pa "Libatina. You’ve been scraping by on scraps. You eat now or I carry you tomorrow."
    pa "And you know, you’re too old for that."

    l "…Fine."

    "She takes a bite."

    pa "Good. Now that’s a survivor."

    pause 2.0

    l "…Father, how long is this supposed to go on?"
    l "Hiding, moving, running for a hundred years."
    l "When does it all end?"

    "That question again."
    "Dammit."
    "But this time… she’s not angry?"
    "It seems like she’s more afraid of the answer."

    play sound male_sigh
    pa "Libatina, listen carefully."

    l "…I’m listening."

    pa "This isn’t forever. We weren’t made to rot in the shadows."
    pa "I was a king once."
    pa "Ruling over thousands. Do you think that happened by accident?"
    pa "Short answer, It did not."
    pa "One day it’ll come."
    pa "One day, we will go back, Libatina."

    l "To the kingdom?"

    pa "Yes."

    l "After everything? With what army? What allies? What strength?"

    pa "All of that can be rebuilt."
    pa "We just need to survive long enough to gather it."

    l "And if we don’t? If every kingdom drives us away?"

    pa "Then we keep collecting what we can. Supplies. Knowledge. Secrets. Opportunities."
    pa "They always come. Even if it takes a century."
    pa "Everything happens for a reason, Libatina."

    l "A century has already passed."

    pa "And yet, here we are. Not dead. Not defeated. Just… delayed."

    "She stares into the fire. Taking it all in at once."

    l "…You really think we can get it back?"

    pa "I don’t think."
    pa "I know."

    l "How?"

    pa "The same way we survived this long.."
    pa "Step by step. We gather strength, rebuild magic, understand the prophecy."
    pa "And when the world gets careless?"
    pa "We strike."

    l "You make it sound so simple."

    pa "Heh, It won’t be."
    pa "But we’ll do it anyway."

    l "…Why are you so sure?"

    pa "Because they tried to erase us. And we’re still here."

    "She eats again. Really eats this time."
    "Her shoulders ease, just slightly."

    l "…I just want a home, Father."
    l "And I know that you do too."

    pa "And we’ll have one. I promise you."
    pa "Even if it takes one hundred more years."

    l "You’ve promised that for so long."
    l "I’m not saying I don’t trust you, it’s just that…"

    pa "And I’ve kept you alive all those years. That counts for something, doesn’t it?"

    l "…Yeah. It does."
    l "I apologize, Father."

    "She inches closer to the fire. Not comforted, but grounded."
    "Older. Mature. But still my daughter."

    l "I’ll keep walking with you, no matter what happens."

    pa "Good. Now eat."
    pa "Finish your meal before the fire dies."

    l "You’re bossy tonight."

    pa "Someone has to keep you from wasting away into nothing."

    l "…You’re impossible sometimes."

    mo "Thank you. I try."

    play sound dying_fire
    stop music fadeout 1.0
    
    # Scene: 1700 Path (outdoor)
    scene bg path_1700
    show fog
    with fade
    # Sprite hue: greyish rainyish-blue

    pa "Welp… guess we gotta keep walking."
    pa "And that’s our dinner for tonight."
    pa "Maybe we’ll find a rabbit soon enough."

    show libitina base amus regalia evening at t11
    l "Heh, I'm not sure I’ll live that long if all I eat is dead critters."

    pa "Like I always tell you. Eat fast when you get the chance."
    pa "Even if the main course isn’t exactly ideal.."
    pa "Now come on, we gotta get moving."

    "Our walk back begins, boots sinking into mud, the fog hiding the forest around us."

    # Fade in/out to path
    scene black
    with fade
    scene bg path_1700
    show fog
    with fade

    "We’ve been trudging through this weird, unfamiliar path for longer than I’d like to admit."

    play sound male_sigh

    pa "Never gets old, does it?"

    show libitina base upse regalia evening at t11
    l "Not for you, apparently."
    l "Me? I’m this close to keeling over."
    l "You know, Father, what if we find a village? Or people?"
    l "Someone who lives close to here?"

    pa "It’s possible."
    pa "I mean, we would have more soldiers. More allies."
    pa "A home.."

    show libitina base worr regalia evening at t11
    l "But I know, not everything’s that simple."
    l "One wrong move, and they could all come back and destroy everything we’ve built."

    pa "Exactly. That’s why we keep our blades ready."

    "The trees begin to thin slowly, letting a hint of light slip through the branches."

    show libitina base vsur regalia evening at t11
    l "W-What the—"
    l "…Father, do you see that?"

    pa "Huh?"

    "Libatina points to the tangled branches."

    play sound branches
    "I push them aside, clearing the way."

    # Dramatic fade to crater
    scene bg 1700Crater
    show fog
    with fade
    pause 2.5
    # Visuals: sway back and forth
    hide libitina

    "What the hell?"
    "The land opens up before us."
    "A vast emptiness stretches across the earth. The ground seems… gone."
    "Like something had torn the world itself apart?"

    pa "I do, though I can’t say what it is."
    pa "I’ve lived long enough to see many things, but never this.."

    "The void seems like it goes on forever. It’s not land, not a pit—just gone?"
    "Black, empty, and deeper than I can wrap my head around."

    show libitina base lsca regalia evening at t11
    l "…It’s like the world just vanished?"

    pa "Or something threw it aside.."
    pa "Either way, this is not natural. Something made this happen. Something deliberate."

    l "…Should we get closer?"

    pa "Yes. But let’s go slowly. Every step we make counts."

    "I draw my knife and brace for whatever’s coming."

    pa "Take your knife out, Libatina."

    "She lifts it from her pocket and sharpens it smoothly."

    pa "Keep your eyes open, and remember to keep your hands ready."
    pa "Something like this… it rarely exists without a reason."

    "We move closer, carefully, both knives in hand."

    pause 1.5
    "Almost there.."

    "We eventually find a narrow section of the edge that feels stable enough to drop down into."

    show libitina base conc regalia evening at t11
    l "…Careful, this edge isn’t exactly forgiving."

    pa "I know. Keep your composure, and your knife ready."

    "Time to drop into this mess and see what’s waiting."

    pause 1.5
    play sound collapse

    show libitina base unsu regalia evening at t11
    l "…I don’t see anything. Just more broken ground?"

    pa "Keep your eyes peeled. The answers aren’t always obvious."

    "Then, a faint crack catches my attention."

    l "…Father, look there."

    "She points to a narrow opening, carved into the void floor itself, almost hidden against the jagged rock."
    "It’s got sharp lines, perfect angles. Not a crack you’d just see in nature. Someone had to have built this."

    pa "Well, finally, something interesting."
    pa "The opening must be right here."

    "I gesture at the crack, then kneel and peer inside, like it’s a peephole in a door."

    pa "It could be a passage. Could be trouble. Doesn’t matter."
    pa "This could be life changing, for us, Lib."
    pa "We’re going down."

    show libitina base vsca regalia evening at t11
    l "What?!"
    l "You’re joking, right?"
    l "That’s a huge drop!"

    pa "Good. The deeper it goes, the more likely it holds answers."
    pa "It’ll be okay, Libatina."
    pa "Just keep your eyes open."

    l "Ah—"
    l "Alright.."

    "We try to drop in carefully, searching for anything solid to land on."

    pa "Libatina, do you see tha—{nw}"
    # Line cuts off fast

    #TODO set textbox "Lib And Morvayn"
    show screen shake
    play sound fall

    us "AHHHHHHH"  #TODO line cuts off when sfx ends

    # Fast cut to black screen
    scene black
    with fade
    play ambient wind
    window show

    "We drop. Hard. The ground smacks us face-first like it’s been waiting all day to do it."
    "For a couple seconds, I can’t see anything."

    pa "Ugh, are you okay, Libatina?"
    l "I-I think so?"

    "I flip over, blinking hard, trying to get my eyes to cooperate."
    # Visuals: blinking effect for 4–5 seconds

    # Slow fade in cave interior (indoor)
    scene bg CaveInterior
    with Dissolve(3.0)

    pa "What the hell?"
    pa "Libatina..Look."

    "Libatina rolls onto her back and lets her eyes feast on this beauty."

    show libitina base vsur regalia green at t11
    l "Oh my—"
    l "…It’s amazing."
    l "It looks almost man-made?"

    pa "Heh, every inch of it does."
    pa "Like it was crafted long before we arrived. And somehow, it’s even more impressive than I would’ve imagined."

    "We rise slowly, brushing off the dirt and forcing ourselves to stay steady."
    "Once we’re on our feet, we start moving carefully through the cave."
    "I scoff subtly under my breath. Maybe she’s the one keeping me alive now."
    "Fast, clever, steady… a lot like her mother used to be. I can't help but admire that."
    "Rounding the corner, my thoughts of her vanish, replaced by something both familiar and gut-punching."

    # Fast slide to cave text
    scene bg CaveText
    with slide

    "The walls are covered in text I can’t quite recognize."
    "But somehow… they feel familiar."
    "Little lines, etched deep, curling like roots, faintly glowing in the dim light."
    "I swear my stomach almost flips."
    "But I can't let my guard down."
    "Libatina freezes beside me, flabbergasted."
    "I glance at her, then back at the text."
    "Holy hell… she’s never looked at anything like this before. Not even in all our years on the run."

    show libitina base conc regalia green at t11
    l "Father… what is this?"
    l "Why does it feel so familiar?"

    "So, it’s not just me.."
    "As I stare longer at the text, a memory claws its way to the surface."
    stop ambient fadeout 2.5
    scene white
    with Dissolve(2.5)
    play ambient ext_day fadein 2.0
    scene bg 1400Flashback
    with fade
    # No fog for this scene

    "The cool air brushed against us on a crisp autumn morning, my grandfather and I standing outside, taking in his territory."
    "I was young then. Too young to understand all the games of kings and thrones."

    g "Morvayn, ever think you might end up sitting where I do one day?"

    ym "Me? No chance. I’m far too weak for that."

    pause 0.75

    g "Listen to me. Strength isn’t just in your arm or your sword."
    g "It’s here."

    "He said, pointing to his head."

    g "Your mind, your courage, your heart. That’s what makes a king."
    g "If there ever comes a time, Morvayn… if you take the crown and the kingdom falls… there will be something waiting for you."
    g "You will know it when it comes. You won’t need signs or warnings. It’ll call to you."
    g "I know you, Morvayn. I know you are strong, even if your mind is still growing into your body."
    g "You’re going to do great things. Don’t doubt it. Even if the world doubts you."

    "I remember the weight of those words pressing against my chest."
    "My mind raced, trying to imagine what it meant to fall, to lose everything I’d been promised."
    "I felt fear, yes, but beneath it, a spark of pride — the thrill of possibility."
    "Could I really do what he said? Could I be strong enough?"
    "Could I survive the world if everything turned against me?"

    ym "I’ll show him. I’ll prove I’m not just a boy."
    ym "I’ll do it all. I’ll make him proud… and no one will ever take this from me."

    "Even in that moment, it all felt… unmistakably clear in some way."
    "He wasn’t scaring me. He was warning me."
    "Hell, he was preparing me."
    "Even now, standing in this cave, staring at these words carved long before we arrived, I feel it all again."

    l "Father… are you okay?"
    stop ambient fadeout 1.0

    # Return to cave text (1700)
    scene bg CaveText
    with fade
    # White slow flash + blinking visuals
    play ambient wind fadein 2.0

    "I blink, shaking myself from the memory."

    pa "Heh, heh."
    pa "We’ve found it, Libatina. Just like he said we would."

    "And for the first time in a long time, I allow myself a small genuine smirk."

    l "F-Found what?"
    l "You can’t just say that and leave me hanging."

    pa "Libatina… this… all of this."

    "I point at the walls, letting my hand linger over the carved text."

    pa "It’s exactly what my grandfather warned me about. He said if the kingdom ever fell, there would be something waiting. Something meant for me to find."
    pa "He must have left it here for me. For us."
    pa "He knew the world would turn upside down, and he wanted us to have a guide… a way to understand what comes next."

    l "Wait… he knew?!"

    "I nod slowly, letting the weight of it sink in."

    pa "We’re here. We survived. And now… we’re standing at the edge of something bigger than either of us."
    pa "Something he promised. Something we’re meant to face."
    pa "We need to know what this means, Libatina. No guessing, no waiting around."
    pa "Days, weeks, even years if that’s what it takes. I don’t care how long we have to stay."
    pa "So be it. We endure, we survive, and we uncover every secret hidden here."
    pa "We will find out. Mark my words, nothing stays buried forever."

    l "Don’t panic, Father. You won’t do it alone."

    pa "Good. That’s exactly why I keep you close, Libatina."
    pa "I don’t care what waits down here. Together, we’ll face it."

    "For a moment, we just stand there, letting it all sink in."
    "Something tells me things are about to change."

    l "Then let’s see it through. Step by step."

    pa "Step by step,"

    "I echo, a smug smile tugging at my lips."

    l "Come on, Libatina. Let’s move."

    # Fade out cave text
    stop music fadeout 2.0
    stop ambient fadeout 2.0
    scene black
    with dissolve_scene_full

# Title Card
    scene black
    with fade
    show text "Three Years Later – 1702" with dissolve
    pause 2.0

    # Fade in with white flash
    scene bg CaveInterior
    with fade
    play ambient wind

    "Three years."
    "That is how long these stone walls have been in our lives."
    "Ya know, when we first stumbled in, all we had were cold floors, empty corners, and a wall creepy enough to make a grown man reconsider his life choices."
    "We had no idea what it once was."
    "Frankly, we still don’t."
    "But it was shelter, and when you are running for your life, you do not get picky."
    "So we made it ours."
    "We hammered together beds from whatever wood we could drag inside."
    "They were crooked, squeaky, and unstable, but they kept our backs off the floor."
    "We built a table that somehow still stands even though Libatina leaned on it once and nearly sent it to the afterlife."
    "We stacked shelves out of loose stones and filled them with anything that looked remotely useful."
    "Books, scrolls, paper."
    "Most of it was nonsense."
    "Some of it was frankly, a little dangerous."
    "But that little bit changed everything."
    "Those old symbols became our routine."
    "I would translate until my eyes blurred, and Libatina would read them back to me until her voice cracked."
    "Strange how that became our normal, huh?"
    "Even with all hell on our tails, running didn’t sting as much here."
    "Yeah, we still had to scrounge for food, water, scraps to keep breathing."
    "But we had a home. A proper little lair of our own."
    "A spot to drop when the world got loud, heavy, or downright ridiculous."
    "And you know what? For the first time in forever, that felt like victory."
    "And Libatina."
    "She has grown into someone stronger than I ever expected."
    "More, and more like her mother, heh."
    "The kind of presence that keeps a man from falling apart."
    "And meanwhile, the world outside kept trying to kill us."
    "Wild beasts, starving thieves, soldiers who still think we are worth chasing after all these years."
    "But, none of it stopped us."
    "Three years of this."
    "Three years of fighting, learning, and refusing to disappear."
    "And now, finally, the words carved into these walls have opened themselves to me."
    "The meaning is real."
    "Solid."
    "Dangerous, even."
    "And I have spent half my life preparing for it without even realizing."
    "My grandfather spent years casting blessings over me, rituals I never understood."
    "Back then, I thought it was all superstition."
    "Just traditions he clung to because he was old, proud and stubborn."
    "But now…"
    "Now I see it."
    "The old man was preparing me for this."
    "For here."
    "For today."
    "And I am fucking ready."
    "After three years, the texts have revealed their truth, and it is time I tell Libatina."
    "It is time we go."
    "To Earth…"

    "I round the corner of our home, stepping into the living room we’ve cobbled together over three long years."

    # Cave Text (1702)
    scene bg CaveText
    with fade

    "I sink into the desk I’ve been buried at for the last two years, every scrap of work piled around me."

    pa "Libatina… sit with me for a moment."

    show libitina base conc regalia green at t11
    l "What’s going on?"
    l "You seem a little tense."

    "I hesitate. Two years of nonstop work, and it’s finally done. How the hell do I even begin to explain this?"

    pa "Heh, i-it’s time."
    pa "Time we do what we were destined to do from the beginning."

    pause 0.75

    l "Do you mean… is it finally happening? Are we finally going to..?"

    pa "Yes. All these years of study, of surviving, of chasing these symbols… it leads here."
    pa "All those protections, blessings, rituals my Grandfather set up… I didn’t understand them then.."
    pa "But now, Libatina… I do. And it all makes sense."

    l "You mean… you’re really going to do it? The spell?"
    l "The one we’ve been speaking about?"
    l "The….p-portal?"
    l "Is that what it’s called?"

    pa "Yes, that’s it."
    pa "But I can't do it alone."

    l "W-What?"

    pa "You are the key, Libatina."
    pa "It’s what I recently just figured out."
    pa "The blood that binds us… the line that carries this magic forward."
    pa "I can open the passage, but I cannot force it. Not without you."
    pa "Step by step, Libatina. Like we’ve always done."
    pa "Step by step, we survive. Step by step, we reclaim everything."

    l "Help me understand."

    pa "The first path… is a doorway to another world."
    pa "Heh, a portal as you like to call it."
    pa "A place where power waits, where our people’s strength endures."
    pa "A place called earth."
    pa "We are not going just to look, not to explore, not to wander."
    pa "We are going down to claim bodies."

    show libitina base vsur regalia at t11
    l "W-What?!"

    "Shit… Prince, way to drop that on her out of nowhere."

    pa "I-I didn’t stutter."
    pa "Dead bodies.."
    pa "Every vessel we find will give us power… strength… the kind of growth most people only dream of."
    pa "Each life we step into makes us sharper, stronger, more capable than before."

    l "Wait—so we’re going to… inhabit the dead?"
    l "Just like you did all those years ago?"

    pa "Exactly. But don’t think this is simple. This isn’t just a second life to scrape by."
    pa "The spell I used all those years ago—the one that saved me.."
    pa "It's built on that foundation. Only now it’s refined, perfected."
    pa "We can cast it as many times as we need… but only if there is a body waiting for us, nearby."

    l "So… every body, every vessel, it makes us stronger? More powerful?"

    pa "Yes. Each vessel amplifies our magic and tightens our control."
    pa "Some bodies will be weak, barely worth the effort. Others… rare ones, will be nearly perfect."
    pa "And the final one, the vessel we are destined to find, will give us strength beyond anything our line has touched."

    l "And if, there’s no body nearby?"

    pa "Then the spell fails. Completely."
    pa "Our power drains to nothing and we are stranded, helpless."
    pa "No chance of cheating death."
    pa "Every plan, every sacrifice, gone."
    pa "That is why we choose carefully. Patiently. The right vessels aren’t just important—they are everything."

    l "This is unbelievable, but it’s incredible!"

    pa "And this is only the beginning. Each vessel we take brings us closer."
    pa "We learn. We evolve. Until the destined one finally appears."

    l "I understand, but if I may ask. Why do we need to find these vessels? What is the ultimate goal here?"

    pa "Well, once we find that perfect vessel, our strength will be complete."
    pa "Not just enough to survive or to wander from body to body… but enough to revive an entire kingdom."
    pa "All of Kingdom Mekus. Every soul. Every life taken. Every voice silenced."
    pa "It’s all in our hands now.."

    l "You mean… bring them back? All of them?"

    pa "Yes. Every last one."
    pa "Once we reach the perfect vessel, we will have the power to return them to us."
    pa "To rebuild what was lost. To make Blackbriar whole again."
    pa "No more hiding. No more running. Just… home."
    pa "A real home, again."

    l "That sounds… impossible."

    pa "Haah, it should be. But it isn’t. Not for us. Not anymore."

    l "And all of this. All the vessels, all the steps… it’s for that?"

    pa "It’s for the greater good."
    pa "Our people deserve to live again. To stand in sunlight, to laugh, to thrive."
    pa "And if that means we must do things that are… unpleasant… then so be it."

    l "How unpleasant?"

    pa "We may have to take bodies by force. We may have to kill."
    pa "We may have to kill innocent people."
    pa "We may leave behind chaos in the wake of our purpose."
    pa "But every choice, every action, every sacrifice... leads us to one outcome."

    l "The rebirth of Mekus."

    pa "Yes. Our people would be restored. Our kingdom alive again."
    pa "Just a few small steps, and we no longer have to live like animals anymore."
    pa "Our legacy is no longer buried under centuries of dust."
    pa "And one day, they will thank us for the lengths we went to bring them home."

    "She stands there, eyes full of both fear and thrill."

    show libitina base lsur regalia at t11
    l "T-Then let’s do whatever it takes!"

    pa "Together. Always."
    pa "You ready to kick this off?"

    pa "I grab her hand and squeeze it tightly."
    pa "God, this is really it. No turning back."
    pa "So long, Blackbriar…"
    pa "I’ll see you in another lifetime."

    pa "Ready, Libatina?"

    show libitina base plea regalia at t11
    l "I’ll see you on Earth~"

    # Fade out with slow white flash
    scene white
    with Dissolve(3.0)
    # Everything fades out
    stop music fadeout 3.0
    stop sound fadeout 3.0
    stop ambience fadeout 3.0




    return
