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
        "sing": "sing",
        "conflated": "conflate",
        "troubled": "trouble",
        "sized": "size",
        "hopping": "hop",
        "tanned": "tan",
        "falling": "fall",
        "hissing": "hiss",
        "fizzed": "fizz",
        "failing": "fail",
        "filing": "file",
    }
    for k in test_cases:
        assert stemmer(k) == test_cases[k]


def test_step1c():
    stemmer = PorterStemmer()
    test_cases = {
        "happy" : "happi",
        "sky" : "sky",
    }
    for k in test_cases:
        assert stemmer(k) == test_cases[k]


def test_step2():
    stemmer = PorterStemmer()
    test_cases = {
        "relational"      : "relate",
        "conditional"     :  "conditionrational" ,
        "valenci"         :  "valence" ,
        "hesitanci"       :  "hesitance" ,
        "digitizer"       :  "digitize" ,
        "conformabli"     :  "conformable" ,
        "radicalli"       :  "radical" ,
        "differentli"     :  "different" ,
        "vileli"          :  "vile" ,
        "analogousli"     :  "analogous" ,
        "vietnamization"  :  "vietnamize" ,
        "predication"     :  "predicate" ,
        "operator"        :  "operate" ,
        "feudalism"       :  "feudal" ,
        "decisiveness"    :  "decisive" ,
        "hopefulness"     :  "hopeful" ,
        "callousness"     :  "callous" ,
        "formaliti"       :  "formal" ,
        "sensitiviti"     :  "sensitive" ,
        "sensibiliti"     :  "sensible" ,

    }
    for k in test_cases:
        assert stemmer(k) == test_cases[k]

def test_step3():
    stemmer = PorterStemmer()
    test_cases = {
        "triplicate"   :  "triplic" ,
        "formative"      :  "form" ,
        "formalize"    :  "formal" ,
        "electriciti"  :  "electric" ,
        "electrical"  :  "electric" ,
        "hopeful"      :  "hope" ,
        "goodness"      :  "good" ,

    }
    for k in test_cases:
        assert stemmer(k) == test_cases[k]

def test_step4():
    stemmer = PorterStemmer()
    test_cases = {
        "revival"   :  "reviv" ,
        "allowance"   :  "allow" ,
        "inference"   :  "infer" ,
        "airliner"   :  "airlin" ,
        "gyroscopic"   :  "gyroscop" ,
        "adjustable"   :  "adjust" ,
        "defensible"   :  "defens" ,
        "irritant"   :  "irrit" ,
        "replacement"   :  "replac" ,
        "adjustment"   :  "adjust" ,
        "dependent"   :  "depend" ,
        "adoption"   :  "adopt" ,
        "homologou"   :  "homolog" ,
        "communism"   :  "commun" ,
        "activate"   :  "activ" ,
        "angulariti"   :  "angular" ,
        "homologous"   :  "homolog" ,
        "effective"   :  "effect" ,
        "bowdlerize"   :  "bowdler" ,

    }
    for k in test_cases:
        assert stemmer(k) == test_cases[k]

def test_step5a():
    stemmer = PorterStemmer()
    test_cases = {
        "probate"     :  "probat" ,
        "rate"        :  "rate" ,
        "cease"       :  "ceas" ,

    }
    for k in test_cases:
        assert stemmer(k) == test_cases[k]

def test_step5b():
    stemmer = PorterStemmer()
    test_cases = {
        "controll"       :  "control" ,
        "roll"    :  "roll" ,
    }
    for k in test_cases:
        assert stemmer(k) == test_cases[k]
