from django.conf.urls import url
from . import views
app_name = "ModelForm"
urlpatterns = [
    url(r'^$',views.insert.as_view())
]