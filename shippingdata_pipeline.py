import requests

def get_shipping_costs(cargo_name, start_point, end_point, tracking_number, api_key):
    url = "https://api.freightos.com/v2/rates/quotes"
    params = {
        "cargo_name": cargo_name,
        "start_point": start_point,
        "end_point": end_point,
        "tracking_number": tracking_number,
        "api_key": api_key,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        shipping_costs = data["rates"][0]["total_cost"]
        return shipping_costs
    else:
        return None

if __name__ == "__main__":
    start_point = input("Enter the start point: ")
    cargo_name = input("Enter the cargo name: ")
    end_point = input("Enter the end point: ")
    tracking_number = input("Enter the tracking number: ")
    api_key = ""
    shipping_costs = get_shipping_costs(cargo_name, start_point, end_point, tracking_number, api_key)
    print(shipping_costs)