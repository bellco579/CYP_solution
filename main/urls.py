from django.urls import path
from . import views
# from . import views
urlpatterns = [
    path('',views.home, name = 'home'),
    # path('/(?<goods_id>/$',views.GoodsPage, name = 'Goodspage'),
    # path('', views.AllGoods),

]
