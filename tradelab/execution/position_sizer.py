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

This is class for creating orders based on target weights.
"""
import math
from tradelab.core.order import Order

class PositionSizer:
    """A class for creating orders based on target weights."""

    def generate_orders(self, target_weights, portfolio, prices):
        """Generate orders for a given set of target weights."""
        
        _orders = []

        # Only trade with 95% of portfolio to allow for fees.
        _total_value = 0.95 * portfolio.total_value()

        for ticker, weight in target_weights.items():
            _price = prices[ticker]
            
            if not _price > 0:
                continue

            _target_value = weight * _total_value
            _target_qty = math.floor(_target_value / _price)

            _current_qty = portfolio.positions.get(ticker, 0)

            _delta = _target_qty - _current_qty

            if _delta > 0:
                _orders.append(Order(ticker=ticker, quantity=_delta, side="buy"))
            elif _delta < 0:
                _orders.append(Order(ticker=ticker, quantity=abs(_delta), side="sell"))

        _orders.sort(key=lambda o: o.side == "buy")
        return _orders