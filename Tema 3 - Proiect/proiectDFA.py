transitions = dict()

f = open("dfa_config_project.txt", "rt", encoding="utf-8")

lsOfInts = [int(x) for x in f.readline().split()]
nrOfStates = lsOfInts[0]
nrOfTransitions = lsOfInts[1]

for i in range(0, nrOfTransitions):
    s = f.readline().split()
    p1 = int(s[0])
    p2 = int(s[1])
    t = s[2]
    transitions.update({(p1, t): p2})

initialState = [int(x) for x in f.readline().split()][0]
finalStates = [int(x) for x in f.readline().split()]

nrOfInputs = [int(x) for x in f.readline().split()][0]
for i in range(0, nrOfInputs):
    curState = initialState
    lsOfStates = list()
    lsOfStates.append(curState)
    word = f.readline().strip()
    ok = 1
    for letter in word:
        if (curState, letter) not in transitions:
            ok = 0
            break
        curState = transitions[(curState, letter)]
        lsOfStates.append(curState)

    if ok == 0:
        print("NU")
        continue

    if curState not in finalStates:
        print("NU")
        continue

    print("DA")
    print(lsOfStates)
