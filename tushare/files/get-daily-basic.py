# Get Daily Basic
# documentation url:https://tushare.pro/document/2?doc_id=32
import tushare as ts
from datetime import datetime

pro = ts.pro_api("8a41953856eb533c0b053523d169173a28ff54be54f3b9ae88fcf81f")
trade_date = datetime.strftime(datetime.now(), "%Y%m%d")
df = pro.daily_basic(ts_code='',
                     trade_date=trade_date,
                     fields='ts_code,trade_date,turnover_rate,volume_ratio,pe,pb')
print(df.tail())

#         ts_code trade_date  turnover_rate  volume_ratio        pe       pb
# 4089  300634.SZ   20201218         1.0645          0.73   60.3068   5.7214
# 4090  300126.SZ   20201218         6.6858          0.98  282.3897   2.5475
# 4091  300718.SZ   20201218         2.6034          0.90   29.5978   3.0404
# 4092  688017.SH   20201218         5.2208          1.57  296.2525  10.4514
# 4093  002626.SZ   20201218         2.1914          1.24   52.0586   7.1411
