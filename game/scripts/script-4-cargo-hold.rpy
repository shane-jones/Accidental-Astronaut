# Cargo Hold

label to_cargo_hold:
  "You have arrived in the cargo hold"
  
# 4.0.0. CARGO HOLD ###########################################################
label cargo_hold:

# 4.0.1. JINX… ################################################################
label jinx:

# 4.0.2. PREPARATIONS #########################################################
label preparations:

# 4.0.3. SECRETS ##############################################################
label secrets:

# 4.0.4. THE CODE #############################################################
label the_code:

  menu:
    
    "Give Jinx the code.":
      jump jinx_gets_away
    
    "Give HANC the code.":
      jump hanc_has_the_code
    
    "Do not share the code.":
      jump smart_boy_holloway

# 4.1.0 JINX GETS AWAY ########################################################
label jinx_gets_away:

# 4.1.1 CONTAINER MISTAKE #####################################################
label container_mistage:
  "End."
  return

# 4.2.0 SMART BOY HOLLOWAY ####################################################
label smart_boy_holloway:
  "Play on."
  
# 4.2.1 AGREEMENT #############################################################
label agreement:

"Jump to the shuttle."
jump to_shuttle