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

This is a class for filling trading orders.
"""

class Fill:
    """A class for filling trading orders."""

    def __init__(self, ticker, quantity, price, side):
        """Initalize a new fill."""
        self.ticker = ticker
        self.quantity = quantity
        self.price = price
        self.fee = self._compute_fee()
        self.side = side

    def _compute_fee(self):
        """Compute fee."""
        return min(49.0, max(1.5, 0.0005 * self.quantity * self.price))
