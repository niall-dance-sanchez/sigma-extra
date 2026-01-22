import re

names = ['Finn  Bindeballe',
         'Geir Anders Berge',
         'HappyCodingRobot',
         'Ron Cromberge',
         'Sohil']


# Find people with first and last names only
regex = '^\w+\s+\w+$'
for name in names:
    result = re.search(regex, name)
    if result:
        print(result)


# Search for word char sequence starting with C
regex = 'C\w'
for name in names:
    match = re.search(regex, name)
    if match:
        print(name)
        print(match.span())
        print(match.group())

names = ['Brian Daugette',
         'Veronica Supersonica',
         'Tony Gasparovic',
         'Patrick Germann',
         'm!sha']

# Find people with first and last names only using groups to choose first or last name
regex = '^(?P<fn>\w+)\s+(?P<ln>\w+)$'
for name in names:
    match = re.search(regex, name)
    if match:
        print(name)
        print(match.group(1))
        print(match.group(2))
        print(match.group('fn'))
        print(match.group('ln'))

# Detect the last name
regex = '^[a-zA-Z!]+$'
for name in names:
    if re.search(regex, name):
        print(name)

# Scan for block of lower case letters
regex = '[a-z]+'
for name in names:
    matches = re.findall(regex, name)
    if matches:
        print(matches)

# OR

for name in names:
    matches = re.finditer(regex, name)
    for match in matches:
        print(match)
