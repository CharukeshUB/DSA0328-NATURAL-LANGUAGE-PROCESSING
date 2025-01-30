#2
states = ["START", "S1", "S2", "ACCEPT"]
current_state = "START"
input_string = "xxabab"
for char in input_string:
    if current_state == "START":
        if char == 'a':
            current_state = "S1"
        else:
            current_state = "START"  # Remain in START if not 'a'

    elif current_state == "S1":
        if char == 'b':
            current_state = "ACCEPT"
        elif char == 'a':
            current_state = "S1"  # Stay in S1 if 'a' is repeated
        else:
            current_state = "START"  # Reset on any other character

    elif current_state == "ACCEPT":
        if char == 'a':
            current_state = "S1"
        else:
            current_state = "START"  # Reset if any character follows 'ab'
if current_state == "ACCEPT":
    print("The string ends with 'ab'.")
else:
    print("The string does not end with 'ab'.")
