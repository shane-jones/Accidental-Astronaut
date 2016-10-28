#Shuttle

label to_shuttle:
  "You have arrived on the shuttle."

# 5.0.0. SHUTTLE IN THE CARGO BAY #############################################
label shuttle_in_cargo_hold:

# 5.1.0. INSIDE THE SHUTTLE ###################################################
label inside_shuttle_transfer:

  menu:
    
    "Transfer HANC to the shuttle.":
      jump hanc_transferred_aboard
    
    "Do not transfer HANC to the shuttle.":
      jump leaving_cargo_hold

# 5.0.1 HANC TRANSFERRED ABOARD ###############################################
label hanc_transferred_aboard:

# 5.1.0. HANC TAKES CONTROL ###################################################
label hanc_takes_control:
  "End."
  return

# 5.2.0. LEAVING THE CARGO HOLD ###############################################
label leaving_cargo_hold:
  
  menu:
  
    "Give Jinx the code.":
      jump jinx_gets_the_code
    
    "Keep the code secret.":
      jump preparing_for_orbita

# 5.3.0. JINX GETS THE CODE ###################################################
label jinx_gets_the_code:

# 5.3.1. JINX KILLS HOLLOWAY ##################################################
label jinx_kills_holloway:
  "End."
  return

# 5.4.0 PREPARING FOR ORBITA ##################################################
label preparing_for_orbita:

# 5.4.1 TURNING TOWARD ORBITA #################################################
label turning_towards_orbita:

# 5.5.0 LANDING ON ORBITA #####################################################
label landing_on_orbita:

"Happy ending."
return