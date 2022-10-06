import re
import logging 

from operator import itemgetter
 
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
        try:
            first_team, first_team_score, sec_team, sec_team_score = re.findall(
                r'([a-zA-Z\s]+|[0-9]+)', game.strip())

            first_team_points, sec_team_points = cls._get_points(
            first_team_score, sec_team_score)

            cls._set_teams_points(first_team, first_team_points)
            cls._set_teams_points(sec_team, sec_team_points)
        
        except ValueError:
            logging.error("Invalid input format, (sample format -> First Team 2, Second Team 5)")

            
    def __new__(cls, input_type: str = stdin_input_type, filename: str = "") -> 'GamesManager':
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


    def get_result_ids(self, ordered_scores: list) -> dict:
        """
        Returns a dict that contains the score and its 
        calculated list of ids
        """
        aux_id = 0
        points = {}

        for id, od in enumerate(ordered_scores, start=1):
            current_score = od[1]
            draws = points.get(current_score, [])

            if draws:
                if len(draws) == 1:
                    draws[0] = aux_id
                draws.append(aux_id)
            else:
                aux_id += 1
                points[current_score] = [id]

        return points


    def generate_results_file(self, ordered_scores: list) -> None:
        """
        Generates the .txt file that contains the results
        """
        result_ids = self.get_result_ids(ordered_scores)

        with open(OUTPUT_FILENAME, "w") as result_file:
            for ord_score in ordered_scores:
               team = ord_score[0]
               current_score = ord_score[1]
               points_text_format = "pts" if current_score > 2 or current_score == 0 else "pt"
               line_text_format = f"""{result_ids.get(current_score)[0]}. {team}, {current_score} {points_text_format}\n"""
               result_file.writelines(line_text_format)


    def get_results(self) -> None:
        """
        Main method to order the game results and
        generate the results file
        """
        sorted_by_score = sorted(
            sorted(self._teams.items(), 
            key=itemgetter(0), 
            reverse=True), 
            key=itemgetter(1), 
            reverse=False)
        ordered_scores = list(reversed(sorted_by_score))
        self.generate_results_file(ordered_scores)
