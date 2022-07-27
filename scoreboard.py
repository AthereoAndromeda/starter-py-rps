class Scoreboard:
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.draws = 0

    def display(self):
        print("\n==|| Score ||==")
        print("Wins: " + str(self.wins))
        print("Losses: " + str(self.losses))
        print("Draws: " + str(self.draws))