from enum import Enum


class Interval(Enum):
    MIN_1 = "1min"
    MIN_5 = "5min"
    MIN_15 = "15min"
    MIN_30 = "30min"
    HOUR_1 = "1hour"
    HOUR_4 = "4hour"
    DAY_1 = "1day"


class Indicator(Enum):
    ADX = 'adx'
    DEMA = 'dema'
    EMA = 'ema'
    RSI = 'rsi'
    SMA = 'sma'
    STANDARD_DEVIATION = 'standardDeviation'
    TEMA = 'tema'
    WILLIAMS = 'williams'
    WMA = 'wma'
