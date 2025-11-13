init python:
    renpy.music.register_channel("ambient", "ambient", True)
label Act1:
    scene bg morvaynsroom
    with dissolve
    play music "mod_assets/music/King Morvayn.ogg"
    with flash
    pause 0.1
    play sound "mod_assets/sfx/Dying Fire.ogg"

    "Silence lingers, broken only by the faint crackle of a dying fire."

    #show morvayn neut at t11
    mo "I’ve never been fond of silence, but even I can appreciate a moment’s peace alone."
    mo "Ruling over thousands can wear even a king down in time."

    #play sound "footsteps_soft.ogg"
    "I hear footsteps behind me, approaching softly."
    "I don’t need to turn. The rhythm of those steps is familiar."
    "An adviser, Goro. He always walks like he’s afraid of waking ghosts."
    "I scoff. Though if anyone here should fear the dead, it’s me."

    show goro neut fire at t21
    "Goro pauses at my side, head bowed in respect."

    g "Sire, forgive the intrusion. But I bring troubling news."

    mo "Another matter requiring my judgment?"

    "A faint breath escapes me, tinged with a weary laugh."

    mo "Tell me, Goro... Does a ruler ever truly rest?"

    g "I fear not, King Morvayn. Not while the kingdom still breathes."

    mo "...I thought as much. Speak."

    show goro conc
    g "It is the people."
    g "One by one, they are losing their magic."
    g "Spells are failing. Rituals collapsed."
    g "Folks conjured sparks yesterday—today, nothing."

    "His hands shake as he speaks, though he bows to hide it. His fear is obvious."
    "Although my chest tightens, I do not allow it to show."
    "A leader cannot. Not now."

    mo "You’re certain? None remain untouched?"

    show goro neut
    g "A few sparks remain, but weak. Fading quickly. It spreads like a sickness, sire."

    "I avert my eyes."
    "A powerless kingdom... Warlocks and witches with nothing but their frail bodies."
    "We must not have this."
    "Fear wants to take root in me, but calm is a weapon too."
    "Even if it feels like a lie, it must be spoken."

    mo "Goro, I need you to gather the healers."
    mo "Summon every mage who can still conjure so much as a flame."
    mo "Search the archives. I want answers, and I want them quickly."

    show goro e2
    g "Yes, sire. At once."

    mo "Once that’s done, I’ll take a gander at it myself."
    mo "Carry on now."

    "He bows deeply and retreats, leaving me alone once more, on the sofa."
    hide goro
    "I pull myself upright."
    "A ruler cannot falter. Not in front of them. Not even in front of myself."
    "This must be fixed."
    "I know I can do it."
    scene black
    with dissolve
    stop music fadeout 2.0
    pause
    "3 Days Later"
    scene bg EntLibitinaRoom
    with dissolve
    play sound "mod_assets/sfx/crackling fire.ogg"
    play ambient "mod_assets/ambience/int_day.ogg"
    pause

    "It’s been about two minutes since I stopped in front of Libitina’s cracked door."
    "The wood is splintered at the hinges. I should have had it repaired weeks ago."
    "I just never found the time."
    "And with the way things are, I might as well not ever have the time."

    "For three days now, the wind has felt different."
    "Every morning is colder than the last."
    "Every night feels longer, and heavier."
    "Three days ago, the sky was still clear."
    "The air had that spark of early autumn, cool but full of promise."
    "A promise for a successful winter."

    "But then, my men began to falter."
    "Just like Goro said they would."
    "At first, it was small things, just like he said."
    "A spell that fizzled. A torch that refused to light."
    "Then suddenly, it was nothing. The glow in their palms, the color in their eyes, gone."

    "I told myself it was fatigue."
    "I told myself it would pass."
    "I told myself not to speak of it, not to give it power by saying it out loud."
    "Maybe I just didn’t want to see fear reflected back at me."
    mo "Fuck."
    "I didn’t even tell Libitina."
    "She would ask questions, and she deserves answers I don’t have."
    "She would’ve asked ‘who caused this?’ Or ‘why is this happening?’"
    "And I have no goddamn clue!"

    "So I decided to stay quiet. Pretended it was under control."
    "Pretended I was still the man who could fix things, just like he always has."
    "But silence doesn’t stop decay."
    "You can only hide the rot for so long before the smell gives you away."

    pause 0.5
    "She knows something is wrong. I can feel it."
    "I don’t know what words will come when I open that door."
    "But she deserves the truth."
    "And if I can’t give her hope, then I can at least give her honesty."

    play sound "mod_assets/sfx/door opening.ogg"
    scene bg LibitinaRoom with dissolve

    "I gently open the door."
    "Libitina sits on the floor, legs crossed, and looking down."
    "The wind from the door blows to her, causing her to flinch slightly."
    "I step inside slowly, careful not to break the quiet of the room too much."

    #show morvayn neutral at center
    mo "Libitina, there is something I must tell you."

    show libitina base neut fire at t31
    with dissolve
    "She turns, startled at the sound of my voice breaking the calm."

    show libitina vsur
    l "What is it, Father?"
    show libitina worr
    l "You look pale..."

    mo "I—"
    mo "There’s no easy way to say this..."
    mo "The people, they are losing their magic."
    mo "One by one, their power is fading."

    show libitina neut2 mouth_b
    "Her lips part, a soft gasp catching in her chest."
    "One hand rises instinctively to her heart, pressing there as though steadying herself."

    show libitina sad
    l "Father..."
    l "Without magic, what will we have left?"

    show libitina worr
    mo "We have our people, Lib."
    mo "And we have me."

    "Her eyes search mine, seeking certainty, trying to draw it from the calm in my voice."
    "I meet her gaze, placing a hand lightly on her shoulder, the weight of it grounding both of us."

    show libitina amus
    mo "It is heavy, yes. But we have faced worse burdens."
    mo "And we will carry this one together."

    show libitina sad
    l "I trust you, Father, but it still feels heavy."

    show libitina worr
    "Her fingers curl slightly at her sides."
    "She does not hide it fully."

    show libitina sad
    "I squeeze her shoulder once, firm but gentle, a silent promise that she will not face this alone."

    mo "Then we carry it together. Let us not waste these last moments of calm."
    mo "We will be okay for now. Come with me."
    mo "We will breathe the air while we can."
    mo "And take action when we need to."

    show libitina happ
    l "Yes, Father."

    hide morvayn
    stop sound fadeout 2.0
    scene black with dissolve
    scene bg Village with dissolve
    play music "mod_assets/music/King Morvayn.ogg"
    play ambient "mod_assets/ambience/ext_day.ogg"
    show libitina base neut dusk at t31

    "She steps forward, and together we walk toward the door."
    "The breeze blows lightly on the edges of her dress."
    "The soft echo of our footsteps stretches down the corridor."
    "Servants move quietly, carrying messages and scrolls, their murmurs floating faintly as they walk."

    scene black with fade
    pause 0.2
    scene bg Village with fade
    show libitina base neut dusk at t31
    "A couple of hours pass."
    "The two of us are taking in the cool breeze."
    "The kingdom breathes around us, unaware of the storm bound to happen."

    show libitina amus
    l "Father, look."

    "Her finger points to a space beyond the fields."
    hide libitina with dissolve

    "At first, my eyes catch only shadows moving between the trees."

    stop music fadeout 2.0
    play ambient "mod_assets/ambience/war sounds.ogg"

    scene bg Guards1 with fade
    "But slowly, as I focus, the shapes become clear."
    "Soldiers, mages, battlemages—an army moving with purpose, unrelenting."
    "A kingdom that clearly isn’t our own."

    mo "The curse was not a chance. It was preparation."
    mo "Damn it, how could I have been so careless?"
    mo "Our enemies chose their moment. And now, they come."

    show libitina base worr at t31 with dissolve
    l "T-They caused this?"

    show libitina worr
    mo "I’m sure of it."
    mo "Just..."
    mo "Stay calm. The walls will hold."

    hide libitina with dissolve

    "Even as I speak, I can see the army spreading across the kingdom, each line precise, each step measured."
    "The ground seems to shiver beneath their march."
    "The air is thick with tension, charged as though the storm is not coming but already present."

    "I lift my hands subtly, feeling for the pulse of magic that once ran through the kingdom."
    mo "Come on, come on..."
    "It is thin, almost nonexistent. A few flickers, weak sparks that sputter and die."

    mo "So much power lost. And yet, they come."
    mo "They do not wait for us to recover."
    mo "Why should they?"

    show libitina base worr at t31
    l "Father, can’t you stop them?"

    show libitina sad
    mo "Not like this. Not now."

    hide libitina with dissolve

    "Every strategy I had rehearsed, every spell I had prepared, falls short."
    "The curse that has weakened our people is total. Magic cannot save us today."
    "I feel the weight of the kingdom pressing down, the centuries of power and knowledge reduced to fragile flesh."

    "I step back, my mind racing."
    "The army moves closer, lines of steel and fire spilling into our lands."
    "My heart beats steadily, but a familiar edge of fear sharpens."
    "There is no heroics left. Only survival."

    pause 0.3
    "There is one path I have kept hidden, a spell forbidden, dangerous, ancient."
    "One I swore never to use except in the darkest hour. That hour has come."
    "My last ounce of power..."
    "If there’s no other way, I’ll use the spell, whatever it costs."
    "Until then, I will not speak of it to Libitina. Not here, not now."
    "She must not see. She must not know until we are safe."

    stop ambient fadeout 1.0
    play music "mod_assets/music/Your Sweet 666 (Cover).ogg" fadein 3.0

    mo "Come with me, Libitina."

    "I step away from the railing, scanning the walls, the terrace, the narrow alleys."
    "They will flank us if we stay."
    "I push past the railing, retreating into the shadows of the castle."

    scene bg Guards2 with dissolve
    "Soldiers and mages begin to appear in courtyards, advancing carefully, testing the defenses."

    show libitina base vsca om at t31 with dissolve
    l "Father, what are we going to do?"

    show libitina worr
    mo "Our only goal is to survive."
    mo "Once that’s done, we run, and we take as many with us as possible."

    "Even as I say it, I know survival will demand a sacrifice beyond her understanding."
    "I feel the pulse of the spell inside me, the one I created long ago."
    "The secret I had kept for this very moment."

    "I attempt to call the wind, to use my power—to shift the air, to raise the ground beneath their feet."
    "My fingers trace the familiar signs, the incantations whispered for years."

    play sound "mod_assets/sfx/falter.ogg"
    queue sound "mod_assets/sfx/small whimper.ogg"
    "A single soldier falters, pushed backward by a flicker of energy."
    "A spark lights briefly along the edge of the battlefield, and then nothing."
    "A soldier pulls him away from the battlefield. He’s knocked out for now."

    mo "Damn it..."

    "It is not enough. My body strains, my mind stretches, and still the army advances, relentlessly."
    "A small group attempts to corner us—a handful of soldiers, a mage in the back keeping watch."

    #play sound "running_faint.ogg"
    "There is no time. I catch Libitina’s hand, squeezing it once, and begin to flee."
    "We move fast, but not recklessly."
    "Every step echoes against the ground, but it’s our only chance."

    "Behind us, the enemy advances, their shouts sharp, punctuated by the clatter of armored boots and the hiss of gunsmoke as battlemages test the air."
    "Arrows streak past, digging into the stone railing or embedding in the ground near our feet."

    show libitina sad at t31
    "Libitina clutches my arm, eyes wide, breaths shallow."
    "Her pace matches mine. I keep a hand on her shoulder, guiding and protecting."

    l "Father... I... I can’t—"

    mo "Focus on me, Libitina. Stay close. Do not look back."

    hide libitina with dissolve

    "The kingdom is chaotic."
    "Servants flee, soldiers fight in disorganized pockets."
    "Magic flickers weakly in the hands of those who still can cast it, if even at all."
    "But we cannot wait for reinforcements. The enemy is too strong, too prepared."
    "The curse has stripped our people of their power, and nothing I do here can stop the tide."
    "We have to survive."

    "We spotted a nearby forest. Its entrance lies open and unguarded—a haven for cover."

    show libitina base worr at t31 with dissolve
    l "Father... is it over? Are we—"

    mo "Not yet. Keep moving. Don’t slow."

    hide libitina with dissolve
    stop music fadeout 3.0
    play ambient "mod_assets/ambience/ext_day.ogg"

    scene bg 1600Forest with fade
    pause 1.0

    "Branches scratch our faces instantly."
    "I hear them behind us."
    "The guards shouting orders, the clang of weapons, the snap of gunpowder."
    "I think we've reached safety."
    "For now."
    "The forest thickens."
    "For a few precious seconds, the world feels quieter."

    show libitina base unsu at t21 with dissolve
    l "Maybe... maybe we're safe..."
    show libitina at thide
    hide libitina

    play music "mod_assets/music/Zombie (Cover).ogg" fadein 2.0
    pause 1.0
    
    "But instinct screams at me."
    "Movement in the shadows, figured crouched behind thick trees, hidden, and waiting."
    "Only a few seconds remain."

    mo 'LIBITINA! RUN!'
    
    "She does not hesitate. Her feet pound the ground as she vanishes down a narrow path I cannot follow with her."
    "My heart clenches, knowing what must come next."
    "The spell, long kept secret, waits for this moment."
    "This is it."
    "No time to hesitate. No chance for second thoughts."
    "The kingdom dies fully if I do not act."
    "The only way to protect her, and the last hope of survival is this."

    pause 1.0
    play sound "mod_assets/sfx/THROAT SLITTING.ogg"
    pause 1.0
    
    "A single, straight cut opens my throat. Blood spills, warmth fades, and the world tilts."
    play sound "mod_assets/sfx/collapse.ogg"
    scene black with fade
    "Behind me, the enemy is silent."
    "Then, realization kicks in."
    pause 1.0
    play sound "mod_assets/sfx/the king is dead! (sound effect).ogg"
    en "Everyone's dead! The kingdom is ours!"
    stop music fadeout 2.0

    pause 3.0

    # TODO:  sound effect for gasp.
    scene bg Village
    show fog
    with dissolve_scene_full
    # play sound "mod_assets/sfx/gasp.ogg"

    pause 1.0
    "I awaken slowly, in another soldier's vessel."
    "Limbs that once were strong, now feel brittle and foreign, weighed down by the shell of someone else."
    stop ambient fadeout 2.0
    pause 1.0
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
    pause 1.0
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
    pause 1.0
    scene bg 1700_Forest
    with dissolve_scene_full
    #play ambient "mod_assets/sfx/wind"
    "Nearly a hundred years have passed since the fall of Blackbriar."
    "Years carried in exile, walking in shadows, wearing a face that’s not my own."
    "Yet through all of it, Libitina has remained at my side."
    pause 1.0
    "We have crossed kingdoms, seas, mountains... all searching."
    "Always searching."

    play sound "mod_assets/sfx/crackling fire.ogg"
    "We rest by the fire, the forest around us quiet."

    show libitina base neut at t11 with dissolve
    l "Father... how long will this go on?"
    pause 1.0
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
    pause 1.0
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
    show libitina base conc
    l "Then I will walk with you, Father."
    play sound "mod_assets/sfx/Dying Fire.ogg"
    "The fire fades away, the smell lingering around us."
    show libitina base neut
    l "The fire’s gone, Father."
    l "Do we keep moving?"
    mo "Yes. We cannot stay where the light dies."
    mo "We move until we find shelter."
    scene bg 1700_path
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
    show libitina base unsu at t11
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
    show libitina base worr at t11
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
    play ambient "mod_assets/sfx/int_night.ogg"
    scene bg cave_interior with wipeleft_scene
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
    scene bg cave_text with dissolve
    mo "...Someone was here before us."
    show libitina base unsu at t11
    l "Father, can you read it?"
    "I reach out, fingers brushing against the ancient text."
    pause
    show libitina at thide
    hide libitina
    "I cannot read it yet."
    "But it feels familiar."
    "As though some echo of the words lives in my blood."
    pause 1.0
    "Then I hear it.."
    "Not from the walls, but from memory.."
    "A voice, deep and steady, carried from my childhood."
    "My grandfather’s voice."
    stop ambient fadeout 2.0
    play music "mod_assets/music/King Morvayn.ogg" fadein 3.0
    mo "...I know this text."
    show libitina base unsu at t11
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
    show libitina base worr
    l "He told you this?"
    pause 1.0
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
    pause 1.0
    mo "We must find out what this means."
    mo "If it takes us days, weeks, years.."
    mo "So be it."
    mo "We will find out."
    stop music fadeout 2.0
    scene black
    with dissolve_scene_full

    # Title Card: Three Years Later
    scene bg 1700_Path
    with dissolve_scene_full
    play music "mod_assets\music\Zombie (Cover).ogg" fadein 2.0
    "Three years passed within the stone belly of the crater."
    "Three years of dust and firelight, of words carved into parchment until my hands bled."
    "With many quests as-well along the way."
    "Three years of Libitina’s quiet voice, keeping me anchored when shadows pressed too close."
    "I love her."
    "We’ve gone through hell and back together."
    pause 1.0
    "At last, the language surrendered itself to me."
    "The meaning was not simple... but it was clear."
    "It’s time I tell Libitina."
    "It’s time we go."
    "I step into the cave"
    scene bg cave_text with wipeleft_scene
    mo "Libitina, It’s time." 
    show libitina base unsu night at t11
    l "Oh my?"
    l "Father this is.."
    l "What does it say?"
    mo "It speaks of two paths."
    l "What do they say?"
    mo "The first is a way through."
    mo "A portal."
    mo "A passage to another world."
    mo "A place where our people’s power lies waiting."
    pause 1.0
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
    pause 1.0
    mo"Only then can my power be restored."
    mo"Only then can we return to Blackbriar... and raise our kingdom from its grave."
    mo"Bring the people back."
    mo"And take what’s ours.."
    pause 1.0
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
    pause 1.0
    mo "Without you, Libitina, the kingdom dies with me."
    show libitina conc
    l "...Tell me what to do."
    "I move over to the wall, fingers tracing the deepest lines of the script."
    "My voice takes the rhythm of the old tongue... words my grandfather once whispered by firelight, long ago."
    "The cave trembles."
    # TODO: low hum sfx
    # play sound "mod_assets/sfx/low hum.ogg"
    "A low hum grows in the stone, in the air, in their very blood."
    "The symbols ignite, faint at first, then brighter, as though the chamber itself remembers its purpose."
    mo "Place your hand here, Libitina. Feel the words. Do not fear them."
    "She steps closer, hesitation lingering in her breath."
    "Slowly, she presses her palm to the stone beside mine."
    scene bg cave_text
    with flash
    "Suddenly the wall splits."
    "Light spills forth, pale and shifting, a wound in the air where stone once stood."
    show libitina base lsur night at t11
    l "...Father, it’s real."
    mo "More real than anything we have known."
    pause 1.0
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
    show libitina base conc night at t11
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
