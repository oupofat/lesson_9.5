def consonant_remove(word):
    vowels = "aeoiu"
    begin_letter = ""
    remaining_letter = ""
    state = "open"
    for letter in word:
        if state == "open":
            
            if letter in vowels:
                state = "closed"
                remaining_letter += letter
            else:
                begin_letter+= letter
        else:
            remaining_letter += letter
    piggy = remaining_letter + begin_letter + "ay"
    return piggy
def split_string(string):
    pig_word = []
    word_list=string.split(" ")
    for element in word_list:
        pig_word.append(consonant_remove(element))
    return " ".join(pig_word)
string = "What the Heck"        
print(split_string(string))