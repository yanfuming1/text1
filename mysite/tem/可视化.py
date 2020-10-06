import pymysql
import matplotlib.pyplot as plt
conn=pymysql.connect(host="localhost",user="root",password='077054',database="storage1")
cursor=conn.cursor()
rse=cursor.execute("select 名称,数量 from 物品")
res1=cursor.fetchall()
c=["数码3c","家电","生鲜","日用品"]
d=[]
for iii in c:
    sql="select * from 记录 where 物品种类='%s'"%iii
    print(sql)
    rse1 = cursor.execute(sql)
    d.append(rse1)
print(d)
cursor.close()
conn.close()
a=[]
b=[]

for i,j in res1:
    a.append(i)
    b.append(j)

plt.rcParams['font.sans-serif'] = ['SimHei']
fig,axes=plt.subplots(ncols=1)
axes.bar(a,b,color="m")
axes.axhline(0, color='gray', linewidth=2)
xzhou=0
for x,y in res1:
    plt.text(xzhou-0.4,y+20,"%s"%y)
    xzhou=xzhou+1
plt.title("仓库库存")
plt.xlabel('x 物品名称')
plt.ylabel('y 物品数量')
plt.savefig('E:/eclipes1/stronger/WebContent/image/a1.jpg')
fig,axe=plt.subplots(ncols=1)
axe.bar(c,d,color="m")
axe.axhline(0, color='gray', linewidth=2)
plt.title("交易数量")
xzhou=0
for x,y in zip(c,d):
    plt.text(xzhou,y+0.1,"%s"%y)
    xzhou=xzhou+1

plt.savefig('E:/eclipes1/stronger/WebContent/image/b1.jpg')
plt.show()