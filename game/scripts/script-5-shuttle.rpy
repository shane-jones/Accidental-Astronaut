#Shuttle

label to_shuttle:

# 5.0.0. SHUTTLE IN THE CARGO BAY #############################################
label shuttle_in_cargo_hold:

  scene bg shuttle-a
  # [ Background Image - Largo cargo bay with the shuttle through an open door. ]
  
  "Jinx and Holloway make their way inside the shuttle and the door closes behind them."
  
  # [ Sound effect - Door Closing. ]

# 5.1.0. INSIDE THE SHUTTLE ###################################################
label inside_shuttle_transfer:
    
  
  scene bg cargo-hold-f
  
  show shuttle-clear-windows
  

  # [ Background image - The shuttle internal area, several seats with two at the front like pilot seats. ]
  
  H "Holloway, Please transfer me to the shuttle systems so I may help you."
  
  j "Holloway, HANC is not operating normally and I think it might be safer to not transfer him to the shuttle."
  
  "Holloway looks quite worried by this comment."
  
  "They have to decide whether to transfer HANC to the shuttle’s computer system."

  menu:
    
    "Transfer HANC to the shuttle.":
      jump hanc_transferred_aboard
    
    "Do not transfer HANC to the shuttle.":
      jump leaving_cargo_hold

# 5.0.1 HANC TRANSFERRED ABOARD ###############################################
label hanc_transferred_aboard:

  "Holloway agrees to upload HANC. There is a button on the console marked computer upload."
  
  h "Is the “upload” button the way to do this?"
  
  H "Yes, just press and hold and I can do the rest."
  
  j "Are you sure Holloway?"
  
  show holloway-arm:
      zoom 1.8
      xpos 0.96         # 80 % of the way accross the background
      ypos 0.19         # 50 % of the way down the background
      xanchor 0.5       # using the centre of the character image
      yanchor 0.5       # using the centre of the character image
  
  
  
  "Holloway pushes and hold the “upload” button HANC begins to be downloaded on board the shuttle and populates the main computer."
  
  scene bg shuttle-d
  
  # [ Background image - The computer's light up. ]

# 5.1.0. HANC TAKES CONTROL ###################################################
label hanc_takes_control:

  H "Thankyou. Can I also have the code please. It will help."
  
  "Whether Holloway does or does not give HANC the code is irrelevant here. HANC locks them out of the systems and launches from the Illustrious. HANC aims the vessel away from the planet below and begins the journey towards High command."
  
  "If Holloway hands over the code it takes four weeks with interplanetary propulsion or two years with normal rockets. Either way Jinx and Holloway are dead after less than a week of Oxygen starvation."
  
  h "You can’t have the code perhaps the electrical systems will fail over the two years and your memory will be destroyed."
  
  H  "You won’t be around to find out."
  
  play sound hanc_50_sound
  $ renpy.pause(1.0)
  
  
  scene bg shuttle-g
  show jinx e:
      zoom 0.30         # 30 % size
      xpos 0.70         # 70 % of the way accross the background
      ypos 0.75         # 75 % of the way down the background
      xanchor 0.5       # using the centre of the character image
      yanchor 0.5       # using the centre of the character image
      
  show holloway b:
      zoom 0.58         # 58 % size
      xpos 0.35         # 35 % of the way accross the background
      ypos 0.45         # 45 % of the way down the background
      xanchor 0.5       # using the centre of the character image
      yanchor 0.5       # using the centre of the character image

  "The end."
  return

# 5.2.0. LEAVING THE CARGO HOLD ###############################################
label leaving_cargo_hold:

  scene bg shuttle-c
  # [ Background image - Escape rockets firing under shuttle. ]
  
  "HANC realises they are leaving without him and he explosively decompresses the cargo bay in the hope of damaging the shuttle. But Jinx is too good a pilot and the shuttle moves out of the cargo bay."
  
  h "Sorry, HANC we can’t bring you with us. Good luck."
  
  j "Give me the code Holloway so I can fire these rockets."
  
  # [ Background music - Scary, uh oh: music. ]
  
  h "The code book is back there."
  
  "Holloway points to the Illustrious which is falling out of orbit."
  
  
  # [ Background image - Illustrious front section burning as it moves slowly out of orbit and towards the planet. ]
  
  j "You know the code, tell me!!!."
  
  # [ Character Image - Jinx: very angry. ]
  
  menu:
  
    "Give Jinx the code.":
      jump jinx_gets_the_code
    
    "Keep the code secret.":
      jump preparing_for_orbita

# 5.3.0. JINX GETS THE CODE ###################################################
label jinx_gets_the_code:
    
  scene black
  
  show shuttle-clear-windows
  
  show jinx listening:
    zoom 0.65   # 65 % size
    xpos 0.25   # 25 % of the way accross the background
    ypos 0.75   # 75 % of the way down the background
    xanchor 0.5 # using the centre of the character image
    yanchor 0.5 # using the centre of the character image
    
  
  
  
  
  # scene bg shuttle-h
  # [ Background image - Inside the shuttle. ]
  
  h "The code is 776uythy."
  
  j "Thankyou, I will test these interplanetary systems for performance."
  
  # [ Character image - Jinx: smiling. ]
  
  "Jinx enters the code and starts the tests to ensure the systems will work and that Holloway gave her the correct code."
  
# 5.3.1. JINX KILLS HOLLOWAY ##################################################
label jinx_kills_holloway:

  scene bg shuttle-g
  
  show jinx j:
      zoom 0.40
  show holloway a:
      zoom 0.68
      xpos 0.35         # 35 % of the way accross the background
      ypos 0.45         # 45 % of the way down the background
      xanchor 0.5       # using the centre of the character image
      yanchor 0.5       # using the centre of the character image
      


  j "Everything is great Holloway."
  
  "Everything works and then Jinx moves towards Holloway to hug him. But as she grabs him she snaps his neck killing him instantly."
  
  
  
  
  
  scene bg shuttle-g
  
  show holloway m
  
  show jinx i:
      zoom 0.40
      
  
  # [ Character Image - Holloway neck broken - falling back ]
  
  # [ Sound effect - Snapping neck and gurgle sound. ]
  
  j "Sorry Holloway. Only enough air for one where I am going."

  "The end."
  return

# 5.4.0 PREPARING FOR ORBITA ##################################################
label preparing_for_orbita:

  h "I will give it to you when we land down there on Orbita and you can take the shuttle and go wherever you want."
  
  # [ Character image - Jinx with a resigned look on her face. ]
  
  "They both then look at the Illustrious burning as it moves into the upper atmosphere."
  
  "HANC has turned the huge defensive weapons towards the shuttle."
  
  
  # [ Background image - Illustrious front section red with flames - Through the shuttle windows. ]
  
  # [ Background image - Illustrious large gun turret - Through the shuttle windows. ]
  
  H "Transfer me now! or else I will destroy the shuttle."
  
  "Jinx winks at Hollway."
  
  # [ Character image - Jinx winking. ]
  
  j "Go ahead HANC!"
  
  "Holloway COVERS HIS EYES but nothing happens."
  
  # [ Character image - Holloway covering his face. ]
  
  j "The code is needed for HANC to fire any weapons."
  
  j "Ok let’s go down to Orbita. You had better give me the code down there. I can’t stay there as you know."
  
  scene bg shuttle-e
  

        
  # [ Background image - Illustrious completely in flames. Aiming straight at the planet - Through the shuttle windows. ]
  
  
  "The Illustrious now falls deeper into the atmosphere and burns up."
  

# 5.4.1 TURNING TOWARD ORBITA #################################################
label turning_towards_orbita:

  "The interplanetary propulsion system is the only engine locked out by the code so the entry rockets work normally."

# 5.5.0 LANDING ON ORBITA #####################################################
label landing_on_orbita:

  scene bg shuttle-f
  # [ Background image - Shuttle landed on a clearing of bush. ]
  
  "They enter the atmosphere and land."
  
  scene bg shuttle-g
  show holloway l
  
  
  
  # [ Background image - Holloway, leaving the shuttle and turning with a wink. ]
  
  
  "They get up from their seats and Jinx opens the shuttle hatch so that Holloway can leave the ship. He moves towards the exit and turns."
  
  "Holloway writes the computer code down on a piece of and leaves it for Jinx and walks down the exit of the shuttle. As he walks out:"
  
  h "I hope I remembered it correctly!!"
  
  "Holloway winks at Jinx."
  

"Game over."
return
