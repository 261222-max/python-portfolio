# fix_the_policy.py
# Check a new password against an example policy and classify its length.

MIN_LENGTH = 12

username = input("Username: ")
password = input("New password: ")

# 1. Syntax Error: Added the missing colon (:) at the end of the if header.
if len(password) < MIN_LENGTH:
    print("- Too short.")

# 2. Semantic Error: Changed 'elif' to a separate 'if' so both password rules can be checked and reported.
if password == username:
    print("- Same as the username.")
   
# 3. Semantic Error: Reordered the chain. Put the narrowest test (>= 16) first because order matters in a chain.
if len(password) >= 16:
    strength = "long"
elif len(password) >= MIN_LENGTH:
    strength = "acceptable"
else:
    strength = "short"

# 4. Semantic Error: Unindented the print statement so it runs for every password, not just the "short" ones.
print(f"Length: {len(password)} ({strength})")
