from backtesting import Strategy
from backtesting.lib import crossover

class SmaCross(Strategy):
    n1 = 20
    n2 = 50

    def init(self):
        self.sma1 = self.I(lambda x: x.rolling(self.n1).mean(), self.data.Close)
        self.sma2 = self.I(lambda x: x.rolling(self.n2).mean(), self.data.Close)

    def next(self):
        if crossover(self.sma1, self.sma2):
            self.buy()
        elif crossover(self.sma2, self.sma1):
            self.sell()
