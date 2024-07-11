from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views.home import store, Index
from .views.login import logout_request, login_request
from .views.registration import registration_request

app_name = 'store'
urlpatterns = [
                  # route is a string contains a URL pattern
                  # view refers to the view function
                  # name the URL

                  path(route='', view=store, name='store'),
                  path(route='logout/', view=logout_request, name='logout'),
                  path(route='login/', view=login_request, name='login'),
                  path(route='registration/', view=registration_request, name='registration'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
