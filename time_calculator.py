
def add_time(start, duration, day=''):
    start_split = start.split()

    days_passed = 0
    meridian = start_split[1]  # PM or AM

    def am_pm_switch(meridian, days_passed):  # switches AM-PM / PM-AM
        if meridian == 'AM':
            meridian = 'PM'
        else:
            meridian = 'AM'
            days_passed += 1
        return meridian, days_passed

    start_hour = int(start_split[0].split(':')[0])
    start_min = int(start_split[0].split(':')[1])

    dur_hour = int(duration.split(':')[0])
    dur_min = int(duration.split(':')[1])

    res_hour = start_hour + dur_hour
    res_min = start_min + dur_min

    # formatting minutes
    if res_min >= 60:
        res_hour += res_min // 60
        res_min = res_min % 60

    if res_min < 10:  # add 0 in front of single digit
        res_min = '0' + str(res_min)

    # formatting hours
    if res_hour == 12:
        meridian, days_passed = am_pm_switch(meridian, days_passed)

    elif res_hour > 12:
        subsets = res_hour // 12
        for i in range(subsets):  # apply switch every 12 hours
            meridian, days_passed = am_pm_switch(meridian, days_passed)
        res_hour -= 12 * subsets

    if res_hour == 0:  # ensuring 12h format
        res_hour = 12

    # basic result variable
    new_time = str(res_hour) + ':' + str(res_min) + ' ' + meridian

    # modifying result variable to display weekday
    if day != '':
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

        idx = weekdays.index(day.lower().capitalize())
        cur_w = weekdays[idx]

        for i in range(days_passed):
            if idx + 1 <= 6:
                idx += 1
                cur_w = weekdays[idx]
            elif idx + 1 > 6:
                idx = 0
                cur_w = weekdays[idx]

        new_time += ', ' + cur_w

    # modifying result variable to display days passed
    if days_passed == 1:
        new_time += ' (next day)'
    elif days_passed > 1:
        new_time += ' (' + str(days_passed) + ' days later)'

    return new_time
