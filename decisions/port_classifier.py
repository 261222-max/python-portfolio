#port_classifier.py
#طلب رقم المنفذ وتحويله الى عدد صحيح 

port = int(input("Enter port: "))

#التحقق مما اذا كان المنفذ غير صالح 
if port < 0 or port > 65535 :
    print("invalid port:use a number from 0 to 65535.")
else:
    if 0 <=port<=1023 :
        print("Range:dynamic or private")
    elif 1024 <= port <=49151:
        print("Range:user")
    else:
        print("Range:dynamic or private")

        #تحديد الخدمة للمنافذ الخاصة 
        if port ==22:
            print("service:ssh")
        elif port==80:
            print("service:http")
        elif port ==443:
            print("service:https")
