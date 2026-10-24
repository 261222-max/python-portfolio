#login_decision.py
#Definition of constannts

MAX_FAILED =5 
KNOWN_USER="analyst"
STORED_PASSWORD="Blue#Falcon72"

#Request input in the specified order
username=input("Username: ")
failed_attempts=int(input("Failed attempts so far: "))
password=input("password: ")

#check the conditions in the exact order required
if failed_attempts>=MAX_FAILED:
    print("account loked.")
elif username != KNOWN_USER:
    print("Unknown user.")
elif password !=STORED_PASSWORD:
   attempts_left = MAX_FAILED - failed_attempts - 1
   print(f"Accesss denied.Attempts left: {attempts_left}")
else:
   print("Access granted.")
