from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from .provider import SWCombineProvider


urlpatterns = default_urlpatterns(SWCombineProvider)
