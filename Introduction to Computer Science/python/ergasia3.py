import calendar, datetime, locale
locale.setlocale(locale.LC_TIME, "el")

def print_calendar(yy,mm):
    """ Εμφανίζει το ημερολόγιο του τρέχοντος μήνα, με κατάλληλη επισήμανση των ημερών που
        ανήκουν στον μήνα [], καθώς και με εμφάνιση των ημερών από τον προηγούμενο και επόμενο
        μήνα. Σε περίπτωση που για κάποια ημερομηνία του μήνα έχουν ορισθεί γεγονότα, τότε
        η μέρα αυτή συνοδεύεται με *
    """

    # ανοίγουμε το CSV file για διάβασμα
    f=open('events.csv', 'r')

    # διαβάζουμε όλες τις γραμμές του αρχείου
    lines = f.readlines()

    # δημιουργούμε ένα dictionary για να αποθηκεύσουμε τα γεγονότα
    events = {}

    # αποθηκεύουμε τα γεγονότα στο dictionary
    for line in lines[1:]:  # εξαιρούμε την επικεφαλίδα 
        lista = line.split(',')
        date=lista[0]
        year,month,day = date.split('-')
        # φτιάχνω την ημερομηνία με δύο ψηφία για μέρα και μήνα
        date = f'{year}-{month:0>2}-{day:0>2}'
        events[date] = '*'
    f.close()
    
    # το ημερολόγιο του τρέχοντος μήνα σε εβδομαδιαία μορφή, έχει μηδενικά στις
    # μέρες της πρώτης και της τελευταίας εβδομάδας που δεν ανήκουν στον μήνα
    cal = calendar.monthcalendar(yy, mm)

    # το ημερολόγιο του προηγούμενου μήνα
    previous_month = mm-1
    previous_year = yy
    if previous_month==0:
        previous_month=12
        previous_year -= 1
    previous_cal = calendar.monthcalendar(previous_year, previous_month)

    # το ημερολόγιο του επόμενου μήνα
    next_month = mm+1
    next_year = yy
    if next_month==13:
        next_month=1
        next_year += 1
    next_cal = calendar.monthcalendar(next_year, next_month)

    """
    μετράμε τα μηδενικά της πρώτης και της τελευταίας εβδομάδας του μήνα
    και στη συνέχεια δημιουργούμε μία λίστα zeroes που έχει ως στοιχεία
    τις ημερομηνίες των πρώτων ημερών της πρώτης εβδομάδας που ανήκουν
    στον προηγούμενο μήνα και τις ημερομηνίες τως τελευταίων ημερών της
    τελευταίας εβδομάδας που ανοίκουν στον επόμενο μήνα
    """
    zeroes_first=cal[0].count(0)
    zeroes_last=cal[-1].count(0)
    zeroes=[]
    for i in range (zeroes_first):
        zeroes =zeroes+[previous_cal[-1][i]]
    for i in range (zeroes_last):
        zeroes = zeroes + [next_cal[0][7-zeroes_last+i]]
        
    print('-----------------------------------------------')
    print(calendar.month_abbr[mm].upper(),str(yy))
    print('-----------------------------------------------')
    print(' ΔΕΥΤ |  ΤΡΙ |  ΤΕΤ |  ΠΕΜ |  ΠΑΡ |  ΣΑΒ |  ΚΥΡ')

    # τυπώνουμε το ημερολόγιο με αστεράκια στις ημερομηνίες των γεγονότων
    zero=0
    for week in cal:
        d=0
        for day in week:
            if day == 0:
                if d %7 ==0:
                    print(f'{zeroes[zero]:5}', end=' ')
                else:
                    print(f'|{zeroes[zero]:5}', end=' ')
                zero +=1
            else:
                if d %7 ==0:
                    date = f'{yy}-{mm:02d}-{day:02d}'
                    if date in events:
                        print(f'[*{day:2d}]', end=' ')
                    else:
                        print(f'[ {day:2d}]', end=' ')
                else:
                    date = f'{yy}-{mm:02d}-{day:02d}'
                    if date in events:
                        print(f'|[*{day:2d}]', end=' ')
                    else:
                        print(f'|[ {day:2d}]', end=' ')
            d+=1
        print()

def read_date():
    """
    Διαβάζει και επιστρέφει μια έγκυρη ημερομηνία
    """
    while True:
        # διάβασμα ημερομηνίας
        date_string = input('Ημερομηνία γεγονότος σε μορφή YYYY-MM-DD (π.χ. 2023-05-04): ')

        # έλεγχος αν η ημερομηνία έχει την κατάλληλη μορφή
        if len(date_string) != 10 or date_string[4] != '-' or date_string[7] != '-':
            print('Μη έγκυρη μορφή ημερομηνίας')
            continue

        # διαχωρισμός ημερομηνίας στα συστατικά της
        year, month, day = date_string.split('-')
        year, month, day = int(year), int(month), int(day)

        # έλεγχος αν το έτος είναι μεγαλύτερο του 2022
        if year <= 2022:
            print('Το έτος πρέπει να είναι μεγαλύτερο του 2022')
            continue

        # έλεγχος μήνα 
        if not (1 <= month <= 12):
            print('Ο μήνας πρέπει να είναι μεταξύ 1 και 12')
            continue

        # έλεγχος αν η ημέρα ανήκει στον συγκεκριμένο μήνα
        if not (1 <= day <= 31):
            print('Μη έγκυρη ημέρα')
            continue
        if (day == 31) and (month in [2, 4, 6, 9, 11]):
            print('Μη έγκυρη ημέρα')
            continue
        if (day == 30) and (month == 2):
            print('Μη έγκυρη ημέρα')
            continue
        if (day == 29) and (month == 2) and (year % 4 != 0):
            print('Μη έγκυρη ημέρα')
            continue

        # If the date is valid, return it
        return date_string

def read_time():
    """
    Διαβάζει και επιστρέφει μια έγκυρη ώρα
    """
    while True:
        # διάβασμα ώρας ως string
        time_string = input('Ώρα γεγονότος σε μορφή ΗΗ:ΜΜ (π.χ. 23:00): ')
        # έλεγχος αν η ώρα έχει την κατάλληλη μορφή
        if len(time_string) != 5 or time_string[2] != ':':
            print('Μη έγκυρη μορφή ώρας')
            continue
        # διαχωρισμός ώρας στα συστατικά της
        hours, minutes = time_string.split(":")
        # μετατροπή ωρών και λεπτών σε ακεραίους
        hours = int(hours)
        minutes = int(minutes)
        # έλεγχος εγκυρότητας ώρας
        if 0 <= hours <= 23 and 0 <= minutes <= 59:
          return time_string
        else:
          print('Μή έγκυρη ώρα, ξαναπροσπαθήστε')

def read_positive_int():
    """
    Διαβάζει την διάρκεια του γεγονότος, θετικό αριθμό
    """
    while True:
        x = input('Διάρκεια γεγονότος: ')
        if x.isdigit() and int(x) > 0:
          return x
        print('Μη έγκυρη διάρκεια')


def read_title():
    """
    Διαβάζει τον τίτλο, δεν πρέπει να περιέχει ','
    """
    while True:
        s = input('Τίτλος γεγονότος: ')
        if ',' not in s:
            return s
        print('Ο τίτλος δεν πρέπει να περιέχει ","')

def diaxeirisi_gegonoton():
    while True:
        print('\tΔιαχείριση γεγονότων ημερολογίου, επιλέξτε ενέργεια:')
        print('\t\t1 Καταγραφή νέου γεγονότος')
        print('\t\t2 Διαγραφή γεγονότος')
        print('\t\t3 Ενημέρωση γεγονότος')
        print('\t\t0 Επιστροφή στο κυρίως μενού')
        epil=input()
        if epil=='1':
            date_string = read_date()
            time_string = read_time()
            duration_string = read_positive_int()
            title = read_title()
            event=date_string+','+time_string+','+duration_string+','+title+'\n'
            # ανοίγουμε το CSV file για εγγραφή-προσθήκη
            f=open('events.csv', 'a')
            f.write(event)
            f.close()
        elif epil=='0':
            break

def read_year():
  year = input('Εισάγετε έτος: ')
  while int(year) <= 2021:
    year = input('Παρακαλώ εισάγετε έτος μεγαλύτερο ίσο του 2022: ')
  return str(year)

def read_month():
  while True:
      month = input('Εισάγετε μήνα: ')
      if month.isdigit() and len(month)==2:
         if 1 <= int(month) <= 12:
              return month
      print('Παρακαλώ εισάγετε έγκυρο μήνα: ')

def anazitisi_gegonoton():
    print('=== Αναζήτηση γεγονότων ===')
    etos_string=read_year()
    minas_string=read_month()
    etos_minas=etos_string+'-'+minas_string
    f=open('events.csv', 'r')
    # διαβάζουμε όλες τις γραμμές του αρχείου
    lines = f.readlines()

    i=0
    for line in lines[1:]:  # εξαιρούμε την επικεφαλίδα 
        lista = line.split(',')
        date=lista[0]
        year,month,day = date.split('-')
        # 
        date = f'{year}-{month:0>2}'
        if etos_minas==date:
            print(f'{i}. [{lista[3].strip()}] -> Date: {lista[0]}, Time: {lista[1]}, Duration: {lista[2]}')
            i+=1
    f.close()        
       
if __name__ == '__main__':
    
    # τρέχον έτος, τρέχων μήνας
    today = datetime.date.today()
    yy=today.year
    mm=today.month
    while True:
        print_calendar(yy,mm)
        
        print('Πατήστε ENTER για προβολή του επόμενου μήνα, "q" για έξοδο ή κάποια από τις παρακάτω επιλογές')
        print('\t"-" για πλοήγηση στον προηγούμενο μήνα')
        print('\t"+" για διαχείριση των γεγονότων του ημερολογίου')
        print('\t"*" για εμφάνιση των γεγονότων ενός επιλεγμένου μήνα')

        epil=input()
        if epil=='':
            mm +=1
            if mm == 13:
                mm=1
                yy+=1
        elif epil=='-':
            mm -=1
            if mm==0:
                mm=12
                yy-=1
        elif epil=='+':
            diaxeirisi_gegonoton()
            
        elif epil=='*':
            anazitisi_gegonoton()
            input('Πατήστε οποιονδήποτε χαρακτήρα για επιστροφή στο κυρίως μενού')
        elif epil=='q':
            break

