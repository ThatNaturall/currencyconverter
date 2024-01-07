# Currency Conversion Tool

This Python script allows users to convert currency using an external API.

## Prerequisites

- Python 3.x
- Requests library (`pip install requests`)

## Setup

1. Clone the repository or download the script file.
2. Install the requests library if not installed: `pip install requests`.

## Usage

1. Run the script (`python main.py`).
2. Follow the prompts to enter the initial currency, target currency, and amount to convert.
3. The script will make an API call to perform the currency conversion and display the result.

**Note**: Make sure to have an internet connection as the script relies on an external API to perform conversions.

## How it Works

- The script uses the API provided by apilayer.com to convert currencies.
- It validates the input currency symbols to ensure they are three alphabetic characters.
- It prompts the user for an amount to convert and handles non-numeric inputs.

## Example

Enter the initial currency (3 characters): ZAR
Enter the target currency (3 characters): USD
Enter the amount: 100
Conversion Result: 5.3547
