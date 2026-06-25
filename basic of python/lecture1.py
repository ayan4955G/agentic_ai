spice_mix =  set()

print(f"initial spice mix: {id(spice_mix)}")
print(f"initial spice mix: {spice_mix}")

spice_mix.add("cardamon")
spice_mix.add("Ginger")
 
#  in the python the variables are imutable but when you reassign the variable
# it simply change the reference of the variable of the given variable

# operating overloading

base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

full_liquid = base_liquid + extra_flavor
print(f"full liquid: {full_liquid}")

strong_brew = ["black tea", "water"] * 3
print(f"strong brew: {strong_brew}")

# "CINNAMON"  i want to make it to the 

raw_spice_data = bytearray(b"CINNAMON")

raw_spice_data.replace(b"CINNA", b"CARD")
print("bytes:",raw_spice_data)