import time


def getDateTimeUniqueNumber():
    def get_ist_datetime():
        current_time = time.time()
        ist_time = time.localtime(current_time)  # + (ist_offset * 3600))
        return ist_time

    # Usage example
    current_datetime = get_ist_datetime()
    formatted_date = time.strftime("%y-%m-%d", current_datetime)
    formatted_time = time.strftime("%H:%M:%S", current_datetime)

    return formatted_date.replace("-", "")+formatted_time.replace(":", "")


def getUniqueId():
    return int(time.time()*10000)


ABCD = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def generateId():
    x = str(int(time.time()*1000000))
    t = ""
    time.sleep(0.000000000000000000000000000000000005)
    for i in range(len(x)//2-3):
        t += ABCD[int(x[i*2:i*2+2]) % 26]
    return t + x[11:]
# zz=[]
# print(generateId())
# for i in range(100):
#     zz.append(generateId())
# print(len(set(zz)))
