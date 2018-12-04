from google.oauth2 import service_account
import googleapiclient.discovery
import csv
import datetime
from datetime import timedelta

SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']
SERVICE_ACCOUNT_FILE = 'service_credentials.json'
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
delegated_credentials = credentials.with_subject('nicosearchconsole@woven-operative-222317.iam.gserviceaccount.com')
webmasters_service = googleapiclient.discovery.build('webmasters', 'v3', credentials=delegated_credentials)
site_urls = [['https://reviews.thedenverchannel.com/'], ['https://reviews.newschannel5.com/'], ['https://reviews.kshb.com/'], ['https://reviews.newson6.com/'], ['https://reviews.theindychannel.com/'], ['https://reviews.news9.com/'], ['https://reviews.wxyz.com/'], ['https://mythreecents.com/'], ['https://www.retirementliving.com/'], ['https://reviews.wmar2news.com/'], ['https://reviews.10news.com/'], ['https://reviews.news5cleveland.com/'], ['https://reviews.abcactionnews.com/'], ['https://reviews.abc15.com/'], ['https://blog.consumeraffairs.com/']]

#convertimos la lista de listas en una lista plana para poder iterar
#flat_list = [item for sublist in site_urls for item in sublist]
flat_list = ['https://reviews.news9.com/']
day_to_download = str(datetime.datetime.now().date() - timedelta(days=20))

def execute_site(site, start_row, date):
    request = {
        'startDate': date,
        'endDate': date,
        'dimensions': ['query', 'device', 'page'],
        'aggregationType': 'byPage',
        'rowLimit': '25000',
        'startRow': start_row
    }
    
    try: 
        response = execute_request(webmasters_service, site, request)
        rows = response['rows']
        cantFilas = len(rows)
        print("Now retrieving: " + str(site) + ". Iterando " + str(cantFilas) + " filas. Fecha: " + date)
        
        for row in rows:
            query = row['keys'][0]
            #sometimes we receive queries with 1000+ characters, so we truncate them to 250
            trunc_query = (query[:240] + '..') if len(query) > 240 else query
            device = row['keys'][1]
            address = row['keys'][2]
            clicks = row['clicks']
            impressions = row['impressions']
            ctr = row['ctr']
            position = row['position']
            to_print.append([date, trunc_query, device, address, clicks, impressions, ctr, position])    
            #to_print.append([trunc_query])    
        
        return cantFilas
    except KeyError:
        print("No data available for: " + str(site) + ". Continuing...")

def execute_request(webmasters_service, site, request):
  return webmasters_service.searchanalytics().query(
      siteUrl=site, body=request).execute()

##iterador principal

to_print = []
for site in flat_list:
    for rowOffset in range(0,20000000,25000):
        filas = execute_site(site, rowOffset, day_to_download)
        if filas != 25000:
        	break

## abrimos el csv
with open('queries.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=",",lineterminator="\n") 
    #escribimos
    i = 0
    for value in to_print:
        writer.writerow(value)
        i += 1
print("Finished. Printed " + str(i) + " lines to CSV.")