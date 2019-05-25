    import calendar

    m,d,y=list(input().split())

    ar=['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']

    print(ar[calendar.weekday(int(y),int(m),int(d))])