# main.py
from defi_api import get_crypto_prices
from ai_model import sentiment_analysis, price_prediction

def main():
    # Fetch cryptocurrency prices
    crypto_prices = get_crypto_prices()
    print("Cryptocurrency Prices:", crypto_prices)

    # Example AI model usage
    text = "Bitcoin is performing well"
    sentiment = sentiment_analysis(text)
    print("Sentiment Analysis:", sentiment)

    data = {'BTC_price': crypto_prices['bitcoin']['usd'], 'ETH_price': crypto_prices['ethereum']['usd']}
    predicted_price = price_prediction(data)
    print("Price Prediction:", predicted_price)

if __name__ == "__main__":
    main()
