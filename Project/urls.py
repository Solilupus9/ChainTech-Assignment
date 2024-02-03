from django.urls import path
from django.contrib import admin
from . import views

urlpatterns=[
    path('admin/', admin.site.urls),
    path('',views.main,name='main'),
    path('dataentered/',views.SubmitData.as_view(),name='add'),
    path('success/',views.success,name='success'),
    path('viewdata/',views.viewdata,name='viewdata'),
]
