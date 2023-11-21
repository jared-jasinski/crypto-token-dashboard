import requests


def get_token_info(address):
    endpoint = f"https://api.dexscreener.com/latest/dex/search?q={address}"

    response = requests.get(endpoint)

    if response.status_code == 200:
        token_data = response.json()
        # Process and use the token data as needed
        return token_data
    else:
        print("Failed to retrieve token information. Status code:", response.status_code)
        return None


# token = '0x063af3261d276d3bc25214bb2967991603626a19'
# print(get_token_info(token))
