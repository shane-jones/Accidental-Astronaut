# Airlock

label to_airlock:
  "You have arrived in the airlcok."

# 1.0.0. WAKING UP IN THE AIRLOCK #############################################
label waking_up_in_the_airlock:

# 1.0.1. DECIDING WHAT TO DO ##################################################
label deciding_what_to_do:

  menu:
  
    "Do nothing and wait for help.":
      jump wait_for_help
    
    "Force open the airlock.":
      jump force_open_the_airlock
    
    "Power up the monitor.":
      jump the_last_log

# 1.1.0. WAIT FOR HELP ########################################################
label wait_for_help:
  "End."
  return

# 1.2.0. FORCE OPEN THE AIRLOCK ###############################################
label force_open_the_airlock:
  "End."
  return

# 1.3.0. THE LAST LOG #########################################################
label the_last_log:
  "Play on."

# 1.4.0. HANC #################################################################
label hanc:

# 1.5.0. THE LOCKER ###########################################################
label the_locker:

# 1.6.0. LEAVING THE AIRLOCK ##################################################
label leaving_the_airlock:

  menu:
  
    "Open the airlock and go outside.":
      jump floating_away
      
    "Ponder on how to hold on outside and ask HANC what to do.":
      jump hancs_advice

# 1.7.0. FLOATING AWAY ########################################################
label floating_away:
  "End."
  return

# 1.8.0. HANC’S ADVICE ########################################################
label hancs_advice:
  
  menu:
    
    "Leave the ship.":
      jump radio_silence
    
    "Ask HANC about communications outside the ship.":
      jump radio_controls

# 1.9.0. RADIO SILENCE ########################################################
label radio_silence:
  "End."
  return

# 1.10.0. RADIO CONTROLS ######################################################
label radio_controls:
  "Play on."

"Jump to EVA."
jump to_eva