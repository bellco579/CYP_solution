from django.urls import path
from . import views
# from . import views
urlpatterns = [
	path('every_order/$',views.every_order,name = 'every_order'),
	path('new/$',views.new_order,name = 'new_order'),
	path('show/(?<order_id>)/$',views.show_offer,name = 'show_offer'),
	path('personal_page/(?<order_id>/$',views.order_pp,name = 'order_pp'),
    # path('bascket_riew/$',views.bascket_riew, name = 'bascket_riew'),
    # # path('/(?<goods_id>/$',views.GoodsPage, name = 'Goodspage'),
    # path('add_to_basket/$',views.add_basket, name = 'add_to_basket'),
    # path('', views.AllGoods),
    # path('(?<goods_id>/$',views.GoodsPage, name = 'Goodspage'),

]
