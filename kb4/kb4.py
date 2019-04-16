import json
import requests

from .exceptions import ConfigurationError, HTTPError


__url_cache__ = {}


class KnowBe4(object):

  class_name = "KnowBe4"

  def __init__(self, token=''):
    self._base_url = 'https://us.api.knowbe4.com/v1'
    self._token = token

  def _build_url(self, *args, **kwargs):
    """
    Build a new API url from scratch.
    
    Taken from github.com/sigmavirus24/github3.py
    """
    parts = [kwargs.get("base_url") or self._base_url]
    parts.extend(args)
    parts = [str(p) for p in parts]
    key = tuple(parts)
    if key not in __url_cache__:
      __url_cache__[key] = "/".join(parts)
    return __url_cache__[key]

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
      raise HTTPError(resp.body['message'], resp.status_code)

  def _get(self, url):
    return self._request('GET', url)

  def account(self):
    url = self._build_url("account")
    json = self._json(self._get(url))
    return json