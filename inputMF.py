import pandas as pd
import pymysql

melon_db = pymysql.connect(
    user='joeun',\
    passwd='1234',\
    host='localhost',\
    db='tjoeun',\
    charset='utf8'\
    )
    
cursor = melon_db.cursor(pymysql.cursors.DictCursor)

# member테이블 가져오기
sql = "SELECT * FROM jypprj_member;"
cursor.execute(sql)
sql_result=cursor.fetchall()

pd_result = pd.DataFrame(sql_result)
# print(pd_result)

# m_result = pd.read_csv("M.csv",header=None)
# f_result=pd.read_csv("F.csv",header=None)
m_result = pd.read_csv("/root/Data/result/M/resultM.csv",header=None)
f_result=pd.read_csv("/root/Data/result/F/resultF.csv",header=None)
resultM=""
for i in range(m_result[0].count()):
    resultM = resultM+" "+str(m_result.loc[i,0]) 
    resultM = resultM.strip()
    
resultF=""
for i in range(f_result[0].count()):
    resultF = resultF+" "+str(f_result.loc[i,0]) 
    resultF = resultF.strip()

for i in range(pd_result["id"].count()):
    gender = pd_result.loc[i,"gender"]
    if gender == "남성":
        sql = "UPDATE jypprj_member SET com_genre='"+resultM+"' WHERE id='"+pd_result.loc[i,"id"]+"';"
        cursor.execute(sql)
    else:
        sql = "UPDATE jypprj_member SET com_genre='"+resultF+"' WHERE id='"+pd_result.loc[i,"id"]+"';"
        cursor.execute(sql)

sql = "commit;"
cursor.execute(sql)





