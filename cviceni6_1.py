import sys
from cviceni6 import download_rates

def convert_ammount(ammount, currency):
    rates = download_rates
    if currency not it rates:
        return 0.0
    rate = rates[currency]
    return ammount / rates
    

if __name__ == "__main__":

    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} ammount currency")
        sys.exit()

    ammount = int(sys.argv[1])
    currency = sys.argv[2]

    print(convert_ammount(ammount, currency))