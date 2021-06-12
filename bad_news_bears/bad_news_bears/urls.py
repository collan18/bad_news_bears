"""bad_news_bears URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

# admin route that gets mapped to admin site URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    # add to our urlpatterns to specify which route should go to our
    # wine_recom urls. If you go to wine_recom, reference 
    # the wine_recom URLs
    path('wine_recom/', include('wine_recom.urls')),
]
# line 21 means if we go to our browser and to /wine_recom, then it will
# map that to our wine_recom URLs, then within wine_recom URLs we have
# that empty path that maps on to our home view 