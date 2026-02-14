from src.lession2 import ShareSerivce


def test_buy_shares():
    # Arrange
    apple_ticker = "AAPL"
    share_serivce = ShareSerivce()

    # Act
    share_serivce.buy_some_stocks(apple_ticker, 10)

    # Assert
    assert share_serivce.get_shares(apple_ticker) == 10


# def test_sell_shares():
#     # Arrange
#     apple_ticker = "AAPL"
#     share_serivce = ShareSerivce()

#     # Act
#     share_serivce.sell(apple_ticker, 10)

#     # Assert
#     assert share_serivce.get_shares(apple_ticker) == 0    