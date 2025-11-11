


layeredimage barnes: #All definitions are for her facing forward.
    
    always "mod_assets/MPT/barnes/Expressions/base.png" #We always use the basic face.
    
    group outfit:
        
        attribute uniform default null
    
    
    
    group mood: #Mood determines what the defaults images are for the following attributes:
        #"oe", "ce", "om", "cm", "brow".
        #By changing what the "mood" attribute is, you can easily switch between premade sets of expressions that work well together, speeding up your workflow.
        #Additionally, you can add in any new ones as you like.
        attribute neut default null #neutral
        attribute lsur null
        #attribute xxxx null #xxxx #Do you want to define a new mood?  Here, have a template!
    
    
    
    group pose:
        anchor (0,0) subpixel (True)
        yoffset (-0.5)
        attribute basic default if_any(["uniform"]):
            "mod_assets/MPT/barnes/Poses/1.png"
    
    group mouth:
        
        #Default Closed Mouths:
        # attribute cm default if_any(["happ","nerv"]):
        #     "mod_assets/MPT/barnes/barnes_forward_mouth_ma.png"
        attribute cm default if_any(["neut"]):
            "mod_assets/MPT/barnes/Expressions/Mouth/1.png"
        attribute cm default if_any(["lsur"]):
            "mod_assets/MPT/barnes/Expressions/Mouth/4.png"
        # attribute cm default if_any(["vsur","pout"]):
        #     "mod_assets/MPT/barnes/barnes_forward_mouth_mf.png"
        # attribute cm default if_any(["shoc"]):
        #     "mod_assets/MPT/barnes/barnes_forward_mouth_mi.png"
        # attribute cm default if_any(["cry","sad","angr","flus"]):
        #     "mod_assets/MPT/barnes/barnes_forward_mouth_mj.png"
        # attribute cm default if_any(["vang","pani"]):
        #     "mod_assets/MPT/barnes/barnes_forward_mouth_mm.png"
        # attribute cm default if_any(["laug","sedu"]):
        #     "mod_assets/MPT/barnes/barnes_forward_mouth_mn.png"
        # attribute cm default if_any(["yand"]):
        #     "mod_assets/MPT/barnes/barnes_forward_mouth_mo.png"
        
        # #Open Mouths:
        # attribute om if_any(["happ","sedu"]):
        #     "mod_assets/MPT/barnes/barnes_forward_mouth_mb.png"
        # attribute om if_any(["nerv","yand","laug"]):
        #     "mod_assets/MPT/barnes/barnes_forward_mouth_mc.png"
        # attribute om if_any(["neut","dist"]):
        #     "mod_assets/MPT/barnes/barnes_forward_mouth_me.png"
        # attribute om if_any(["worr","vsur","pout"]):
        #     "mod_assets/MPT/barnes/barnes_forward_mouth_mg.png"
        # attribute om if_any(["anno","flus"]):
        #     "mod_assets/MPT/barnes/barnes_forward_mouth_mh.png"
        # attribute om if_any(["lsur","curi"]):
        #     "mod_assets/MPT/barnes/barnes_forward_mouth_mi.png"
        # attribute om if_any(["sad"]):
        #     "mod_assets/MPT/barnes/barnes_forward_mouth_mk.png"
        # attribute om if_any(["cry","shoc"]):
        #     "mod_assets/MPT/barnes/barnes_forward_mouth_ml.png"
        # attribute om if_any(["vang","angr","doub","pani"]):
        #     "mod_assets/MPT/barnes/barnes_forward_mouth_mq.png"
        
        
        ###All mouths - truncated tags:
        attribute ma:
            "mod_assets/MPT/barnes/Expressions/Mouth/1.png"
        attribute mb:
            "mod_assets/MPT/barnes/Expressions/Mouth/2.png"
        attribute mc:
            "mod_assets/MPT/barnes/Expressions/Mouth/3.png"
        attribute md:
            "mod_assets/MPT/barnes/Expressions/Mouth/4.png"
        attribute me:
            "mod_assets/MPT/barnes/Expressions/Mouth/5.png"
        attribute mf:
            "mod_assets/MPT/barnes/Expressions/Mouth/6.png"
        attribute mg:
            "mod_assets/MPT/barnes/Expressions/Mouth/7.png"
    
    
    
    group eyes:
        
        #Default Opened eyes:
        attribute oe default if_any(["neut"]):
            "mod_assets/MPT/barnes/Expressions/Eyes/1.png"
        # attribute oe default if_any(["worr","flus","dist"]):
        #     "mod_assets/MPT/barnes/barnes_forward_eyes_e1b.png"
        # attribute oe default if_any(["anno","angr","sedu","doub"]):
        #     "mod_assets/MPT/barnes/barnes_forward_eyes_e1d.png"
        # attribute oe default if_any(["cry"]):
        #     "mod_assets/MPT/barnes/barnes_forward_eyes_e1g.png"
        attribute oe default if_any(["lsur"]):
            "mod_assets/MPT/barnes/Expressions/Eyes/2.png"
        # attribute oe default if_any(["nerv"]):
        #     "mod_assets/MPT/barnes/barnes_forward_eyes_e2b.png"
        # attribute oe default if_any(["pani","shoc"]):
        #     "mod_assets/MPT/barnes/barnes_forward_eyes_e2d.png"
        # attribute oe default if_any(["yand"]):
        #     "mod_assets/MPT/barnes/barnes_forward_eyes_e3a.png"
        
        # #Default Closed eyes:
        # attribute ce if_any(["neut","anno","vang","shoc","worr","sad","angr","lsur","vsur","pani","dist","worr"]):
        #     "mod_assets/MPT/barnes/barnes_forward_eyes_e4a.png"#
        # attribute ce if_any(["happ","laug","flus","yand","pout","sedu","nerv","curi","doub"]):
        #     "mod_assets/MPT/barnes/barnes_forward_eyes_e4b.png"#
        # attribute ce if_any(["cry"]):
        #     "mod_assets/MPT/barnes/barnes_forward_eyes_e4e.png"
        
        
        ###All eyes - truncated tags:
        attribute e1:
            "mod_assets/MPT/barnes/Expressions/Eyes/1.png"
        attribute e2:
            "mod_assets/MPT/barnes/Expressions/Eyes/2.png"
    
    
    
    group eyebrows:
        
        #Default Eyebrows:
        attribute brow default if_any(["neut"]):
            "mod_assets/MPT/barnes/Expressions/Eyebrows/1.png"
        # attribute brow default if_any(["cry","worr","shoc","laug","sad","flus","pani","worr","nerv"]):
        #     "mod_assets/MPT/barnes/barnes_forward_eyebrows_b1b.png"#
        # attribute brow default if_any(["anno","sedu"]):
        #     "mod_assets/MPT/barnes/barnes_forward_eyebrows_b1c.png"#
        # attribute brow default if_any(["vang","angr"]):
        #     "mod_assets/MPT/barnes/barnes_forward_eyebrows_b1e.png"#
        attribute brow default if_any(["lsur"]):
            "mod_assets/MPT/barnes/Expressions/Eyebrows/1.png"#
        # attribute brow default if_any(["vsur"]):
        #     "mod_assets/MPT/barnes/barnes_forward_eyebrows_b2a.png"#
        # attribute brow default if_any(["dist","pout"]):
        #     "mod_assets/MPT/barnes/barnes_forward_eyebrows_b1d.png"#
        # attribute brow default if_any(["curi"]):
        #     "mod_assets/MPT/barnes/barnes_forward_eyebrows_b1f.png"#
        
        # #The following brows are for moods that differ between open and closed eyes:
        # attribute brow default if_any(["doub"]) if_all(["oe"]) if_not(["ce"]):
        #     "mod_assets/MPT/barnes/barnes_forward_eyebrows_b1f.png"#
        # attribute brow default if_any(["doub"]) if_all(["ce"]) if_not(["oe"]):
        #     "mod_assets/MPT/barnes/barnes_forward_eyebrows_b3b.png"#
        
        
        #All eyebrows - truncated tags:
        attribute b1a:
            "mod_assets/MPT/barnes/Expressions/Eyebrows/1.png"
        attribute b1b:
            "mod_assets/MPT/barnes/Expressions/Eyebrows/2.png"
        attribute b1c:
            "mod_assets/MPT/barnes/Expressions/Eyebrows/3.png"