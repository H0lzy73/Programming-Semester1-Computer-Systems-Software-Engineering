#Python Currency Converter

# A converter for international currency exchange.
USD_to_GBP = 0.76      
# Today's rate, US dollars to British Pounds
USD_to_EUR = 0.86
USD_to_JPY = 114.08
USD_to_INR = 63.64
USD_to_GEL = 2.6
     
GBP_sign   = '\u00A3'  # Unicode values for non-ASCII currency
EUR_sign   = '\u20AC'  #  symbols.
JPY_sign   = '\u00A5'
INR_sign   = '\u20B9'
GEL_sign   = '₾'

dollars = 1000
      # The number of dollars to convert
pounds = dollars * USD_to_GBP
euros = dollars * USD_to_EUR
yen = dollars * USD_to_JPY
rupees= dollars * USD_to_INR
lari = dollars * USD_to_GEL

print('Today, $' + str(dollars))
       # Printing the results
print('converts to ' + GBP_sign + str(pounds))
print('converts to ' + EUR_sign + str(euros))
print('converts to ' + JPY_sign + str(yen))
print('converts to ' + INR_sign + str(rupees))
print('converts to ' + GEL_sign + str(lari))
