def hello():
    return "Hello, world!"

def greet(name):
    return f"Hello, {name}!"

def calc(a, b):
    return a * b


# -----------------------------
# Task 4: Data Type Conversion
# -----------------------------

def data_type_conversion(value, data_type):
    try:
        if data_type == "int":
            return int(value)
        elif data_type == "float":
            return float(value)
        elif data_type == "str":
            return str(value)
        else:
            return f"You can't convert {value} into a {data_type}."
    except ValueError:
        return f"You can't convert {value} into a {data_type}."


# -----------------------------
# Task 5: Grading With *args
# -----------------------------

def grade(*args):
    try:
        average = sum(args) / len(args)
    except TypeError:
        return "Invalid data was provided."

    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


# -----------------------------
# Task 6: Repeat Using a For Loop
# -----------------------------

def repeat(string, count):
    result = ""
    for _ in range(count):
        result += string
    return result


# -----------------------------
# Task 7: Student Scores (**kwargs)
# -----------------------------

def student_scores(mode, **kwargs):
    if mode == "mean":
        scores = kwargs.values()
        average = sum(scores) / len(scores)
        return average

    elif mode == "best":
        best_score = None
        best_name = None
        for name, score in kwargs.items():
            if best_score is None or score > best_score:
                best_score = score
                best_name = name
        return best_name


# -----------------------------
# Task 8: Titleize
# -----------------------------

def titleize(text):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = text.split()

    if not words:
        return ""

    result_words = []

    for i, word in enumerate(words):
        # Always capitalize first and last word
        if i == 0 or i == len(words) - 1:
            result_words.append(word.capitalize())
        else:
            if word in little_words:
                result_words.append(word)
            else:
                result_words.append(word.capitalize())

    return " ".join(result_words)


# -----------------------------
# Task 9: Hangman
# -----------------------------

def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result


# -----------------------------
# Task 10: Pig Latin
# -----------------------------

def pig_latin(text):
    words = text.split()
    result_words = []
    vowels = "aeiou"

    for word in words:
        # If it starts with a vowel
        if word[0] in vowels:
            result_words.append(word + "ay")
        else:
            # Move consonant prefix
            prefix_end = 0
            for i, letter in enumerate(word):
                if letter in vowels:
                    prefix_end = i
                    break

            consonant_prefix = word[:prefix_end]
            rest_of_word = word[prefix_end:]
            pig_word = rest_of_word + consonant_prefix + "ay"
            result_words.append(pig_word)

    return " ".join(result_words)