def factorial(n: int) -> int:
    """Обчислення факторіала числа n."""
    if n < 0:
        raise ValueError("Факторіал визначено лише для невід'ємних чисел.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_even(n: int) -> bool:
    """Перевірка, чи є число парним."""
    return n % 2 == 0