from django import forms
from django.forms import ModelForm
from app1.models import maijia,chanpin,dingdan
class maijiaform(ModelForm):
    class Meta:
        model=maijia
       # fields="__all__"
       # exclude=["time"]
        fields=['name','dianhua','emal']
        labels={
            "name":'姓名',
            "dianhua":'电话',
            "emal":"邮箱",
        }
        widgets={
            "name":forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"请输入姓名"
            }),
            "dianhua": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "请输入电话"
            }),
            "emal": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "请输入邮箱"
            })
        }
class chanpinform(ModelForm):
    class Meta:
        model=chanpin
        #fields="__all__"
        #exclude=["time"]
        fields = ['name', 'jiage', 'zhonglei',"miaoshu"]
        labels={
            "name":"产品名称",
            "jiage":"产品价格",
            "zhonglei":"产品种类",
            "miaoshu":"产品描述"
        }
        widgets={
            "name":forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"请输入产品名称"
            }),
            "jiage": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "请输入产品价格"
            }),
            "zhonglei": forms.Select(attrs={
                "class": "form-control",
                "placeholder": "请输入产品种类"
            }),
            "miaoshu": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "请输入产品描述"
            })
        }
class dingdanform(ModelForm):
    class Meta:
        model=dingdan
        fields="__all__"
        exclude=["time"]
        widgets = {
            "maijia": forms.Select(attrs={
                "class": "form-control",
                "placeholder": "请输入产品名称"
            }),
            "chanpin":forms.Select(attrs={
                "class": "form-control",
                "placeholder": "请输入产品名称"
            }),
            "zhuangtai": forms.Select(attrs={
                "class": "form-control",
                "placeholder": "请输入产品名称"
            }),
        }