from django.db import models
# Create your models here.
class maijia(models.Model):
    name=models.CharField(max_length=32) #生成varchar类型
    dianhua=models.CharField(max_length=30)
    emal=models.EmailField()#自动判断是否为邮箱账号
    time=models.DateTimeField(auto_now_add=True)  #写入当前系统时间
    def __str__(self):
        return self.name
class chanpin(models.Model):
    cat=(("shiwai","shiwai"),
         ("shinei","shinei")
    )
    name=models.CharField(max_length=20)
    jiage=models.CharField(max_length=30)
    zhonglei=models.CharField(max_length=30,choices=cat)#可以进行选项，选择室内还是室外
    miaoshu=models.TextField(blank=True,null=True)
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
class dingdan(models.Model):
    zhuangtai=(
        ("等待","等待"),
        ("正在","正在"),
        ("送达", "送达")

    )
    maijia=models.ForeignKey(maijia,on_delete=models.CASCADE,related_name="c_dingdan")
    chanpin=models.ForeignKey(chanpin,on_delete=models.CASCADE,related_name="d_dingdan")
    time= models.DateTimeField(auto_now_add=True)
    zhuangtai=models.CharField(max_length=30,choices=zhuangtai)
    def __str__(self):
        return self.zhuangtai
