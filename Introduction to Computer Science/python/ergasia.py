import calendar
import datetime


def print_calendar(yy, mm, lines):
    """ Εμφανίζει το ημερολόγιο του τρέχοντος μήνα, με κατάλληλη επισήμανση των ημερών που
        ανήκουν στον μήνα [], καθώς και με εμφάνιση των ημερών από τον προηγούμενο και επόμενο
        μήνα. Σε περίπτωση που για κάποια ημερομηνία του μήνα έχουν ορισθεί γεγονότα, τότε
        η μέρα αυτή συνοδεύεται με *
    """

    # δημιουργούμε ένα dictionary για να αποθηκεύσουμε τα γεγονότα
    events = {}

    # αποθηκεύουμε τα γεγονότα στο dictionary
    for line in lines[1:]:  # εξαιρούμε την επικεφαλίδα
        lista = line.split(',')
        date = lista[0]
        year, month, day = date.split('-')
        # φτιάχνω την ημερομηνία με δύο ψηφία για μέρα και μήνα
        date = f'{year}-{month:0>2}-{day:0>2}'
        events[date] = '*'

    # το ημερολόγιο του τρέχοντος μήνα σε εβδομαδιαία μορφή, έχει μηδενικά στις
    # μέρες της πρώτης και της τελευταίας εβδομάδας που δεν ανήκουν στον μήνα
    cal = calendar.monthcalendar(yy, mm)

    # το ημερολόγιο του προηγούμενου μήνα
    previous_cal = calendar.monthcalendar(yy if month !=1 else yy-1, mm if month !=1 else 12)

    # το ημερολόγιο του επόμενου μήνα
    next_cal = calendar.monthcalendar(yy if month !=12 else yy+1, mm if month !=12 else 1)
    
    """
    μετράμε τα μηδενικά της πρώτης και της τελευταίας εβδομάδας του μήνα
    και στη συνέχεια δημιουργούμε μία λίστα zeroes που έχει ως στοιχεία
    τις ημερομηνίες των πρώτων ημερών της πρώτης εβδομάδας που ανήκουν
    στον προηγούμενο μήνα και τις ημερομηνίες τως τελευταίων ημερών της
    τελευταίας εβδομάδας που ανοίκουν στον επόμενο μήνα
    """
    zeroes_first = cal[0].count(0)
    zeroes_last = cal[-1].count(0)
    zeroes = []
    for i in range(zeroes_first):
        zeroes = zeroes+[previous_cal[-1][i]]
    for i in range(zeroes_last):
        zeroes = zeroes + [next_cal[0][7-zeroes_last+i]]

    print('-----------------------------------------------')
    print(month_word(mm),'  ',str(yy))
    print('-----------------------------------------------')
    print(' ΔΕΥΤ |  ΤΡΙ |  ΤΕΤ |  ΠΕΜ |  ΠΑΡ |  ΣΑΒ |  ΚΥΡ')

    # τυπώνουμε το ημερολόγιο με αστεράκια στις ημερομηνίες των γεγονότων
    zero = 0
    for week in cal:
        d = 0
        for day in week:
            if day == 0:
                if d % 7 == 0:
                    print(f'{zeroes[zero]:5}', end=' ')
                else:
                    print(f'|{zeroes[zero]:5}', end=' ')
                zero += 1
            else:
                if d % 7 == 0:
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
            d += 1
        print()

def month_word(month):
    months = ['ΙΑΝ','ΦΕΒ','ΜΑΡ','ΑΠΡ','ΜΑΙ','ΙΟΥΝ','ΙΟΥΛ','ΑΥΓ','ΣΕΠ','ΟΚΤ','ΝΟΕ','ΔΕΚ']
    return months[month-1]

def read_date():
    """
    Διαβάζει και επιστρέφει μια έγκυρη ημερομηνία
    """
    while True:
        # διάβασμα ημερομηνίας
        date_string = input(
            'Ημερομηνία γεγονότος σε μορφή YYYY-MM-DD (π.χ. 2023-05-04): ')

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


def event_management(lines):
    while True:
        print('\tΔιαχείριση γεγονότων ημερολογίου, επιλέξτε ενέργεια:')
        print('\t\t1 Καταγραφή νέου γεγονότος')
        print('\t\t2 Διαγραφή γεγονότος')
        print('\t\t3 Ενημέρωση γεγονότος')
        print('\t\t0 Επιστροφή στο κυρίως μενού')
        print('\t\t-> ',end='')
        epil = input()
        if epil == '1':
            date_string = read_date()
            time_string = read_time()
            duration_string = read_positive_int()
            title = read_title()
            event = date_string+','+time_string+','+duration_string+','+title+'\n'
            lines.append(event)
            lines = sort_events(lines)
        elif epil == '2':
            events = search_events(lines)
            if events:
                while True:
                    d = int(input('Επιλέξτε γεγονός για διαγραφή: '))
                    if 0 <= d < len(events):
                        break
                lines.remove(events[d])
            else:
                print('Δεν βρέθηκαν γεγονότα, πατήστε πλήκτρο για συνέχεια')
                x = input()
        elif epil == '3':
            events = search_events(lines)
            if events:
                while True:
                    d = int(input('Επιλέξτε γεγονός προς ενημέρωση: '))
                    if 0 <= int(d) < len(events):
                        break
                index = lines.index(events[d])
                lista = events[d].split(',')
                date = lista[0]
                hour = lista[1]
                duration = lista[2]
                title = lista[3].strip()
                print('Hμερομηνία γεγονότος ('+date+'): ', end=' ')
                date_new = input()
                if date_new != '':
                    date = date_new
                print('Ώρα γεγονότος ('+hour+'): ', end=' ')
                hour_new = input()
                if hour != '':
                    hour = hour_new
                print('Διάρκεια γεγονότος ('+duration+'): ', end=' ')
                duration_new = input()
                if duration_new != '':
                    duration = duration_new
                print('Τίτλος γεγονότος ('+title+'): ', end=' ')
                title_new = input()
                if title_new != '':
                    title = title_new

                lista = date+','+hour+','+duration+','+title+'\n'
                lines[index] = lista 
            else:
                print('Δεν βρέθηκαν γεγονότα, πατήστε πλήκτρο για συνέχεια')
                x = input()
            lines = sort_events(lines)
        elif epil == '0':
            lines = sort_events(lines)
            return (lines)
            break


def read_year():
    while True:
        year = input('Εισάγετε έτος: ')
        if year.isdigit() and int(year) >= 2022:
            return str(year)
        print('Παρακαλώ εισάγετε έτος μεγαλύτερο ίσο του 2022: ')


def read_month():
    while True:
        month = input('Εισάγετε μήνα: ')
        if month.isdigit() and len(month) == 2:
            if 1 <= int(month) <= 12:
                return month
        print('Παρακαλώ εισάγετε έγκυρο μήνα: ')


def search_events(lines):
    print('=== Αναζήτηση γεγονότων ===')
    year_string = read_year()
    month_string = read_month()
    year_month = year_string+'-'+month_string

    i = 0
    events = {}
    for line in lines[1:]:  # εξαιρούμε την επικεφαλίδα
        lista = line.split(',')
        date = lista[0]
        year, month, day = date.split('-')

        date = f'{year}-{month:0>2}'
        if year_month == date:
            flag = True
            print(
                f'{i}. [{lista[3].strip()}] -> Date: {lista[0]}, Time: {lista[1]}, Duration: {lista[2]}')
            events[i] = line
            i += 1
    return events


def sort_events(lines):
    # ταξινομεί την λίστα των γεγονώτων
    # παραλειπουμε την πρώτη γραμμά γιατί έχει τις επικεφαλίδες
    data = lines[1:]
    data.sort()
    lines = [lines[0]]+data
    return lines


if __name__ == '__main__':

    # τρέχον έτος, τρέχων μήνας
    today = datetime.date.today()
    yy = today.year
    mm = today.month

    # αν το αρχείο events.csv δεν υπάρχει, το δημιουργούμε
    # και γραφουμε μέσα την επικεφαλίδα: Date,Hour,Duration,Title
    try:
        f = open('events.csv', 'r')
        pass
    except FileNotFoundError:
        # το αρχείο δεν υπάρχει, οπότε το δημιουργούμε και γράφουμε μέσα την επικεφαλίδα
        f.write('Date,Hour,Duration,Title\n')
        f.close()

    # ανοίγουμε το CSV file για διάβασμα
    f = open('events.csv', 'r')
    # διαβάζουμε όλες τις γραμμές του αρχείου
    lines = f.readlines()
    f.close()
    events = {}
    while True:
        print_calendar(yy, mm, lines)

        print('Πατήστε ENTER για προβολή του επόμενου μήνα, "q" για έξοδο ή κάποια από τις παρακάτω επιλογές')
        print('\t"-" για πλοήγηση στον προηγούμενο μήνα')
        print('\t"+" για διαχείριση των γεγονότων του ημερολογίου')
        print('\t"*" για εμφάνιση των γεγονότων ενός επιλεγμένου μήνα')
        print('\t-> ',end='')

        epil = input()
        if epil == '':
            mm += 1
            if mm == 13:
                mm = 1
                yy += 1
        elif epil == '-':
            mm -= 1
            if mm == 0:
                mm = 12
                yy -= 1
        elif epil == '+':
            lines = event_management(lines)
        elif epil == '*':
            search_events(lines)
            input('Πατήστε οποιονδήποτε χαρακτήρα για επιστροφή στο κυρίως μενού')
        elif epil == 'q' or 'Q':
            f = open('events.csv', 'w')
            for line in lines:
                f.write(line)
            f.close()
            break
