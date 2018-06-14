from django.urls import path
from . import views
# from . import views
urlpatterns = [
	path('every_order',views.every_order,name = 'every_order'),
	path('new',views.new_order,name = 'new_order'),
	path('show/(?<order_id>)',views.show_offer,name = 'show_offer'),
	path('personal_page/(?<order_id>',views.order_pp,name = 'order_pp'),

]
