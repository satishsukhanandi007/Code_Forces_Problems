n = int(input())
years = n // 365
months = (n % 365) // 30
days = (n % 365) % 30
print(f'''{years} years
{months} months
{days} days''')