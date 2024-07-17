# defi_api.py
import requests

def get_crypto_prices():
    """
    Fetches cryptocurrency prices from CoinGecko API.

    Returns:
    dict: Dictionary containing cryptocurrency prices.
          Example: {'bitcoin': {'usd': 50000}, 'ethereum': {'usd': 3000}}
    """
    try:
        url = 'https://api.coingecko.com/api/v3/simple/price'
        params = {
            'ids': 'bitcoin,ethereum',
            'vs_currencies': 'usd'
        }
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise exception for bad response status
        prices = response.json()
        return prices
    except requests.exceptions.RequestException as e:
        print(f"Error fetching cryptocurrency prices: {e}")
        return None

# Example usage
if __name__ == "__main__":
    crypto_prices = get_crypto_prices()
    if crypto_prices:
        print("Cryptocurrency Prices:", crypto_prices)
