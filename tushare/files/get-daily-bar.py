# Get Daily Bar
# documentation url:https://tushare.pro/document/2?doc_id=109
from datetime import datetime
import tushare as ts

ts.set_token("8a41953856eb533c0b053523d169173a28ff54be54f3b9ae88fcf81f")
df = ts.pro_bar(ts_code='600196.SH', adj='qfq',
                start_date='20100101',
                end_date=datetime.strftime(datetime.now(), "%Y%m%d"))
print(df.columns)
print(df.tail())

# Index(['ts_code', 'trade_date', 'open', 'high', 'low', 'close', 'pre_close',
#        'change', 'pct_chg', 'vol', 'amount'],
#       dtype='object')

#         ts_code trade_date     open  ...  pct_chg        vol      amount
# 2632  600196.SH   20100111  12.1552  ...  -0.7956  114963.29  231769.825
# 2633  600196.SH   20100107  12.1258  ...  -2.7584  200120.06  408398.817
# 2634  600196.SH   20100106  11.8028  ...   3.9223  439556.96  919264.933
# 2635  600196.SH   20100105  11.3801  ...   2.6841  205340.20  403771.476
# 2636  600196.SH   20100104  11.5680  ...  -1.0216   95265.58  185187.718

