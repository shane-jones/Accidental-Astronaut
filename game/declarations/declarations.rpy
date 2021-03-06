label declarations:

#testing on mac

# All image and sound files used in this declaration are referenced in the readme file
# as part of this Visual Novel.


###############################################################################
# Character declarations
###############################################################################

define a = Character('Captain Abrahams')
define h = Character('Holloway')
define ht = Character('Holloway', image='holloway')
define H = Character('HANC', image='hanc', who_font='bitwise.ttf')
define HT = Character('HANC -Text', image='hanc', who_font='bitwise.ttf')
define j = Character('Jinx')
define jt = Character('Jinx', image='jinx')                                                  
define l = Character('Log Computer')
define p = Character ('PC')

###############################################################################
# Character images
###############################################################################

# Captain Slade Abrahams

image abrahams a = "images/characters/abrahams/abrahams-headshot.png"
image abrahams b = "images/characters/abrahams/abrahams-piercing-stare-arms-down.png"
image abrahams c = "images/characters/abrahams/abrahams-upset-big-yawn-while-standing.png"
image abrahams d = "images/characters/abrahams/abrahams-wide-eyed-fear-standard-idle.png"

# Frank Holloway

image holloway a = "images/characters/holloway/holloway-back.png"
image holloway b = "images/characters/holloway/holloway-dead-from-hanc-takeover.png"
image holloway c = "images/characters/holloway/holloway-dead-neck-snap-1.png"
image holloway d = "images/characters/holloway/holloway-dead-neck-snap-2.png"
image holloway e = "images/characters/holloway/holloway-dying-backwards.png"
image holloway f = "images/characters/holloway/holloway-floating.png"
image holloway g = "images/characters/holloway/holloway-goodbye-jinx.png"
image holloway h = "images/characters/holloway/holloway-intense-stare-walking-forward-looking-right.png"
image holloway i = "images/characters/holloway/holloway-looked-in-the-box.png"
image holloway j = "images/characters/holloway/holloway-slammed.png"
image holloway k = "images/characters/holloway/half-holloway-facing-away.png"
image holloway l = "images/characters/holloway/holloway-back-resized.png"
image holloway m = "images/characters/holloway/holloway-dead-neck-snap-resized.png"
image side holloway = "images/characters/holloway/holloway-thinking.png"

#This 
#image holloway n = "images/characters/holloway/holloway-arm.png"

image holloway floating = "images/characters/holloway/holloway-floating.png"
image holloway slammed = "images/characters/holloway/holloway-slammed.png"

# HANC Handy Autonomous Networking Computer

image hanc a = "images/characters/hanc/hanc-soundwave.jpg"
image hanc b = "images/characters/hanc/side-hanc-soundwave.jpg"
image side hanc silent = "images/characters/hanc/side-hanc.png"
image side hanc radio = "images/characters/hanc/side-hanc-soundwave.jpg"
image side hanc = "images/characters/hanc/side-hanc-soundwave.jpg"


# Jinx Takanoma

image jinx a = "images/characters/jinx/jinx-a-cheeky-smile-leaning-forward-elbows-on-knees.png"
image jinx b = "images/characters/jinx/jinx-anticipating-female-standing-jump-in-place.png"
image jinx c = "images/characters/jinx/jinx-anticipating-reclined-facepalm.png"
image jinx d = "images/characters/jinx/jinx-anticipating-sitting-slightly-aggravated.png"
image jinx e = "images/characters/jinx/jinx-displeased-laying-vomiting-into-a-bag.png"
image jinx f = "images/characters/jinx/jinx-laughing-softly-hands-on-hips-looking-over-shoulder.png"
image jinx g = "images/characters/jinx/jinx-none-reaction-to-getting-clipped-while-walking-unaware.png"
image jinx h = "images/characters/jinx/jinx-piercing-stare-arms-behind-back.png"
image jinx i = "images/characters/jinx/jinx-thoughtful-smile-backward-run-turning-right.png"
image jinx j = "images/characters/jinx/jinx-thoughtful-smile-walking.png"
image jinx k = "images/characters/jinx/jinx-totally-calm-arms-down.png"
image jinx l = "images/characters/jinx/jinx-wide-eyed-fear-leaning-forward-right-hand-supporting.png"
image jinx m = "images/characters/jinx/jinx-totally-calm-arms-down-standing-closeup.png"
image jinx n = "images/characters/jinx/jinx-piercing-stare-arms-behind-back-crop-page.png"
image jinx o = "images/characters/jinx/jinx-sitting-and-shaking-finger.png"

image jinx listening = "images/characters/jinx/jinx-anticipating-sitting-slightly-aggravated.png"
image jinx standing_thinking = "images/characters/jinx/jinx-anticipating-female-standing-jump-in-place.png"
image side jinx = "images/characters/jinx/jinx-thinking.png"



###############################################################################
# Background images
###############################################################################

# Miscs

image black = "#000"

# 1 Airlock

image bg airlock-a = "images/backgrounds/1-airlock/airlock-1(copy).png"
image bg airlock-b = "images/backgrounds/1-airlock/airlock-monitor.png"
image bg airlock-c = "images/backgrounds/1-airlock/airlock-doorice.png"
image bg airlock-d = "images/backgrounds/1-airlock/airlock-4.png"
image bg airlock-e = "images/backgrounds/1-airlock/airlock-4-with-door-open.png"
image bg airlock-f = "images/backgrounds/1-airlock/holloway-floating-away.png"
image bg airlock-g = "images/backgrounds/1-airlock/captain-background(copy).png"

image bg airlock-door-open = "images/backgrounds/1-airlock/airlock-4-with-door-open.png"
image bg airlock-door-closed = "images/backgrounds/1-airlock/airlock-4.png"


# 2 EVA

image bg eva-a = "images/backgrounds/2-eva/eva-2.png"
image bg eva-b = "images/backgrounds/2-eva/eva-space.jpg"
image bg eva-c = "images/backgrounds/2-eva/eva-with-a-frame.png"
image bg eva-d = "images/backgrounds/2-eva/eva-with-planet-background.png"
image bg eva-e = "images/backgrounds/2-eva/eva-with-bolts-fired.png"
image bg eva-f = "images/backgrounds/2-eva/eva-with-a-frame-and-door-open.png"

image bg eva-empty-space = "images/backgrounds/2-eva/eva-space.jpg"
image bg eva-with-planet = "images/backgrounds/2-eva/eva-with-planet-background.png"
image bg eva-with-a-frame = "images/backgrounds/2-eva/eva-with-a-frame.png"
image bg eva-open-airlock = "images/backgrounds/2-eva/eva-with-a-frame-and-door-open.png"
image bg eva-bolts-fired = "images/backgrounds/2-eva/eva-with-bolts-fired.png"

# 3 Bridge

image bg bridge-a = "images/backgrounds/3-bridge/bridge-20161002-124219.jpg"
image bg bridge-b = "images/backgrounds/3-bridge/bridge-20161007-193840.jpg"
image bg bridge-c = "images/backgrounds/3-bridge/bridge-door.png"
image bg bridge-d = "images/backgrounds/3-bridge/HANC-background.png"
image bg bridge-e = "images/backgrounds/3-bridge/bridge-with-stars.png"
# Was moved/deleted?
#image bg bridge-f = "images/backgrounds/3-bridge/shuttle-in-cargohold.png"
image bg bridge-g = "images/backgrounds/3-bridge/bridge-close-up.png"
image bg bridge-h = "images/backgrounds/3-bridge/bridge-door-open.png"

# 4 Cargo Hold
image bg cargo-hold-a = "images/backgrounds/4-cargo-hold/cargo-hold-1.png"
image bg cargo-hold-b = "images/backgrounds/4-cargo-hold/cargo-hold-2.png"
image bg cargo-hold-c = "images/backgrounds/4-cargo-hold/cargo-hold-3.png"
image bg cargo-hold-d = "images/backgrounds/4-cargo-hold/cargo-hold-20161007-181949.jpg"
image bg cargo-hold-e = "images/backgrounds/4-cargo-hold/cargo-hold-20161007-181955.jpg"
image bg cargo-hold-f = "images/backgrounds/4-cargo-hold/cargo-hold-bay-1.png"
image bg cargo-hold-g = "images/backgrounds/4-cargo-hold/cargo-hold-bay-2.png"
image bg cargo-hold-h = "images/backgrounds/4-cargo-hold/cargo-hold-door.png"
image bg cargo-hold-i = "images/backgrounds/4-cargo-hold/cargo-hold-shuttle-in-cargo-hold-1280x720.jpg"
image bg cargo-hold-j = "images/backgrounds/4-cargo-hold/cargo-hold-two-containers.png"
image bg cargo-hold-k = "images/backgrounds/4-cargo-hold/cargo-hold-with-shuttle.png"
image bg cargo-hold-l = "images/backgrounds/4-cargo-hold/cargo-shuttle-door-closed.png"
image bg cargo-hold-m = "images/backgrounds/4-cargo-hold/shuttle-hold.png"

image bg shuttle-in-cargo-hold = "images/backgrounds/4-cargo-hold/cargo-hold-shuttle-in-cargo-hold-1280x720.jpg" 

# 5 Shuttle
# The shuttle image with transparent windows will need to be used with a bg image.
# See objects

image bg shuttle-a = "images/backgrounds/5-shuttle/cargo-hold-shuttle.png"
image bg shuttle-b = "images/backgrounds/5-shuttle/shuttle-in-cargo-hold-1280x720.png"
image bg shuttle-c = "images/backgrounds/5-shuttle/shuttle-leaving-illustrious.png"
image bg shuttle-d = "images/backgrounds/5-shuttle/flight-deck.png"
image bg shuttle-e = "images/backgrounds/5-shuttle/goodbye-illustrious.png"
image bg shuttle-f = "images/backgrounds/5-shuttle/land.png"
image bg shuttle-g = "images/backgrounds/5-shuttle/rear-of-shuttle.png"
image bg shuttle-h = "images/backgrounds/5-shuttle/jinx-cheeky-smile-leaning-elbows-on-knees-in-shuttle.png"
image bg shuttle-i = "images/backgrounds/5-shuttle/Ship_enters_atmosphere.png"
image bg shuttle-j = "images/backgrounds/5-shuttle/Shuttle-comming-in-to-land.png"
image bg shuttle-k = "images/backgrounds/5-shuttle/Ship_enters_atmosphere2.png"
image bg shuttle-l = "images/backgrounds/5-shuttle/game-over.png"

###############################################################################
# Objects
###############################################################################

image shuttle a = "images/objects/shuttle-with-drawn-picture-filter.png"
show shuttle a 

image shuttle-clear-windows = "images/objects/shuttle-clear-windows-1280x720.png"

image helmet-black = "images/objects/helmet-black-1280x720.png"

image long-rope = "images/objects/long-rope.png"

image long-rope = "images/objects/long-rope-2.png"

image two-tethers = "images/objects/two-tethers.png"

image holloway-arm = "images/objects/holloway-arm.png"

image airlock-door-open-transparent = "images/backgrounds/1-airlock/airlock-4-with-door-open-transparent.png"

image captains-manual = "images/objects/captains-manual.png"

###############################################################################
# Music
###############################################################################

define audio.space_main_theme = "sounds/music/space-main-theme.mp3"

###############################################################################
# Sound effects
###############################################################################

define audio.beep_sound = "sounds/effects/beep-sound.mp3" 
define audio.breathing_sound = "sounds/effects/breathing-sound.mp3"
define audio.ice_sound = "sounds/effects/ice-sound.mp3"
define audio.illustrious_sound = "sounds/effects/illustrious.mp3"

# 3 EVA
define audio.tether_snap_sound = "sounds/effects/cartoon-springboard-ruler-twang-pitched-shifted-up-001.mp3"
define audio.pained_grunt_sound = "sounds/effects/noisecreations-nc-sfx-fistpunch-fistpunch-vocal-01.mp3"
define audio.explosive_bolt_sound = "sounds/effects/explosion-loud-internal-reverberant.mp3"
define audio.distant_explosive_bolt_sound = "sounds/effects/explosion-distant-002.mp3"
define audio.repressurisation = "sounds/effects/industrial-machine-air_pressure-machine.mp3"
define audio.door_release = "sounds/effects/johnj-science-fiction-door-open-air-pressure-release.mp3"
define audio.breathing = "sounds/effects/human-breath-inhale-and-exhale-through-snorkel.mp3"

# Cargo Hold
define audio.door_open = "sounds/effects/science_fiction_space_door_slide_internal_001.mp3"
define audio.door_close = "sounds/effects/science_fiction_space_door_slide_internal_002.mp3"

# 5 Shuttle
define audio.hanc_50_sound = "sounds/effects/hanc-50.mp3"
define audio.launch_sound = "sounds/effects/launch.mp3"
                                                         
###############################################################################
# Character Voices - Sounds
###############################################################################                                                                                      
 
# 1 Airlock
define audio.hanc_1_4_0_sound = "sounds/effects/hanc-1-4-0.mp3"
define audio.hanc_1_4_0b_sound = "sounds/effects/hanc-1-4-0b.mp3"
define audio.hanc_1_6_0_sound = "sounds/effects/hanc-1-6-0.mp3"
define audio.hanc_1_8_0_sound = "sounds/effects/hanc-1-8-0.mp3"
define audio.hanc_1_8_0b_sound = "sounds/effects/hanc-1-8-0b.mp3"
define audio.hanc_1_10_0_sound = "sounds/effects/hanc-1-10-0.mp3"

# 2 EVA
define audio.hanc_2_0_1_sound = "sounds/effects/hanc-2-0-1.mp3"
define audio.hanc_2_0_3_sound = "sounds/effects/hanc-2-0-3.mp3"
define audio.hanc_2_0_3b_sound = "sounds/effects/hanc-2-0-3b.mp3"
define audio.hanc_2_2_0_sound = "sounds/effects/hanc-2-2-0.mp3"
define audio.hanc_2_2_2_sound = "sounds/effects/hanc-2-2-2.mp3"
define audio.hanc_2_2_2b_sound = "sounds/effects/hanc-2-2-2b.mp3"
define audio.hanc_2_3_0_sound = "sounds/effects/hanc-2-3-0.mp3"
define audio.hanc_2_3_2_sound = "sounds/effects/hanc-2-3-2.mp3"
define audio.hanc_2_3_2b_sound = "sounds/effects/hanc-2-3-2b.mp3"
define audio.hanc_2_3_2c_sound = "sounds/effects/hanc-2-3-2c.mp3"


# 3 Bridge
define audio.hanc_3_0_1_sound = "sounds/effects/hanc-3-0-1.mp3"
define audio.hanc_3_0_1b_sound = "sounds/effects/hanc-3-0-1b.mp3"
define audio.hanc_3_0_1c_sound = "sounds/effects/hanc-3-0-1c.mp3"
define audio.hanc_3_1_0_sound = "sounds/effects/hanc-3-1-0.mp3"
define audio.hanc_3_1_0b_sound = "sounds/effects/hanc-3-1-0b.mp3"
define audio.hanc_3_1_1_sound = "sounds/effects/hanc-3-1-1.mp3"
define audio.hanc_3_1_2_sound = "sounds/effects/hanc-3-1-2.mp3"
define audio.hanc_3_1_2b_sound = "sounds/effects/hanc-3-1-2b.mp3"
define audio.hanc_3_1_2c_sound = "sounds/effects/hanc-3-1-2c.mp3"


# 4 Cargo Hold
define audio.hanc_4_0_0_sound = "sounds/effects/hanc-4-0-0.mp3"
define audio.hanc_4_0_1_sound = "sounds/effects/hanc-4-0-1.mp3"
define audio.hanc_4_0_2_sound = "sounds/effects/hanc-4-0-2.mp3"
define audio.hanc_4_1_1_sound = "sounds/effects/hanc-4-1-1.mp3"
define audio.hanc_4_1_1b_sound = "sounds/effects/hanc-4-1-1b.mp3"
define audio.hanc_4_1_1c_sound = "sounds/effects/hanc-4-1-1c.mp3"
 
 
# 5 Shuttle
define audio.hanc_5_0_1_sound = "sounds/effects/hanc-5-0-1.mp3" 
define audio.hanc_5_1_0_sound = "sounds/effects/hanc-5-1-0.mp3"
define audio.hanc_5_1_1_1_sound = "sounds/effects/hanc-5-1-1-1.mp3"
define audio.hanc_5_1_1_2_sound = "sounds/effects/hanc-5-1-1-2.mp3"
define audio.hanc_5_4_0_sound = "sounds/effects/hanc-5-4-0.mp3"

#### REFERENCE FOR VOICE TO ADD HERE #####

