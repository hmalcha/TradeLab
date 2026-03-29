# TradeLab
A python package for testing algorithmic trading strategies.

## Usage
Execute the provided Jupyter nootebooks to analyze the performance of
various trading strategies.

## Trading Model
![Visualization of trading model.](img/tradelab_model.png?raw=true "Trading Model")

The trading model consits of a data handler, a trading strategy, a trading engine, and a portfolio.

The data handler downloads stock data and serves it to the trading engine.
The trading strategy runs a backtest for a given timeline.
For every day in the timeline it uses the trading strategy and the historic
data provided by the data handler to compute the list of orders and then
executes them on a portfolio. The portfolio records all transactions.
The trading engine returns a list of the positions and total value of the
portfolio for each day in the timeline.


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
