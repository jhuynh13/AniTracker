from django.shortcuts import render
from django.http import HttpResponse
from pytrends.request import TrendReq
import pandas as pd

# Create your views here.

def home(request):

    location = "US"

    location = request.POST.get("geo", "")

    # Only need to run this once, the rest of requests will use the same session.
    pytrend = TrendReq()

    # Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
    pytrend.build_payload(kw_list=['anime'], geo=location, cat=317)

    # Interest Over Time
    interest_over_time_df = pytrend.interest_over_time()
    interest_df = interest_over_time_df.tail(10)
    interest_array = []
    for m in interest_df.iterrows():
       
        interest_array.append([m[0],m[1][0]])
 

    # anime interest by regions in US
    interest_by_region_df = pytrend.interest_by_region()
    sorted_df = interest_by_region_df.sort_values(['anime'], ascending=False).head(10)
    region_array = []
    # Convert df to array
    for i in sorted_df.iterrows():
        parsed_row = int(i[1][0])
        region_array.append([i[0],parsed_row])

    return render(request, "main/view.html", {"regions": region_array, "interest": interest_array, 
    "location": location})

