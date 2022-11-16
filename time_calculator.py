def add_time(start, duration, initial_day=""):
    hours, minutes, half = split_time(start, duration)
    days, hours, minutes, half = do_addition(hours, minutes)
    if minutes < 10:
        new_time = f"{hours}:0{minutes} {half}"
    else:
        new_time = f"{hours}:{minutes} {half}"

    if initial_day:
        new_time += f", {calculate_day(days, initial_day.lower())}"

    if days == 0:
        return new_time
    elif days == 1:
        new_time += " (next day)"
    else:
        new_time += f" ({days} days later)"


    return new_time


def split_time(start, duration):
    hours = 0
    minutes = 0
    start = start.split(" ")
    half = start[1]
    start = start[0].split(":")
    hours = int(start[0])
    if half == "PM":
        hours += 12
    minutes = int(start[1])
    duration = duration.split(":")
    hours += int(duration[0])
    minutes += int(duration[1])


    return hours, minutes, half


def do_addition(hours, minutes):
    days = 0
    if minutes > 59:
        hours += 1
        minutes %= 60
    if hours > 24:
        days = hours // 24
        hours %= 24

    if hours == 0:
        hours = 12
        half = "AM"
    elif hours < 12:
        half = "AM"
    else:
        half = "PM"
        if hours != 12:
            hours -= 12


    return days, hours, minutes, half


def calculate_day(days, initial_day):
    days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    init_num = days_of_week.index(initial_day)
    result = (init_num + days % 7) % 7
    return days_of_week[result].capitalize()
