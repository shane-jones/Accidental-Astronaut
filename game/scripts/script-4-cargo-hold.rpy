# Cargo Hold

label to_cargo_hold:
  
# 4.0.0. CARGO HOLD ###########################################################
label cargo_hold:

  scene bg cargo-hold-h
  # [ Background image - door to the cargo bay. ]
  
  "Holloway is about to open the door, but pauses and looks up at a screen, sarcastically."

  # show hanc b:
  #   zoom 0.8 xpos 0.18 ypos 0.56 xanchor 0.5 yanchor 0.5 # small, left side middle
  
  H radio "It is safe to open that door, unknown human is in there though."

  # hide hanc

# 4.0.1. JINX… ################################################################
label jinx:
  
  scene bg cargo-hold-b
  # [ Background image - cargo hold. ]

  "Holloway opens the door and Jinx is hiding in one corner."

  show jinx l:
    zoom 0.065 xpos 0.72 ypos 0.48 xanchor 0.5 yanchor 0.5 # Jinx tiny - crouched down 
  
  "HANC identifies Jinx’s position and she emerges from the shadows after realising Holloway is not an officer."
  
  "Jinx quickly realises that HANC is around."

  show jinx k: 
    zoom 0.5 xpos 0.7 ypos 0.8 xanchor 0.5 yanchor 0.5 #[ Jinx standing normal ]
  
  j "Hi. My name is Jinx 'Takanoma'."

  hide jinx
  
  "HANC, of course, runs this name through a database and is unable to locate a match."
  
  h "Hi Jinx, Im Frank Holloway. Everyone else on board managed to escape before the collision, so it is just me left."
  
  h "Why were you hiding?"
  
  show jinx k: 
    zoom 0.5 xpos 0.7 ypos 0.8 xanchor 0.5 yanchor 0.5 #[ Jinx standing normal ]

  j "I was not sure if you were armed."
  
  "Jinx changes the subject."
  
  j "I am a flight training officer and I can pilot the shuttle... just."

  hide jinx

  # show hanc b:
  #   zoom 0.5 xpos 0.59 ypos 0.39 xanchor 0.5 yanchor 0.5 # small, left side middle
  
  H "It is easy, I am the most capable so I will do it."

  # hide hanc

# 4.0.2. PREPARATIONS #########################################################
label preparations:

  "There is quite a bit of prep work to be done."
  
  "Holloway follows instructions from HANC and Jinx to prepare the shuttle."
  
  # [ Additional graphic - Two Containers (close up) ]
  scene bg cargo-hold-j
  
  "There are also two large containers in the hold. Both have supplies and rescue equipment in them. One does say 'CAUTION'."

  scene bg cargo-hold-b

  h "Jinx, are you able to get the shuttle to the surface below?"
  
  # [ Character graphic - Jinx with arms out to side (shrugging shoulders) ]
  show jinx k: 
    zoom 0.5 xpos 0.7 ypos 0.8 xanchor 0.5 yanchor 0.5 #[ Jinx standing normal ]
  
  j "I can’t be sure. I think we must go into deep space and attempt to get to the next planet some three weeks away - Dorphia. The planet below is very primitive so we should avoid it."
  
  hide jinx

  h "If you can fly, Why not use the freighter?"

  # show hanc b:
  #   zoom 0.5 xpos 0.59 ypos 0.39 xanchor 0.5 yanchor 0.5 # small, left side middle
  
  H radio "The Illustrious is far too damaged to even attempt this."

  # hide hanc
  
  h "Protocols suggest we must go to the nearest suitable planet in an emergency. Since the Illustrious is too damaged we will take the shuttle and land below."
  
# 4.0.3. SECRETS ##############################################################
label secrets:

  "HANC and Jinx have secrets."
  
  "HANC is not able to control the main ship completely without the code. He also knows the extent of the damage."
  
  "Jinx is under arrest on the planet below and can’t return. She can pilot the Illustrious which has interstellar capabilities but it’s a very difficult large ship to control alone."
  
  "It is a  mega class freighter which is easily detected once away from this remote planet system and back on the main space shipping channels at cruising speed and may well be met by enforcement patrols."
  
  "She is also concerned by its damage."
  
  "Poor Holloway knows nothing."

# 4.0.4. THE CODE #############################################################
label the_code:

  # [ Character graphic - Jinx with hand on face (thinking pose). ]
  show jinx k: 
    zoom 0.5 xpos 0.7 ypos 0.8 xanchor 0.5 yanchor 0.5 #[ Jinx standing normal ]

  j "Holloway must have the captains code book with him as he managed to transfer bridge control to the Cargo bay. I need to figure out a way to obtain it."
  
  hide jinx 

  h "So the best thing for us to do is get to the planet below for help."
  
  "Holloway has basic training which tells him all trading planets have contact facilities left by high command in case of a problem and its suitable in accordance with standard emergency procedures."
  
  "Jinx can’t go there without an escape plan."
  
  "HANC wants the shuttle and can go far into space beyond oxygen levels and make it to command headquarters and rebuild his systems."
  
  show jinx k: 
    zoom 0.5 xpos 0.7 ypos 0.8 xanchor 0.5 yanchor 0.5 #[ Jinx standing normal ]

  j "Holloway, I’ll need the captain’s code to finish the preparations."

  hide jinx
  
  "What should Holloway do with the code?"

  menu:
    
    "Give Jinx the code.":
      jump jinx_gets_away
    
    "Give HANC the code.":
      jump hanc_has_the_code
    
    "Do not share the code.":
      jump smart_boy_holloway

# 4.1.0 JINX GETS AWAY ########################################################
label jinx_gets_away:

  "Holloway is convinced to give Jinx the code."
  
  h "The code is: 776uythy"
  
  show jinx f: 
    zoom 0.7 xpos 0.53 ypos 0.6 xanchor 0.5 yanchor 0.5 #[ Jinx laughing ]
  
  j "Thankyou. You won’t regret it..."

  hide jinx
  
  "Jinx uses the code to prepare the shuttle/locks and cargo door."

  show jinx k: 
    zoom 0.5 xpos 0.7 ypos 0.8 xanchor 0.5 yanchor 0.5 #[ Jinx standing ]
  
  j "Now before we board the shuttle, there is only one more thing that we need..."

  hide jinx
  
  "Jinx instructs Holloway to grab the ropes from the container on the right, the one with ‘caution’ written on the label."


  # [ Additional graphic - close up of container with ‘CAUTION’ on the label. ]

  scene bg cargo-hold-b
  
  show holloway i: 
    zoom 0.6 xpos 0.9 ypos 0.6 xanchor 0.5 yanchor 0.5 #[ Holloway looks in box]

  show jinx i: 
    zoom 0.14 xpos 0.93 ypos 0.55 xanchor 0.5 yanchor 0.5 #[ Jinx standing in escape door ]

  "As Holloway turns his back to open the container, Jinx slips into the Shuttle and engages the locks."

  hide holloway
  hide jinx

  show holloway g: 
    zoom 0.6 xpos 0.9 ypos 0.6 xanchor 0.5 yanchor 0.5 #[ Holloway faces door closing]
  
  "Holloway opens the lid and turns to ask which rope density only to see the door to the Shuttle close."

  scene bg cargo-hold-a # cargo door closes
  
  "He realises he has been tricked."

# 4.1.1 CONTAINER MISTAKE #####################################################
label container_mistage:

  H radio "Please tell me you did not open that container?"
  
  h "Umm. What if I did."
  
  H radio "There is a toxic gas that was isolated in there. It was leaking out of that chamber and is now infecting the cargo cabin."
  
  H radio "I’m afraid you do not have long."
  
  "Holloway keels over and suffocates to death. He tried his best."

  "The end."
  return

# 4.2.0 SMART BOY HOLLOWAY ####################################################
label smart_boy_holloway:
  
  "Holloway keeps the code to himself."
  
  "He speaks frankly with Jinx."
  
  h "Look, I just want to get back safely on land and my best shot is Orbita, the planet below."
  
  show jinx n

  j "I understand, but there is a small problem."

  hide jinx
  
  "Jinx identifies her dilemma and confesses she does not want to be arrested. They agree to go to the planet below and drop him off so Jinx can continue on to planet Dorphia."
    
# 4.2.1 AGREEMENT #############################################################
label agreement:

  "Holloway and Jinx agreement alone is the only way for Holloway to survive."
  
  "Without the code HANC can do little other than attempt an explosive decompression/shutdown power on the Illustrious if he finds out what’s happening."
  
  "These should not stop the shuttle getting way."
  
  "They chat while tying some ropes and Holloway tells her that he has the code in his head and will only give it to her once they are on the planet below providing some security."
  
  "They agree. Jinx is concerned however, Can she trust Holloway to give her the code once they are on the planet? She might try again later to get the code from him."

jump to_shuttle
