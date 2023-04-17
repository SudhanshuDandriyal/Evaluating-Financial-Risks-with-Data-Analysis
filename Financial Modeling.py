#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, jsonify, request
import numpy as np
import yfinance as yf

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def financial_stats():
    if request.method == 'POST':
        # Get start and end dates from user input
        start_date = request.form['start_date']
        end_date = request.form['end_date']

        # Download S&P 500 data
        df = yf.download("^GSPC", start=start_date, end=end_date)
        df['Daily Returns'] = df['Close'].pct_change()
        df.dropna()

        # Calculate mean daily return and daily standard deviation
        mean_return = df['Daily Returns'].mean()
        std_dev = df['Daily Returns'].std()

        # Calculate annualized mean return and standard deviation
        annualized_mean_return = (1 + mean_return) ** 252 - 1
        annualized_std_dev = std_dev * np.sqrt(252)

        # Calculate maximum drawdown
        cumulative_returns = (1 + df['Daily Returns']).cumprod()
        max_drawdown = (cumulative_returns.cummax() - cumulative_returns) / cumulative_returns.cummax()

        # Calculate value at risk (VaR) at 95% confidence level
        VaR_95 = np.percentile(df['Daily Returns'], 5)

        # Calculate conditional value at risk (CVaR) at 95% confidence level
        CVaR_95 = df['Daily Returns'][df['Daily Returns'] <= VaR_95].mean()

        # Create dictionary of financial statistics
        stats = {
            'mean_daily_return': mean_return,
            'daily_standard_deviation': std_dev,
            'annualized_mean_return': annualized_mean_return,
            'annualized_standard_deviation': annualized_std_dev,
            'maximum_drawdown': max_drawdown.min(),
            'VaR_95': VaR_95,
            'CVaR_95': CVaR_95
        }

        # Return financial statistics as JSON
        return jsonify(stats)

    # If the request method is GET, render the HTML form
    return '''
        <form method="post">
            <label for="start_date">Start Date:</label>
            <input type="date" id="start_date" name="start_date"><br><br>
            <label for="end_date">End Date:</label>
            <input type="date" id="end_date" name="end_date"><br><br>
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '__main__':
    app.run()

