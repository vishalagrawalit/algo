# Pythonic Way for String Matching

#It returns True if pattern is present in text, otherwise it will return False.
def match_string(text, pattern):
    if pattern in text:
        return True
    return False
