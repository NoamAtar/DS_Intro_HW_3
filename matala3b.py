#A

def read_line(n, file):
        try:
            data = open(file)
            lines=data.readlines()
            type(lines)
            count = 0
            for line in lines:
                count = count + 1
            if type(n) != int:
                 return ("invalid input detected")
            if n > count:
                return (" " +"line " + str(n) + " doesn't exist")
            else:
                 return (str(lines[n-1].rstrip()))
        except:
            return ("file not found")
    
read_line(4, "ex3_text.txt")
read_line(9, "ex3_text.txt")
read_line(25, "ex3_text.txt")
read_line('jdj', "ex3_text.txt")                
read_line(4, "file")  

#B

import re
def longest_words(file):
    try:
        data1 = open(file)
        data2 = data1.read()
        file_without_special_char = re.sub('[^a-zA-Z0-9\n\.]', ' ', data2)
        words1 = re.split("\s|(?<!\d)[,.](?!\d)", file_without_special_char)
        worsd1 = list(filter(None, words1))
        sorte_word = sorted(words1,key=len,reverse=True) 
        
        return(sorte_word[:5])
    except:
        return "file not found"
 
longest_words("ex3_text.txt")    
longest_words("ex4_text.txt")


   
    