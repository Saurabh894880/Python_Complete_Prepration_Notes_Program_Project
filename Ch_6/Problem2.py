#WAP to find out whether a student is pass or fail, if it requires total 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as input from user.
sub1 = int(input("Enter marks of subject 1: "))
sub2 = int(input("Enter marks of subject 2: "))
sub3 = int(input("Enter marks of subject 3: "))
total = sub1 + sub2 + sub3
percentage = (total / 300) * 100
if sub1 < 33 or sub2 < 33 or sub3 < 33:
    print("You have failed because you scored less than 33% in one or more subjects.")
elif percentage < 40:
    print("You have failed because your total percentage is less than 40%.")
else:
    print("You have passed.")