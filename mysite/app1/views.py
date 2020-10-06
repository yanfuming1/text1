from django.shortcuts import render, redirect
from . import models
# Create your views here.
from .models import maijia, chanpin, dingdan
from .forms import maijiaform, chanpinform, dingdanform


def a(request):
    return render(request, "shouye.html")


def b(request):
    yonghu = maijia.objects.all()
    shuliang = yonghu.count()
    changjia = chanpin.objects.all()

    dengdai = dingdan.objects.filter(zhuangtai="等待").count()
    zhengzai = dingdan.objects.filter(zhuangtai="正在").count()
    songda = dingdan.objects.filter(zhuangtai="送达").count()
    context = {
        "yonghu": yonghu,
        "shuliang": shuliang,
        "changjia": changjia,
        "dengdai": dengdai,
        "zhengzai": zhengzai,
        "songda": songda
    }
    return render(request, "index/home.html", context)


def crate(request):
    a = maijiaform()
    b = chanpinform()
    c = dingdanform()

    if request.method == "POST":

        if 'a' in request.POST:

            a_form = maijiaform(request.POST)

            if a_form.is_valid():
                name = a_form.cleaned_data["name"]
                dianhua = a_form.cleaned_data["dianhua"]
                emal = a_form.cleaned_data["emal"]

                jiaru = maijia.objects.create(name=name, dianhua=dianhua, emal=emal)
                jiaru.save()
                return redirect("shouye")
        if "b" in request.POST:
            shuju = request.POST
            jiaru = chanpin.objects.create(name=shuju["name"], jiage=shuju["jiage"], zhonglei=shuju["zhonglei"],
                                           miaoshu=shuju["miaoshu"])
            jiaru.save()
            return redirect("shouye")
    context = {"maijia": a,
               "shangpin": b,
               "dingdan": c,
               }
    return render(request, "index/crate.html", context)


def gai(request):
    return 0;


def gengxin(request, pk):
    geng = chanpin.objects.get(id=pk)
    a_form = chanpinform(instance=geng)
    if "b" in request.POST:

        a_form = chanpinform(request.POST)
        print(a_form.is_valid())
        if a_form.is_valid():
            name = a_form.cleaned_data["name"]
            jiage = a_form.cleaned_data["jiage"]
            zhonglei = a_form.cleaned_data["zhonglei"]
            miaoshu = a_form.cleaned_data["miaoshu"]
            a = chanpin.objects.filter(id=pk).update(id=pk, name=name, jiage=jiage, zhonglei=zhonglei, miaoshu=miaoshu)
            print("sdf")
            return redirect("shouye")

    context = {
        "ord": geng,
        "chanpin": a_form,
    }
    return render(request, "caozuo/gengxin.html", context)


def shanchu(request, pk):

    chanpin.objects.filter(id=pk).delete()
    return redirect("shouye")
