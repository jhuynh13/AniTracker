from pytrends.request import TrendReq
import pandas as pd

# Only need to run this once, the rest of requests will use the same session.
pytrend = TrendReq()

# Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
pytrend.build_payload(kw_list=['anime'], geo='US', cat=317)

# Interest Over Time
interest_over_time_df = pytrend.interest_over_time()
print(interest_over_time_df.tail(20))

interest_by_region_df = pytrend.interest_by_region()
print(interest_by_region_df.sort_values(['anime'], ascending=False).head(20))