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
#
# This class is an exact copy of the Root class from the SimpLie programm
# written by Teake Nutma, which is available at
# https://github.com/teake/simplie.

"""
TradeLab is a a python package for testing automated trading strategies.

This class handles the data coming from yFinance so it can be used by the engine.

"""

import yfinance as yf

class YFinanceDataHandler:
    def __init__(self, tickers, start, end):
        self.tickers = tickers
        self.start = start
        self.end = end
        self.data = self._download()


    def _download(self):
        """Download data."""
        
        _df = yf.download(self.tickers, start=self.start, end=self.end, auto_adjust=False)

        # Use adjusted close
        if len(self.tickers) == 1:
            _df = _df[["Adj Close"]].rename(columns={"Adj Close": self.tickers[0]})
        else:
            _df = _df["Adj Close"]

        _df.columns = [ col if isinstance(col, str) else col[-1] for col in _df.columns]

        return _df
    
    def get_prices(self, t):
        """Get prices."""
        _row = self.data.loc[t]
        return _row.to_dict()
    
    def get_timeline(self):
        """Get timeline."""
        return list(self.data.index)