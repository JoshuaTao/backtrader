from datetime import datetime
import tushare as ts
import backtrader as bt
import pandas as pd
import matplotlib.pyplot as plt


ts.set_token("8a41953856eb533c0b053523d169173a28ff54be54f3b9ae88fcf81f")


def get_ts_data(ts_code, start_time="20200101", end_time="20201125"):
    df = ts.pro_bar(ts_code=ts_code, adj='qfq',
                    start_date=start_time,
                    end_date=end_time)
    df["datetime"] = pd.to_datetime(df["trade_date"])
    df.set_index("datetime", inplace=True)
    df.sort_index(inplace=True)
    df["volume"] = df["vol"]
    df["openinterest"] = 0
    df = df[["open", "high", "low", "close", "volume", "openinterest"]]
    return df


# print(get_ts_data("601318.SH"))

if __name__ == '__main__':
    # Create a cerebro entity
    cerebro = bt.Cerebro()

    stock_data = get_ts_data("600196.SH")

    # Create a Data Feed
    data = bt.feeds.PandasData(dataname=stock_data,
                               # Do not pass values before this date
                               fromdate=datetime(2020, 1, 1),
                               # Do not pass values before this date
                               todate=datetime(2020, 11, 25),
                               )

    # Add the Data Feed to Cerebro
    cerebro.adddata(data)
    from strategy import MyStrategy
    # Add a strategy
    cerebro.addstrategy(
        MyStrategy,
        maperiod=20)

    # Set our desired cash start
    cerebro.broker.setcash(10000.0)

    # Add a FixedSize sizer according to the stake
    cerebro.addsizer(bt.sizers.FixedSize, stake=100)

    # Set the commission
    cerebro.broker.setcommission(commission=0.0003)

    # Run over everything
    cerebro.run(maxcpus=1)

    cerebro.plot(style="candlestick")

    plt.show()
