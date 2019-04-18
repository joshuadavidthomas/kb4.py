from dotenv import load_dotenv
import os
from pytest import fixture
import vcr

from kb4 import KnowBe4

load_dotenv()
KB4_API_KEY = os.environ.get('KB4_API_KEY', None)


@fixture
def account_info():
  return [
            'name',
            'type',
            'domains',
            'admins',
            'subscription_level',
            'subscription_end_date',
            'number_of_seats',
            'current_risk_score',
            'risk_score_history'
          ]


@vcr.use_cassette('tests/cassettes/account_info.yml')
def test_account_info(account_info):
  """Tests an API call to get KnowBe4 account info."""

  kb4 = KnowBe4(KB4_API_KEY).account()

  assert isinstance(kb4, dict)
    assert set(account_info).issubset(
        kb4.keys()), "All keys should be in the response"

