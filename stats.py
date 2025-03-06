def number_of_words(string):
    return len(string.split())

def counting_character(string):
    unique_characters = {}
    for char in string:
        lower_char = char.lower()
        
        unique_characters.setdefault(lower_char, 1)
        unique_characters[lower_char] += 1
        
    return unique_characters

def sorter(dictionary):
    def sort_on(dict):
        return dict["num"]
    
    list_of_dictionaries = []
    
    for char, count in dictionary.items():
        list_of_dictionaries.append({"char": char, "num": count})
        
    list_of_dictionaries.sort(reverse=True, key=sort_on)
    
    return(list_of_dictionaries)