# import path
from django.urls import path

# import views
from . import views

# create a path for our wine_recom homepage. This is the view that
# gets run when we go to /admin. Use an empty path to go to homepage
# specify the view that we want to handle the logic at homepage route
# to be the home view from our views module in wine_recom directory
urlpatterns = [
    path('', views.Home, name='wine_recom-Home'),
    path('Report', views.Report, name='Report'),
    path('Suggestion', views.Suggestion, name='Suggestion')
]