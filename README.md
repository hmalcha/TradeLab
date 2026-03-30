# TradeLab
A python package for testing algorithmic trading strategies.

## Usage
Execute the provided Jupyter nootebooks to analyze the performance of
various trading strategies.

## Trading Model
![Visualization of trading model.](img/tradelab_model.png?raw=true "Trading Model")

The trading model consits of a data handler, a trading strategy, and
a trading engine. 
Moreover, it contains classes for stock portfolios and trading orders, which
are used to execute the trading model.

The data handler recieves historic stock data from a remote provider such as
Yahoo Finance.
The data is served to the trading engine and the trading strategy.
The trading engine runs a backtest of the trading strategy.
For every data point in the stock data the trading engine calls the trading
strategy to compute a list of buy and sell orders.
The trading engine then places these order on the portfolio and records
the performance data.
The portfolio records a list of all transactions.
Finally, the trading engine returns a list of the positions held and the total
value of the portfolio for each time in the stock data.
This output is used in the Jupyter notebooks to visualize the performance of
various trading strategies.

## License
Copyright © 2026 Hannes Malcha

TradeLab is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

TradeLab is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the 
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with TradeLab. If not, see https://www.gnu.org/licenses/.