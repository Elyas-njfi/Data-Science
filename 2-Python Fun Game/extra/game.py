import numpy as np

class RandomArrayGame:
    def __init__(self, user_number):
        """
        Initialize the RandomArrayGame object.

        Parameters:
        - user_number (int): Number of elements in the random array.
        """
        self.user_number = user_number
        self.random_array = np.array([])
        self.max_value = 0

    def generate_random_array(self):
        """
        Generate a random array with elements between 0 and 100.
        """
        self.random_array = np.random.randint(0, 101, self.user_number)

    def find_max_value(self):
        """
        Find the maximum value in the generated random array.
        """
        self.max_value = np.max(self.random_array)

    def display_result(self):
        """
        Display the generated random array, its maximum value, and the result (Win or Fail).
        """
        print(f"Random array: {self.random_array}")
        print(f"Maximum value: {self.max_value}")

        if self.max_value > 70:
            print("Win!")
        else:
            print("Fail")

def play_game(user_number):
    """
    Play the Random Array Game.

    Parameters:
    - user_number (int): Number of elements in the random array.
    """
    game = RandomArrayGame(user_number)
    game.generate_random_array()
    game.find_max_value()
    game.display_result()
