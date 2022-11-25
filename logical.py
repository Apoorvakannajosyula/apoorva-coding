sno=int(input('Enter student number: '))
sname=input('Enter student name: ')
group=input('Enter student group: ')
s1=int(input('Enter subject1 marks:'))
s2=int(input('Enter subject2 marks:'))
s3=int(input('Enter subject3 marks:'))
print('Student number is :',sno)
print('Student name is :',sname)
print('Student group is :',group)
if s1>=35 and s2>=35 and s3>=35:
    print('pass')
else:
    print('fail')

    
    OUTPUT:
      
      
      Enter student number: 23
Enter student name: Apoorva
Enter student group: BCA
Enter subject1 marks:56
Enter subject2 marks:72
Enter subject3 marks:64
Student number is : 23
Student name is : Apoorva
Student group is : BCA
pass
