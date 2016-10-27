# EVA

label to_eva:
  scene bg eva-empty-space
  "You have arrived at EVA."

label outside:
   

label the_ship:

label two_tethers:

  menu:
    "Hook this tether to your suit and release the other tether.":
     $ has_two_tethers = False
          
    "Hook this tether to your suit and keep the other tether attached.":
     $ has_two_tethers = True

label the_repair:

label a_sign_of_life:

label the_ship_is_sealed:

label back_to_the_ship:

  if has_two_tethers:
    "You have both tethers."
    jump enough_rope
  else:
    "You have one tether."
    jump not_enough_rope
    
label enough_rope:
  "Play on."
  jump pressurising

label not_enough_rope:
  "End."
  return

label pressurising:

  menu:
  
    "Push the button to open the door to go inside.":
      jump slammed

    "Ask HANC if it’s okay to open the door to go inside.":
      jump sixty_more_seconds

label slammed:
  "End."
  return

label sixty_more_seconds:

label jinx_makes_plans:
  
"Jump to the bridge."
jump to_bridge  