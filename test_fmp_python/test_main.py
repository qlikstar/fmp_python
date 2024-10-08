import unittest

from pandas import DataFrame
from fmp_python.fmp import FMP
from fmp_python.models.enums import Interval

API_KEY = "YOUR_TEST_KEY"


class TestFMPIntegration(unittest.TestCase):

    def test_missing_api_key(self):
        # Act and Assert
        with self.assertRaises(ValueError) as context:
            FMP()

        # Log the exception message for debugging
        if context.exception:
            print("Exception message:", str(context.exception))

        self.assertEqual(
            str(context.exception),
            "API key is missing. Please provide a valid API key."
        )

    def test_get_historical_price_reversed_order(self):
        # Arrange
        fmp = FMP(api_key=API_KEY)

        # Act
        df: DataFrame = fmp.get_historical_price("AAPL", 10)
        reversed_df = df.iloc[::-1]

        # Assert
        self.assertTrue(isinstance(df, DataFrame))
        self.assertTrue(isinstance(reversed_df, DataFrame))
        self.assertEqual(df.shape, reversed_df.shape)

        # Check if the DataFrame is reversed
        self.assertTrue(df.equals(reversed_df.iloc[::-1]))

    def test_stock_price_change(self):
        # Arrange
        fmp = FMP(api_key=API_KEY)

        # Act
        df: DataFrame= fmp.stock_price_change("AAPL")
        print(df)

        # Assert
        self.assertIsInstance(df, DataFrame)
        self.assertEqual(len(df), 1)

    def test_get_historical_chart(self):
        fmp = FMP(api_key=API_KEY)
        df: DataFrame = fmp.get_historical_chart('AAL', Interval.HOUR_4)
        expected_columns = ['date', 'open', 'low', 'high', 'close', 'volume']
        self.assertListEqual(list(df.columns), expected_columns)
        self.assertGreater(len(df), 0)


if __name__ == '__main__':
    unittest.main()
