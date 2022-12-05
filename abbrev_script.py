def Abbreviator(txt_file):
    """This script is designed to read a text file (txt) containing list
    of names of some kind and generate three-letter abbreviations for each of these objects.
    Some functions was created to help achieve this.
    """
    # Import random and set seed to 1
    import random
    random.seed(1)

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
        return vc

    """Function to select unique index number from words after removing the first character. 
    This index are arranged in ascending order to obey the rule where two further letters in 
    name are selected in order 
    """
    def uniq_ind(joined_word):
        index = []
        # generate random numbers that fall in the range of the current word
        gen = random.randint(0, len(joined_word)-1)
        for x in range(2):
            while gen in index:
                gen = random.randint(0, len(joined_word)-1)
            index.append(gen)
        # Sort the numbers generated in ascending order
        index.sort()
        return index
        
    """Function to make abbreviations. It loops through each word in the list and extract the 
    first letter as a constant, followed by two further letters with the help of the previous 
    function.
    """
    def extract_letters(lst):
        # Empty list to hold abbreviation strings
        all_abbre = []
        # Empty list to hold the remaining letters after removing the first letter.
        part = []
        all_abbre.append(lst[0][0])
        for each in lst:
            first_out = each[1:]
            part.append(first_out)
        joined = ''.join(part)
        joined = joined.replace(' ', '')
        ind = uniq_ind(joined)
        # Adding two letter to the list with the index number generated
        all_abbre.append(joined[ind[0]])
        all_abbre.append(joined[ind[1]])
        str_abb = ''.join(all_abbre)
        return str_abb

    """Here, all functions created above are put to use to perform the task. 
    """
    # Remove apostrophes and non-letter character
    new_word = remove_punctuation(txt_file)
    # Empty list to hold the new results, words followed by its abbreviation.
    abb_let = []
    # loop through the clean names, seperate any joined words, and extract letters.
    # Add results to the empty list above.
    for word in new_word:
        if any(x in word for x in others):
            sep = seperate_compound(word=word)
            abb = extract_letters(sep)
            abb_let.append(word)
            abb_let.append(abb)
        else:
            abb = extract_letters([word])
            abb_let.append(word)
            abb_let.append(abb)
    
    # Creating file output name as per requirements
    input_name = txt_file.split('.')[0]
    sur_name = 'Omidiji'
    output_name = (f'{sur_name.lower()}_{input_name.lower()}_abbrevs.txt')
    
    # writing the results to the created file above
    with open(output_name, 'w') as file:
        file.write('\n'.join(abb_let))  

# Script based condition to run if script is in main scope 
if __name__ == '__main__':
    file_name = input('Enter file name: ')
    Abbreviator(txt_file=file_name)