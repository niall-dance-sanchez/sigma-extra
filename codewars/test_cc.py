from caesar_cypher import extract_words, count_valid_words, shift_character


def test_extract_words_basic_1():

    assert extract_words("Hello world") == ["hello", "world"]


def test_extract_words_basic_2():

    assert extract_words("justoneword") == ["justoneword"]


def test_extract_words_basic_3():

    assert extract_words("blahBlah?    &&world!!!") == ["blahblah", "world"]


def test_extract_words_basic_4():

    assert extract_words(".  $£%££$@%") == []


def test_count_valid_words_normal_input1():

    assert count_valid_words(["hello", "world"], ["hello", "world"]) == 2


def test_count_valid_words_normal_input2():

    assert count_valid_words(["A", "E", "FFFF"], ["A", "B", "C"]) == 1


def test_shift_character_valid1():

    assert shift_character("a", 1) == "b"


def test_shift_character_valid2():

    assert shift_character("n", 2) == "p"


def test_shift_character_valid3():

    assert shift_character("f", -2) == "d"


def test_shift_character_valid4():

    assert shift_character("a", -2) == "y"


def test_shift_character_valid5():

    assert shift_character("z", 2) == "b"
