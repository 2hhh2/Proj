import random
import datetime

numchar = '0123456789QWERTYUIOPASDFGHJKLZXCVBNM'

start_date = datetime.date(2023, 7, 1)
end_date = datetime.date.today()
end_date += datetime.timedelta(days=180)

days_since_start = (end_date - start_date).days


with open(r'X:\大二下\数据库系统\实践\期末项目\数据\flight619.txt', 'a', encoding='utf-8') as f:
    for i in range(180):
        id=''
        for j in range(8):
            id = id + str(random.choice(numchar))
        airline = '公司'+str(random.randint(1,10))

        da = random.randint(1,39)
        while(1):
            aa = random.randint(1,39)
            if aa!=da:
                break

        random_number_of_days = random.randrange(days_since_start)
        #random_number_of_days = 90

        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        random_hour = random.randint(0, 22)
        random_time = datetime.time(random_hour, random.randint(0, 59), random.randint(0, 59))
        dt = datetime.datetime.combine(random_date, random_time)

        random_hour2 = random.randint(random_hour, 23)
        random_time2 = datetime.time(random_hour2, random.randint(0, 59), random.randint(0, 59))
        at = datetime.datetime.combine(random_date, random_time2)

        price = random.randint(500,3000)

        availseat = random.randint(0,500)
        print(id, airline, da, aa, dt, at, price, availseat, file=f, sep='\t')
        #print(id, airline, da, aa, dt, at, price, availseat, sep='\t')



