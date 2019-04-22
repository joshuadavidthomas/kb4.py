import json
import requests

from .exceptions import ConfigurationError, HTTPError


__url_cache__ = {}


class KnowBe4(object):

    class_name = 'KnowBe4'

    def __init__(self, token=''):
        self._base_url = 'https://us.api.knowbe4.com/v1'
        self._token = token

    def _build_url(self, *args, **kwargs):
        '''
        Build a new API url from scratch.

        Taken from github.com/sigmavirus24/github3.py
        '''
        parts = [kwargs.get('base_url') or self._base_url]
        parts.extend(args)
        parts = [str(p) for p in parts]
        key = tuple(parts)
        if key not in __url_cache__:
            __url_cache__[key] = '/'.join(parts)
        return __url_cache__[key]

    def _append_parameters(self, url, *args, **kwargs):
        parameters = []
        for i in kwargs:
            parameters.append(str(i) + "=" + str(kwargs[i]))
        parameters = '&'.join(parameters)
        url = url + '?' + parameters
        return url

    def _check_token(self):
        if not self._token:
            raise ConfigurationError('No API Token set.')

    def _headers(self):
        return {'Authorization': 'Bearer {0}'.format(self._token)}

    def _json(self, response):
        if response is None:
            return None
        else:
            ret = response.json()
        return ret

    def _request(self, method, url, data=None, headers=None, json=True):
        self._check_token()
        headers = self._headers()
        resp = requests.request(method, url, data=data, headers=headers)
        if resp.status_code == 204:
            return None
        if 200 <= resp.status_code < 300:
            return resp
        else:
            resp.raise_for_status()

    def _get(self, url):
        return self._request('GET', url)

    def _api_call(self, *args, **kwargs):
        url = self._build_url(*args)
        if kwargs:
            url = self._append_parameters(url=url, **kwargs)
        json = self._json(self._get(url))
        return json

    def account(self):
        return self._api_call('account')

    def users(self):
        return self._api_call('users')

    def groups(self):
        return self._api_call('groups')

    def group(self, id):
        return self._api_call('groups', id)

    def group_members(self, id):
        return self._api_call('groups', id, 'members')

    def user(self, id):
        return self._api_call('users', id)

    def phishing_campaigns(self):
        return self._api_call('phishing', 'campaigns')

    def phishing_campaign(self, id):
        return self._api_call('phishing', 'campaigns', id)

    def phishing_security_tests(self):
        return self._api_call('phishing', 'security_tests')

    def phishing_campaign_security_tests(self, id):
        return self._api_call('phishing', 'campaigns', id, 'security_tests')

    def phishing_campaign_security_test(self, id):
        return self._api_call('phishing', 'security_tests', id)

    def phishing_campaign_security_test_recipients(self, id):
        return self._api_call('phishing', 'security_tests', id, 'recipients')

    def phishing_campaign_security_test_recipient(self, pst_id, id):
        return self._api_call('phishing', 'security_tests', pst_id, 'recipients', id)

    def store_purchases(self):
        return self._api_call('training', 'store_purchases')

    def store_purchase(self, id):
        return self._api_call('training', 'store_purchases', id)

    def policies(self):
        return self._api_call('policies')

    def policy(self, id):
        return self._api_call('policies', id)

    def training_campaigns(self):
        return self._api_call('training', 'campaigns')

    def training_campaign(self, id):
        return self._api_call('training', 'campaigns', id)

    def training_enrollments(self):
        return self._api_call('training', 'enrollments')

    def training_enrollment(self, id):
        return self._api_call('training', 'enrollment', id)
