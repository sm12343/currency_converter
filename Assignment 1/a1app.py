"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and
an amount. It prints out the result of converting the first currency to
the second.

Author: Salaiha Mughal
Date:   2/17/2022
"""
import a1

source_currency = str(input('Enter source currency: '))
target_currency = str(input('Enter target currency: '))
original_amount = float(input('Enter original amount: '))
new_currency_amt = a1.exchange(source_currency,
                               target_currency, original_amount)
print('You can exchange', original_amount,
      source_currency, 'for', new_currency_amt, target_currency, '.')