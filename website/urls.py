from django.urls import path
from website import views

urlpatterns = [
    path('',views.index,name='index'),
    path('article/<int:id>',views.article,name='article'),
    path('test/',views.test_article,name='test_article'),
    path('page/<int:pagenum>',views.page,name='page'),
    path('tag/<tagname>',views.orderBytags,name='tag')
]


