from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views.checkout import checkout_view
from .views.detail import product_detail
from .views.cart import cart, update_cart
from .views.home import store, Index
from .views.login import logout_request, login_request
from .views.registration import registration_request

app_name = 'store'
urlpatterns = [
                  # route is a string contains a URL pattern
                  # view refers to the view function
                  # name the URL
                  path(route='', view=Index.as_view(), name='homepage'),
                  path(route='index/', view=store, name='store'),
                  path(route='logout/', view=logout_request, name='logout'),
                  path(route='login/', view=login_request, name='login'),
                  path(route='registration/', view=registration_request, name='registration'),
                  path(route='cart/', view=cart, name='cart'),
                  path(route='update_cart/', view=update_cart, name='update_cart'),
                  path(route='product-detail/', view=product_detail, name='product_detail'),
                  path(route='checkout-view/', view=checkout_view, name='checkout_view'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
