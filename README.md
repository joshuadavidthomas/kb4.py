# knowbe4.py: A Python wrapper for the KnowBe4 API

![KnowBe4](knowbe4.jpg)

knowbe4.py is a simple Python wrapper for the KnowBe4 reporting API.

For more information on the API, please visit the [KnowBe4 API documentation](https://developer.knowbe4.com/).

## Installation

```bash
pip install knowbe4.py
```

## Usage

```python
from kb4 import KnowBe4

KB4_API_KEY='<Secret key obtained from KnowBe4 website.>'

kb4 = KnowBe4(KB4_API_KEY)

kb4.account()
kb4.users()
kb4.user(USER_ID)
kb4.groups()
kb4.group(GROUP_ID)
kb4.group_members(GROUP_ID)
kb4.phishing_campaigns()
kb4.phishing_campaign(CAMPAIGN_ID)
kb4.phishing_security_tests()
kb4.phishing_campaign_security_tests(CAMPAIGN_ID)
kb4.phishing_campaign_security_test(PST_ID)
kb4.phishing_campaign_security_test_recipients(PST_ID)
kb4.phishing_campaign_security_test_recipient(PST_ID, USER_ID)
kb4.store_purchases()
kb4.store_purchase(STORE_PURCHASE_ID)
kb4.policies()
kb4.policy(POLICY_ID)
kb4.training_campaigns()
kb4.training_campaign(CAMPAIGN_ID)
kb4.training_enrollments()
kb4.training_enrollment(ENROLLMENT_ID)
```

## Contributing

All contributions are welcome and appreciated.

1. Fork
2. Feature branch
3. Pull request

## Meta

Josh Thomas - josh@joshuadavidthomas.com

Distributed under the MIT license. See `LICENSE` for more information.

[https://github.com/elderlydoofus/knowbe4.py](https://github.com/elderlydoofus/knowbe4.py)
