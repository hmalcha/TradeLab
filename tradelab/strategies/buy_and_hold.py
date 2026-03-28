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


This class defines a simple buy and hold trading strategy.
"""

import pandas as pd
from tradelab.core.order import Order
from tradelab.strategies.base import Strategy

class BuyAndHold(Strategy):
    """
    A class for a simple buy and hold strategy.
    """

    def __init__(self, ticker, quantity, start_time, end_time):
        self.ticker = ticker
        self.quantity = quantity
        self.start_time = pd.Timestamp(start_time)
        self.end_time = pd.Timestamp(end_time)
        self.has_bought = False
        self.has_sold = False
    


    def generate_orders(self, data_handler, portfolio, t):
        """
        Returns a list of orders to execute at time t.
        """
        
        _orders = []

        if t >= self.start_time and not self.has_bought:
            _orders.append(Order(
                ticker = self.ticker,
                quantity = self.quantity,
                side = "buy"
            ))
            self.has_bought = True

        elif t >= self.end_time and not self.has_sold:
            # Sell everything
            _qty = portfolio.positions.get(self.ticker)
            if _qty > 0:
                _orders.append(Order(
                    ticker = self.ticker,
                    quantity = _qty,
                    side = "sell"
                ))
            self.has_sold = True

        return _orders
    