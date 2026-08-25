import random

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

responses = [
    "The gremlin is amused by your presence.",
    "The terminal accepts your offering.",
    "The gremlin has updated your file.",
    "Your fate has been logged.",
    "No errors detected. Emotionally, however... uncertain."

]

print("\nFinal assessment:")
print(random.choice(responses))

print("\n========================================")
print("      IDENTITY SCAN")
print("========================================")

threat_level = random.randint(1, 100)

approval_options = [
    "APPROVED",
    "PENDING...",
    "SUSPICIOUS",
    "PROBABLY FINE",
    "DO NOT TRUST",
    "ERROR: UNDEFINED",
    "GREMLIN DETECTED",
    "TERMINAL OVERRIDE REQUIRED",
    "WHO LET YOU IN?",
    "ACCESS GRANTED",
    "GREMLIN APPROVED",
    "GREMLOUSLY SUSPICIOUS"
]

gremlin_approval = random.choice(approval_options)

print(f"IDENTITY CONFIRMED: {name}")
print("ACCESS LEVEL:  Questionable")
print(f"THREAT LEVEL: {threat_level}")
print(f"GREMLIN APPROVAL: {gremlin_approval}")   