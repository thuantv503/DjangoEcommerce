from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views.home import store, Index

app_name = 'store'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL

    path(route='', view=store, name='store'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)