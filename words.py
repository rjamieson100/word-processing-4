def get_sample_word_list():
    return ["morning", "coffee", "donut", "computer"]

def all_vowels(word_list):
     return ["BAT", "BET", "BIT", "BOT", "BUT"]


"""
Given a list, letter x, and two indecies, determines
which index x occurs at most for each word in
the list.

@param: word_list = The list of words word_list will scan.
@param: letter = the letter to check indecies for.
@param: num_1 = the first index to check.
@param: num_2 = the second index to check.
@return: the index of the given two which x occurs most,
         if the two indecies have equal occurances of x
         -1 will be returned, if one of the given indecies
         if out of range for all words -2 is returned. 
"""
def here_or_there(word_list, letter, num_1, num_2):
    num_1_counter = 0
    num_2_counter = 0
    invalid_index = True
    
    for x in (word_list):
        if (len(x) >= 5) & (num_1 < len(x)) & (num_2 < len(x)):
            invalid_index = False
            if x[num_1] == letter:
                num_1_counter += 1
            
            if x[num_2] == letter:
                num_2_counter += 1
                
    if invalid_index:
        return -2
    elif num_1_counter > num_2_counter:
        return num_1
    elif num_1_counter < num_2_counter:
        return num_2
    else:
        return -1
                
words = get_sample_word_list()

print(here_or_there(words, "m", 2, 3))

