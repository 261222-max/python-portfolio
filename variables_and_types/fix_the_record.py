 #fix_the_record.py
 #this program prints a short record about a network device.

device_name="edge-router"
#  (syntax error)الخطأ هو البدء باسم  المتغير ب رقم 2 
end_ip = "192.0.2.1"
# (syntax error) الخطأ هو استخدام اسم المتغير بقيمة محجوزه للغة
device_type="router"
# (runtime error)تحويل نص مكون الى حروف رقم النظام لايمكنه ذلك 
port = int("22")
#(runtime error)الخطأ هو عدم كتابه اسم المتغير كامل 
print("Device:",device_name)
#الخطأ هو عدم تغير اسم المتغير بعد تعديله 
print("BUCKUP IP",end_ip)
print("Type:", device_type)
print("port:",port)
#يكتشف بايثون الاخطاء القواعدية 
#syntax Errors اولا قبل تشغيل اي سطر كود لانه يفحص بنية الملف كاملة قبل التنفيذ