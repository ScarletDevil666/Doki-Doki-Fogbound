init -5 python:

    #Just change the base_path variable if you need to adjust your path to the folder
    base_path = "mod_assets/MPT/goro/"
    outfits_path = base_path + "outfits/"
    expressions_path = base_path + "expressions/"

layeredimage goro:
    
    #better rendering and also avoid the vertical/horizontal line issues + autofocus
    at renpy.partial(Flatten, drawable_resolution=False)

    always base_path + "base.png"

    group mood: #Mood determines what the defaults images are for the following attributes:
        #"oe", "ce", "om", "cm", "brow".
        #By changing what the "mood" attribute is, you can easily switch between premade sets of expressions that work well together, speeding up your workflow.
        #Additionally, you can add in any new ones as you like.
        attribute neut default null #neutral
        attribute conc null

    group outfit:
        attribute uniform default null

    group center:
        attribute forward default if_any "uniform":
            outfits_path + "toyama_base_uniform_bodybase.png"

    group mouth:

        # Closed mouth.
        attribute cm default if_any(["neut"]):
            expressions_path + "mouths/m1.png"
        # Open mouth
        attribute om default if_any(["conc"]):
            expressions_path + "mouths/m2.png"

    group eyes:

        # Open eyes.
        attribute oe default if_any(["neut"]):
            expressions_path + "eyes/e1.png"

        # To da left
        attribute eb default if_any(["conc"]):
            expressions_path + "eyes/e2.png"
        attribute e2:
            expressions_path + "eyes/e2.png"

        # Closed eyes.
        attribute ce:
            expressions_path + "eyes/e3.png"

    group eyebrows:

        # Neutral
        attribute ba default if_any(["neut"]):
            expressions_path + "eyebrows/b1.png"

        # Questioning
        attribute bb default if_any(["conc"]):
            expressions_path + "eyebrows/b2.png"

        # Bothered
        attribute bc:
            expressions_path + "eyebrows/b3.png"