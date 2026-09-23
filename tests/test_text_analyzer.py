import pytest

from text_analyzer import Character


def test_character_accepts_a_single_character_string():
    character = Character("a")

    assert character.value == "a"


@pytest.mark.parametrize("value", ["", "ab"])
def test_character_rejects_strings_that_are_not_one_character_long(value):
    with pytest.raises(ValueError, match="exactly one character"):
        Character(value)


def test_character_rejects_non_string_values():
    with pytest.raises(TypeError, match="must be a string"):
        Character(1)


@pytest.mark.parametrize(
    ("char", "display"),
    [("x", "x"), (" ", "<space>"), ("\n", "<newline>"), ("\t", "<tab>")],
)
def test_character_display(char, display):
    assert Character(char).display() == display
