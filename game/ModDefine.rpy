#BG
image bg morvaynsroom = "mod_assets/bgs/Morvayns Room (Updated).png"
image bg EntLibitinaRoom = "mod_assets/bgs/1600 entrance to libatinas room (updated).png"
image bg LibitinaRoom = "mod_assets/bgs/1600 libatinas room.PNG"
image bg CalmVillage = "mod_assets/bgs/1600 calm b4 the storm village (updated).png"
image bg Railing = "mod_assets/bgs/1600 railing (updated).png"
image bg MorvaynsTerritory = "mod_assets/bgs/1600 morvayns territory.png"
image bg WarRailing = "mod_assets/bgs/1600 war railing (updated).png"
image bg MorvaynsRoomZoom = "mod_assets/bgs/Morvayns Room (Zoomed In-Updated).png"
image bg ArmedSoldier = "mod_assets/bgs/Armed Soldier (1600).PNG"
image bg ArmedGuards = "mod_assets/bgs/Armed Guards #1 (and only).png"
image bg AwayPath = "mod_assets/bgs/away path.png"
image bg 1600Forest = "mod_assets/bgs/1600 forest (updated).png"
image bg 1600ForestZoom = "mod_assets/bgs/1600 Forest (Updated-Zoomed In).png"
image bg FireVillage = "mod_assets/bgs/1600 firey village.png"
image bg Village1 = "mod_assets/bgs/Village #1.png"
image bg Guards1 = "mod_assets/bgs/Armed Guards #1.png"
image bg Guards2 = "mod_assets/bgs/Armed Guards #2.png"
image bg 1700Crater = "mod_assets/bgs/1700 crater (will be updated).png"
image bg 1700Forest = "mod_assets/bgs/1700 forest (no fire).png"
image bg 1700ForestFire = "mod_assets/bgs/1700 forest (fire).png"
image bg 1700Path = "mod_assets/bgs/1700 path (updated).png"
image bg CaveInterior = "mod_assets/bgs/Cave Interior (1700).png"
image bg CaveText = "mod_assets/bgs/Cave Text (1700).png"
image bg 1400Flashback = "mod_assets/bgs/1400 flashback village.png"
image bg Away_Path = "mod_assets/bgs/away path.png"
image bg War Railing = "mod_assets/bgs/1600 war railing (updated).png"
image bg fire_village = "mod_assets/bgs/1600 firey village.png"
image bg fire_path = "mod_assets/bgs/1600 firey path.png"

define flash = Fade(.25, 0, .75, color="#fff")
#characters
define mo = Character("Morvayn", window_background=Image("/mod_assets/UI/text boxes/Morvayn Text Box (1600-1700).png", xalign=0.5, yalign=1.0), who_style='say_label_Morvayn')
define l = Character("Libitina", window_background=Image("/mod_assets/UI/text boxes/Libatina Text Box (1600-1700).png", xalign=0.5, yalign=1.0), who_style='say_label_Libitina')
define g = Character("Goro", window_background=Image("/mod_assets/UI/text boxes/Goro Text Box (1600).png", xalign=0.5, yalign=1.0), who_style='say_label_Goro')
#define en = Character("Enemies")
define pa = Character("Prince Ale", window_background=Image("/mod_assets/UI/text boxes/Prince Ale_Morvayns Vessel Text Bod (1700).png", xalign=0.5, yalign=1.0), who_style='say_label_Ale')
define gr = Character("Grandfather", window_background=Image("/mod_assets/UI/text boxes/Morvayns Grandfather Text Box (1400 Flashback).png", xalign=0.5, yalign=1.0), who_style='say_label_Ale')
define us = Character("Us", window_background=Image("/mod_assets/UI/text boxes/Libatina And Morvayn Text Box (1700).png", xalign=0.5, yalign=1.0), who_style='say_label_Us')
define ym = Character("Morvayn", window_background=Image("/mod_assets/UI/text boxes/Young Morvayn Text Box (1400 Flashback).png", xalign=0.5, yalign=1.0), who_style='say_label_YMorvayn')

# Sounds
# Music
define audio.barnes = "mod_assets/ost/Barnes(2000s-Updated).ogg"
define audio.fogbound = "mod_assets/ost/Fogbound (Main Menu).ogg"
define audio.heartshapedbox = "mod_assets/music/Heart Shaped Box (Vinyl 1600-Prologue-Cover).ogg"
define audio.istilldo = "mod_assets/ost/I Still Do (Cover).ogg"
define audio.littlecutvariant = "mod_assets/ost/Just a Little Cut (Variant).ogg"
define audio.littlecut = "mod_assets/ost/Just a Little Cut.ogg"
define audio.kingmorvayn = "mod_assets/ost/King Morvayn (Prologue).ogg"
define audio.massanastasia = "mod_assets/ost/Mass Anastasia (Cover-2000s).ogg"
define audio.morningrain = "mod_assets/music/Morning Rain! (2000s).ogg"
define audio.nothingelse = "mod_assets/ost/Nothing Else Matters (Cover-Prologue).ogg"
define audio.sextape = "mod_assets/ost/sextape (Cover-2000s).ogg"
define audio.tallerbeauty = "mod_assets/music/Taller Beauty (Cover).ogg"
define audio.tragedyhill = "mod_assets/music/Tragedy Hill.ogg"
define audio.sweet666 = "mod_assets/ost/Your Sweet Six Six Six (Cover-Prologue)-Updated.ogg"
define audio.zombie = "mod_assets/ost/Zombie (Prologue-Cover).ogg"
define audio.sleep = "mod_assets/ost/Where Did You Sleep_ (Prologue-Cover).ogg"

# SFX
define audio.branches = "mod_assets/sfx/Branches.ogg"
define audio.collapse = "mod_assets/sfx/Collapse.ogg"
define audio.crackling_fire = "mod_assets/sfx/crackling fire.ogg"
define audio.door_opening = "mod_assets/sfx/door opening (updated).ogg"
define audio.dying_fire = "mod_assets/sfx/Dying Fire.ogg"
define audio.faint_footsteps_ext = "mod_assets/sfx/Faint Footsteps (Ext).ogg"
define audio.faint_footsteps_int = "mod_assets/sfx/Faint Footsteps (Int).ogg"
define audio.faint_running = "mod_assets/sfx/Faint Running.ogg"
define audio.fall = "mod_assets/sfx/Fall.ogg"
define audio.falter = "mod_assets/sfx/Falter.ogg"
define audio.female_sigh = "mod_assets/sfx/Female Sigh.ogg"
define audio.gasp = "mod_assets/sfx/Gasp.ogg"
define audio.goro_gunshot = "mod_assets/sfx/Goro Gunshot.ogg"
define audio.low_hum = "mod_assets/sfx/Low Hum.ogg"
define audio.male_sigh = "mod_assets/sfx/Male Sigh.ogg"
define audio.running_1600 = "mod_assets/sfx/Running (1600).ogg"
define audio.sayori_laugh = "mod_assets/sfx/sayori laugh.ogg"
define audio.sayoris_laugh = "mod_assets/sfx/Sayoris Laugh.ogg"
define audio.school_bell = "mod_assets/sfx/School Bell.ogg"
define audio.slash = "mod_assets/sfx/slash_cut (updated).ogg"
define audio.small_whimper = "mod_assets/sfx/Small Whimper.ogg"
define audio.king_is_dead_sfx = "mod_assets/sfx/The king is dead! (sound effect).ogg"
define audio.king_is_dead_voice = "mod_assets/sfx/The King Is Dead! (voice acted sound effect).ogg"
define audio.throat_slitting = "mod_assets/sfx/THROAT SLITTING.ogg"
define audio.vinyl_1600 = "mod_assets/sfx/Vinyl (1600).ogg"

# Ambience
define audio.chatter = "mod_assets/ambience/Chatter.ogg"
define audio.crackling_fire = "mod_assets/ambience/Crackling Fire.ogg"
define audio.ext_day_updated = "mod_assets/ambience/Ext_Day (Updated).ogg"
define audio.ext_day = "mod_assets/ambience/ext_day.ogg"
define audio.ext_night = "mod_assets/ambience/Ext_Night.ogg"
define audio.int_day = "mod_assets/ambience/Int_Day.ogg"
define audio.int_night = "mod_assets/ambience/Int_Night.ogg"
define audio.muffled_rain_interior = "mod_assets/ambience/muffled rain interior.ogg"
# This is a png file?? - define audio.muffled_war_sounds_int = "mod_assets/ambience/Muffled War Sounds (Int).png"
define audio.rain_ext = "mod_assets/ambience/Rain_Ext.ogg"
define audio.walking_forest_1700 = "mod_assets/ambience/Walking In The Forest (1700).ogg"
define audio.war_sounds = "mod_assets/ambience/War Sounds.ogg"
define audio.wind_fog = "mod_assets/ambience/Wind (Fog).ogg"
define audio.wind = "mod_assets/ambience/wind.ogg"

# Movies
image movie = Movie(size=(1280, 720))
image moviefg = Movie(size=(1280, 720), channel="moviefg", side_mask=True)