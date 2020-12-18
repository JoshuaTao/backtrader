# get stock list
# documentation url: https://waditu.com/document/2?doc_id=25
import tushare as ts

pro = ts.pro_api("8a41953856eb533c0b053523d169173a28ff54be54f3b9ae88fcf81f")
data = pro.stock_basic(exchange='', list_status='L',
                       fields='ts_code,symbol,name,area,industry,market,list_date')
print(data.tail())

#         ts_code  symbol      name area industry market list_date
# 4098  688699.SH  688699       N明微   深圳      半导体    科创板  20201218
# 4099  688777.SH  688777      中控技术   浙江     软件服务    科创板  20201124
# 4100  688788.SH  688788      科思科技   深圳     通信设备    科创板  20201022
# 4101  688981.SH  688981    中芯国际-U   上海      半导体    科创板  20200716
# 4102  689009.SH  689009  九号公司-UWD   北京     专用机械    CDR  20201029
