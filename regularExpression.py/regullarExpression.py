import re
'''
# Regular Expression
target = 'abababbaba'
pattern = re.compile('bb')

matcher = re.finditer(pattern, target)

for match in matcher:
    print(match.start(), ',,,,,,,,,,,', match.end(), ',,,,,,,,,,,', match.group())
'''



target = 'abababbaba'
matcher = re.finditer('aba', target)

for match in matcher:
    print(match.start(), ',,,,,,,,,,,', match.end(), ',,,,,,,,,,,', match.group())