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

This is a class defines a portfolio of cash and stocks.
"""

class Portfolio:
    """A class for a portfolio of cash and stock positions."""

    def __init__(self, deposit):
        """Initialize a new portfolio with an inital cash deposit."""

        self.cash = deposit
        self.positions = dict()
        self.prices = dict()
        self.trades = []
    
    def total_value(self):
        "Return the total value of the portfolio given the last known prices."
        return self.cash + self.market_value()
    
    def market_value(self):
        "Return total value of all positions for the last known price."
        return sum(qty * self.prices.get(ticker) for ticker, qty in self.positions.items())
    
    def update_price(self, ticker, price):
        "Update price of a ticker."
        self.prices[ticker] = price

    def update_prices(self, price_dict):
        "Update prices of all tickers."
        self.prices.update(price_dict)

    def buy_stock(self, ticker, quantity, price, timestamp, fee = 0.0):
        """Buy a stock."""

        _cost = quantity * price + fee

        if _cost > self.cash:
            raise ValueError("Not enough cash.")
        
        self.cash -= _cost
        self.positions[ticker] = self.positions.get(ticker, 0.0) + quantity
        self.prices[ticker] = price

        self.trades.append({
            "ticker": ticker,
            "qty": quantity,
            "price": price,
            "timestamp": timestamp,
            "side": "buy"
            })

    def sell_stock(self, ticker, quantity, price, timestamp, fee = 0.0):
        """Sell a stock."""

        _payoff = quantity * price - fee

        if ticker not in self.positions or self.positions[ticker] < quantity:
            raise ValueError("Not enough shares.")

        
        self.cash += _payoff
        self.positions[ticker] -= quantity
        self.prices[ticker] = price

        if self.positions[ticker] == 0:
            del self.positions[ticker]

        self.trades.append({
            "ticker": ticker,
            "qty": quantity,
            "price": price,
            "timestamp": timestamp,
            "side": "sell"
            })