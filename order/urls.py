from django.urls import path
from . import views
# from . import views
urlpatterns = [
	path('^new/$',views.new_order,name = 'new_order')
    # path('bascket_riew/$',views.bascket_riew, name = 'bascket_riew'),
    # # path('/(?<goods_id>/$',views.GoodsPage, name = 'Goodspage'),
    # path('add_to_basket/$',views.add_basket, name = 'add_to_basket'),
    # path('', views.AllGoods),

]
