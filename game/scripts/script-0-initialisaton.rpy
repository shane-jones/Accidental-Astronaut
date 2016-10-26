# Run the declartions.
call declaratons

# The game starts here.

label start:
  
  # Temporary menu for debugging.
  
  menu:
  
    "Start at airlock.":
      jump waking_up_in_the_airlock
    
    "Start at EVA.":
      jump outside
    
    "Start at Bridge.":
      jump walking_to_the_bridge
    
    "Start at Cargo Hold.":
      jump cargo_hold
    
    "Start at Shuttle.":
      jump shuttle_in_cargo_hold
  
return