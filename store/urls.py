from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views.home import Index

app_name = 'store'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL
    path(route='', view=Index.as_view(), name='index'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)