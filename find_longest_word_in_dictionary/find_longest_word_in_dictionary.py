# https://techdevguide.withgoogle.com/paths/foundational/find-longest-word-in-dictionary-that-subsequence-of-given-string#!
# Given a string S and a set of words D, find the longest word in D that is a subsequence of S.
# Word W is a subsequence of S if some number of characters, possibly zero, can be deleted from S to form W, without reordering the remaining characters.
# Note: D can appear in any format (list, hash table, prefix tree, etc.
# For example, given the input of S = "abppplee" and D = {"able", "ale", "apple", "bale", "kangaroo"} the correct output would be "apple"
# The words "able" and "ale" are both subsequences of S, but they are shorter than "apple".
# The word "bale" is not a subsequence of S because even though S has all the right letters, they are not in the right order.
# The word "kangaroo" is the longest word in D, but it isn't a subsequence of S.

def find_longest_word_in_dictionary_that_subsequence_of_given_string(S, D):
    indexer = {}
    result = ''
    maxLen = -1

    for i, letter in enumerate(S):
        if letter not in indexer:
            indexer[letter] = []
        indexer[letter].append(i)

    for word in D:
        prevB = -1
        for letter in word:
            if letter not in indexer:
                # if the word in D has a letter that S doesn't have,
                # it's impossible for it to be a subsequence
                break
            for position in indexer[letter]:
                if position > prevB:
                    prevB = position
                    break
            else:
                break
        else:
            # subsequence found
            if len(word) > maxLen:
                result = word
                maxLen = len(word)
    return result

        
            
                
            
