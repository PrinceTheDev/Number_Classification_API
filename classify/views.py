from django.http import JsonResponse
import requests
from django.views import View



def is_prime(number):
    
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def is_perfect(number):
    divisors = [i for i in range(1, number // 2 + 1) if number % i == 0]
    return sum(divisors) == number

def is_armstrong(number):
    digits = [int(digit) for digit in str(number)]
    power = len(digits)
    return sum(digit ** power for digit in digits) == number

class Number_Classification(View):
    def get(self, request):
        number = request.GET.get("number")
        
        if not number or not number.isdigit():
            return JsonResponse({"number": number, "error": True}, status=400)
        
        number = int(number)
        properties = []
        
        if is_armstrong(number):
            properties.append("armstrong")
        properties.append("even" if number % 2 == 0 else "odd")
        
        digit_sum = sum(int(d) for d in str(number))
        
        fun_fact_response = requests.get(f"http://numbersapi.com/{number}/math?json")
        fun_fact = fun_fact_response.json().get("text", "No fact available")
        
        return JsonResponse({
            "number": number,
            "is_prime": is_prime(number),
            "is_perfect": is_perfect(number),
            "properties": properties,
            "digit_sum": digit_sum,
            "fun_fact": fun_fact
        })