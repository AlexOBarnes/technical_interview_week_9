'''Tests for main.py coding problem solution'''
from main import get_word_points, draw_players_rack, read_dictionary, filter_dictionary


def test_get_word_points():
    assert get_word_points("GUARDIAN") == 10

def test_get_word_points_1():
    assert get_word_points("gUarDiAN") == 10

def test_get_word_points_empty():
    assert get_word_points("") == 0

def test_draw_players_rack():
    assert len(draw_players_rack()) == 7

def test_draw_players_rack_type():
    assert isinstance(draw_players_rack(),list)

def test_read_dictionary_type():
    assert isinstance(read_dictionary(),list)

def test_read_dictionary_length():
    assert len(read_dictionary()) == 178691

def test_read_dictionary_first_word():
    assert read_dictionary()[0] == "aa"

def test_filter_dictionary():
    assert len(filter_dictionary(["G","U","A","R","D","I","A","N"])) != len(read_dictionary())
    assert "guardian" in filter_dictionary( ["G", "U", "A", "R", "D", "I", "A", "N"])
