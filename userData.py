import pymysql
import csv
import pandas as pd
from datetime import datetime

today = datetime.today().year                               
save_date = datetime.today().strftime( "%Y-%m-%d" )

melon_db = pymysql.connect(
    user='joeun',\
    passwd='1234',\
    host='localhost',\
    db='tjoeun',\
    charset='utf8'\
    )
    
cursor = melon_db.cursor(pymysql.cursors.DictCursor)

sql = "SELECT m.id, m.gender, m.birthday, p.num FROM  jypprj_member m, jypprj_playlist p where m.id = p.user_id_id; "
cursor.execute(sql)
user_result = cursor.fetchall()
def user_DB(user_result):
    userDF = pd.DataFrame(user_result,columns=["id", "gender", "birthday", "num"])
    num=userDF["id"].count()
    userD = pd.DataFrame(columns=["id", "gender", "birthday", "num"])
    userG = pd.DataFrame(columns=["id", "gender", "birthday", "num"])
    
    for i in range(num):
        udnum=0
        num2=int(userG["id"].count())
        # print(type(num2))
        print("="*20)
        userDF.loc[i,"num"] = userDF.loc[i,"num"].strip()
        print("userDF.loc[i,num] : ", userDF.loc[i,"num"])
        udnum=userDF.loc[i,"num"].split(' ')
        print(udnum)
        # print(len(udnum))
        userD =  userDF.loc[i,:]
        if len(udnum) >= 2 :
            
            # print(userD["id"])
            # userDF=userDF.drop(userDF.index[userDF["id"] == userD["id"]].tolist())
            for j in range(len(udnum)):
                print("i: {}, j :{}".format(i,j))
                userG.loc[num2+j,"id"] = userD["id"]
                if userD["gender"] == "남성":
                    userG.loc[num2+j,"gender"] ="M"
                elif userD["gender"] == "여성" :
                    userG.loc[num2+j,"gender"] ="F"
                age=int(userD["birthday"][0:2])
                # print(type(userD["birthday"]))
                if age >=60 and age <=99:
                    userG.loc[num2+j,"birthday"] =str(age+1900)
                elif age >=0 and age <=20:
                    userG.loc[num2+j,"birthday"] =str(age+2000)
                userG.loc[num2+j,"num"] = udnum[j]
                
        else : 
            userG.loc[num2+i,"id"] = userD["id"]
            age=int(str(userDF.loc[i,"birthday"][0:2]))
            if age >=60 and age <=99:
                userG.loc[num2+i,"birthday"] =str(age+1900)
            elif age >=0 and age <=20:
                userG.loc[num2+i,"birthday"] =str(age+2000)
            if userD["gender"] == "남성":
                userG.loc[num2+i,"gender"] ="M"
            elif userD["gender"] == "여성" :
                userG.loc[num2+i,"gender"] ="F" 
            userG.loc[num2+i,"num"] = udnum[0]
    return userG
userG = user_DB(user_result)
userG = userG.reset_index(drop=True)
userG.to_csv('/root/Data/userData/userData.csv',index=False,encoding='utf-8-sig')

# sql = "SELECT m.id, m.gender, m.birthday, l.num FROM  jypprj_member m, jypprj_like l where m.id = l.user_id_id; "
# cursor.execute(sql)
# user_result = cursor.fetchall()
# userG = user_DB(user_result)
# userG = userG.reset_index(drop=True)
# userG.to_csv('userLdata.csv',index=False,encoding='utf-8-sig')
# userDF.to_csv('~/userData.csv',index=False,encoding='utf-8-sig')
# ========================
# userd = pd.read_csv('~/userData.csv',encoding='utf-8',header=0)
# artistd = pd.read_csv('~/artist_Data.csv',encoding='utf-8',header=0)

userP = pd.read_csv('/root/Data/userData/userData.csv',encoding='utf-8',header=0)
# userL = pd.read_csv('userPdata.csv',encoding='utf-8',header=0)

artistd = pd.read_csv('/root/Data/artistData/artist_Data.csv',encoding='utf-8',header=0)



def user_Data(userd, num):
    df = pd.DataFrame(columns=["userID","gender","age","singer"])
    for i in range(num):
        num2 = df["userID"].count()
        index = artistd.index[artistd["num"]==str(userd.loc[i,"num"])].tolist()
        # print( artistd.loc[artistd["num"]==str(userd.loc[i,"num"]),"num"])
        # print("="*50)
        # print(userd.loc[i,"id"])
        if len(index) == 0:
            df.loc[num2+i,"userID"]=userd.loc[i,"id"]
            df.loc[num2+i,"gender"]=userd.loc[i,"gender"]
            age= int( (2021 - userd.loc[i,"birthday"]) / 10)
            if age == 1:
                df.loc[num2+i,"age"]=10
            elif age == 2:
                df.loc[num2+i,"age"]=20
            elif age == 3:
                df.loc[num2+i,"age"]=30
            elif age == 4:
                df.loc[num2+i,"age"]=40
            elif age == 5:
                df.loc[num2+i,"age"]=50
            elif age == 6:
                df.loc[num2+i,"age"]=60
            elif age == 7:
                df.loc[num2+i,"age"]=70
            df.loc[num2+i,"singer"]=artistd.loc[num2+i,"singer"]
        else:
            for j in range(len(index)) :
                df.loc[num2+j,"userID"]=userd.loc[i,"id"]
                df.loc[num2+j,"gender"]=userd.loc[i,"gender"]
                age= (2021 - userd.loc[i,"birthday"]) // 10
                if age == 1:
                    df.loc[num2+j,"age"]=10
                elif age == 2:
                    df.loc[num2+j,"age"]=20
                elif age == 3:
                    df.loc[num2+j,"age"]=30
                elif age == 4:
                    df.loc[num2+j,"age"]=40
                elif age == 5:
                    df.loc[num2+j,"age"]=50
                elif age == 6:
                    df.loc[num2+j,"age"]=60
                elif age == 7:
                    df.loc[num2+j,"age"]=70
                df.loc[num2+j,"singer"]=artistd.loc[index[j],"singer"]
    df = df.reset_index(drop=True)
    df = df.sort_values("userID",axis=0)
    df = df.reset_index(drop=True)
    return df
num = userP["id"].count()
df = user_Data(userP,num)
df.to_csv('/root/Data/userGenre/userP'+save_date+'.csv',index=False,encoding='utf-8-sig',header=None)
# df = user_Data(userL,num)
# df.to_csv('userL'+save_date+'.csv',index=False,encoding='utf-8-sig',header=None)
print("작업완료")













