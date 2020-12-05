# Documentation: Mortgage Package - Updated 04/12/2020

## Financial
### **creditRating**
***
```
class creditRating:

    A class used to convert home buyer's financial characteristics into individual credit score components
    
    ...

    Attributes
    ----------
    age : int
        home buyer's age in years
    home : str
        home buyer's current residence status; own or rent
    income : int
        home buyer's annual income
    score_age : int
        points awarded to credit score based on home buyer's age
    score_home : int
        points awarded to credit score based on home buyer's current residence status
    score_income : int
        points awarded to credit score based on home buyer's annual income

    Methods
    -------
    convert_age()
        Returns credit points by converting home buyer's age based on 7 possible age ranges.
    convert_home()
        Returns credit points by converting home buyer's current residence status based on 2 possible residence statuses.
    convert_income()
	Returns credit points by converting home buyer's annual income based on 6 possible annual income ranges.



score(buyer):

    Prints calculated score with decision of loan approval.
    Calculates credit score with individual component scores from class creditRating to determine loan approval.

    Argument
    --------
    buyer : object
        object from class creditRating

    Return
    ---------
    int
        sum of component scores age + home + income

```


### **debtServiceRatio**
***
```
class debtServiceRatio:

    A class used to represent an individual and their information regarding debt service ratios
    Storing buyer objects this way is useful for determining their maximum allowable annual and monthly mortgage payments
    
    ...

    Attributes
    ----------
    income : numeric
        home buyer's annual income
    property_tax : numeric
        home buyer's annual property tax
    heat_cost : numeric
        home buyer's annual heat cost
    car_payment : numeric
        home buyer's annual car payment
    credit_card_payment : numeric
        home buyer's annual credt card payment
    downpayment : int
        home buyer's proposed downpayment
    home_price : int
        home buyer's desired home price
    months : int
        months in one year
    gds_ratio : float
        current ratio for Gross Debt Service
    gds_max_annual_spend : numeric
        calculates home buyer's maximum annual spending available
    gds_max_mortgage_annual : numeric
        calculates home buyer's maximum annual mortgage payments
    gds_max_mortgage_monthly : numeric
        calculates home buyer's maximum monthly mortgage payments
    tds_ratio : numeric
        current ratio for Total Debt Service
    tds_max_annual_spend : numeric
        calculates home buyer's maximum annual spending available
    tds_max_mortgage_annual : numeric
        calculates home buyer's maximum annual mortgage payments
    tds_max_mortgage_monthly : numeric
        calculates home buyer's maximum monthly mortgage payments

    Methods
    -------
    gds(self, prin = False)
    
        Calculates buyer's max annual spending, max annual mortgage payment, and max monthly mortgage payments based on Gross Debt Service Ratio of 32%
    
    	Arguments
        ----------
	self : debtServiceRatio object
	    Object representing the buyer and their information
	prin : bool
	    Optional condition if extra object attributes should be printed (Default = False)
	     
        Returns
        -------
        float
	    minimum downpayment
	
    tds(self, prin = False)
    
        Calculates buyer's max annual spending, max annual mortgage payment, and max monthly mortgage payments based on Total Debt Service Ratio of 40%

    	Arguments
        ----------
	self : debtServiceRatio object
	    Object representing the buyer and their information	
	prin : bool
	    Optional condition if extra object attributes should be printed (Default = False)
	     
        Returns
        -------
        float
	    maximum allowable downpayment

    

mortgage_max(buyer_dsr)

    Calculates maximum loan available to offer based on buyer's proposed downpayment and downpayment percent
    
    Arguments
    ----------
    buyer_dsr : debtServiceRatio object
        Buyer object defined in the debtServiceRatio class
    
    Returns
    -------
    float
        Returns maximum available loan to be offered
    


min_dp(buyer_dsr, pri = False):
    
    Compares Gross Debt Service Ratio and Total Debt Service Ratio and returns expected annual and monthly maximum mortgage payments and minimum downpayment

    Arguments
    ----------
    buyer_dsr : debtServiceRatio object
        Buyer object defined in the debtServiceRatio class
    prin : bool
        Optional condition if extra object attributes should be printed (Default = False)
	
    Return
    ------
    float
        minimum downpayment
```

## Mortgages
### **mortgages**
***
```
class RealEstate()
     
    A class for real estate assets in CAD 
    
    ...
    
    Attributes
    ----------
    prop : str
        Name identifier for the property ('Clearview Residential Home')
    price : numeric > 0
        Property value
    prop_owner : str
        Name identifier ('Brookfield Asset Management')
    prov : str
        Canadian provicial identifier (BC, ON, QC...)
    props_initialized : int
        Number of properties currently initialized in memory (counter)
    
    Methods
    -------
    getProp():
        Returns property name or ID defined by the legal owner.
    getPrice():
        Returns asset price.
    getPropOwner():
        Returns legal owner of the asset.
    getProv():
        Returns Provincial location of the asset.



class Residential(RealEstate):
    
    A class for residential real estate assets in CAD.
    
    ...
    
    Attributes
    ----------
    prop : str
        Name identifier for the property ('Clearview Residential Home')
    price : numeric > 0
        Property value
    prop_owner : str
        Name identifier ('Brookfield Asset Management')
    area : str
        Name of residential area
    city : str
        Name of city
    prov : str
        Canadian provicial identifier (BC, ON, QC...)
    sq_footage : int
        Property square footage
    year_built : int
        Year property was constructed
        
    Methods
    -------
    getArea():
        Returns area or community the property is located in.
    getCity():
        Returns city the property is located in.
    getSq_footage():
        Returns square footage of the property.
    getYear_built():
        Returns year property was built.
    
    Inherited Methods
    -----------------
    getProp():
        Returns property name or ID defined by the legal owner.
    getPrice():
        Returns asset price.
    getPropOwner():
        Returns legal owner of the asset.
    getProv():
        Returns Provincial location of the asset.
```


### **mortgage_estimator**
***
```
property_filter(property_data, downpayment, mortgage_rate=None, mortgage_term=None, max_monthly_payment=None, max_loan=None)
    
    Returns a dataframe containing the properties/areas.
        
    Arguments
    ----------
    data : dataframe 
        Areas/properties in column index 0 (str)
        Respective prices in column index 1 (numeric) 
        
    downpayment : numeric
        Your maximal downpayment
    
    mortgage_rate : numeric 
        Interest rate on the mortgage loan (leave empty if mortgage_term is provided)
    
    mortgage_term : int 
        Contract length in years (1 to 10) for the mortgage interest rate.
        Only specify if you do not know what mortgage_rate to enter (leave empty if mortgage_rate provided)
        
    max_monthly_payment : numeric 
        Your max affordable or bank limited monthly payment towards your home
        
    max_loan : numeric
        Max eligible loan based on your downpayment
    
    Return
    ------
    dataframe
        Properties/Areas
        Prices/Average area price
        Minimum_Downpayment
        Mortgage_Insurance
        Principal
        Monthly_Payment
        Shortest_Amortization
        Total_Interest
        Net_Cost (assuming no other fees)
        


min_downpayment(price)
    
    Returns the minimum downpayment required for a real estate
    price defined by the Financial Consumer Agency of Canada.
    (https://www.canada.ca/en/financial-consumer-agency/services/mortgages/down-payment.html)
    
    Arguments
    ----------
    price : numeric
        Property price or avereage area property price
        
    Return
    ------
    float
        minimum downpayment
        
    
        
mort_rate(term)
    
    If no mortgage rate is specified this function can be used to
    return an estimated mortgage rate based on a regression fit (R^2 = 0.926)
    on average Canadian mortgage rates for possible term lengths.
    (https://www.superbrokers.ca/tools/mortgage-rates-comparison/)
        
    Arguments
    ----------
    term : int
        contract length in years (from 1 to 10 years)
        
    Return
    ------
    float
        interest rate
    
    
    
mortgage_insurance(price, downpayment)
    
    Returns the cost of mortgage insurance.
    
    Insurance rates are calculated from loan to asset price ratio.
    Rates are applied to the loan to generate a lump sum amount that's
    then added to the principal of the loan to give mortgage insurance.
    
    Arguments
    ----------
    price : int or float
        Property price
    
    downpayment : int or float
        Downpayment on property
        
    Return
    ------
    float
        Mortgage insurance
     
     
    
optimal_monthly_payment(principal, mortgage_rate, max_monthly_payment)
    
    Returns the first amortization period which has a monthly payment
    less than your max_monthly_payment (ie. within budget). The shortest
    possible amortization period has the lowest long term interest cost.
    
    Arguments
    ----------
    principal : numeric
    
    mortgage_rate : float
          Annual mortgage rate (loan interest)
    
    max_monthly_payment: numeric
        Your max affordable monthly contribution
    
    
    Return
    ------
    list
        mp: monthly payment for a given amortization
        i: amortization period in years


monthly_payment(principal, mortgage_rate, amortization, months=False)
    
    Returns the monthly payment required to meet the given amortization period.
    Assumes payments occur on a monthly basis.
    
    Arguments
    ----------
    principal : numeric
    
    mortgage_rate : float
        Annual mortgage rate (loan interest)
    
    amortization: int
        Amortization period in years (or in months if months == True)
        
    months : bool 
        (Optional) if True, amortization period is interpreted in months (default = False)
    
    Return
    ------
    float
        monthly payment
        


total_interest(principal, mortgage_rate, monthly_payment)
    
    Returns the cumulative interest paid on a given principal, mortgage rate, and monthly payment.
    
    Arguments
    ----------
    principal : numeric
    
    mortgage_rate : float
        Annual mortgage rate (loan interest)
    
    amortization: int
        Amortization period in years (or in months if months == True)
        
    monthly_payment : bool 
        Monthly contribution towards the principal
    
    Return
    ------
    float
        Cumulative interest paid
```
