def add_time(start, duration, day=False):
    # print("Start time:", start)
    # print("Duration:", duration)
    # print("Day:", day)
  
    hours, mins = start.split(":")
    mins, day_time = mins.split(" ")
    duration_hours, duration_mins = duration.split(":")

  # Make the data consistent
    hours = int(hours)  
    mins = int(mins)  
    duration_hours = int(duration_hours)  
    duration_mins = int(duration_mins)  
    day_time = day_time.strip().lower() # 'am' or 'pm'

  # Get the totals
    total_hours = hours + duration_hours
    total_mins = mins + duration_mins

    if total_mins >= 60:
      total_hours = total_hours + int(total_mins / 60)
      total_mins = int(total_mins % 60)

  # If there was a duration - calculate the passage of time
    days_later = 0
    if duration_hours or duration_mins:
      if day_time == "pm" and total_hours > 12:
      # Changing to another day if start time is pm
        if total_hours % 24 >= 1.0:
          days_later += 1  
              
      if total_hours >= 12:
        hours_left = total_hours / 24
        days_later = days_later + int(hours_left)

      total_hours_storage = total_hours
      while True:
        if total_hours_storage < 12:
          break
        if total_hours_storage >= 12:
          if day_time == "am":
            day_time = "pm"
          elif day_time == "pm":
            day_time = "am"
        total_hours_storage = total_hours_storage - 12

    remaining_hours = int(total_hours % 12) or hours + 1
    remaining_mins = int(total_mins % 60)

    # Format the resulting time 
    result = f'{remaining_hours}:{remaining_mins:02} {day_time.upper()}'


    # Deal with days
    week_day =  [
        'monday', 'tuesday',
        'wednesday', 'thursday',
        'friday', 'saturday',
        'sunday'
      ]
  
    if day: 
        day = day.strip().lower()
        starting_day_index = week_day.index(day)
        new_day_index = int((starting_day_index + days_later) % 7)
        new_day = week_day[new_day_index]
        if days_later == 1:
          days_later_tag = "(next day)"
          result = result + f', {new_day.title()} {days_later_tag}'
        elif days_later > 1:
          days_later_tag = f"({days_later} days later)"
          result = result + f', {new_day.title()} {days_later_tag}'
        elif days_later == 0:
          result = result + f', {new_day.title()}'
    else: 
        if days_later == 1:
          days_later_tag = "(next day)"
          result = result + " " + days_later_tag
        elif days_later > 1:
          days_later_tag = f"({days_later} days later)"
          result = result + " " + days_later_tag
          
    # print(result.strip())
    return result.strip()