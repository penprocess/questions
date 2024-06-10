def letter_count(s):
    count_dict = {}
    for i in s: 
        if i in count_dict:
            count_dict[i] += 1 
        else:
            count_dict[i] = 1
    return count_dict

        
s = input("Enter the word: ")
print(letter_count(s))