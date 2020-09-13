def average(x):
    pass
lastname = str(input("Please enter your last name: "))
firstname = str(input("Please enter your first name: "))
age = str(input("Please enter your age: "))
score1 = int(input("Please enter your first score: "))
score2 = int(input("Please enter your second score: "))
score3 = int(input("Please enter your third score: "))
average = int((score1 + score2 + score3) / 3)
print(lastname,',',firstname,'age:',age,'Your average score is',(average))
