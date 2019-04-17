# knowbe4.py: A Python wrapper for the KnowBe4 API

![KnowBe4](knowbe4.jpg)

knowbe4.py is a basic Python wrapper for the KnowBe4 reporting API. 

For more information on the API, please visit the [KnowBe4 API documentation](https://developer.knowbe4.com/).

## Installation

Clone this repository.

```bash
git clone https://github.com/elderlydoofus/knowbe4.py
```

## Usage

```python
from kb4 import KnowBe4

KB4_API_KEY='<Secret key obtained from KnowBe4 website.>'

kb4 = KnowBe4(KB4_API_KEY)

kb4.account() # returns dict containing basic account information
```

## Release History

- 0.0.1
  - 🚨 Work in progress. 🚨

## Contributing

All contributions are welcome and appreciated.

1. Fork
2. Feature branch
3. Pull request

## Meta

Josh Thomas - josh@joshuadavidthomas.com

Distributed under the MIT license. See `LICENSE` for more information.

[https://github.com/elderlydoofus/knowbe4.py](https://github.com/elderlydoofus/knowbe4.py)
