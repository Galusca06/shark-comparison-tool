
# Application used for shark species comparison.
# Metrics used will be : 1. shark habitat; 2.estimated maximum speed; 3.maximum length
# The shark species are : Shortfin Mako sharks, Great White sharks, Bull sharks, Tiger sharks, Blue sharks
print("===== Shark Comparison Tool =====")
great_white= {
    "species": "Great White Shark",
   "distribution": "temperate and subtropical oceans",
   "max_length_m": 6.0,
   "max_speed_kmh": 40
}

bull_shark= {
    "species": "Bull Shark",
    "distribution": "tropical/coastal waters",
    "max_length_m": 4.0,
    "max_speed_kmh": 19
}

tiger_shark={
    "species": "Tiger Shark",
    "distribution": "tropical/subtropical coastal waters",
    "max_length_m": 5.5,
    "max_speed_kmh": 32.0
}

blue_shark={
    "species": "Blue Shark",
    "distribution": "open ocean worldwide",
    "max_length_m": 4.0,
    "max_speed_kmh": 39.0
}

mako_shark={
    "species": "Shortfin Mako",
    "distribution": "open ocean",
    "max_length_m": 4.0,
    "max_speed_kmh": 64.0   
}

sharks=[great_white,bull_shark,tiger_shark,blue_shark,mako_shark]

for number, shark in enumerate(sharks, start=1):
    print(number,shark["species"])



choice1= int(input(" \n Choose a shark (1-5)\n"))
choice2= int(input(" Choose a shark (1-5)\n "))

if choice1 < 1 or choice1 > 5 or choice2 < 1 or choice2 > 5:
    print("Not so fast cowboy! Only numbers between 1-5")
    raise SystemExit

elif choice1 == choice2:
    print("\nGotta be different sharks, my man!\n")
    raise SystemExit

else:
    print("\nI like them numbers!\n")
    
index1=choice1-1
index2=choice2-1

selected_shark1=sharks[index1]
selected_shark2=sharks[index2]

print(f"Species: {selected_shark1['species']}")
print(f"Distribution: {selected_shark1['distribution']}")
print(f"Max Length: {selected_shark1['max_length_m']} m")
print(f"Max Speed: {selected_shark1['max_speed_kmh']} km/h \n")

print(f"Species: {selected_shark2['species']}")
print(f"Distribution: {selected_shark2['distribution']}")
print(f"Max Length: {selected_shark2['max_length_m']} m")
print(f"Max Speed: {selected_shark2['max_speed_kmh']} km/h")

print("\n RESULTS OF COMPARISON \n")

if selected_shark1["max_length_m"] > selected_shark2["max_length_m"]:
    print(f"{selected_shark1['species']} is longer than {selected_shark2['species']}")

elif selected_shark1["max_length_m"] < selected_shark2["max_length_m"]:
    print(f"{selected_shark2['species']} is longer than {selected_shark1['species']}.")
else:
    print(f"{selected_shark1['species']} and {selected_shark2['species']} have the same maximum length.")


if selected_shark1["max_speed_kmh"] > selected_shark2["max_speed_kmh"]:
    print (f"{selected_shark1['species']} is faster than {selected_shark2['species']}.")

elif selected_shark1["max_speed_kmh"] < selected_shark2["max_speed_kmh"]:
    print(f"{selected_shark2['species']} is faster than {selected_shark1['species']}.")
else:
    print(f"{selected_shark1['species']} and {selected_shark2['species']} have the same maximum speed.")
    
print(f"{selected_shark1['species']}: {selected_shark1['distribution']} | {selected_shark2['species']}: {selected_shark2['distribution']}")
