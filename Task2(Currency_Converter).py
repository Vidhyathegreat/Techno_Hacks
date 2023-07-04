exchange_rates = {
    'USD': 1.0,   
    'EUR': 0.85,  
    'GBP': 0.72,  
    'INR': 74.85, 
    
}

def convert_currency(amount, from_currency, to_currency):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        raise ValueError("Currency not supported.")
    converted_amount = amount * (exchange_rates[to_currency] / exchange_rates[from_currency])
    return converted_amount

# Example usage
amount = int(input("Enter the amount")) # Amount to convert
from_currency = 'USD'  # Currency to convert from
to_currency = 'EUR'  # Currency to convert to

converted_amount = convert_currency(amount, from_currency, to_currency)
print(f'{amount} {from_currency} is equal to {converted_amount} {to_currency}.')
