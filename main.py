import requests

def convert_curr():
    

    while True:
        init_currency = input("Enter the initial currency: ")
        if not init_currency.isalpha():
            print("Please input the correct symbol")
            continue
        else:
            break

    while True:
        target_currency = input("Enter the target currency: ")
        if not target_currency.isalpha():
            print("Please input the correct symbol")
            continue
        else:
            break
    
    while True:
        try:
            amount = float(input('Enter the amount: '))
        except:
            print('The number needs to be a numeric')
            continue

        if not amount > 0:
            print('Amount needs to be greater than O')
            continue
        else:
            break
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={target_currency}&from={init_currency}&amount={amount}"

    payload = {}
    headers= {
    "apikey": "hrLmwknU1ZnJfkCwxBjmTbJy4XwdjMtT"
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    status_code = response.status_code
    result = response.text

    if status_code !=200:
        result = response.json()
        print('Error response: '+ str(result))
        quit()

    result = response.json()
    print('Conversion Result: '+str(result['result']))

if __name__ == '__main__':
    convert_curr()


