
from django.urls import path , include

from .views import UpdateModelDetailAPIViews , UpdateModelListAPIViews


urlpatterns = [
    path('' , UpdateModelListAPIViews.as_view()),     # api/updates/ - List/Create
    path('<int:id>/' , UpdateModelDetailAPIViews.as_view()),

]
