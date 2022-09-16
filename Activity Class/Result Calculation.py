print("----- Result calculation By Anmol Shrestha -----")

sub1 = int(input("Enter the marks of first subject : \n"))
sub2 = int(input("Enter the marks of second subject : \n"))
sub3 = int(input("Enter the marks of third subject : \n"))
sub4 = int(input("Enter the marks of fourth subject : \n"))
sub5 = int(input("Enter the marks of fifth subject : \n"))

total = sub1 + sub2 + sub3 + sub4 + sub5
percent = (total/500)*100

if percent >=85 :
    gpa = 4
    grade = "A+"
elif percent >= 80 and percent<=84 :
    gpa = 3.7
    grade = "A"
elif percent >= 75 and percent<=79 :
    gpa = 3.3
    grade = "B+"
elif percent >= 70 and percent<=74 :
    gpa = 3.0
    grade = "B"
elif percent >= 65 and percent<=69 :
    gpa = 2.7
    grade = "C+"
elif percent >= 60 and percent<=64 :
    gpa = 2.3
    grade = "C"
elif percent >= 55 and percent<=59 :
    gpa = 2.0
    grade = "D+"
elif percent >= 50 and percent<=54 :
    gpa = 1.7
    grade = "D"
elif percent >= 45 and percent<=49 :
    gpa = 1.3
    grade = "E+"
elif percent >= 40 and percent<=44 :
    gpa = 1.0
    grade = "E"
elif percent <40 :
    gpa = 0
    grade = "F"

print("Total : {}".format(total))
print("Percentage : {}%".format(percent))
print("GPA : {}".format(gpa))
print("Grade : {}".format(grade))