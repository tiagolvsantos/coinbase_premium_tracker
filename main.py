import requests
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import winsound
import argparse


# Use dark background style
plt.style.use('dark_background')

def get_bitcoin_price(symbol):
    """
    Get the current price of Bitcoin from Coinbase.

    Parameters:
    symbol (str): The symbol of the cryptocurrency (e.g., BTC, ETH, LTC).

    Returns:
    float: The current price of Bitcoin.
    """
    response = requests.get(f'https://api.coinbase.com/v2/prices/{symbol}-USD/spot')
    data = response.json()
    return float(data['data']['amount'])

def get_binance_bitcoin_price(symbol):
    """
    Get the current price of Bitcoin from Binance.

    Parameters:
    symbol (str): The symbol of the cryptocurrency (e.g., BTC, ETH, LTC).

    Returns:
    float: The current price of Bitcoin.
    """
    response = requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}USDT')
    data = response.json()
    return float(data['price'])

def calculate_premium(symbol):
    """
    Calculate the premium of Bitcoin on Coinbase compared to Binance.

    Parameters:
    symbol (str): The symbol of the cryptocurrency (e.g., BTC, ETH, LTC).

    Returns:
    float: The premium of Bitcoin on Coinbase.
    """
    coinbase_price = get_bitcoin_price(symbol)
    binance_price = get_binance_bitcoin_price(symbol)
    return coinbase_price - binance_price

data = []

def update(i):
    """
    Update the plot with new data.

    Parameters:
    i (int): The index of the data point to be added.

    Returns:
    None
    """
    # Declare global variables
    global symbol
    global enable_sound

    premium = calculate_premium(symbol)
    data.append({'date_time': datetime.now(), 'premium': premium})
    df = pd.DataFrame(data)
    plt.cla()  # clear the current axes
    df.plot(x='date_time', y='premium', ax=plt.gca(), color='orange', linewidth=2.0)  # plot on the current axes
    plt.axhline(df['premium'].mean(), color='pink', linestyle='--')  # add a horizontal line with the average premium value
    plt.title(f"Coinbase {symbol} Spot Premium: {df['premium'].iloc[-1]:.2f}", fontsize=16)
    plt.xlabel('Date Time', fontsize=14)
    plt.ylabel('Premium', fontsize=14)

    # Highlight the last data point
    color = 'green' if df['premium'].iloc[-1] >= 0 else 'red'
    plt.scatter(df['date_time'].iloc[-1], df['premium'].iloc[-1], color=color)

    # If premium is negative, play a beep sound
    if premium < 0 and enable_sound:
        winsound.Beep(100, 500)  

# Create the parser
parser = argparse.ArgumentParser(description='Plot cryptocurrency data.')

# Add the arguments
parser.add_argument('Symbol', metavar='symbol', type=str, help='the symbol of the cryptocurrency to plot ex: BTC, ETH, LTC, etc.')
parser.add_argument('--EnableSound', dest='enable_sound', action='store_true', help='whether to enable the sound alert')
parser.set_defaults(enable_sound=False)
parser.add_argument('--UpdateInterval', dest='update_interval', type=int, help='the update interval in seconds', default=60)

# Print the argument options
parser.print_help()
# Parse the arguments
args = parser.parse_args()

# Declare global variables
global symbol
global enable_sound

# Get the values
symbol = args.Symbol
enable_sound = args.enable_sound
update_interval = args.update_interval * 1000 

ani = FuncAnimation(plt.gcf(), update, interval=update_interval, save_count=100)
plt.show()