# Get Money Flow
# documentation url:https://tushare.pro/document/2?doc_id=170

import tushare as ts
from datetime import datetime

pro = ts.pro_api("8a41953856eb533c0b053523d169173a28ff54be54f3b9ae88fcf81f")
end_date = datetime.strftime(datetime.now(), "%Y%m%d")
df = pro.moneyflow(ts_code='600196.SH', start_date='20200101', end_date=end_date)
print(df.tail())

