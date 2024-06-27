#Grade Card Creator For Five Subjects
name=input("Enter your name: ")
c=input("Enter your class: ")
s1=int(input("Enter marks in English: "))
s2=int(input("Enter marks in Hindi: "))
s3=int(input("Enter marks in Maths: "))
s4=int(input("Enter marks in Science: "))
s5=int(input("Enter marks in SST: "))
tt=s1+s2+s3+s4+s5
per=(tt/5)
if per>90:
  g="A"
elif per>80:
  g="B"
elif per>70:
  g="C"
elif per>60:
  g="D"
elif per>50:
  g="E"
else:
  g="F"
print("\n================================\n")
print("Name:",name,"\tClass:",c)
print("\nSubject\t\tMarks\n")
print("English\t\t",s1)
print("Hindi  \t\t",s2)
print("Maths  \t\t",s3)
print("Science\t\t",s4)
print("SST    \t\t",s5)
print("\n--------------------------------\n")
print("\nTotal\n\tMarks:",tt,"\n\tPercentage:",per,"\n\tGrade:",g)
print("\n================================\n")