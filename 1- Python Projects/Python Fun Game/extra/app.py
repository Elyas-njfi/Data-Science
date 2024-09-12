import argparse
from game import play_game

def main():
    parser = argparse.ArgumentParser(description="Play the Random Array Game.")
    parser.add_argument("user_number", nargs='?', type=int, help="Number of elements in the random array.")

    args = parser.parse_args()
    
    if args.user_number is None:
        print("Welcome to the Random Array Game!")
        print("To play the game, enter a number.")
        print("If you needed any help: (python app.py -h) OR (python app.py --help)")
    else:
        user_number = args.user_number
        play_game(user_number)

if __name__ == "__main__":
    main()
