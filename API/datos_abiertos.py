import panda as pd
from sodapy import socrata

#Enter to the dataframe like an user
client = socrata("www.datos.gov.co", None)

#Get the data from the API
results = client.get("gt2j-8ykr", limit=1000)
