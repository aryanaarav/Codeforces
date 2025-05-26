my_dict = {"a": 1, "b": 2}

target_value = 2  # Value you know
key = my_dict.get(target_value)  # Use get to find the key associated with the value

if key:
    print(key)  # This will print "b"
else:
    print("No key found for value", target_value)
