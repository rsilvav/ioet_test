import sys
import logging

# Monday - Friday
# 00:01 - 09:00 25 USD
# 09:01 - 18:00 15 USD
# 18:01 - 00:00 20 USD
# Saturday and Sunday
# 00:01 - 09:00 30 USD
# 09:01 - 18:00 20 USD
# 18:01 - 00:00 25 USD

# This can be read from a configfile, but is not in scope of challenge
mon_fri = (25,)*9 + (15,)*9 + (20,)*6
sat_sun = (30,)*9 + (20,)*9 + (25,)*6

pay_values = {"MO": mon_fri, "TU": mon_fri, "WE": mon_fri, "TH": mon_fri, "FR": mon_fri,
              "SA": sat_sun, "SU": sat_sun}


def get_name_intervals(line_string):
    # Parses input line (NAME=INTERVALS) into a tuple with name and working intervals
    data = line_string.partition("=")
    name = data[0]
    intervals = data[-1]
    days = intervals.split(",")
    return (name, days)


def string_to_hour(time_string):
    # Converts a time string (HH:MM or H:MM) into hour int (H)
    if time_string == "23:59":
        return 24    # 00:00 (not handled) and 24:00 (handled) correspond to next day, so correct input is considered to be 23:59
    hour_minutes = time_string.partition(":")
    hour_string = hour_minutes[0]
    if hour_string.isnumeric():
        hour_int = int(hour_string)
    else:
        hour_int = 0
        logging.error("Bad time input: " + time_string)
    return hour_int


def get_day_payment(day_hours):
    # Calculates daily payment from a DD-HH:MM string
    if len(day_hours) <= 2:
        logging.error("Bad day-time input: " + day_hours)
        return 0
    day = day_hours[0:2]
    times_string = day_hours[2:]
    limit_times = times_string.partition("-")
    start_time = limit_times[0]
    end_time = limit_times[-1]
    start_hour = string_to_hour(start_time)
    end_hour = string_to_hour(end_time)
    values = pay_values[day]
    earned = values[start_hour:end_hour]
    day_payment = sum(earned)
    return day_payment


def main():
    file_path = sys.argv[1]
    file = open(file_path, "r")

    for line in file:
        name, days = get_name_intervals(line)
        pay = 0
        for interval in days:
            pay += get_day_payment(interval)
        print("The amount to pay", name, "is:", pay, "USD")
    file.close()


if __name__ == '__main__':
    main()
