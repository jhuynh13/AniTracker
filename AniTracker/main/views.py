from django.shortcuts import render
from django.http import HttpResponse
from pytrends.request import TrendReq
import pandas as pd

# Create your views here.

def home(response):

    # Only need to run this once, the rest of requests will use the same session.
    pytrend = TrendReq()

    # Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
    pytrend.build_payload(kw_list=['anime'], geo='KR', cat=317)

    # Interest Over Time
    interest_over_time_df = pytrend.interest_over_time()
    #print(interest_over_time_df.tail(20))


    # MAKE A SIDE BY SIDE COMPARISON OF POPULARITY OF DIFFERENT ANIME
    # KEYWORDS OF INTEREST OVER TIME FOR DIFFERENT REGIONS




    # anime interest by regions in US
    interest_by_region_df = pytrend.interest_by_region()
    sorted_df = interest_by_region_df.sort_values(['anime'], ascending=False).head(20)
    region_array = []
    # Convert df to array
    for i in sorted_df.iterrows():
        parsed_row = i[1][0]
        region_array.append([i[0],parsed_row])

    return render(response, "main/view.html", {"regions":region_array})

def list(response):

    return render(response, "main/index.html", {})
