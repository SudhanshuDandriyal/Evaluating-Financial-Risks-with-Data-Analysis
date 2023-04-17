# Financial Statistics API
This is a Flask API that calculates financial statistics for the S&P 500 index based on data from Yahoo Finance. The API uses the yfinance library to download daily price data and calculates the following financial statistics:

Mean daily return
Daily standard deviation
Annualized mean return
Annualized standard deviation
Maximum drawdown
Value at risk (VaR) at 95% confidence level
Conditional value at risk (CVaR) at 95% confidence level

# Getting Started
To run this API on your local machine, you will need to install Python 3 and the required Python packages. You can install the packages using pip with the following command:
pip install -r requirements.txt
You can start the API by running the following command:
python app.py
The API will be available at http://localhost:5000/. You can use a web browser or a tool like curl to send HTTP requests to the API and receive JSON responses.

# Usage
The API has a single endpoint at the root URL that returns a JSON object containing the financial statistics. You can send a GET request to the root URL to retrieve the statistics.

# License
This code is licensed under the MIT License. You can use it for any purpose, including commercial projects, as long as you include the original copyright notice.

# Credits
This API was created by [Sudhanshu Dandriyal] as a demonstration of Flask and financial data analysis. The code is based on examples from the Flask and yfinance documentation.
