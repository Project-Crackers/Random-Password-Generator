import random

password = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()[]}{|,./:;<>/*-+"
pwd_len = int(input("Enter the length of the password you want : "))

p = "".join(random.sample(password,pwd_len))
print (f"Your password is {p}")

