def main():
    book_path = "\\\\wsl.localhost\\Ubuntu\\home\\admin_01\\workspace\\github.com\\Bootstinkt\\bookbot\\books\\frankenstein.txt"
    text = get_book_text(book_path)
    return text

    
def get_book_text(path):
    with open(path) as f:
        return f.read()


def word_count():
    counter = 0
    words = main().split()
    for word in words:
        counter +=1 
    print(f"---Begin report of books/frankenstein.txt---\n{counter} words found in the document\n"  )


def char_counter():
    counter = {}
    text = main()
    for word in text:
        if word.isalpha():
            if word.lower() in counter:
                counter[word.lower()] += 1
            else:
                counter[word.lower()] = 1
    return counter

def sort_on(dict):
    return dict[1]

def output(dict):
    for key in dict:
        print(f"The {key} character was found {dict[key]} times")
    print(f"--- End report ---")

         
word_count()
char_dic = char_counter()
sorted_char_dic = dict(sorted(char_dic.items(), key=sort_on, reverse=True))
output(sorted_char_dic)


