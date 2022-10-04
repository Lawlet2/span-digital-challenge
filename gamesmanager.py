import re

from operator import attrgetter, itemgetter


from constants import (
    FILENAME_INPUT_TYPE,
    STDIN_INPUT_TYPE,
    GAME_DRAW,
    GAME_WIN, 
    OUTPUT_FILENAME)

class GamesManager():
    """
    Class used to parse the games results, calulate teams points
    and return the sorted teams in descending order
    """
    
    _teams = {}
    filename_input_type = FILENAME_INPUT_TYPE
    stdin_input_type = STDIN_INPUT_TYPE
    game_draw = GAME_DRAW
    game_win = GAME_WIN

    @classmethod
    def _get_points(cls, first_team_score: int, sec_team_score: int) -> tuple:
        """
        Returns the points for each team based on lose, win or draw
        """

        first_team_points = 0
        sec_team_points = 0

        if first_team_score == sec_team_score:
            first_team_points += cls.game_draw
            sec_team_points += cls.game_draw
        elif first_team_score > sec_team_score:
            first_team_points += cls.game_win
        elif sec_team_score > first_team_score:
            sec_team_points += cls.game_win

        return first_team_points, sec_team_points


    @classmethod
    def _set_teams_points(cls, team: str, team_points: int) -> None:
        """
        If the team exists in _teams adds the team points otherwise
        set the first team points for the given team
        """

        team = team.strip()
        if  cls._teams.get(team):
            cls._teams[team] = cls._teams.get(team) + team_points
        else:
            cls._teams[team] = team_points


    @classmethod
    def _parse_game_results(cls, game: str) -> None:
        """
        Parse the game results and calls _set_teams_points
        to create and update the _teams dict
        """
        first_team, first_team_score, sec_team, sec_team_score = re.findall(
            r'([a-zA-Z\s]+|[0-9]+)', game.strip())
        first_team_points, sec_team_points = cls._get_points(
            first_team_score, sec_team_score)
        cls._set_teams_points(first_team, first_team_points)
        cls._set_teams_points(sec_team, sec_team_points)


    def __new__(cls, input_type: str = stdin_input_type, filename: str = ""):
        """
        Creates the object based on the input type
        """
        if input_type == cls.stdin_input_type:
                games_results = int(input("Enter the number of games\n"))
                while games_results > 0:
                    gr = input()
                    cls._parse_game_results(gr)
                    games_results -= 1

        elif input_type == cls.filename_input_type:
                with open(filename, "r") as file:
                    for line in file.readlines():
                        cls._parse_game_results(line)
        
        return super().__new__(cls)

    def order_results(self):
        """
        Write the ordered scores in a .txt file
        """
        sorted_by_score = sorted(
            sorted(self._teams.items(), 
            key=itemgetter(0), 
            reverse=True), 
            key=itemgetter(1), 
            reverse=False)

        ordered_scores = reversed(sorted_by_score)

        with open(OUTPUT_FILENAME, "w") as f:
            for id, ord_score in enumerate(ordered_scores, 1):
                team = ord_score[0]
                current_score = ord_score[1]
                points_text_format = "pts" if current_score > 2 or current_score == 0 else "pt"
                f.write(f"{id}. {team}, {current_score} {points_text_format}\n")
