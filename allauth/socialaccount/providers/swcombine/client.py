import requests

from allauth.socialaccount.providers.oauth2.client import (
    OAuth2Client,
    OAuth2Error,
)


class SWCombineClient(OAuth2Client):
    def get_access_token(self, code, pkce_code_verifier=None):
        data = {
            "code": code,
            "client_id": self.consumer_key,
            "client_secret": self.consumer_secret,
            "redirect_uri": self.callback_url,
            "grant_type": "authorization_code",
        }

        resp = requests.request(self.access_token_method, self.access_token_url, data=data, headers=self.headers)

        access_token = None
        if resp.status_code in [200, 201]:
            access_token = resp.json()
        if not access_token or "access_token" not in access_token:
            raise OAuth2Error("Error retrieving access token: %s" % resp.content)
        return access_token
