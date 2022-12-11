def Abbreviator(txt_file):
    """This script is designed to read a text file (txt) containing list
    of names of some kind and generate three-letter abbreviations for each of these objects.
    Some functions was created to help achieve this.
    """


    """Function to remove all apostrophes from each names in the list.
    It clean the names for further processes. 
    """
    # List of non-letter characters that are likely used for compound words
    others = ["-", "_"]
    def remove_punctuation(filename):
        with open(filename, 'r', encoding='utf-8') as open_file:
            content = open_file.read().split('\n')
            # dictionary of non-letter characters that are likely to exist in names
        punctuation = {
            "'":"",
            "+":"",
            "!":"",
            "’":"",
            "`":""
        }
        no_punctuation = []
        # Looping through each word and removing non-letter characters defined in the dictionary
        for i in content:
            remv_punc = i.translate(str.maketrans(punctuation)).upper()
            no_punctuation.append(remv_punc)
        no_punctuation
        return no_punctuation

    """Function to detect any compound word with a non-letter joining them, like those defined
    in the variable (others) above. Once it detects such, it split the word by that character. 
    For words that are single or does not have a non-letter joining them, the function returns 
    a list of word, seperated if more than one.  
    """
    def seperate_compound(word):
        vc = []
        vc1 = []
        if len(word.split()) > 1:
            # Loops through the cleaned names and split by space first 
            for x in word.split():
                for s in others:
                    # Checking if the charaters in others is in any of the splitted words 
                    if s in x:
                        # Split the word by that charater found in the word
                        d=x.split(s)
                        # Add the splitted word to the list defined above
                        vc  += d
                    else:
                        pass
            # Add word that did not fall in the if statement above to the list.
            vc.append(x)
        elif len(word.split()) == 1:
            for x in word.split():
                for s in others:
                    if s in x:
                        d=x.split(s)
                vc+=d
        return vc
    
    values_dict = {
        'A':25, 'B':8, 'C':8, 'D': 9, 'E':35,
        'F':7, 'G':9, 'H':7, 'I':25, 'J':3,
        'K':6, 'L':15, 'M':8, 'N':15, 'O':20,
        'P':8, 'Q':1, 'R':15, 'S':15, 'T':15, 
        'U':20, 'V':7, 'W':7, 'X':3, 'Y':7, 'Z':1
    }

    def low_num_char_selector(string):
        split = [*string]
        new_dict = {}
        for x,y in values_dict.items():
            if x in split:
                new_dict[x] = y
                
        key_lst = list(new_dict.keys())
        val_lst = list(new_dict.values())
        num_lst = []
        for x in split[1:]:
            num_lst.append(new_dict[x])
        num_lst.sort()

        first = num_lst[0]
        sec = num_lst[1]
        val1 = val_lst.index(first)
        val2 = val_lst.index(sec)
        two = key_lst[val1] + key_lst[val2]
        
        arr = []
        split1 = [*string]
        split2 = [*two]
        arr.append(split1.index(split2[0]))
        arr.append(split1.index(split2[1]))
        arr.sort()
        return split1[arr[0]]+split1[arr[1]]
    
    def low_num_char_selector1(string):
        split = [*string]
        new_dict = {}
        for x,y in values_dict.items():
            if x in split:
                new_dict[x] = y
                
        key_lst = list(new_dict.keys())
        val_lst = list(new_dict.values())
        num_lst = []
        for x in split[1:]:
            num_lst.append(new_dict[x])
        num_lst.sort()

        first = num_lst[0]
        val1 = val_lst.index(first)
        one = key_lst[val1]
        return one

    """Here, all functions created above are put to use to perform the task. 
    """
    # Remove apostrophes and non-letter character
    new_word = remove_punctuation(txt_file)
    # Empty list to hold the new results, words followed by its abbreviation.
    abb_let = []
    part = []
    # loop through the clean names, seperate any joined words, and extract letters.
    # Add results to the empty list above.
    for word in new_word:
        string = ''
        if any(x in word for x in others):
            sep = seperate_compound(word=word)
            abb_let.append(sep)
            if len(sep) > 2:
                string += sep[0][0] + sep[1][0] + sep[2][0]
                part.append(word)
                part.append(string)
            elif len(sep) == 2:
                string += sep[0][0] + sep[1][0] + low_num_char_selector1(sep[1])
                part.append(word)
                part.append(string)
        else:
            each = word.split() 
            if len(each) > 2: 
                string += each[0][0] + each[1][0] + each[2][0]
                part.append(word)
                part.append(string)
            elif len(each) == 2:
                string += each[0][0] + each[1][0] + low_num_char_selector1(each[1])
                part.append(word)
                part.append(string)
            elif len(each) == 1:
                chars = each[0]
                string += each[0][0] + low_num_char_selector(chars)
                part.append(word)
                part.append(string)
    print(part)

    # Creating file output name as per requirements
    input_name = txt_file.split('.')[0]
    sur_name = 'Omidiji'
    output_name = (f'{sur_name.lower()}_{input_name.lower()}_abbrevs.txt')
    
    # writing the results to the created file above
    with open(output_name, 'w') as file:
        file.write('\n'.join(part)) 

# Script based condition to run if script is in main scope 
if __name__ == '__main__':
    file_name = input('Enter file name: ')
    Abbreviator(txt_file=file_name)