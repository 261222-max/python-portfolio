# risk_score.py
# This program calculates a login risk score based on three security rules

score = 0

failed_attempts = int(input("Failed attempts in the last hour (int): "))
login_hour = int(input("Login hour (0-23) (int): "))
new_device = input("New device (yes/no): ")

if failed_attempts >= 3:
    score += 40

if login_hour < 6:
    score += 30

if new_device == "yes":
    score += 30

if score >= 70:
    level = "HIGH"
elif score >= 30:
    level = "MEDIUM"
else:
    level = "LOW"

print(f"Risk score: {score} ({level})")
