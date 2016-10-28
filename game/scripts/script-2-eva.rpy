# EVA

label to_eva:
  scene bg eva-empty-space
  "You have arrived at EVA."

# 2.0.0. OUTSIDE ##############################################################
label outside:
   
# 2.0.1. THE SHIP #############################################################
label the_ship:

# 2.0.2. TWO TETHERS ##########################################################
label two_tethers:

  menu:
    "Hook this tether to your suit and release the other tether.":
     $ has_two_tethers = False
          
    "Hook this tether to your suit and keep the other tether attached.":
     $ has_two_tethers = True

# 2.0.3. THE REPAIR ###########################################################
label the_repair:

# 2.1.0. A SIGN OF LIFE #######################################################
label a_sign_of_life:

# 2.2.0. THE SHIP IS SEALED ###################################################
label the_ship_is_sealed:

# 2.2.1. BACK TO THE SHIP #####################################################
label back_to_the_ship:

  if has_two_tethers:
    "You have both tethers."
    jump enough_rope
  else:
    "You have one tether."
    jump not_enough_rope
    
# 2.2.2 ENOUGH ROPE ###########################################################
label enough_rope:
  "Play on."
  jump pressurising

# 2.2.3. NOT ENOUGH ROPE ######################################################
label not_enough_rope:
  "End."
  return

# 2.3.0. PRESSURISING #########################################################
label pressurising:

  menu:
  
    "Push the button to open the door to go inside.":
      jump slammed

    "Ask HANC if it’s okay to open the door to go inside.":
      jump sixty_more_seconds

# 2.3.1. SLAMMED ##############################################################
label slammed:
  "End."
  return

# 2.3.2. 60 MORE SECONDS ######################################################
label sixty_more_seconds:

# 2.4.0. JINX MAKES PLANS #####################################################
label jinx_makes_plans:
  
"Jump to the bridge."
jump to_bridge  