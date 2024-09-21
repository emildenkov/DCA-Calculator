import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

ticker = 'AAPL'
start_date = '2018-01-01'
end_date = '2024-01-01'
interval = '3M'
amount = 500

total_invested = 0
total_shares = 0

data = yf.download(ticker, start=start_date, end=end_date)

data = data.dropna()

resampled_data = data.resample(interval).first()

dca_log = []

for date, row in resampled_data.iterrows():
    price = row['Adj Close']
    bought_shares = amount / price

    total_shares += bought_shares
    total_invested += amount

    dca_log.append({
        'Date': date,
        'Price': price,
        'Total Shares': total_shares,
        'Invested money': total_invested,
        'Portfolio Value': total_shares * price
    })

dca_df = pd.DataFrame(dca_log)

final_portfolio_value = total_shares * data.iloc[-1]['Adj Close']
profit = final_portfolio_value - total_invested

print(f'Final Portfolio Value: {final_portfolio_value}')
print(f'Profit: {profit}')

plt.figure(figsize=(10, 6))
plt.plot(dca_df['Date'], dca_df['Portfolio Value'], label='Portfolio Value')
plt.plot(dca_df['Date'], dca_df['Invested money'], label='Invested Money')
plt.xlabel('Date')
plt.ylabel('Value in $')
plt.title(f'Dollar Cost Average for {ticker}')
plt.legend()
plt.grid(True)
plt.show()