print("=======================================")
print("           TERMINAL GREMLIN V1.0")
print("=======================================")

name = input("State your name, mortal:")

print(f"\nHmm... {name}. ")
print("The terminal has acknowledged your presence.")

mood = int(input("\nHow emotionally stable are you from 1-10? "))

if mood <= 3:
      print("Oh.")
       print("That number came with a distress signal.")

elif mood <= 7:
      print("Hmm. I see.")
      print("The gremlin is watching.")

else:
        print("Ah, a happy mortal!")
        print("The gremlin is pleased with your emotional state.")  

