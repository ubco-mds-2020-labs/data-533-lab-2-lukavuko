#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class debtServiceRatio:
    downpayment = 0

    def __init__(self, income, property_tax, heat_cost, car_payment, credit_card_payment, downpayment, home_price):
        self.income = income
        self.property_tax = property_tax
        self.heat_cost = heat_cost
        self.car_payment = car_payment
        self.credit_card_payment = credit_card_payment
        self.downpayment = downpayment
        self.home_price = home_price

    def gds(self, prin = False): #max affordability based on GDS score
        gds_ratio = 0.32 #change to 0.35
        months = 12

        gds_max_annual_spend = self.income * gds_ratio
        gds_max_mortgage_annual = gds_max_annual_spend - self.property_tax - self.heat_cost
        gds_max_mortgage_monthly = gds_max_mortgage_annual / months
        
        if prin == True:
            print("Max Annual Spending: ${}".format(gds_max_annual_spend))
            print("Max Annual Mortgage Payment: ${}".format(gds_max_mortgage_annual))
            print("Max Monthly Mortgage Payment: ${}".format(gds_max_mortgage_monthly))
        #return (max_annual_spend, max_mortgage_annual, max_mortgage_monthly)

        if self.downpayment > gds_max_mortgage_annual:
            downpayment = gds_max_mortgage_annual
            if prin == True:
                print("Your downpayment: ${}".format(gds_max_mortgage_annual))
            return gds_max_mortgage_annual
        else:
            downpayment = self.downpayment
            if prin == True:
                print("Your downpayment: ${}".format(self.downpayment))
            return self.downpayment #######

    def tds(self, prin = False): #max affordability based on TDS score
        tds_ratio = 0.40 # change to 0.42
        months = 12

        tds_max_annual_spend = self.income * tds_ratio
        tds_max_mortgage_annual = tds_max_annual_spend - self.property_tax - self.heat_cost - self.car_payment - self.credit_card_payment
        tds_max_mortgage_monthly = tds_max_mortgage_annual / months
        if prin == True:
            print("Max Annual Spending: ${}".format(tds_max_annual_spend))
            print("Max Annual Mortgage Payment: ${}".format(tds_max_mortgage_annual))
            print("Max Monthly Mortgage Payment: ${}".format(tds_max_mortgage_monthly))

        if self.downpayment > tds_max_mortgage_annual: #
            downpayment = tds_max_mortgage_annual
            if prin == True:
                print("Your downpayment: ${}".format(tds_max_mortgage_annual))
            return tds_max_mortgage_annual #######
        else:
            downpayment = self.downpayment
            if prin == True:
                print("Your downpayment: ${}".format(self.downpayment))
            return self.downpayment #######

    def mortgage_max(self):
        downpayment_percent = 0

        if self.home_price <= 500000:
            downpayment_percent = 0.05
        elif self.home_price > 500000 and self.home_price <= 1000000:
            downpayment_percent = 0.1
        else:
            downpayment_percent = 0.2

        #loan = self.max_dp() / downpayment_percent
        loan = self.downpayment / downpayment_percent
        return loan

    def max_dp(self, pri = False):
        return min(self.gds(prin = pri), self.tds(prin = pri))

