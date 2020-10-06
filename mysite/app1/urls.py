
from django.urls import path,include

from app1 import views

urlpatterns = [
    path("a",views.a),
    path("",views.b,name="shouye"),
    path("crateq",views.crate,name="crate"),
    path("gai",views.gai,name="gai"),
    path("gengxin/<str:pk>",views.gengxin,name="gengxin"),
    path("shanchu/<str:pk>",views.shanchu,name="shanchu"),
]