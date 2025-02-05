from django.http import JsonResponse
import httpx
import asyncio
from django.views import View

async def fetch_fun_fact(number):
    url = f"http://numbersapi.com/{number}/math?json"
    try:
        async with httpx.AsyncClient(timeout=0.3) as client:
            response = await client.get(url)
            if response.status_code == 200:
                return response.json().get("text", "No fact available")
    except httpx.RequestError:
        return "No fact available"

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
    async def get(self, request):
        number = request.GET.get("number")
        if not number or not number.isdigit():
            return JsonResponse({"number": number, "error": True}, status=400)

        number = int(number)
        properties = ["armstrong"] if is_armstrong(number) else []
        properties.append("even" if number % 2 == 0 else "odd")
        digit_sum = sum(int(d) for d in str(number))

        # Run the API call asynchronously
        fun_fact = await fetch_fun_fact(number)

        return JsonResponse({
            "number": number,
            "is_prime": is_prime(number),
            "is_perfect": is_perfect(number),
            "properties": properties,
            "digit_sum": digit_sum,
            "fun_fact": fun_fact
        })
