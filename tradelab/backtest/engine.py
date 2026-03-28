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

This class defines the trading engine used for backtesting.

"""

class TradingEngine:
    """
    A class for the trading engine.
    """

    def __init__(self, portfolio, strategy, data_handler):
        self.portfolio = portfolio
        self.strategy = strategy
        self.data_handler = data_handler
        self.history = []

    def run_backtest(self):
        _timeline = self.data_handler.get_timeline()

        for t in _timeline:
            # Get prices from data handler
            _prices = self.data_handler.get_prices(t)

            # Update portfolio prices
            self.portfolio.update_prices(_prices)

            # Generate orders
            _orders = self.strategy.generate_orders(self.data_handler, self.portfolio, t)

            # Execute orders
            for order in _orders:
                _price = _prices[order.ticker]
                if order.side == "buy":
                    self.portfolio.buy_stock(order.ticker, order.quantity, _price, t, fee = 0.0)
                elif order.side == "sell":
                    self.portfolio.sell_stock(order.ticker, order.quantity, _price, t, fee = 0.0)

            # Record History
            self.history.append({
                "timestamp": t,
                "positions": self.portfolio.positions.copy(),
                "total_value": self.portfolio.total_value()
            })

        return self.history




