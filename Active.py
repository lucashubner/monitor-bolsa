import requests

class Active:
    def __init__(self,name, buy_val, quantity):
        self.name = name
        self.buy_val = buy_val
        self.quantity = quantity
        self.actual_value = 0
        self.stonk = 0
        self.percent_stonk = 0

    def setActualValue(self, actualValue):
        self.actual_value = actualValue
        self.percent_stonk = (actualValue - self.buy_val)  / self.buy_val
        self.stonk = (actualValue - self.buy_val) * self.quantity

    def refresh(self):
        try:
            request_url = "https://query2.finance.yahoo.com/v10/finance/quoteSummary/"+ self.name +"?formatted=false&lang=en-US&region=US&modules=price%2CsummaryDetail%2CpageViews&corsDomain=finance.yahoo.com"
            response = requests.get(request_url)
            response = response.json()
            self.setActualValue(response['quoteSummary']['result'][0]['price']['regularMarketPrice'])
        except:
            print("Error refreshing " + self.name)


