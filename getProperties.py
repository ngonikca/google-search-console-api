from google.oauth2 import service_account
import googleapiclient.discovery

SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']
SERVICE_ACCOUNT_FILE = 'service_credentials.json'

credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

delegated_credentials = credentials.with_subject('nicosearchconsole@woven-operative-222317.iam.gserviceaccount.com')

webmasters_service = googleapiclient.discovery.build('webmasters', 'v3', credentials=delegated_credentials)

site_list = webmasters_service.sites().list().execute()
verified_sites_urls = [s['siteUrl'] for s in site_list['siteEntry'] if s['permissionLevel'] != 'siteUnverifiedUser']

print(verified_sites_urls)

listoflists = [[i] for i in verified_sites_urls]

