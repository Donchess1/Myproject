import requests
def is_armstrong(number):
    num_str = str(number)
    return sum(int(digit) ** len(num_str) for digit in num_str) == number

def is_odd(number):
    return number % 2 != 0

def get_properties(number):
    return ("armstrong, odd" if is_armstrong(number) and is_odd(number) else
            "armstrong, even" if is_armstrong(number) and not is_odd(number) else
            "odd" if is_odd(number) else "even")
def get_fun_fact(number):
    try:
        response = requests.get(f"http://numbersapi.com/{number}/math")
        if response.status_code == 200:
            return response.text
    except requests.exceptions.RequestException:
        return "No fun fact available."
    return