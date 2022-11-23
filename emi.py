p=int(input('Enter principal amount: '))
r=float(input('Enter rate of interest : '))
t=int(input('enter time: '))
si=(p*t*r)/100
emi=(si*p)/(t*12)
print('Your cost of EMI is : ',emi)


OUTPUT:
  
  Enter principal amount: 100000
Enter rate of interest : 10.99
enter time: 3
Your cost of EMI is :  91583333.33333333
  
  
