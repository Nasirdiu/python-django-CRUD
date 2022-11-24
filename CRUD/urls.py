
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.INDEX,name='home'),
    path('add',views.ADD,name='add'),
    path('edit',views.EDIT,name='edit'),
    path('update/<str:id>',views.Update,name='update'),
]
