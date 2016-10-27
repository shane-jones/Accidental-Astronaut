# Airlock

label to_airlock:
  "You have arrived in the airlcok."

label waking_up_in_the_airlock:

label deciding_what_to_do:

  menu:
  
    "Do nothing and wait for help.":
      jump wait_for_help
    
    "Force open the airlock.":
      jump force_open_the_airlock
    
    "Power up the monitor.":
      jump the_last_log

label wait_for_help:
  "End."
  return

label force_open_the_airlock:
  "End."
  return

label the_last_log:
  "Play on."

label hanc:

label the_locker:

label leaving_the_airlock:

  menu:
  
    "Open the airlock and go outside.":
      jump floating_away
      
    "Ponder on how to hold on outside and ask HANC what to do.":
      jump hancs_advice

label floating_away:
  "End."
  return

label hancs_advice:
  
  menu:
    
    "Leave the ship.":
      jump radio_silence
    
    "Ask HANC about communications outside the ship.":
      jump radio_controls

label radio_silence:
  "End."
  return

label radio_controls:
  "Play on."

"Jump to EVA."
jump to_eva