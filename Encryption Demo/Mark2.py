#How to get average from array of marks given?
# total = 0;
# for(var i = 0; i < grades.length; i++) {
#     total += grades[i];
# }
# avg = total / grades.length;

import urllib.request, json
resp = urllib.request.urlopen('https://query2.finance.yahoo.com/v10/finance/quoteSummary/tsla?modules=price')
data = json.loads(resp.read())
price = data['quoteSummary']['result'][0]['price']['regularMarketPrice']['raw']
print(price)

#"//how to get the stock data of Tesla in python?" 


