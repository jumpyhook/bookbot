import string 

def main():
    lv_file="books/frankenstein.txt"
    with open(lv_file) as f:
        file_contents = f.read()
        # print(file_contents)
        lv_letter_dict = dict.fromkeys(string.ascii_lowercase, 0)
        lv_total = 0
        lv_char_count = 0 
        lv_word_count = len(file_contents.split())
        for key in lv_letter_dict:
            lv_char_count = countcharacters(key,file_contents )
            lv_letter_dict.update({key: lv_char_count})
            lv_total = lv_total + lv_char_count
        lv_letter_dict.update({' ': file_contents.count(' ')})

        report(lv_file, lv_letter_dict, lv_word_count)
        




def countWords(lv_string):
    lv_count = len(lv_string.split())
    return lv_count

def countcharacters(lv_character, lv_string):
    lowered_string = lv_string.lower()
    lv_count = lowered_string.count(lv_character)
    return(int(lv_count))

def report(lv_filename, lv_letter_dict, lv_word_count):

    # Title
    print(f"--- Begin report of {lv_filename} ---")
    print(f"{lv_word_count} words found in the document")
    print(" ")
    lv_letter_dict.popitem()
    for key in lv_letter_dict:
        value=lv_letter_dict[key]
        print(f"The '{key}' character was found {value} times")

    print("--- End report ---")

main()