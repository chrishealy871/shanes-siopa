from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.hello_world, name='index'),
]