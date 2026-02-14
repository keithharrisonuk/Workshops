
class ShareSerivce:
    items = {}

    def buy_some_stocks(self, ticker, quantity):
        self.items[ticker] = self.items.get(ticker, 0) + quantity

    # def sell(self, ticker, quantity):
    #     self.items[ticker] = self.items.get(ticker, 0) - quantity

    def get_shares(self, ticker):
        return self.items.get(ticker, 0)