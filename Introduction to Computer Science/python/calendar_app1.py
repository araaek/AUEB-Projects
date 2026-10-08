import calendar
from datetime import date
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
    x=input('-> ')
    while int(x) not in range(4):
        x = input('H επιλογη δεν ειναι εγκυρη. Δοκιμαστε ξανα\n-> ', )
    if x == '1' :
        get_event_details() 
    elif x == '2' :
        delete_event()
    elif x == '3' :
        updateevent()
    calnd_print(month,year)
    
def get_event_details():
    while True:
        date = input('Εισάγετε την ημερομηνία του γεγονότος(ΥYYY-MM-DD): ')
        if checkdate(date) == True:
            break
        else:
            print('Η ημερομηνία δεν είναι έγκυρη. Παρακαλώ δοκιμάστε ξανά')
        
    while True:
        time = input('Εισάγετε την ώρα του γεγονότος(ΗΗ:ΜΜ): ')
        if checktime(time) == True:
            break
        else:
            print('Η ώρα δεν είναι έγκυρη. Παρακαλώ δοκιμάστε ξανά')

    while True:
        dur=input('Εισάγετε την διάρκεια του γεγονότος: ')
        if int(dur) <= 0:
            print('Η διάρκεια δεν είναι έγκυρη.Παρακαλώ δοκιμάστε ξανά')
        else:
            break

    s = ','
    while True:
        title= input('Εισάγετε τον τίτλο του γεγονότος:')
        if s in title:
            print('Ο τίτλος δεν πρέπει να περιέχει κόμματα. Παρακαλώ δοκιμάστε ξανά')
        else:
            break

    addevent(date,time,dur,title)

def searchevents():
    print('===Aναζήτηση Γεγονότων===')
    while True:
        search_year=input('Εισάγετε έτος: ')
        if int(year) <= 2022:
            print('Το έτος δεν είναι έγκυρο. Παρακαλώ δοκιμάστε ξανά')
        else:
            break

    while True:
        search_month=input('Εισάγετε μήνα: ')
        if int(month) not in range(1,13):
            print('Ο μήνας δεν είναι έγκυρος. Παρακαλώ δοκιμάστε ξανά')
        else:
            break

    event_dates = []
    for i in events:
        selected_month = i.split('-')
        if i == 'date':
            continue
        elif selected_month[0] == search_year and int(selected_month[1]) == int(search_month):
            event_dates.append(i)
            print(str(len(event_dates)-1)+'. ['+events[i][2]+'] -> Date: '+i+', Time: '+events[i][0]+', Duration: '+events[i][1])
        if event_dates == []:
            print('Δεν ηπάρχουν γεγονότα σε αυτό το μήνα')
    return event_dates

def delete_event():
    event_dates = searchevents()
    if event_dates != []:
        while True:
            x = int(input('Επιλέξτε γεγονός προς διαγραφή: '))
            if x in range(len(event_dates)-1):
                del events[event_dates[x]]
                writeevents(events)
            else:
                print('Η επιλογή σας δεν είναι έγκυρη. Προσπαθήστε ξανά')
    return


def updateevent():
    event_dates = searchevents()
    if event_dates != []:
        while True:
            x = int(input('Επιλέξτε γεγονός προς ενημέρωση: '))
            if x in range(len(event_dates)):
                selected = events[event_dates[x]]
            else:
                print('Η επιλογή σας δεν είναι έγκυρη. Προσπαθήστε ξανά')

    while True:
        new_date = input('Ημερομηνία γεγονότος ('+selected+'): ')
        if checkdate(new_date) == True:
            break
        else:
            print('Η ημερομηνία δεν είναι έγκυρη. Παρακαλώ δοκιμάστε ξανά')
        
    while True:
        new_time = input('Ώρα γεγονότος ('+events[selected][0]+'): ')
        if checktime(new_time) == True:
            break
        else:
            print('Η ώρα δεν είναι έγκυρη. Παρακαλώ δοκιμάστε ξανά')

    while True:
        dur=input('Διάρκεια γεγονότος ('+events[selected][1]+'): ')
        if int(dur) <= 0:
            print('Η διάρκεια δεν είναι έγκυρη.Παρακαλώ δοκιμάστε ξανά')
        else:
            break

    s = ','
    while True:
        title= input('Τίτλος γεγονότος ('+events[selected][2]+'): ')
        if s in title:
            print('Ο τίτλος δεν πρέπει να περιέχει κόμματα. Παρακαλώ δοκιμάστε ξανά')
        else:
            break

    if new_date == selected:
        events[selected] == [new_time,dur,title]
        writeevents(events)
    else:
        del events[selected]
        events[new_date] == [new_time,dur,title]
        writeevents(events)

def writeevents(events):
    e = open('events.csv','w')
    for i in events:
        e.write(i+','+events[i][0]+','+events[i][1]+','+events[i][2]+'\n')
    e.close()

def addevent(date,time,dur,title):
    events[date] = [time,dur,title]
    e = open('events.csv','a')
    e.write(date+','+time+','+dur+','+title+'\n')
    e.close()

def checkdate(date):
    dash_count = 0
    for i in date:
        if i == '-':
            dash_count += 1
    if dash_count == 2:
        year,month,day= date.split('-')
        p=calendar.monthrange(int(year),int(month))
        x = p[1]
        return (int(year)>2022 and (int(month) in range(1,13)) and (int(day) in range(1,x+1)))
    else:
        return False

def checktime(time):
    hours,minutes=time.split(':')
    return (int(hours) in range (0,24) and (int(minutes) in range (0,60)))
    
if __name__ == '__main__':

    events = {}
    events['date'] = ['time', 'duration', 'title']
    writeevents(events)
    today = str(date.today())
    today = today.split('-')
    year, month = int(today[0]),int(today[1])
    monthlist = calendar.monthcalendar(year,month)
    calnd_print(month,year)

    while True:
        selection = input('-> ')
        match selection:
            case '-':
                if year == 2023 and month == 1:
                    print('Το πρόγραμμα δεν υποστηρίζει έτη πριν το 2023')
                else:
                    if month == 1:
                        month = 12
                        year -= 1
                    else:
                        month -= 1
                
            case '+':
                event_management(month,year)
            case '*':
                searchevents()
                x = input('Πατήστε οποιοδήποτε χαρακτήρα για επιστροφή στο κυρίως μενού:')
            case '':
                if month == 12:
                    month = 1
                    year += 1
                else:
                    month += 1 
            case 'q':
                break
        calnd_print(month,year)
