from django.urls import path
from django.views.generic import TemplateView
from bootpages.views import HomeView

app_name = "bootpages"

urlpatterns = [path("", HomeView.as_view(template_name="pages/home.html"), name="home")]
