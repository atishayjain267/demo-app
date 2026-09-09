import requests


def get_ip_info():
    url = "https://httpbin.org/get"
    response = requests.get(url)

    if response.status_code == 200:
        print("Successfully reached API!")
        print(f"Server Response URL: {response.json().get('url')}")
    else:
        print(f"Request failed with status code: {response.status_code}")


if __name__ == "__main__":
    get_ip_info()