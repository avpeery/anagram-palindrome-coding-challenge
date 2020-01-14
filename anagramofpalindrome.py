"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.

Examples::

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aba aba")
    True

    >>> is_anagram_of_palindrome("arceacer")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

"""

def make_dict(word):
    new_dict = {}
    for i in word:

        if i not in new_dict:
            new_dict[i] = 0

        new_dict[i] += 1

    return new_dict

def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    if len(word) == 1:
        return True

    new_dict = make_dict(word)

    odd = False

    for count in new_dict.values():
        if count % 2 == 1:
            if odd:
                return False
            odd = True

    return True






if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. AWESOMESAUCE!\n")
