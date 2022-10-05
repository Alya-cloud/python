print('Имя?')
A=str(input()) #A-name
print('Фамилия?')
B=str(input()) #B-surname
print('Год рождения?')
C=int(input()) #C-year 
print(A,B,C,sep='_')

A,B=B,A
C+=60
print(A,B,C,sep='_')

