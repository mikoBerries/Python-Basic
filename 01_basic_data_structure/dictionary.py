# Dictionaries are unoreded mapping to storing object using key value
# similar to map in java or go
# Dictionaries cannot be sorted

# construct
my_dictionary = {"jhon":100,"doe":10}
# accessing
print(my_dictionary)
print(my_dictionary.get("jhon"))
print(my_dictionary["doe"])

# unlike map dictionary can hold KEY string with multiple diffrent value inside
unccomon_but_supported = {"key1":123,"key2":[0,20,31,1],"key3":{"other_dictionary1":"this is nested dictionary 1","other_dictionary2":"this is nested dictionary 2"}}

print(unccomon_but_supported)
print(unccomon_but_supported["key3"])
print(unccomon_but_supported["key3"]["other_dictionary1"])
print(unccomon_but_supported["key3"]["other_dictionary2"])


print(unccomon_but_supported["key3"]["other_dictionary2"].upper())

# adding key to dictionary
unccomon_but_supported["key4"]="this is new"
print(unccomon_but_supported)
# updating
unccomon_but_supported["key4"]="this is new but updated!"
print(unccomon_but_supported)

# just getting keys 
print(unccomon_but_supported.keys())
# just getting value
print(unccomon_but_supported.values())
# getting paired keys and value
print(unccomon_but_supported.items())