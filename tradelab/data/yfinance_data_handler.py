#!/usr/bin/env python3

# This file is part of TradeLab.
#
# Copyright (C) 2026 Hannes Malcha 
#
# TradeLab is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# TradeLab is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with TradeLab. If not, see <https://www.gnu.org/licenses/>.
#

"""
TradeLab is a a python package for testing automated trading strategies.

This class serves stock data from yfinance to the trading engine.
"""

import yfinance as yf

class YFinanceDataHandler:
    """A class for serving data from yfinance to the trading engine."""

    def __init__(self, tickers, start_time, end_time):
        """Initialize the data handler and download the stock data."""

        self.tickers = tickers
        self.start_time = start_time
        self.end_time = end_time
        self.data = self._download()


    def _download(self):
        """Download and prepare stock data."""

        print("Downloading stock data")
        _df = yf.download(self.tickers, start=self.start_time, end=self.end_time, auto_adjust=False)

        # Only keep the adjusted close
        if len(self.tickers) == 1:
            _df = _df[["Adj Close"]].rename(columns={"Adj Close": self.tickers[0]})
        else:
            _df = _df["Adj Close"]

        _df.columns = [ col if isinstance(col, str) else col[-1] for col in _df.columns]

        return _df
    
    def get_prices(self, t):
        """
        Serve prices at time t as a dict with ticker as a key and price
        as value.
        """

        _row = self.data.loc[t]
        return _row.to_dict()
    
    def get_timeline(self):
        """Serve timeline."""
        return list(self.data.index)