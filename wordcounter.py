def words(f):
    word = f.split()
    number_of_words = len(word)
    return(number_of_words)

def repetitions(f):
    characters = {}
    for character in f:
        lowered_character = character.lower()
        if lowered_character not in characters:
            characters[lowered_character] = 1
        else:
            characters[lowered_character] += 1
    return characters

def get_book_path(path):
    with open(path) as f:
        return f.read()

def reports(file_contents):
    char_counter = repetitions(file_contents)
    list_of_dict = []
    for key in char_counter:
        if key.isalpha():
            list_of_dict.append({"name":key, "num":char_counter[key]})
    
    def sort_on(dict):
        return dict["num"]

    list_of_dict.sort(reverse=True, key=sort_on)    
    result = ""
    for key in list_of_dict:
        result += f"The '{key['name']}' character was found {key['num']} times\n"
    return result
