import functools

import pandas as pd

from fmp_python.common.fmpexception import FMPException


class FMPDecorator:

    @classmethod
    def inject_api_key(cls, func):
        @functools.wraps(func)
        def deco_function(self, *args, **kwargs):
            api_key = self.api_key
            request = func(self, *args, **kwargs)
            if '?' not in request:
                return request + '?apikey=' + api_key
            else:
                return request + '&apikey=' + api_key

        return deco_function

    @classmethod
    def format_data(cls, func):
        @functools.wraps(func)
        def _call_wrapper(self, *args, **kwargs):
            response = func(self, *args, **kwargs)
            if self.output_format == 'json':
                return response.json()
            elif self.output_format == 'pandas':
                df = pd.DataFrame(response.json())
                df.reset_index(drop=True, inplace=True)
                return df
            else:
                raise FMPException("Output must be either pandas or json",
                                   FMPDecorator.format_data.__name__)

        return _call_wrapper

    @classmethod
    def format_historical_data(cls, func):
        @functools.wraps(func)
        def _call_wrapper(self, *args, **kwargs):
            response = func(self, *args, **kwargs)
            resp = response.json()
            if self.output_format == 'json':
                return resp
            elif self.output_format == 'pandas':
                if isinstance(resp, dict):
                    return pd.DataFrame(resp.get('historical', []))
                else:
                    return pd.DataFrame(resp)
            else:
                raise FMPException("Output must be either pandas or json",
                                   FMPDecorator.format_historical_data.__name__)

        return _call_wrapper
