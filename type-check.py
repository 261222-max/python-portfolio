#type_check.py
#this program checks data types and converts values

# predictions:
# 8080 is an int.
# 99.5 is a str.
# "198.51.100.7" is a str.
# 1_000 is an int.

print(type(8080))
print(type("8080"))
print(type(99.5))
print(type("198.51.100.7"))
print(type(1_000))

#convert the values to different types.

converted_int= int("443")
converted_str = str(8080)
converted_float = float("2.5")

print(converted_int,type(converted_int))
print(converted_str,type(converted_str))
print(converted_float,type(converted_float))

