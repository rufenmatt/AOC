with open("input.txt", "r") as doc:
	inst = doc.read().split("\n")
	for n in range(len(inst)):
		inst[n] = [inst[n][0], int(inst[n][1:])]

x, y = 0, 0
facing = "E"
directions = ["E", "S", "W", "N"]

def solveA(direct, dist):
	global x, y
	if direct == "N":
		y += dist
	elif direct == "S":
		y -= dist
	elif direct == "E":
		x += dist
	elif direct == "W":
		x -= dist

for i in inst:
	action, value = i[0], i[1]
	if action == "F":
		solveA(facing, value)
	elif action == "L" or action == "R":
		turns = int(value / 90)
		current_idx = directions.index(facing)
		if action == "L":
			facing = directions[(current_idx - turns) % 4]
		else:
			facing = directions[(current_idx + turns) % 4]
	else:
		solveA(action, value)

print("Part 1 solution:", abs(x) + abs(y))

x, y = 0, 0
posX, posY = 10, 1

def SolveB(direct, dist):
	global posX, posY
	if direct == "N":
		posY += dist
	elif direct == "S":
		posY -= dist
	elif direct == "E":
		posX += dist
	elif direct == "W":
		posX -= dist

for i in inst:
	action, value = i[0], i[1]
	if action == "F":
		x += value * posX
		y += value * posY
	elif action == "L" or action == "R":
		turns = int(value / 90) % 4
		if action == "L":
			turns = 4 - turns
		if turns == 1:
			posX, posY = posY, -posX
		elif turns == 2:
			posX, posY = -posX, -posY
		elif turns == 3:
			posX, posY = -posY, posX
	else:
		SolveB(action, value)

print("Part 2 solution:", abs(x) + abs(y))
