""" Write and test three functions that each take two words (strings) as parameters and
return sorted lists (as defined above) representing respectively:
Letters that appear in at least one of the two words.
Letters that appear in both words.
Letters that appear in either word, but not in both.
Hint: These could all be done programmatically, but consider carefully what topic we
have been discussing this week! Each function can be exactly one line."""

def letters_in_either(word1, word2):
    return sorted(set(word1).union(word2))

def letters_in_both(word1, word2):
    return sorted(set(word1).intersection(word2))

def letters_in_either_but_not_both(word1, word2):
    return sorted(set(word1).symmetric_difference(word2))

if __name__ == "__main__":
    name_challenger = "John Wick"
    name_contender = "Martinez"

    print("Letters in either word:", letters_in_either(name_challenger, name_contender))
    print("Letters in both words:", letters_in_both(name_challenger, name_contender))
    print("Letters in either, but not both:", letters_in_either_but_not_both(name_challenger, name_contender))
