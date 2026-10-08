import calendar
from datetime import date
from time import sleep
def calnd_print(month,year):
    print('_________________________________________________')
    print(monthword(month),'  ',year)
    print('_________________________________________________')
    print('  ΔΕΥ |  ΤΡΙ |  ΤΕΤ |  ΠΕΜ |  ΠΑΡ |  ΣΑΒ |  ΚΥΡ  ')
    monthdata = calendar.monthcalendar(year,month)
    previousmonth = calendar.monthrange(year if month != 1 else year-1,month-1 if month != 1 else 12)
    thismonth = calendar.monthrange(year,month)
    lastduration = previousmonth[1]
    firstday = thismonth[0]
    x, y = 1, 1
    for week in monthdata:
        temp = ''
        counter = 0
        for day in week:
            if day not in range(1,32):
                if monthdata.index(week) == 0:
                    daydisplay = '   ' + str(lastduration - firstday + y)
                    y += 1
                elif day == 0:
                    daydisplay = '    ' + str(x)
                    x += 1
            else:
                if has_event(day,month,year):
                    daynumber = '*'+ str(day)
                else:
                    daynumber =' ' + str(day)
                if day in range(1,10):
                    daydisplay = '[ ' + daynumber + ']'
                else:
                    daydisplay = '[' + daynumber + ']'
            counter += 1
            temp += daydisplay if counter == 7 else (daydisplay + ' |')
        print(temp)
    print('_________________________________________________')
    print('                                                 ')
    print('Πατήστε ENTER για προβολή του επόμενου μήνα , "q" για έξοδο ή κάποια από τις παρακάτω επιλογές: ')
    print('     "-" για πλοήγηση στον προηγούμενο μήνα')
    print('     "+" για διαχείριση των γεγονότων του ημερολογίου')
    print('     "*" για εμφάνιση των γεγονότων ενός επιλεγμένου μήνα')
    
def has_event(day,month,year):
    for i in events:
        datedata = i.split('-')
        if datedata[0] == str(year) and int(datedata[1]) == month and int(datedata[2]) == int(day):
            return True
    return False

def monthword(month):
    months = ['ΙΑΝ','ΦΕΒ','ΜΑΡ','ΑΠΡ','ΜΑΙ','ΙΟΥΝ','ΙΟΥΛ','ΑΥΓ','ΣΕΠ','ΟΚΤ','ΝΟΕ','ΔΕΚ']
    return months[month-1]

def event_management(month,year):
    print('Διαχείριση γεγονότων ημερολογίου, επιλέξτε ενέργεια:')
    print('     1 Καταγραφή νέου γεγονότος')
    print('     2 Διαγραφή γεγονότος')
    print('     3 Ενημέρωση γεγονότος')
    print('     0 Επιστροφή στο κυρίως μενού')
    x=input('->')
    while int(x) not in range(4):
        x = input('H επιλογη δεν ειναι εγκυρη. Δοκιμαστε ξανα\n->', )
    if x == '1' :
        addevent() 
    elif x == '2' :
        delete_event()
    elif x == '3' :
        updateevent()

    
def addevent():
    while True:
        date = input('Εισάγετε την ημερομηνία του γεγονότος(ΥYYY-MM-HH): ')
        if checkdate(date) == True:
            date = formatdate(date)
            break
        else:
            print('Η ημερομηνία δεν είναι έγκυρη. Παρακαλώ δοκιμάστε ξανά')
        
    while True:
        time = input('Εισάγετε την ώρα του γεγονότος(ΗΗ:ΜΜ): ')
        if checktime(time) == True:
            time = formattime(time)
            break
        else:
            print('Η ώρα δεν είναι έγκυρη. Παρακαλώ δοκιμάστε ξανά')

    while True:
        dur=input('Εισάγετε την διάρκεια του γεγονότος: ')
        if dur.isalpha():
            print('Η διάρκεια δεν είναι έγκυρη. Παρακαλώ δοκιμάστε ξανά')
        elif dur == '':
            print('Η διάρκεια δεν είναι έγκυρη. Παρακαλώ δοκιμάστε ξανά')
        elif int(dur) > 0:
            dur = str(int(dur))
            break
        else:
            print('Η διάρκεια δεν είναι έγκυρη. Παρακαλώ δοκιμάστε ξανά') 

    s = ','
    while True:
        title= input('Εισάγετε τον τίτλο του γεγονότος: ')
        if s in title:
            print('Ο τίτλος δεν πρέπει να περιέχει κόμματα. Παρακαλώ δοκιμάστε ξανά')
        elif title == '':
            print('Ο τίτλος δεν είναι έγκυρος. Παρακαλώ δοκιμάστε ξανά')
        else:
            break

    events[date] = [time,dur,title]
    e = open('events.csv','a')
    e.write(date+','+time+','+dur+','+title+'\n')
    e.close()

def searchevents():
    print('===Aναζήτηση Γεγονότων===')
    while True:
        search_year=input('Εισάγετε έτος: ')
        if int(search_year) <= 2022:
            print('Το έτος δεν είναι έγκυρο. Παρακαλώ δοκιμάστε ξανά')
        else:
            break

    while True:
        search_month=input('Εισάγετε μήνα: ')
        if int(search_month) not in range(1,13):
            print('Ο μήνας δεν είναι έγκυρος. Παρακαλώ δοκιμάστε ξανά')
        else:
            break

    event_dates = []
    for i in events:
        selected_month = i.split('-')
        if int(selected_month[0]) == int(search_year) and int(selected_month[1]) == int(search_month):
            event_dates.append(i)
            print(str(len(event_dates)-1)+'. ['+events[i][2]+'] -> Date: '+i+', Time: '+events[i][0]+', Duration: '+events[i][1])
    if event_dates == []:
        print('Δεν ηπάρχουν γεγονότα σε αυτό το μήνα')
        sleep(2)
    return event_dates

def delete_event():
    event_dates = searchevents()
    if event_dates != []:
        while True:
            x = int(input('Επιλέξτε γεγονός προς διαγραφή: '))
            if x in range(len(event_dates)):
                del events[event_dates[x]]
                writeevents(events)
                return
            else:
                print('Η επιλογή σας δεν είναι έγκυρη. Προσπαθήστε ξανά')

def updateevent():
    event_dates = searchevents()
    if event_dates != []:
        while True:
            x = input('Επιλέξτε γεγονός προς ενημέρωση: ')
            if x.isalpha() or x == '':
                print('Η επιλογή σας δεν είναι έγκυρη. Προσπαθήστε ξανά')
            elif int(x) in range(len(event_dates)):
                selected = event_dates[int(x)]
                break
            else:
                print('Η επιλογή σας δεν είναι έγκυρη. Προσπαθήστε ξανά')

        while True:
            new_date = input('Ημερομηνία γεγονότος ('+selected+'): ')
            if new_date == '':
                new_date = selected
                break
            elif checkdate(new_date) == True:
                new_date = formatdate(new_date)
                break
            else:
                print('Η ημερομηνία δεν είναι έγκυρη. Παρακαλώ δοκιμάστε ξανά')
            
        while True:
            new_time = input('Ώρα γεγονότος ('+events[selected][0]+'): ')
            if new_time == '':
                new_time = events[selected][0]
                break
            elif checktime(new_time) == True:
                new_time = formattime(new_time)
                break
            else:
                print('Η ώρα δεν είναι έγκυρη. Παρακαλώ δοκιμάστε ξανά')

        while True:
            dur=input('Διάρκεια γεγονότος ('+events[selected][1]+'): ')
            if dur == '':
                dur = events[selected][1]
                break
            elif int(dur) <= 0:
                print('Η διάρκεια δεν είναι έγκυρη.Παρακαλώ δοκιμάστε ξανά')
            else:
                dur = str(int(dur))
                break

        s = ','
        while True:
            title= input('Τίτλος γεγονότος ('+events[selected][2]+'): ')
            if title == '':
                title = events[selected][2]
                break
            elif s in title:
                print('Ο τίτλος δεν πρέπει να περιέχει κόμματα. Παρακαλώ δοκιμάστε ξανά')
            else:
                break
        
        del events[selected]
        events[new_date] = [new_time,dur,title]
        writeevents(events)

def writeevents(events):
    e = open('events.csv','w')
    e.write('date,time,duration,title\n')
    for i in events:
        e.write(i+','+events[i][0]+','+events[i][1]+','+events[i][2]+'\n')
    e.close()

def checkdate(date):
    dash_count = 0
    for i in date:
        if i not in numstring:
            if i == '-':
                dash_count += 1
            else:
                return False
    if dash_count == 2:
        year,month,day= date.split('-')
        p=calendar.monthrange(int(year),int(month))
        x = p[1]
        return (int(year)>2022 and (int(month) in range(1,13)) and (int(day) in range(1,x+1)))
    else:
        return False

def checktime(time):
    coloncount = 0
    for i in time:
        if i not in numstring:
            if i == ':':
                coloncount += 1
            else:
                return False
    if coloncount == 1:
        hours,minutes=time.split(':')
        return (int(hours) in range (0,24) and (int(minutes) in range (0,60)))
    else:
        return False

def loadevents():
    e = open('events.csv','r')
    list = e.readlines()
    for i in list[1:]:
        eventdata = i.split(',')
        events[eventdata[0]] = [eventdata[1],eventdata[2],eventdata[3][:-1]]
    e.close

def formatdate(date):
    temp = date.split('-')
    temp[1] = '0' + str(int(temp[1])) if len(str(int(temp[1]))) == 1 else str(int(temp[1]))
    temp[2] = '0' + str(int(temp[2])) if len(str(int(temp[2]))) == 1 else str(int(temp[2]))
    return str(int(temp[0])) + '-' + temp[1] + '-' + temp[2]

def formattime(time):
    temp = time.split(':')
    temp[0] = '0' + str(int(temp[0])) if len(str(int(temp[0]))) == 1 else str(int(temp[0]))
    temp[1] = str(int(temp[1])) + '0' if len(str(int(temp[1]))) == 1 else str(int(temp[1]))
    return temp[0] + ':' + temp[1]

if __name__ == '__main__':

    numstring = ['1','2','3','4','5','6','7','8','9','0']
    events = {}
    loadevents()
    print(events)
    today = str(date.today())
    today = today.split('-')
    year, month = int(today[0]),int(today[1])
    monthlist = calendar.monthcalendar(year,month)
    calnd_print(month,year)

    while True:
        selection = input('->')
        match selection:
            case '-':
                if year == 2023 and month == 1:
                    print('Το πρόγραμμα δεν υποστηρίζει έτη πριν το 2023')
                    sleep(0.7)
                else:
                    if month == 1:
                        month = 12
                        year -= 1
                    else:
                        month -= 1
                calnd_print(month,year)
            case '+':
                event_management(month,year)
                calnd_print(month,year)
            case '*':
                searchevents()
                x = input('Πατήστε οποιοδήποτε χαρακτήρα για επιστροφή στο κυρίως μενού:')
                calnd_print(month,year)
            case '':
                if month == 12:
                    month = 1
                    year += 1
                else:
                    month += 1
                calnd_print(month,year)
            case 'q':
                exit()
            case _:
                print('Η επιλογή σας δεν είναι έγκυρη. Προσπαθήστε ξανά')     