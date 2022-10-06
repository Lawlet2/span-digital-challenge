import io

import pytest

import main as main_module


def test_main_wrong_input(monkeypatch):
    """ 
    Test if raises EOFError for input with 
    only the enter number games value
    """
    sample_input = "3\n"
    monkeypatch.setattr('sys.stdin', io.StringIO(sample_input))
    with pytest.raises(EOFError): 
        main_module.main()  

def test_main_correct_input(monkeypatch):
    """ 
    Test not raises exception with 
    correct input
    """
    sample_input = "2\nLions 3, Zebras 4\n, Snakes 5, Turtles 6"
    monkeypatch.setattr('sys.stdin', io.StringIO(sample_input))
    main_module.main()


def test_main_correct_file_input(monkeypatch):
    """ 
    Test not raises exception with 
    correct input
    """
    sample_input = "--file='test.txt'"
    monkeypatch.setattr('sys.stdin', io.StringIO(sample_input))
    main_module.main()

