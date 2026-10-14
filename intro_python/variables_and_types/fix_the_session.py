#fix_the_session.py
#يقوم هذا الملف باصلاح الاخطاء البرمجية والمنطقية في تقرير وقت الجلسة 
username = input("username:")
#int()الخطا هو انه تم ادخال الثواني ك نص وهذا غير منطقي يجب اضافة التحويل الى عدد صحيح باستخدام 
total_seconds = int(input("session length in seconds:"))
#(//)الخطا هنا هو انه تم استخدام القسمة العادية لحساب النتائج بالدقائق لكن الناتج سيكون عدد غير صحيح  لذا يجب استخدام 
minutes = total_seconds//60
seconds= total_seconds%60
print("="*30)    
# f(f_streng) الخطا هنا  هو نسيان حرف 
print(f"user:{username}")
#لان اداة الربط تستعمل فقط للربط بين النصوص فقط  str() الخطا هنا عدم تحويل الدقائق الى نص باستخدام 
print("session:"+ str(minutes)+"min"+str(seconds)+"s")
print("="*30)
