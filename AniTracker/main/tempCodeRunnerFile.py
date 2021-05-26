from pytrends.request import TrendReq

pytrend = TrendReq()

# Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
pytrend.build_payload(kw_list=['anime'], geo='CA', cat=317)

# Interest Over Time
interest_over_time_df = pytrend.interest_over_time()
print(interest_over_time_df.tail(20))
