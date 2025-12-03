with open("./day1_input.txt", "r") as f:
    rotation_string = f.read()


# rotation_string = """
# L68
# L30
# R248
# L5
# R60
# L55
# L1
# L99
# R14
# L82
# """

zero_count = 0
current_position = 50
rotations = rotation_string.strip().split("\n")
for rotation in rotations:
    #print(f"Current position before rotation {rotation}: {current_position}")
    passed_zero = False
    
    if rotation[0] == "L":
        if current_position == 0:
            zero_count -= 1
        current_position -= int(rotation[1:])
        while current_position < 0:
            current_position += 100
            zero_count += 1

    elif rotation[0] == "R":
        current_position += int(rotation[1:])
        while current_position >= 100:
            passed_zero = True
            current_position -= 100
            zero_count += 1
    
    if current_position == 0 and not passed_zero:
        zero_count += 1

    #print(f"Zero count after rotation {rotation}: {zero_count}")
print(f"Zero count: {zero_count}")