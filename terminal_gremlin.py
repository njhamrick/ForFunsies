import random
import time

print("=======================================")
print("         TERMINAL GREMLIN V1.0")
print("=======================================")

name = input("State your name, mortal:")

print(f"\nHmm... {name}. ")
print("The terminal has acknowledged your presence.")

secret_password = "gremlin"
authorized = False
failed_attempts = 0

print("\nSECURITY CHECK REQUIRED.")
print("You have 3 attempts to provide the secret password.")

for attempt in range(3):
    password = input("\nPASSWORD: ")
  

    if password.lower() == secret_password:
        print("PASSWORD ACCEPTED.")
        print("Access to the gremlin network granted.")
        authorized = True
        break

    else:
        failed_attempts = failed_attempts + 1
        attempts_left = 2 - attempt

        if attempts_left > 0:
            print("INCORRECT PASSWORD.")
            print(f"Attempts remaining: {attempts_left}")

        else:
            print("INCORRECT PASSWORD.")
            print("NO ATTEMPTS REMAINING.")

intruder_bonus = failed_attempts * 10     
if authorized == False:
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("     SECURITY BREACH DETECTED")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("IDENTITY FLAGGED.")
        print("AUTHORIZATION: DENIED")
        print("INTRUSION ATTEMPT: LOGGED")
        print("GREMLIN RESPONSE TEAM: DISPATCHED")
        print("\nContinuing scan against security recommendations...")

        intruder_bonus = 25

    
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

print("\nINITIALIZING GREMLIN SECURITY PROTOCOL...")
time.sleep(1)

print("Scanning identity...")
time.sleep(1)

print("Checking forbidden knowledge...")
time.sleep(1)

print("Analyzing threat potential...")
time.sleep(1)

print("Searching for unauthorized admin privileges...")
time.sleep(1)

print("Calculating gremlin compatibility...")
time.sleep(1)

print("Scan complete.")
time.sleep(1)

print("\n========================================")
print("            IDENTITY SCAN")
print("========================================")

threat_level = random.randint(1, 100)
if threat_level <= 20:
    risk_level = "LOW"
    threat_reaction = "LOW RISK: Barely a threat. Proceed with caution."

elif threat_level <= 40:
    risk_level = "MILD"
    threat_reaction = "MILD RISK: Slightly concerning. Monitor closely."

elif threat_level <= 69:
    risk_level = "MODERATE"
    threat_reaction = "MODERATE RISK: Potentially dangerous. The gremlin is taking note."

elif threat_level <= 89:
    risk_level = "HIGH"
    threat_reaction = "HIGH RISK: Keep away from admin privileges. The gremlin is on high alert."

elif threat_level <= 99:
    risk_level = "CRITICAL"
    threat_reaction = "CRITICAL RISK: Immediate action required. The gremlin is preparing countermeasures."

else:
    risk_level = "100% RISK"
    threat_reaction = "The gremlin has detected a severe threat. ABANDON ALL HOPE."

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

clearance_options = [
    "PEASANT",
    "COMMONER",
    "ACOLYTE",
    "WITCH",
    "HEXWEAVER",
    "WARLOCK",
    "OVERLORD",
    "FORBIDDEN USER",
    "ABOSLUTE CHAOS"
]
gremlin_approval = random.choice(approval_options)
if threat_level <= 20:
    clearance_level = random.choice([
        "PEASANT",
        "COMMONER",
        "ACOLYTE"
    ])

elif threat_level <= 40:
    clearance_level = random.choice([
        "COMMONER",
        "ACOLYTE",
        "WITCH"
    ])

elif threat_level <= 69:
    clearance_level = random.choice([
        "ACOLYTE",
        "WITCH",
        "HEXWEAVER"
    ])

elif threat_level <= 89:
    clearance_level = random.choice([
        "WITCH",
        "HEXWEAVER",
        "WARLOCK",
        "OVERLORD"
    ])

else:
    clearance_level = random.choice([
        "OVERLORD",
        "FORBIDDEN USER",
        "ABSOLUTE CHAOS"
    ])

print(f"IDENTITY CONFIRMED: {name}")
if authorized:
    print("ACCESS LEVEL: Questionable")
else:
    print("ACCESS LEVEL: UNAUTHORIZED INTRUDER")
print(f"FAILED LOGIN ATTEMPTS: {failed_attempts}")
print(f"CLEARANCE LEVEL: {clearance_level}")
print(f"THREAT LEVEL: {threat_level}%")
print(f"RISK CLASSIFICATION: {risk_level}")
print(f"ASSESSMENT: {threat_reaction}")
print(f"GREMLIN APPROVAL: {gremlin_approval}")
