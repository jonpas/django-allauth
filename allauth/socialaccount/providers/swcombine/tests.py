from allauth.socialaccount.tests import OAuth2TestsMixin
from allauth.tests import MockedResponse, TestCase

from .provider import SWCombineProvider


class SWCombineTests(OAuth2TestsMixin, TestCase):
    provider_id = SWCombineProvider.id

    def get_mocked_response(self):
        return MockedResponse(
            200,
            """
{
    'version': '2.0', 'timestamp': 1698708007, 'swcapi': {
        'character': {
            'uid': '1:1402816',
            'name': 'Handle',
            'image': '',
            'lastlogin': {
                'years': 24,
                'days': 338,
                'hours': 16,
                'mins': 18,
                'secs': 54,
                'timestamp': '1698707934'
            },
        }
    }
}
        )
