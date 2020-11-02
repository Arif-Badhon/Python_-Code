#Sometimes some words like "localization" or "internationalization" are so long that writing them many 
# times in one text is quite tiresome.

#Let's consider a word too long, if its length is strictly more than 10 characters. 
# All too long words should be replaced with a special abbreviation.

#This abbreviation is made like this: we write down the first and the last letter 
# of a word and between them we write the number of letters between the first and the last letters. 
# That number is in decimal system and doesn't contain any leading zeroes.

#Thus, "localization" will be spelt as "l10n", and "internationalization» will be spelt as "i18n".

#You are suggested to automatize the process of changing the words with abbreviations. 
# At that all too long words should be replaced by the abbreviation and the words that 
# are not too long should not undergo any changes.

#Input
#The first line contains an integer n (1 ≤ n ≤ 100). Each of the following n 
# lines contains one word. All the words consist of lowercase Latin letters and possess 
# the lengths of from 1 to 100 characters.

#Output
#Print n lines. The i-th line should contain the result of replacing of the 
# i-th word from the input data.


#n = int(input("Enter the total number of words: "))

#print(n)
#print(type(n))
#my_list = []

#for x in range(1, n+1):
    #print(x)
    #words = str(input("Enter the word: "))
    
    #if len(words) > 10:
        
        #my_list.append(words[0] + str(len(words) - 2) + words[-1])
    #else:
        #my_list.append(words)


#print(*my_list, sep = "\n")

for _ in range(int(input())):
    s= str(input())
    print (s[0]+str(len(s)-2)+s[-1]) if len(s)>10 else print(s)