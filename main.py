from bagels.bagels import Bagels

# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    game = Bagels(max_guesses=10, num_digits=3)
    game.run()
