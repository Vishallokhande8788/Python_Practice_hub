# character classes

'''
[abc] 
[a-z]
[A-Z]
[0-9]
[a-zA-Z0-9]
[^abc]
[^a-z]
[^A-Z]
[^0-9]
[^a-zA-Z0-9]

pre define character classes

\d - digit
\D - except digit
\w - word character
\W - except word character
\s - whitespace
\S - except whitespace
a+ - at least one a
a? - at most one a
a* - zero or more a , any number of a

'''
import re
matcher = re.finditer('[a-z]' , 'a5b1C3cDT$%t @73A 8788')

for match in matcher:
    print(match.start(), ',,,,,,,,,,,', match.end(), ',,,,,,,,,,,', match.group())  



