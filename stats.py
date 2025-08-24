def get_num_words(text):
    split_text = text.split()
    return len(split_text)

def get_number_of_characters(text):
    result_dictionary = {}
    
    for char in text:
        char = char.lower()
        if char in result_dictionary:
            result_dictionary[char] += 1
        else:
            result_dictionary[char] = 1
    
    return result_dictionary

def sort_dictionary(dictionary):
    sorted_items = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
    return dict(sorted_items)

def print_data(dictionary):
    for key, value in dictionary.items():
        if key.isalpha():
            print(f"{key}: {value}")

    