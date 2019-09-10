from src.stem import PorterStemmer


def test_step1():
    stemmer = PorterStemmer()
    test_cases = {
        "caresses": "caress",
        "ponies": "poni",
        "ties": "ti",
        "caress": "caress",
        "cats": "cat"
    }
    for k in test_cases:
        assert stemmer(k) == test_cases[k]