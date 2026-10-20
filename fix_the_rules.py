#fix_the_rules.py
#this program checks a connection against three rules

role=input("Role")
#FIX 1(Runtime):convert input to int to allow numerical comparison 
port=int(input("port:"))
#FIX 2 (semantic):use"=="instead of "="for boolean comparison
is_admin = role =="admin"
#Fix 3 (syntax):use"<=" instead of "=<"
is_system_port=port<=1023
#Fix 4 (semantic):repeat the variable comparison on both sides of "or"
is_web_port=(port==80 or port==443)

print(f"admin:{is_admin}")
print(f"system port:{is_system_port}")
print(f"web port:{is_web_port}")