""""
import calendar
t=int(input())
while t:
    lst=[]
    t-=1
    c=0
    m1,y1=map(int,input().split())
    m2,y2=map(int,input().split())
    if m1>2:
        y1+=1
    if m2<2:
        y2-=1
    for y in range(y1, y2 + 1):
        first_week = calendar.monthcalendar(y, 2)[0]
        second_week = calendar.monthcalendar(y, 2)[1]
        if first_week[calendar.FRIDAY]:
            holi_day = first_week[calendar.FRIDAY]
            lst.append(holi_day)
        else:
            holi_day = second_week[calendar.FRIDAY]
            lst.append(holi_day)


    print(lst)
    print(len(lst))

import calendar

t = int(input())
while t:
    t -= 1
    c = 0
    m1, y1 = map(int, input().split())
    m2, y2 = map(int, input().split())
    if m1 > 2:
        y1 += 1
    if m2 < 2:
        y2 -= 1
    for y in range(y1, y2 + 1):
        last_sunday = max(week[-1] for week in calendar.monthcalendar(y, 2)) - 7
        if last_sunday==15 or last_sunday==16:
            c += 1
    print(c)

import calendar
t = int(input())
while t:
    lst = []
    t -= 1
    c = 0
    m1, y1 = map(int, input().split())
    m2, y2 = map(int, input().split())
    if m1 > 2:
        y1 += 1
    if m2 < 2:
        y2 -= 1
    for y in range(y1, y2 + 1):
        first_week = calendar.monthcalendar(y, 2)[0]
        second_week = calendar.monthcalendar(y, 2)[1]
        if first_week[calendar.FRIDAY]:
            holi_day = first_week[calendar.FRIDAY]
        else:
            holi_day = second_week[calendar.FRIDAY]
        if holi_day==7:
            c+=1
        else:
            if holi_day==6:
                if (y % 4) == 0:
                    if (y % 100) == 0:
                        if (y % 400) != 0:
                            c+=1
                else:
                    c+=1
    print(c)

year=int(input())
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) != 0:
           print(year)
else:
   print(year)
print(760%400)


t = int(input())
l=[5,10,11,16,21,22,27]
while t:
    lst = []
    t -= 1
    c = 0
    m1, y1 = map(int, input().split())
    m2, y2 = map(int, input().split())
    if m1 > 2:
        y1 += 1
    if m2 < 2:
        y2 -= 1
    x=int(y1/28)
    print(x)
    print(y1%28)
    y=int(y2/28)
    print(y)
    print(y2%28)
    c+=(y-x)*7
    for i in range((y1%28),(y2%28)+1):
        if i in l:F
            c+=1
    print(c)

import calendar
t = int(input())
while t:
    t -= 1
    c = 0
    m1, y1 = map(int, input().split())
    m2, y2 = map(int, input().split())
    if int((y2-y1)/400)==0:
        if m1 > 2:
            y1 += 1
        if m2 < 2:
            y2 -= 1
        for y in range(y1, y2 + 1):
            first_week = calendar.monthcalendar(y, 2)[0]
            second_week = calendar.monthcalendar(y, 2)[1]
            if first_week[calendar.FRIDAY]:
                holi_day = first_week[calendar.FRIDAY]
            else:
                holi_day = second_week[calendar.FRIDAY]
            if holi_day == 7:
                c += 1
            else:
                if holi_day == 6:
                    if (y % 4) == 0:
                        if (y % 100) == 0:
                            if (y % 400) != 0:
                                c += 1
                    else:
                        c += 1
    else:
        if y1%400==0 and y2%400==0:
            c += int((y2 - y1) / 400) * 101
            if m1 > 2:
                c -= 1
            if m2 < 2:
                c -= 1
            print(c)

        elif y1%400!=0 or y2%400!=0:
            f=int(y2/400)*400
            g=(int(y1/400)+1)*400
            c+=int((f-g)/400)*101
            if y1%400!=0:
                for y in range(y1,((int(y1/400)+1)*400)+1):
                    first_week = calendar.monthcalendar(y, 2)[0]
                    second_week = calendar.monthcalendar(y, 2)[1]
                    if first_week[calendar.FRIDAY]:
                        holi_day = first_week[calendar.FRIDAY]
                    else:
                        holi_day = second_week[calendar.FRIDAY]
                    if holi_day == 7:
                        c += 1
                    else:
                        if holi_day == 6:
                            if (y % 4) == 0:
                                if (y % 100) == 0:
                                    if (y % 400) != 0:
                                        c += 1
                            else:
                                c += 1
            if y2%400!=0:
                for y in range(int(y2/400)*400,y2+1):
                    first_week = calendar.monthcalendar(y, 2)[0]
                    second_week = calendar.monthcalendar(y, 2)[1]
                    if first_week[calendar.FRIDAY]:
                        holi_day = first_week[calendar.FRIDAY]
                    else:
                        holi_day = second_week[calendar.FRIDAY]
                    if holi_day == 7:
                        c += 1
                    else:
                        if holi_day == 6:
                            if (y % 4) == 0:
                                if (y % 100) == 0:
                                    if (y % 400) != 0:
                                        c += 1
                            else:
                                c += 1
    print(int(c))



import calendar
y1,y2=map(int,input().split())
c=0
for y in range(int(y2/400)*400,y2+1):
    first_week = calendar.monthcalendar(y, 2)[0]
    second_week = calendar.monthcalendar(y, 2)[1]
    if first_week[calendar.FRIDAY]:
        holi_day = first_week[calendar.FRIDAY]
    else:
        holi_day = second_week[calendar.FRIDAY]
    if holi_day == 7:
        c += 1
    else:
        if holi_day == 6:
            if (y % 4) == 0:
                if (y % 100) == 0:
                    if (y % 400) != 0:
                        c += 1
            else:
                c += 1
print(c)
c=0
for y in range(int(y2/400)*400,y2+1):
    first_week = calendar.monthcalendar(y, 2)[0]
    second_week = calendar.monthcalendar(y, 2)[1]
    if first_week[calendar.FRIDAY]:
        holi_day = first_week[calendar.FRIDAY]+10
    else:
        holi_day = second_week[calendar.FRIDAY]+10
    last_sunday = max(week[-1] for week in calendar.monthcalendar(y, 2)) - 7
    if last_sunday<holi_day:
        c+=1
print(c)
"""
l=[3,9,14,15,20,25,26,31,37,42,43,48,53,54,59,65,70,71,76,81,82,87,93,98,99,105,110,111,116,121,122,127,133,138,139,144,149,150,155,161,166,167,172,177,178,183,189,194,195,200,201,206,207,212,217,218,223,229,234,235,240,245,246,251,257,262,263,268,273,274,279,285,290,291,296,302,303,308,313,314,319,325,330,331,336,341,342,347,353,358,359,364,369,370,375,381,386,387,392,397,398]
lst1=[0]*400
for i in l:
    lst1[i-1]+=1
t=int(input())
while t:
    t-=1
    c=0
    m1,y1=map(int,input().split())
    m2,y2=map(int,input().split())
    if m1>2:
        y1+=1
    if m2<2:
        y2-=1
        c=0
    if y1%400==0 and y2%400==0:
        c+=int((y2-y1)/400)*101
    else:
        f = int(y1 / 400)
        g = int(y2 / 400)
        if y1%400!=0 and y2%400==0:
            c+=lst1[y1%400-1:].count(1)
            f+=1
            c+=(g-f)*101
        elif y2%400!=0 and y1%400==0:
            c+=lst1[:y2%400].count(1)
            c += (g - f) * 101
        else:
            c += lst1[y1 % 400-1:].count(1)
            c += lst1[:y2 % 400].count(1)
            f += 1
            c += (g - f) * 101
    print(c)