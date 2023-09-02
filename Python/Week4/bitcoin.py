import requests
import sys

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")
elif len(sys.argv) == 2:
    try:
        b_coin = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()
    result = b_coin * o["bpi"]["USD"]["rate_float"]
    print(f"${result:,.4f}")
