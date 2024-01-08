#************************************************************Basic String Programs******************************************
# Python program to check whether the string is Symmetrical or Palindrome

#I/p = 'malayalam'
#o/p= 'malayalam'

lis=[]
str='khokho'
for i in range(len(str)-1,-1,-1):
    lis.append(str[i])
final_string=''.join(lis)
if final_string==str:
    print('Palindrome')
else:
    print("Not palindrome")





# Reverse words in a given String in Python





# Ways to remove i’th character from string in Python

# Input: 'Geeks123For123Geeks'
# Output: GeeksForGeeks
# Explanation: In This, we have removed the '123' character from a string.

lis=[]
for i in 'Geeks123For123Geeks':
    if i in ('123'):
        continue
    else:
        lis.append(i)
final_string=''.join(lis)
print(final_string)



# Find length of a string in python (4 ways)

str="Piyush"
count=0
for  i in str:
    count=count+1
print(f"the length of string is {count}")







# Python program to print even length words in a

# Input: s = "This is a python language"
# Output: This is python language
str='This is a python language'
lis=[]
for i in str.split():
    if len(i)%2==0:
        lis.append(i)

final_string=' '.join(lis)
print(final_string)




# Python – Uppercase Half String

# Input : test_str = 'geeksforgeek'
# Output : geeksfORGEEK
# Explanation : Latter half of string is uppercased.




# Python program to capitalize the first and last character of each word in a string


# Input: hello world
# Output: HellO WorlD
lis=[]
str='hello world'
for i in str.split():
    lis.append(i)
print(lis)




# Python program to check if a string has at least one letter and one number


# Input: welcome2ourcountry34
# Output: True
#
# Input: stringwithoutnum
# Output: False
str='stringwithoutnum'
print(str.isalnum())



# Python | Program to accept the strings which contains all vowels

# Input : geeksforgeeks
# Output : Not Accepted
# All vowels except 'a','i','u' are not present
str='geeksforgeeks'
if 'a' in str and 'e' in str and 'i' in str and 'o' in str and 'u' in str:
    print('Accepeted')
else:
    print('Not accepted')



# Python | Count the Number of matching characters in a pair of string

# Input : str1 = 'abcdef'
#         str2 = 'defghia'
# Output : 4
# (i.e. matching characters :- a, d, e, f)

print(len(set('abcdef').intersection(set('defghia'))))





# Python program to count number of vowels using sets in given string


# Input : GeeksforGeeks
# Output : No. of vowels : 5
# Explaination: The string GeeksforGeeks contains 5 vowels in it 4 letter of 'e' and 1 'o'.

str='GeeksforGeeks'
count=0
for i in str:
    if i in ('aeiou'):
        count=count+1
print(f"no of vowel present isn string are {count}")





# Python Program to remove all duplicates from a given string


# Input : geeksforgeeks
# Output : geksfor

lis=[]
for i in 'geeksforgeeks':
    if i not in lis:
        lis.append(i)
final_string=''.join(lis)
print(final_string)




# Python – Least Frequent Character in String

# The original string is : GeeksforGeeks
# The minimum of all characters in GeeksforGeeks is : f

str='GeeksforGeeks'
lis=[]
dic={}
for i in str:
    lis.append(i)
for i in lis:
    dic[i]=lis.count(i)
for key,val in dic.items():
    if val==min(dic.values()):
        print(key)




# Python | Maximum frequency character in String


# The original string is : GeeksforGeeks
# The maximum of all characters in GeeksforGeeks is : e

str='GeeksforGeeks'
lis=[]
dic={}
for i in str:
    lis.append(i)
for i in lis:
    dic[i]=lis.count(i)
for key,val in dic.items():
    if val==max(dic.values()):
        print(key)




# Python – Odd Frequency Characters


# Input : test_str = 'geekforgeeks'
# Output : ['r', 'o', 'f', 's']

str='geekforgeeks'
lis=[]
main_list=[]
for i in str:
    lis.append(i)
for i in lis:
    dic[i]=lis.count(i)

for key,val in dic.items():
    if val%2!=0:
        main_list.append(key)
print(main_list)





# Python – Specific Characters Frequency in String List


# Input :
test_list = ['geeksforgeeks is best for geeks']
chr_list = ['e', 'b', 'g', 'f']
# Output : {‘g’: 3, ‘e’: 7, ‘b’: 1, ‘f’ : 2}
# Explanation : Frequency of certain characters extracted.



lis1=list(''.join(test_list))
dic={}
for i in chr_list:
    dic[i]=lis1.count(i)
print(dic)




# Python | Frequency of numbers in String


# The original string is : geeks4feeks is No. 1 4 geeks
# Count of numerics in string : 3






# Python | Program to check if a string contains any special character

#
# Input : Geeks$For$Geeks
# Output : String is not accepted.
# Input : Geeks For Geeks
# Output : String is accepted



# Find words which are greater than given length k

# Input : str = "hello geeks for geeks
#           is computer science portal"
#         k = 4
# Output : hello geeks geeks computer
#          science portal
# Explanation : The output is list of all
# words that are of length more than k.

str = "hello geeks for geeks is computer science portal"
lis=[]
for i in str.split():
    if len(i)>4:
        lis.append(i)
print(' '.join(lis))


# Python program for removing i-th character from a string



# Input : Geek
#         i = 1
# Output : Gek
#
# Input : Peter
#         i = 4
# Output : Pete
str='Peter'
for i in range(len(str)):
    if i==4:
        continue
    else:
        print(str[i])


# Python program to split and join a string

# Split the string into list of strings
#
# Input : Geeks for Geeks
# Output : ['Geeks', 'for', 'Geeks']

lis=[]
for i in str:
    lis.append(i)


# Join the list of strings into a string based on delimiter ('-')
#
# Input :  ['Geeks', 'for', 'Geeks']
# Output : Geeks-for-Geeks

lis=['Geeks', 'for', 'Geeks']
print('-'.join(lis))



# Python | Check if a given string is binary string or not


#
# Input: str = "01010101010"
# Output: Yes
#
# Input: str = "geeks101"
# Output: No

str = "geeks101"
for i in str:
    if i in ('01'):
        print('yes')
    else:
        print('No')
        break




# Python | Find all close matches of input string from a list




#
# Input : patterns = ['ape', 'apple',
#                   'peach', 'puppy'],
#           input = 'appel'
# Output : ['apple', 'ape']






# Python program to find uncommon words from two Strings


# Input : A = “Geeks for Geeks”,  B = “Learning from Geeks for Geeks”
# Output : [‘Learning’, ‘from’]

A = 'Geeks for Geeks'
B = 'Learning from Geeks for Geeks'









#**********************************************************Advance String Programs********************************************

# Python | Convert numeric words to numbers
#
# Input: S = “zero four zero one”
# Output: 0401
#
# Input: S = “four zero one four”
# Output: 4014

# Python | Word location in String



# The original string is : geeksforgeeks is best for geeks
str='geeksforgeeks is best for geeks'
wrd='best'
# The location of word is : 3
lis=str.split()
for i in range(len(lis)):
    if lis[i]==wrd:
        print(i+1)

