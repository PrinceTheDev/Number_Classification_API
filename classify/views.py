from django.http import JsonResponse
import httpx
import asyncio
from django.views import View

def is_prime(number):
    number = abs(number)
    if number < 2:
        return False
    if number in (2, 3):
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def is_perfect(number):
    number = abs(number)
    if number < 2:
        return False
    divisors_sum = 1
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            divisors_sum += i
            if i != number // i:
                divisors_sum += number // i
    return divisors_sum == number

def is_armstrong(number):
    digits = [int(d) for d in str(abs(number))]
    return sum(d ** len(digits) for d in digits) == abs(number)

async def get_fun_fact(number):
    url = f"http://numbersapi.com/{number}/math?json"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json().get("text", "")

class NumberClassification(View):
    async def get(self, request):
        number = request.GET.get("number")
        
        try:
            number = int(number)
        except (TypeError, ValueError):
            return JsonResponse({"error": "Invalid number"}, status=400)
        
        prime_task = asyncio.to_thread(is_prime, number)
        perfect_task = asyncio.to_thread(is_perfect, number)
        armstrong_task = asyncio.to_thread(is_armstrong, number)
        fun_fact_task = get_fun_fact(number)

        properties = ["armstrong"] if await armstrong_task else []
        properties.append("even" if number % 2 == 0 else "odd")
        digit_sum = sum(int(d) for d in str(abs(number)))

        is_prime_result, is_perfect_result, fun_fact = await asyncio.gather(
            prime_task, perfect_task, fun_fact_task
        )

        return JsonResponse({
            "number": number,
            "is_prime": is_prime_result,
            "is_perfect": is_perfect_result,
            "properties": properties,
            "digit_sum": digit_sum,
            "fun_fact": fun_fact
        })
