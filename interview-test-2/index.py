## For solving this problem, we doing
## 1. Making Get api call and get the partners
## 2. Preparing the Post api request payload from the partners which we recieved from the previous get call.
## 3. Making a Post api call with prepared Request payload from the previous step
##
##
import json
import requests
from datetime import datetime, timedelta

apiKey = "c6ecf2ff937d313d57b670b147f4" # API Key
apiBaseURI = "https://candidate.hubteam.com/candidateTest/v3/problem/"

# 2. prepare the payload for the post API
def prepareRequestPayloadForPostAPI (partners):
    countriesAvailability = []
    sortedAvailableCountriesAndDates = {}

    # get the all the available dates by country (sorted order)
    for partner in partners:
        country = partner["country"]
        if country not in sortedAvailableCountriesAndDates:
            sortedAvailableCountriesAndDates[country] = []
        #removing duplicates of available dates
        availableDates = list(set(sortedAvailableCountriesAndDates[country] + partner["availableDates"]))
        sortedAvailableCountriesAndDates[country] = sorted(availableDates, key=lambda x: datetime.strptime(x, '%Y-%m-%d'))

    # print(sortedAvailableCountriesAndDates)
    # get the partners availability
    for country in sortedAvailableCountriesAndDates:
        partnersListFromRequest = filter(lambda x: x["country"] == country, partners)
        partnersInDateRange = []
        startDate = None

        for date in sortedAvailableCountriesAndDates[country]:
            currentPartnerInDateRange = []
            for partner in partnersListFromRequest:
                availableDates = partner["availableDates"]
                currentDate = date
                # adding 1 day to the date for checking availability for continouous day.
                nextDate = datetime.strptime(currentDate, "%Y-%m-%d") + timedelta(days=1)
                # print(currentDate, nextDate, datetime.strftime(nextDate, "%Y-%m-%d"))
                # compare continues days
                if currentDate in availableDates and datetime.strftime(nextDate, "%Y-%m-%d") in availableDates:
                    currentPartnerInDateRange.append(partner)
            
            if len(partnersInDateRange) < len(currentPartnerInDateRange):
                partnersInDateRange = currentPartnerInDateRange
                startDate = date
        
        countryDetails = {}
        if len(partnersInDateRange) is 0:
            countryDetails["attendeeCount"] = 0
            countryDetails["startDate"] = None
        else:
            countryDetails["attendeeCount"] = len(partnersInDateRange)
            countryDetails["startDate"] = startDate
            countryDetails["attendees"] = []
            # getting the email details
            for partnerInDateRange in partnersInDateRange:
                countryDetails["attendees"].append(partnerInDateRange["email"])
        countryDetails["name"] = country
        countriesAvailability.append(countryDetails)
    
    return { "countries": countriesAvailability }


# 1. get the dataset from the api
response = requests.get(f"{apiBaseURI}dataset?userKey={apiKey}")

if response.status_code == 200:
    # get the partners from the response
    partners = (response.json())["partners"]
    
    # prepare the payload for the postAPI
    postPayload = prepareRequestPayloadForPostAPI(partners)
    
    # print(json.dumps(postPayload))

    # post the payload to api
    postResponse = requests.post(f"{apiBaseURI}result?userKey={apiKey}", json=postPayload)

    # print(postResponse.text)

    if postResponse.status_code == 200:
        print("Successfully Posted the request")
    else:
        print(f"something went wrong while making post call to the api {postResponse.status_code}, {postResponse.reason}, {postResponse.text} ")

else:
    print(f"something went wrong while making get call to the api {response.status_code}, {response.reason} ")