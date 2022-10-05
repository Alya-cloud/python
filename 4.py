print("Введите 1, если требуется найти кол-во экспонатов; введите 0, если неизвестно время")
a=int(input()) #1 или 0

print('Кол-во минут на изучение одного экспоната?')
mine=int(input())

if a==1:
    print('Кол-во високосных лет?')
    cntvi=int(input())
    print('Кол-во невисокосных лет?')
    cntne=int(input())
    print('Кол-во минут в день в музее?')
    mind=int(input())

    cnt_eks=(mind*(366*cntvi+365*cntne))//mine
    print('Кол-во экспонатов=',cnt_eks)

else:
    
    print('Кол-во экспонатов?')
    num_eks=int(input())
    cnt_min=num_eks*mine
    print('Кол-во минут=',cnt_min, 'Кол-во часов=',cnt_min/60, 'Кол-во дней=',(cnt_min/60)/24)

