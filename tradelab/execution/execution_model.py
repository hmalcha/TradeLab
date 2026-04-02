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

This is a class for executing trading orders.
"""

from tradelab.execution.fill import Fill

class ExecutionModel:
    """A class for executing trading orders."""

    def execute_order(self, order, price):
        """Execute an order."""
        _fill = Fill(
            ticker=order.ticker,
            quantity=order.quantity,
            price=price,
            side=order.side,
        )

        return _fill