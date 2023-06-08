def dirReduc(arr):
    stack = []
    for direction in arr:
        if len(stack) == 0:
            stack.append(direction)
        else:
            if direction == 'NORTH' and stack[-1] == 'SOUTH':
                stack.pop()
            elif direction == 'SOUTH' and stack[-1] == 'NORTH':
                stack.pop()
            elif direction == 'EAST' and stack[-1] == 'WEST':
                stack.pop()
            elif direction == 'WEST' and stack[-1] == 'EAST':
                stack.pop()
            else:
                stack.append(direction)
    return stack


values = [["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"], ["NORTH", "WEST", "SOUTH", "EAST"]]

for v in values:
    print(dirReduc(v))