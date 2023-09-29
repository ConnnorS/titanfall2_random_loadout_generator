import random

# pilot
tactical = ["Cloak", "Pulse Blade", "Grapple", "Stim", "A-Wall", "Phase Shift", "Holo Pilot"]
ordnance = ["Frag Grenade", "Arc Grenade", "Firestar", "Gravity Star", "Electric Smoke","Satchel"]
primary = ["R-201 Carbine", "R-101 Carbine", "Hemlok BF-R", "G2A5", "V-47 Flatline", "CAR", "Alternator", "Volt", "R-97", "Spitfire", "L-Star", "X-55 Devotion",
           "Kraber-AP Sniper", "D-2 Double Take", "Longbow-DMR", "EVA-8 Auto", "Mastiff", "Sidewinder SMR", "EPG-1", "R-6P Softball", "EM-4 Cold War"]
secondary = ["B3 Wingman", "Hammond P2016", "RE-45 Auto"]
anti_titan = ["Charge Rifle", "MGL Mag Launcher", "LG-97 Thunderbolt", "Archer"]
kit1 = ["Power Cell", "Fast Regen", "Ordnance Expert", "Phase EmbarK"]
kit2 = ["Kill Report", "Wallhang", "Hover", "Low Profile", "Titan Hunter"]

# titan
titan = ["Ion", "Scorch", "Northstar", "Ronin", "Tone", "Legion", "Monarch"]
titan_main_kit = ["Assault Chip", "Stealth Auto-Eject", "Turbo Engine", "Overcore", "Nuclear Ejection", "Counter Ready"]

# titan-specific kits
titan_specific_kits = {
    "Ion": ["Entangled Energy", "Zero-Point Tripwire", "Vortex Amplifier", "Grand Cannon", "Refraction Lens"],
    "Scorch": ["Wildfire Launcher", "Tempered Plating", "Inferno Shield", "Fuel for the Fire", "Scorched Earth"],
    "Northstar": ["Piercing Shot", "Enhanced Payload", "Twim Traps", "Viper Thrusters", "Threat Optics"],
    "Ronin": ["Ricochet Rounds", "Thunderstorm", "Temporal Anomaly", "Highlander", "Phase Reflex"],
    "Tone": ["Enhanced Tracker Rounds", "Reinforced Particle Wall", "Pulse-Echo", "Rocket Barrage", "Burst Loader"],
    "Legion": ["Enhanced Ammo Capacity", "Sensor Array", "Bulwark", "Light-Weight Alloys", "Hidden Compartment"],
    "Monarch": ["Shield Amplifier", "Energy Thief", "Rapid Rearm", "Survival of the Fittest"]
}

# choose the titan
titan_choice = random.choice(titan)

# print the loadout
print("Your loadout...")
print("Tactical: " + random.choice(tactical))
print("Ordnance: " + random.choice(ordnance))
print("Primary: " + random.choice(primary))
print("Secondary: " + random.choice(secondary))
print("Anti-Titan: " + random.choice(anti_titan))
print("Kit 1: " + random.choice(kit1))
print("Kit 2: " + random.choice(kit2))
print()
print("Your titan...")
print("Titan: " + titan_choice)
print("Kit: " + random.choice(titan_main_kit))
print(titan_choice + " Kit: " + random.choice(titan_specific_kits[titan_choice]))