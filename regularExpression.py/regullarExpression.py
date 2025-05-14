# import re
'''
# Regular Expression
target = 'abababbaba'
pattern = re.compile('bb')

matcher = re.finditer(pattern, target)

for match in matcher:
    print(match.start(), ',,,,,,,,,,,', match.end(), ',,,,,,,,,,,', match.group())
'''

'''

target = 'abababbaba'
matcher = re.finditer('aba', target)

for match in matcher:
    print(match.start(), ',,,,,,,,,,,', match.end(), ',,,,,,,,,,,', match.group())
    '''

'''
# search function - match 
import re

pattern = input('Enter the pattern: ')
target = 'python is simple to learn '

m = re.match(pattern, target)
if m!=None:
    print('pattern found begning at string ')

else:
    print('pattern not found at begning of target string')
'''

'''
# search function - search

import re

pattern = input('Enter the pattern: ')
target = 'python is simple to learn '

m = re.search(pattern, target)
if m!=None:
    print('pattern found  ')

else:
    print('pattern not found ')

'''
'''
# search function - full match


import re
pattern = input('Enter the pattern: ')
target = 'python is simple to learn '

m = re.fullmatch(pattern, target)
if m!=None:
    print('pattern found  ')
else:
    print('pattern not found ') 
    '''
#  '''
# # search function - substitute
# import re
# res = re.sub('a', '#', 'ababababababab ')
# print(res)
#  '''
'''
search function - substitute n
import re
res = re.subn('a', '#', 'ababababababab ')
print(res)

'''
'''

import re

pattern = '[6-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'

or

pattern = '[6-9]\d{9}'

or

pattern = '[6-9][0-9]{9}'

mob = input("Enter your mobile number: ")
m=re.fullmatch(pattern , mob)
if m!=None:
    print("valid mobile no ")
else:
    print("invalid mobile no ")
    
'''
import re 
pattern = '[M][H][0][0-4][A-Z][A-Z][0-9]{4}'

noplate = input ("Enter a no ")

m=re.fullmatch(pattern , noplate)
if m!=None:
    print("valid no plate ")
else:
    print("invalid  no plate ")
