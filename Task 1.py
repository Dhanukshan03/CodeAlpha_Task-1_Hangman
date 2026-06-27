import random

def hangman(n):
    figure=['|','O','/','|','\\','/','\\']
    print("___")
    for i in range(0,n+1):
        if i<2:
            print(f" {figure[i]} ")
        elif i==2 or i==3:
            print(figure[i],end="")
        elif i==4:
            print(f"{figure[i]}")
        elif i==5:
            print(f"{figure[i]} ",end="")
        elif i==6:
            print(f"{figure[i]}\n")
    print()
            
words_list=["Dumbledore","Hermione","Voldemort","Bellatrix","Nymphadora","Sirius","Dolores","Harry","McGonagall","Draco","Narcissa"]
choice=True
while choice:
    temp=words_list.copy()
    ans=random.choice(temp)
    real=list(ans)
    print("--- Welcome to Hangman Game! ---")
    print("\nWords are names of characters from Harry Potter Series. Are you ready?\n")
    print("You have 6 lives so be careful! Let's start!\n")
    print(f"Your word has {len(real)} letters and note only first ones are in uppercase.\n")
    for x in real:
        print("- ",end="")
    correct_guess=[]
    wrong_guess=[]
    count=0
    while count<6:
        print()
        guess= input("\nEnter a letter: ")
        if guess in correct_guess or guess in wrong_guess:
            print(f"\nYou have already guessed '{guess}'! Try different.")
            continue
        
        if guess in real:
            print("\nCorrect! You have guessed it right.\n")
            if guess not in correct_guess:
                correct_guess.append(guess)
            win= True
            for x in real:
                if x in correct_guess:
                    print(x,end=" ")
                else:
                    print('-',end=" ")
                    win= False
            print()
            if win:
                print("\nYou have won. Congratulations!")
                choice=bool(int(input("\nWanna replay? If it is, enter 1 else 0: ")))
                print()
                break
        else: 
            count+=1
            print(f"Wrong! You have {6-count} attempts.")
            wrong_guess.append(guess)
            hangman(count)
            for x in real:
                if x in correct_guess:
                    print(x,end=" ")
                else:
                    print('-',end=" ")
            
    else:
        print(f"\nYou are out! The word was {ans}.")
        choice=bool(int(input("\nWanna replay? If it is, enter 1 else 0: ")))
else:
    print("\nThank you for playing this game!")
    
    
    

