currency = ["KSH" , "USD" , "EURO" , "POUND"]

def currency_converter(amount, from_currency, to_currency):
 
    conversion_rates = {
        'USD': 0.92,  
        'EURO': 1.09,  
        'POUND': 1.25,  
        
    }

    converted_amount = amount * conversion_rates[from_currency] / conversion_rates[to_currency]
    return converted_amount
amount = 100
from_currency = "USD"
to_currency = "EURO"
converted_amount = currency_converter(amount , from_currency, to_currency)
print(converted_amount)