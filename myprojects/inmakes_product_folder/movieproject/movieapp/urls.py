
from django.urls import path,include
from.import views
app_name='movieapp'
urlpatterns = [

    path('',views.index,name='index'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('add/',views.add_movie,name='add_movie'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    # path('movie/<int:movie_id>/',views.addon,name='addon'),
    # path('update1/<int:id>/',views.update1,name='update1')

]
