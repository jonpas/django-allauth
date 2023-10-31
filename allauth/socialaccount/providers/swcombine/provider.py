from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class SWCombineAccount(ProviderAccount):
    def get_avatar_url(self):
        return self.account.extra_data.get("image")

    def to_str(self):
        dflt = super(SWCombineAccount, self).to_str()
        return self.account.extra_data.get("name", dflt)


class SWCombineProvider(OAuth2Provider):
    id = "swcombine"
    name = "SWCombine"
    account_class = SWCombineAccount

    def extract_uid(self, data):
        return str(data["uid"])

    def extract_common_fields(self, data):
        return dict(
            name=data.get("name", ""),
            image=data.get("image", ""),
        )

    def get_default_scope(self):
        return ["character_read"]


provider_classes = [SWCombineProvider]
