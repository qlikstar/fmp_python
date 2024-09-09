[![Build Status](https://travis-ci.com/qlikstar/fmp_python.svg?branch=master)](https://travis-ci.com/qlikstar/fmp_python)
[![PyPI version](https://badge.fury.io/py/fmp-python.svg)](https://badge.fury.io/py/fmp-python)
[![Average time to resolve an issue](https://isitmaintained.com/badge/resolution/qlikstra/fmp_python.svg)](http://isitmaintained.com/project/qlikstar/fmp_python "Average time to resolve an issue")
[![Percentage of issues still open](https://isitmaintained.com/badge/open/qlikstar/fmp_python.svg)](http://isitmaintained.com/project/qlikstar/fmp_python "Percentage of issues still open")

# Financial Modeling Prep Python Module

Python module to get stock data from the Financial Modeling Prep API

# Install

This library requires you to have an account with Financial Modeling Prep (sign
up [here](https://financialmodelingprep.com/))

You can install the package:

- Using **pip**:

```
pip install fmp_python
```

- From the source:

```
git clone https://github.com/qlikstar/fmp_python.git

pip install -e fmp_python
```

# Usage

To get data from the API:

- import the library and call the object with your API key:

```
from fmp_python.fmp import FMP

fmp = FMP(api_key='YOUR_API_KEY')
fmp.get_quote('AAL')
```

- Or, you can store it in the environment variable FMP_API_KEY

```
from fmp_python.fmp import Interval, FMP

fmp = FMP(output_format='pandas')
fmp.get_quote('AAL')
```

You can choose which output format you want your data **output_format = 'pandas' or 'json'**.

*'pandas' is the default value*

## Real Time Stock Price

*Reference*: https://financialmodelingprep.com/developer/docs/#Company-Quote

```
fmp.get_quote(symbol: str)
```

*Usage Example*

```
fmp: DataFrame = FMP(api_key="YOURAPIKEY")
fmp.get_quote('AAL')

OR

fmp = FMP(output_format = 'json')
fmp.get_quote('AAL')
```


## Stock Time Series

### 1. Stock Price

*Reference*: https://financialmodelingprep.com/developer/docs/#Stock-Price

```
fmp.get_quote_short(symbol: str)
```

*Usage Example*

```
fmp: DataFrame = FMP(api_key="YOURAPIKEY")
fmp.get_quote('AAL')
```

### 2. Stock Historical Price

*Reference*: https://financialmodelingprep.com/developer/docs/#Stock-Historical-Price

```
fmp.get_historical_chart(symbol: str, interval:str)
```

*Usage Example*

```

fmp = FMP(output_format = 'pandas')
fmp.get_historical_chart('AAL', Interval.MIN_5)
```

## Market Indexes

### 1. Most of the majors indexes (Dow Jones, Nasdaq, S&P 500)

*Reference*: https://financialmodelingprep.com/developer/docs/#Most-of-the-majors-indexes-(Dow-Jones,-Nasdaq,-S&P-500)

```
fmp.get_index_quote(symbol: str)
```

*Usage Example*

```
fmp = FMP(output_format = 'pandas')
fmp.get_index_quote('GSPC')
```

### 2. Historical stock index prices

*Reference*: https://financialmodelingprep.com/developer/docs/#Historical-stock-index-prices

- By timelapse:

```
fmp.get_historical_chart_index("AAPL", Interval.HOUR_4)
fmp.get_historical_chart_index('GSPC', Interval.MIN_1)
fmp.get_historical_price('GSPC')
```

### 3. Technical Indicators

*Reference*: https://site.financialmodelingprep.com/developer/docs#technicals

```
from fmp_python.models.enums import Interval, Indicator
res = fmp.get_technical_indicator("AAPL", Interval.DAY_1, Indicator.RSI, period=14)
```


### 4. Stock screener
```
df = fmp.get_stock_screener(volume_gt=100000, price_gt=20, price_lt=500, beta_gt=0.3, limit=5000)
```

### Run Tests
1. Add your API key to the `API_KEY` in `test_main.py`

2. Now run the tests in the folder `test_fmp_python`
