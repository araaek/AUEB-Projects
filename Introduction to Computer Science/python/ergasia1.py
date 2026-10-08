import calendar

# Store the events in a dictionary with the date as the key and the event as the value
events = {}
with open('events.csv', 'r') as f:
    # Skip the header line
    f.readline()
    for line in f:
        # Split the line by the comma delimiter
        date, _, _, event = line.split(',')
        # Pad the month and day values with a leading zero if they are single digits
        year, month, day = date.split('-')
        if len(month) == 1:
            month = f'0{month}'
        if len(day) == 1:
            day = f'0{day}'
        events[f'{year}-{month}-{day}'] = event.strip()

# Generate the calendar for the desired month with 6 rows
year = 2022
month = 12
cal = calendar.monthcalendar(year, month)

# Get the first and last day of the month
first_day = calendar.monthrange(year, month)[0]
last_day = calendar.monthrange(year, month)[1]

# Iterate over the weeks in the calendar and over the days in each week
for week in cal:
    for day in week:
        # If the day is zero, print the day of the previous or next month
        if day == 0:
            if week.index(day) < first_day:
                # Print the day of the previous month
                if month == 1:
                    # If it is January, the previous month is December of the previous year
                    print(calendar.monthrange(year-1, 12)[1] - first_day + week.index(day) + 1, end=' ')
                else:
                    # Otherwise, it is the last month of the current year
                    print(calendar.monthrange(year, month-1)[1] - first_day + week.index(day) + 1, end=' ')
            else:
                # Print the day of the next month
                if month == 12:
                    # If it is December, the next month is January of the next year
                    print(week.index(day) - last_day + 1, end=' ')
                else:
                    # Otherwise, it is the next month of the current year
                    print(week.index(day) - last_day + 1, end=' ')
        else:
            # Check if the day has an event in the events dictionary
            if day in events:
                # If it does, add an asterisk before the day
                print(f'*{day}', end=' ')
            else:
                print(day, end=' ')
    print()
