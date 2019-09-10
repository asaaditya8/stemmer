from src.stem import PorterStemmer


def test_step1a():
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

def test_step1b():
    stemmer = PorterStemmer()
    test_cases = {
        "feed": "feed",
        "agreed": "agree",
        "plastered": "plaster",
        "bled": "bled",
        "motoring": "motor",
        "sing": "sing"
    }
    for k in test_cases:
        assert stemmer(k) == test_cases[k]