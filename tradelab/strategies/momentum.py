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

import numpy as np
import pandas as pd
from tradelab.strategies.base import Strategy
from tradelab.execution.position_sizer import PositionSizer


class Momentum(Strategy):
    """A class for trading a list of stocks or ETFs based on momentum."""

    def __init__(self, tickers, start_time, end_time, offset="0D", rebalance_frequency=30, momentum_lookback=5, volatility_lookback=30, buy_top_n=1):
        """Initialze a new strategy."""

        if len(tickers) < buy_top_n:
            raise ValueError(f"Not enough ticker to buy {buy_top_n} different stocks.")
        
        self.tickers = tickers
        self.start_time = pd.Timestamp(start_time) + pd.Timedelta(offset)
        self.end_time = pd.Timestamp(end_time) - pd.Timedelta(offset)
        self.rebalance_frequency = rebalance_frequency
        self.momentum_lookback = momentum_lookback
        self.volatility_lookback = volatility_lookback
        self.buy_top_n = buy_top_n
    
    def generate_target_weights(self, data_handler, portfolio, t):
        """Return a dict of target weights at time t."""

        _target_weights = dict()
        _timeline = data_handler.get_timeline()


        if _timeline.index(t) % self.rebalance_frequency == 0 and t >= self.start_time and t < self.end_time:
            _momenta = [(ticker, self._compute_momentum(ticker, _timeline, data_handler, t)) for ticker in self.tickers]            
            _momenta = sorted(_momenta, key=lambda x: x[1], reverse=True)

            # Find best performing tickers
            _top_tickers = [ticker for ticker, momentum in _momenta[:self.buy_top_n] if momentum > 0]

            # Compute their volatilities
            _volatilities = {ticker: self._compute_volatility(ticker, _timeline, data_handler, t) for ticker in _top_tickers}
            _inv_volatilities = {ticker: 1 / _volatilities[ticker] for ticker in _top_tickers}
            _total = sum(_inv_volatilities.values())

            # Compute weights according to volatility
            _target_weights = {
                ticker: (_inv_volatilities[ticker] / _total if ticker in _top_tickers else 0.0)
                for ticker in self.tickers
            }

            # Add the best performing stock and keep stocks with positive momentum
            #_top_set = {ticker for ticker, momentum in _momenta[:self.buy_top_n]}

            #_top_tickers = [
            #    ticker for ticker, momentum in _momenta
            #    if momentum > 0 and (ticker in _top_set or ticker in portfolio.positions)
            #]

            #_weight = 1.0 / max(len(_top_tickers), 1.0)

            # Do not keep any stock in portfolio; consider only momentum
            #_weight = 1.0 / self.buy_top_n
            #_top_tickers = [ticker for ticker, momentum in _momenta[:self.buy_top_n] if momentum > 0]

            #_target_weights = {
            #    ticker: (_weight if ticker in _top_tickers else 0.0)
            #    for ticker in self.tickers
            #}
        
        elif t >= self.end_time:
            _target_weights = {ticker : 0 for ticker in self.tickers}

        return _target_weights


    def _compute_momentum(self, ticker, timeline, data_handler, t):
        """Compute the momentum of a ticker."""

        # Find day at least momentum_lookback number of days before t in timeline
        _t0 = pd.Timestamp(t) - pd.Timedelta(str(self.momentum_lookback)+"D")
        while(_t0 not in timeline):
            _t0 = _t0 - pd.Timedelta("1D")

            if _t0 < min(timeline):
                raise ValueError("Cannot compute strategy because past timeline is too short.")

        # Get closing price from 20 days ago and from today
        _price_t0 = data_handler.get_prices(_t0)[ticker]
        _price_t = data_handler.get_prices(t)[ticker]

        # Return momentum
        return (_price_t - _price_t0) / _price_t0
    

    def _compute_volatility(self, ticker, timeline, data_handler, t):
        """Compute the actual current volatility of a ticker."""

        # Find day at least volatility_lookback number of days before t in timeline
        _t0 = pd.Timestamp(t) - pd.Timedelta(str(self.volatility_lookback)+"D")
        while(_t0 not in timeline):
            _t0 = _t0 - pd.Timedelta("1D")

            if _t0 < min(timeline):
                raise ValueError("Cannot compute strategy because past timeline is too short.")
            
        # Get closing price for all trading days between t0 and t.
        _i0 = timeline.index(_t0)
        _i = timeline.index(t)
        _prices = [data_handler.get_prices(x)[ticker] for x in timeline[_i0:_i+1]]

        # Compute logarithmic returns
        _log_returns = [np.log(_prices[t]) - np.log(_prices[t+1]) for t in range(len(_prices)-1)]

        # Compute the volatility
        _volatility = np.std(_log_returns) * np.sqrt(len(_log_returns))

        return _volatility