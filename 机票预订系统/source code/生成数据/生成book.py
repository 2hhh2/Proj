import random
from datetime import datetime, timedelta

with open(r'X:\大二下\数据库系统\实践\期末项目\数据\user.txt', 'r', encoding='utf-8') as f1:
    lines1 = f1.readlines()
    with open(r'X:\大二下\数据库系统\实践\期末项目\数据\flight.txt', 'r', encoding='utf-8') as f2:
        lines2 = f2.readlines()
        with open(r'X:\大二下\数据库系统\实践\期末项目\数据\book.txt', 'a', encoding='utf-8') as f3:
            for i in range(50000):
                id = ''
                for j in range(12):
                    id = id +str(random.randint(0,9))

                row1 = random.randint(1,99899)
                l1 = lines1[row1]
                data1 = l1.split(' ')
                u_id = data1[1]
                row2 = random.randint(1,999999)
                l2 = lines2[row2]
                data2 = l2.split('\t')
                f_id = data2[0]


                datetime1 = datetime.strptime(data2[4], "%Y-%m-%d %H:%M:%S")
                datetime2 = datetime1 - timedelta(days=1)

                seatnum = random.randint(0,300)

                print(id,u_id,f_id,datetime2,seatnum,file=f3,sep='\t')





