# Get Trading Calendar
# documentation url:https://waditu.com/document/2?doc_id=26
import tushare as ts

pro = ts.pro_api("8a41953856eb533c0b053523d169173a28ff54be54f3b9ae88fcf81f")
df = pro.trade_cal(exchange='SSE', start_date='20200101', end_date='20201231')
print(df.tail())

#     exchange  cal_date  is_open
# 361      SSE  20201227        0
# 362      SSE  20201228        1
# 363      SSE  20201229        1
# 364      SSE  20201230        1
# 365      SSE  20201231        1
