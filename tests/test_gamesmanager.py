import io

import pytest

from gamesmanager import GamesManager
from constants import OUTPUT_FILENAME


def test_get_points_method():
    """ 
    Test the points for each team based on lose, win or draw
    """
    win = GamesManager._get_points(5, 2)
    lose = GamesManager._get_points(1, 9)
    draw = GamesManager._get_points(6, 6)

    assert win == (3, 0)
    assert lose == (0, 3)
    assert draw == (1, 1)


def test_set_teams_points_method():
    """ 
    Test if the team exists in _teams adds the team points otherwise
    set the first team points for the given team
    """
    GamesManager._teams = {}
    
    teams_list = [
        ("Tarantulas", "6"), ("Lions", "5"), 
        ("FC Awesome", "1"), ("Snakes", "1"),
        ("Grouches", "0"), ("First Team Sample", "0")]

    for team in teams_list:
        GamesManager._set_teams_points(team[0], int(team[1]))

    expected_dict = {
        'Tarantulas': 6, 'Lions': 5, 
        'FC Awesome': 1, 'Snakes': 1, 
        'Grouches': 0, 'First Team Sample': 0}

    assert GamesManager._teams == expected_dict


def test_parse_game_results_method():
    """
    Test if parse the game results update the _teams dict
    """
    GamesManager._teams = {}

    games_list = [
        "Lions 3, Snakes 3",
        "Tarantulas 1, FC Awesome 0",
        "Lions 1, FC Awesome 1",
        "Tarantulas 3, Snakes 1",
        "Lions 4, Grouches 0"
    ]

    for game in games_list:
        GamesManager._parse_game_results(game)

    expected_dict = {
        'Lions': 5, 'Snakes': 1, 
        'Tarantulas': 6, 'FC Awesome': 1, 
        'Grouches': 0}
    
    assert GamesManager._teams == expected_dict


def test_get_result_ids_method(monkeypatch):
    """
    Test if returns a dict that contains the score and its 
    calculated list of ids
    """
    sample_input = """9\n
                      Lions 3, Snakes 3\n
                      Tarantulas 1, FC Awesome 0\n
                      Lions 1, FC Awesome 1\n
                      Tarantulas 3, Snakes 1\n
                      Lions 4, Grouches 0\n
                      Tarantulas 0, Grouches 0\n
                      Cats 1, Lobsters 1\n
                      Bears 2, Flies 1\n
                      Turtles 2, Owls 2"""

    monkeypatch.setattr('sys.stdin', io.StringIO(sample_input))
    gmanager = GamesManager()

    ordered_scores = [
        ('Tarantulas', 7), ('Lions', 5), ('Bears', 3), 
        ('Cats', 1), ('FC Awesome', 1), ('Grouches', 1), 
        ('Lobsters', 1), ('Owls', 1), ('Snakes', 1), 
        ('Turtles', 1), ('Flies', 0)]

    result_ids_dict = gmanager.get_result_ids(ordered_scores)

    expected_dict = {
        7: [1], 5: [2], 3: [3], 
        1: [4, 4, 4, 4, 4, 4, 4], 
        0: [11]}

    assert result_ids_dict == expected_dict


@pytest.fixture
def output_filename_var(mocker, tmpdir):
    file = tmpdir.join(OUTPUT_FILENAME)
    return mocker.patch("OUTPUT_FILENAME", new=file, autospec=False)


def test_generate_results_file_method(monkeypatch):
    """
    Test if the results file is created and 
    the content is correct
    """
    sample_input = """9\n
                      Lions 3, Snakes 3\n
                      Tarantulas 1, FC Awesome 0\n
                      Lions 1, FC Awesome 1\n
                      Tarantulas 3, Snakes 1\n
                      Lions 4, Grouches 0\n
                      Tarantulas 0, Grouches 0\n
                      Cats 1, Lobsters 1\n
                      Bears 2, Flies 1\n
                      Turtles 2, Owls 2"""

    monkeypatch.setattr('sys.stdin', io.StringIO(sample_input))
    gmanager = GamesManager(output_filename_var)

    ordered_scores = [
        ('Tarantulas', 7), ('Lions', 5), ('Bears', 3), 
        ('Cats', 1), ('FC Awesome', 1), ('Grouches', 1), 
        ('Lobsters', 1), ('Owls', 1), ('Snakes', 1), 
        ('Turtles', 1), ('Flies', 0)]
        
    gmanager.generate_results_file(ordered_scores)

    expected_result = ("1. Tarantulas, 7 pts\n2. Lions, 5 pts\n3. Bears, 3 pts\n"
                        "4. Cats, 1 pt\n4. FC Awesome, 1 pt\n4. Grouches, 1 pt\n"
                        "4. Lobsters, 1 pt\n4. Owls, 1 pt\n4. Snakes, 1 pt\n"
                        "4. Turtles, 1 pt\n11. Flies, 0 pts")

    with open(OUTPUT_FILENAME, "r") as f:
        assert f.read().split() == expected_result.lstrip().split()


def test_raise_error_negative_input(monkeypatch, caplog):
    """
    Test invalid input format log for negative input
    """
    sample_input = """9\n
                      Lions 3, Snakes 3\n
                      Tarantulas 1, FC Awesome 0\n
                      Lions 1, FC Awesome 1\n
                      Tarantulas -3, Snakes 1\n
                      Lions 4, Grouches 0\n
                      Tarantulas 0, Grouches 0\n
                      Cats 1, Lobsters 1\n
                      Bears 2, Flies 1\n
                      Turtles 2, Owls 2"""

    monkeypatch.setattr('sys.stdin', io.StringIO(sample_input))
    GamesManager()
    expected_log = ("ERROR    root:gamesmanager.py:98 Invalid input format, (sample format -> First Team 2, Second Team 5)\n")
    assert expected_log in caplog.text


def test_raise_error_invalid_input_format(monkeypatch, caplog):
    """
    Test invalid input format log for malformed input
    """
    sample_input = """9\n
                      Lions 3, Snakes 3\n
                      Tarantulas 1, FC Awesome 0\n
                      Lions 1, FC Awesome 1\n
                      Tarantulas -3, Snakes 1\n
                      Lions 4, Grouches 0\n
                      Tarantulas 0, Grouches 0\n
                      Cats 1, Lobsters 1\n
                      Bears 2, Flies 1\n
                      Turtles 2, Owls 2"""

    monkeypatch.setattr('sys.stdin', io.StringIO(sample_input))
    GamesManager()
    expected_log = ("ERROR    root:gamesmanager.py:98 Invalid input format, (sample format -> First Team 2, Second Team 5)\n")
    assert expected_log in caplog.text

