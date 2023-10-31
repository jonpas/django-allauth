import requests

from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2CallbackView,
    OAuth2LoginView,
)

from .client import SWCombineClient
from .provider import SWCombineProvider


class SWCombineOAuth2Adapter(OAuth2Adapter):
    client_class = SWCombineClient
    provider_id = SWCombineProvider.id

    provider_base_url = "https://www.swcombine.com/ws"

    access_token_url = f"{provider_base_url}/oauth2/token/"  # requires trailing slash!
    authorize_url = f"{provider_base_url}/oauth2/auth/"
    character_url = f"{provider_base_url}/v2.0/character"

    headers = {"Accept": "application/json"}

    def complete_login(self, request, app, token, **kwargs):
        resp = requests.get(self.character_url, params={"access_token": token}, headers=self.headers)
        resp.raise_for_status()
        extra_data = resp.json()["swcapi"]["character"]
        return self.get_provider().sociallogin_from_response(request, extra_data)

oauth2_login = OAuth2LoginView.adapter_view(SWCombineOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(SWCombineOAuth2Adapter)
