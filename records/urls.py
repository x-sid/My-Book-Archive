from django.urls import path,re_path
from records import views

app_name='records'

urlpatterns = [

    re_path(r'^books/create/$',views.bookcreate,name='create'),
    re_path(r'^books/(?P<pk>\d+)/update/$',views.book_update,name='book_update'),
    re_path(r'^books/(?P<pk>\d+)/delete/$',views.book_delete,name='book_delete'),

]
