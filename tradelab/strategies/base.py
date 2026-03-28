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


This class defines a trading strategy, i.e. a list of order to execute at time t.
"""

class Strategy:
    def generate_orders(self, data, portfolio, t):
        """
        Returns a list of orders to execute at time t.
        """

        raise NotImplementedError
    
    