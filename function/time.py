def convert_durasi(time):
    hours = time // 3600
    minutes = (time % 3600)//60
    secs = time % 60
    return hours,minutes,secs