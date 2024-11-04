def main(path):
    print(f"--- Begin report of {path} ---")
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
    words = file_contents.split()
    print(f"{len(words)} words found in the document")
    char_dic = {}
    for word in words:
        for char in word:
            if char.isalpha():
                char_lower = char.lower()
                char_dic[char_lower] = char_dic.get(char_lower,0) + 1
    for k,v in char_dic.items():
        print(f" The '{k}' letter appears {v} times.")
    print("--- End Report ---")
            
    


main("books/frankenstein.txt")
