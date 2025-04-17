import Maze

def view(grid):
	for i in range(len(grid)):
		for j in range(len(grid[i])):

			if grid[i][j] == Maze.EMPTY:
			print("  ", end = "")

			elif grid[i][j] == Maze.WALL:
			print("##", end = "")

			elif grid[i][j] == Maze.START:
			print("^^", end = "")

			elif grid[i][j] == Maze.END:
			print("$$", end = "")

			elif grid[i][j] == Maze.VISITED:
			print("..", end = "")

			else:
			raise AssertionError

		print()


	print("Find a solution to get from ^^ to $$, using the characters " + "'" + NORTH + "', '" + EAST + "', '" + SOUTH + "' and '" + WEST + "'" + " (for north, east, south and west).")
	solution = input("Your solution: ")
	currentRow = 1
	currentCol = 0
	done = False
	solved = False
	charIndex = 0
	solutionLength = len(solution)

	while not done and charIndex < solutionLength:

		direction = solution[charIndex]
		print("Location: (" + str(currentRow) + ", " + str(currentCol) 
				+ "), next direction: '" + direction + "'")

		if direction == NORTH:
			currentRow -= 1

		elif direction == EAST:
			currentCol += 1

		elif direction == SOUTH:
			currentRow += 1

		elif direction == WEST:
			currentCol -= 1

		else:
			print("GG go next buddy") # Invalid direction.

		if (currentRow < 0 or currentCol < 0 or currentRow >= len(grid) or currentCol >= len(grid[currentRow])):
			done = True
			print("wow unlucky tbh ") # Out of bounds.

		else:
			if grid[row][col] == Maze.EMPTY:
				grid[row][col] = Maze.VISITED

			elif grid[row][col] == Maze.WALL:
				done = True
				print("uninstall") # Hit wall.

			elif grid[row][col] == Maze.END:
				done = True
				solved = True
				print("You somehow scaled :skull") # Solved.

			else:
				pass # Do nothing

		charIndex += 1
# end-while


		if not solved:
			print("MESSAGE 5") # Did not reach the end.


		for i in range(len(grid)):
			for j in range(len(grid[i])):

				if grid[i][j] == Maze.EMPTY:
					print("  ", end = "")

				elif grid[i][j] == Maze.WALL:
					print("##", end = "")

				elif grid[i][j] == Maze.START:
					print("^^", end = "")

				elif grid[i][j] == Maze.END:
					print("$$", end = "")

				elif grid[i][j] == Maze.VISITED:
					print("..", end = "")

				else:
					raise AssertionError

		print()

