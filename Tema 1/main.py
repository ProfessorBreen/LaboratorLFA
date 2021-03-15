states = set()
final_states = set()
start_states = set()
words = set()
transitions = dict()
ok1 = ok2 = ok3 = 0

# Section 1 - comments
string = input().strip()
while string[0] == '#':
    string = input().strip()

# Section 1
if string == "Sigma:":
    ok1 += 1
    string = input().strip()
    while string != "End":
        stringWords = string.split(" ")
        if len(stringWords) >= 2:
            raise Exception("Too many words on a line")
        words.add(string)
        string = input().strip()
elif string == "States:":
    ok2 += 1
    string = input().strip()
    while string != "End":
        stringWords = string.split(" ")
        if len(stringWords) >= 4:
            raise Exception("Too many attributes on a line")
        for i in range(0, len(stringWords) - 1):
            if stringWords[i].endswith(","):
                stringWords[i] = stringWords[i].removesuffix(",")
        if len(stringWords) == 3:
            if stringWords[1] != "F" and stringWords[1] != "S":
                raise Exception("Unknown attribute of state")
            if stringWords[2] != "F" and stringWords[2] != "S":
                raise Exception("Unknown attribute of state")
            if stringWords[1] == stringWords[1]:
                raise Exception("Identical attributes of state")
            if len(start_states) >= 1:
                raise Exception("There can be only one start state")

            final_states.add(stringWords[0])
            start_states.add(stringWords[0])
        elif len(stringWords) == 2:
            if stringWords[1] == "F":
                final_states.add(stringWords[0])
            elif stringWords[1] == "S":
                if len(start_states) >= 1:
                    raise Exception("There can be only one start state")
                else:
                    start_states.add(stringWords[0])
            else:
                raise Exception("Unknown attribute of state")
        states.add(stringWords[0])
        string = input().strip()
elif string == "Transitions:":
    ok3 += 1
    string = input().strip()
    while string != "End":
        stringWords = string.split(", ")
        if len(stringWords) != 3:
            raise Exception("Too many or too few elements")
        transitions.update({(stringWords[0], stringWords[2]): stringWords[1]})
        string = input().strip()
else:
    raise Exception("Unknown section")

# Section 2 - comments
string = input().strip()
while string[0] == '#':
    string = input().strip()

# Section 2
if string == "Sigma:":
    ok1 += 1
    string = input().strip()
    while string != "End":
        stringWords = string.split(" ")
        if len(stringWords) >= 2:
            raise Exception("Too many words on a line")
        words.add(string)
        string = input().strip()
elif string == "States:":
    ok2 += 1
    string = input().strip()
    while string != "End":
        stringWords = string.split(" ")
        if len(stringWords) >= 4:
            raise Exception("Too many attributes on a line")
        for i in range(0, len(stringWords) - 1):
            if stringWords[i].endswith(","):
                stringWords[i] = stringWords[i].removesuffix(",")
        if len(stringWords) == 3:
            if stringWords[1] != "F" and stringWords[1] != "S":
                raise Exception("Unknown attribute of state")
            if stringWords[2] != "F" and stringWords[2] != "S":
                raise Exception("Unknown attribute of state")
            if stringWords[1] == stringWords[1]:
                raise Exception("Identical attributes of state")
            if len(start_states) >= 1:
                raise Exception("There can be only one start state")

            final_states.add(stringWords[0])
            start_states.add(stringWords[0])
        elif len(stringWords) == 2:
            if stringWords[1] == "F":
                final_states.add(stringWords[0])
            elif stringWords[1] == "S":
                if len(start_states) >= 1:
                    raise Exception("There can be only one start state")
                else:
                    start_states.add(stringWords[0])
            else:
                raise Exception("Unknown attribute of state")
        states.add(stringWords[0])
        string = input().strip()
elif string == "Transitions:":
    ok3 += 1
    string = input().strip()
    while string != "End":
        stringWords = string.split(", ")
        if len(stringWords) != 3:
            raise Exception("Too many or too few elements")
        transitions.update({(stringWords[0], stringWords[2]): stringWords[1]})
        string = input().strip()
else:
    raise Exception("Unknown section")

# Section 3 - comments
string = input().strip()
while string[0] == '#':
    string = input().strip()

# Section 3
if string == "Sigma:":
    ok1 += 1
    string = input().strip()
    while string != "End":
        stringWords = string.split(" ")
        if len(stringWords) >= 2:
            raise Exception("Too many words on a line")
        words.add(string)
        string = input().strip()
elif string == "States:":
    ok2 += 1
    string = input().strip()
    while string != "End":
        stringWords = string.split(" ")
        if len(stringWords) >= 4:
            raise Exception("Too many attributes on a line")
        for i in range(0, len(stringWords) - 1):
            if stringWords[i].endswith(","):
                stringWords[i] = stringWords[i].removesuffix(",")
        if len(stringWords) == 3:
            if stringWords[1] != "F" and stringWords[1] != "S":
                raise Exception("Unknown attribute of state")
            if stringWords[2] != "F" and stringWords[2] != "S":
                raise Exception("Unknown attribute of state")
            if stringWords[1] == stringWords[1]:
                raise Exception("Identical attributes of state")
            if len(start_states) >= 1:
                raise Exception("There can be only one start state")

            final_states.add(stringWords[0])
            start_states.add(stringWords[0])
        elif len(stringWords) == 2:
            if stringWords[1] == "F":
                final_states.add(stringWords[0])
            elif stringWords[1] == "S":
                if len(start_states) >= 1:
                    raise Exception("There can be only one start state")
                else:
                    start_states.add(stringWords[0])
            else:
                raise Exception("Unknown attribute of state")
        states.add(stringWords[0])
        string = input().strip()
elif string == "Transitions:":
    ok3 += 1
    string = input().strip()
    while string != "End":
        stringWords = string.split(", ")
        if len(stringWords) != 3:
            raise Exception("Too many or too few elements")
        transitions.update({(stringWords[0], stringWords[2]): stringWords[1]})
        string = input().strip()
else:
    raise Exception("Unknown section")

string = input().strip()
if string != "":
    raise Exception("Too many sections")

if ok1 == 0:
    raise Exception("No words defined")
if ok2 == 0:
    raise Exception("No states defined")
if ok3 == 0:
    raise Exception("No transitions defined")

if ok1 >= 2:
    raise Exception("Two or more words sections defined")
if ok2 >= 2:
    raise Exception("Two or more states sections defined")
if ok3 >= 2:
    raise Exception("Two or more transitions sections defined")

for (k1, k2) in transitions:
    if k1 not in states:
        raise Exception("Unknown state: " + k1)
    if k2 not in states:
        raise Exception("Unknown state: " + k2)
    if transitions[(k1, k2)] not in words:
        raise Exception("Unknown word: " + transitions[(k1, k2)])

print("YEEEEY! It is valid")
