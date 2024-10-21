import random
#import num_word_form
import math
while input() != 9:
    with open('english_nouns.txt', 'r') as f:
        nouns = f.read().split('\n')
    with open('english_verbs.txt', 'r') as f:
        verbs = f.read().split('\n')
    with open('english_adjectives.txt', 'r') as f:
        adj = f.read().split('\n') 
    match random.randint(1,7):
        case 1:
            rnn = random.choice(["The","Absolute"]) + " " + random.choice(nouns)
        case 2:
            rnn = random.choice(["","The "]) + random.choice(adj) + " " + random.choice(nouns)
        case 3:
            rnn = random.choice(["","The "]) + random.choice(nouns) + " " + random.choice(nouns+verbs+adj)
        case 4:
            rnn = random.choice(["","The "]) + random.choice(adj) + " " + random.choice(nouns)
        case 5:
            rnn = random.choice(["","The "]) + random.choice(nouns) + " of Numbers"
        case 6:
            rnn = random.choice(["","The "]) + random.choice(nouns+nouns+nouns+verbs+adj) + " of the " + random.choice(nouns+verbs+adj)
        case 7:
            rnn = random.choice(["","The "]) + random.choice(adj) + " " + random.choice(nouns) + " of Numbers"
    if random.random() < 0.3:
        rnn += random.choice([" Zero", " One", " Zero", " One", " Zero", " One", " Null", " Null", " Two"])
    print(rnn)
    try:
        char = chr(random.choice([random.randint(32,65535)]))
        while random.randint(1,8)==1:
            char = char + chr(random.choice(random.randint(32,149186)))
        if "zero " in rnn.lower()+" " or "null " in rnn.lower()+" ":
            char += random.choice(["0","₀","(0)","[0]","{0"+"}"])
        if "one " in rnn.lower()+" ":
            char += random.choice(["1","₁","(1)","[1]","{1"+"}"])
        if "two " in rnn.lower()+" ":
            char += random.choice(["2","₂","(2)","[2]","{2"+"}"])
        print(char)
    except:
        char = "[This Number has no Symbol]"
        print(char)
    