# Task 6: Implement a class Team with len so that len(team) returns the number of players.

class Team:
    def __init__(self, name, n_players):
        self.name = name
        self.n_players = n_players

    def __len__(self):
        return self.n_players
    
aryan_team = Team("aryan_team", 10)
print(len(aryan_team))