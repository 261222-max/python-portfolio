#تعريف المتغيرات الاساسية
user = "analyst"
role = "viewer"
failed = 3
port = 22

#الاختبار 1 باستخدام ==   true 
print(user=="analyst")
#الاختبار 2 باستخدام!=    true 
print(role!="admin")
#الاختبار 3 باستخدام >  true
print(failed>2)
#الاختبار 4 باستخدام<   true
print(port<80)
#الاختبار 5 باستخدام>=  true
print(failed>=3)
#الاختبار 6 باستخدام <=    false
print(port<=23)
#الاختبار 7 باستخدام ==  false
print(port==25)
#الاختبار 8 باستخدام !=     false
print(role!="viewer")
#الاختبار 9 باستخدام <=      false
print(failed<=2 )
#الاختبار 10 باستخدام == and !=   false
print(failed==2 and port!=23)


