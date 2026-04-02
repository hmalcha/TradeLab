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
TradeLab is a a python package for testing algorithmic trading strategies.

This is a derived trading strategy class.
"""

import pandas as pd
from tradelab.strategies.base import Strategy
from tradelab.core.order import Order

class BuyAndHold(Strategy):
    """A class for a simple buy and hold strategy of a single stock."""

    def __init__(self, tickers, start_time, end_time, offset="0D"):
        """Initialze a new strategy."""
        self.tickers = tickers
        self.start_time = pd.Timestamp(start_time) + pd.Timedelta(offset)
        self.end_time = pd.Timestamp(end_time) - pd.Timedelta(offset)
        self.has_bought = False
        self.has_sold = False
    

    def generate_target_weights(self, data_handler, portfolio, t):
        """Return a dict of target weights at time t."""
        
        _target_weights = dict()
        _weight = 1.0 / len(self.tickers)

        if t >= self.start_time and not self.has_bought:
            _target_weights = {ticker: _weight for ticker in self.tickers}
            self.has_bought = True

        elif t >= self.end_time and not self.has_sold:
            # For simplicity sell everything.
            _target_weights = {ticker: 0 for ticker in self.tickers}
            self.has_sold = True

        return _target_weights
    