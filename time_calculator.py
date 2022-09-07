def add_time(start, duration, day=False):
  
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

    print("Total hours:", total_hours)
    print("Total mins:", total_mins)
    return "Testing"