def return_delay():
    import datetime
    now=datetime.datetime.now()
    #print(now)
    hour=int(now.strftime("%H"))
    minute=int(now.strftime("%M"))

    r_hours=8
    r_minutes=30

    if r_hours > hour:
        if r_minutes>=minute:
            n_hours=r_hours-hour
            n_minutes=r_minutes-minute
        else:
            hour=hour-1
            minute=minute+60
            n_hours=r_hours-hour
            n_minutes=r_minutes-minute
        run_at=now+datetime.timedelta(hours=n_hours,minutes=n_minutes)
        delay=(run_at-now).total_seconds()
        return delay

    elif r_hours==hour:
        if r_minutes>minute:
            n_hours=0
            n_minutes=r_minutes-minute
        elif r_minutes==minute:
            delay=5
            return delay
        else:
            print("please run at before 8.30")
            return False
        
        run_at=now+datetime.timedelta(hours=n_hours,minutes=n_minutes)
        delay=(run_at-now).total_seconds()
        return delay

    else:
        print("Please run at before 8.30 time")
        return False

