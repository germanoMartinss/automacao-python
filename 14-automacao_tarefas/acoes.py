import yfinance as yf # type: ignore
from datetime import datetime
from matplotlib import pyplot as plt

end_date = datetime.now().strftime('%Y-%m-%d')
# print(end_date)

bb = yf.Ticker('BBAS3.SA')
data_bb = bb.history(
    start=datetime(2025, 1, 1),
    end=end_date
)
data_bb['Close'].plot()
plt.savefig('bb_preco.png')