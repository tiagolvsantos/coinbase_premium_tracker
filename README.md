# Coinbase Cryptocurrency Tracker

This project is a simple cryptocurrency tracker that fetches the latest premium values for a specified cryptocurrency from Coinbase and plots them in real-time.

## Features

- Fetches real-time premium values for a specified cryptocurrency from Coinbase.
- Plots the premium values in real-time.
- Highlights the last premium value on the plot.
- Plays a beep sound when the premium is negative (can be enabled or disabled).
- Accepts the cryptocurrency symbol, the sound alert option, and the update interval as command-line arguments.

## Usage

1. Install the required Python packages:

```bash
pip install -r requirements.txt
```

2. Run the script with the cryptocurrency symbol, the sound alert option, and the update interval as command-line arguments:

```bash
python main.py ETH --EnableSound --UpdateInterval 120
```


This will start tracking the premium values for Ethereum (ETH), play a beep sound when the premium is negative, and update the plot every 120 seconds.

License
This project is licensed under the MIT License.


Please replace the placeholders with the actual information about your project. You can also add more sections to the README file as needed, such as "Installation", "Contributing", "Credits", etc.