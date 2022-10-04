"""
Span Digital Code Challenge
"""
import argparse

from gamesmanager import GamesManager

from constants import FILENAME_INPUT_TYPE

def main():
    """
    Creates a GamesManager obj based on the --filename argument
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--filename", 
        type=str,
        default=None,
        required=False,
        help="Enter the file that contains the games results",
        )
    args = parser.parse_args()

    if args.filename:
        gmanager = GamesManager(input_type=FILENAME_INPUT_TYPE, filename=args.filename)

    else:
        gmanager = GamesManager()

    gmanager.order_results()
                
if __name__ == "__main__":
    main()