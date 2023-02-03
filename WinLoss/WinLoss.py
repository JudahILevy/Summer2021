import json

# Load the json file into memory
file = open('wins.json')
data = json.load(file)

# List of team names
teams = ['BRO', 'BSN', 'CHC', 'CIN', 'NYG', 'PHI', 'PIT', 'STL']

# The grid containing all the team records
matrix = []
for i in range(len(teams)):
    # This team's wins
    wins = []
    current_team = teams[i]
    for j in range(len(teams)):
        current_opponent = teams[j]
        # placeholder value for the 'record against itself'
        if i == j:
            wins.append(-1)
        else:
            wins.append(data[current_team][current_opponent]['W'])
    matrix.append(wins)


# Print the matrix containing the records
def display():
    for i in range(len(teams)):
        print('\t', teams[i], end='')
    print()

    for i in range(len(teams)):
        print(teams[i], end='')

        for j in range(len(matrix[i])):
            if matrix[i][j] == -1:
                print('\t\t--', end='')
            else:
                print('\t\t', matrix[i][j], end='')
        print()


display()
