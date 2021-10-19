import random

def game(comp, me):

    #if game got equal 
    if comp == me:
        return None
    
    #if computer choose 's'
    elif comp=='s':
        if me == 'w':
            return False
        elif me =='g':
            return True

    #if computer choose 'w'
    elif comp == 'w':
        if me == 'g':
            return False
        elif me == 's':
            return True

    #if computer choose 'g'
    elif comp == 'g':
        if me == 's':
            return False
        elif me == 'w':
            return True
    
print("comp Turn: Snake(S) water(w) Gun(g)?")
randNo = random.randint(1, 3)
if randNo ==1:
    comp = 's'
elif randNo ==2:
    comp = 'w'
elif randNo ==3:
    comp = 'g'

me = input("Your Turn: Snake(s) water(w) Gun(g)?")
a=game(comp, me)

print(f"computer choose {comp}")
print(f"you chose {me}")

if a == None:
    print("Tie!")
elif a:
    print("Win!")
else:
    print("Lose!")