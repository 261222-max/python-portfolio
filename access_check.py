#MAX_FAILED=5 

#استقبال المدخلات من المستخدم 
role = input("Role")
mfa_input=input("MFA passed (yes/no):")
failed=int(input("failed attempts:"))
#تحويل المدخل الى رقم صحيح

#حساب القيم المنطقية   (Boolean variables)
mfa_ok=mfa_input=="yes"
is_privileged =(role=="admin"or role=="root")
can_log_in=mfa_ok and (failed<MAX_FAILED)

#طباعه النتائج باستخدام f-string
print(f"MFA OK:{mfa_ok}")
print(f"privileged role:{is_privileged}")
print(f"can log in :{can_log_in}")