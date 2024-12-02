a=1
print(a+a)
# Aanpassen element in tuple op indirecte wijze , want direct kan immers niet
Steden_tuple= ("As", "Hoeselt", "Gent", "Gent")
print(Steden_tuple)
Steden_list = list(Steden_tuple)
Steden_list[2] = "Brussel"
Steden_tuple = tuple(Steden_list)
print(Steden_tuple)
