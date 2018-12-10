from googleads import adwords
from googleads import oauth2

CLIENT_ID = '465735130748-shmh1886i93pqao17n9potg9vb9ssnst.apps.googleusercontent.com'
CLIENT_SECRET = 'xWYU8ekO2QCF0S_AXVaHsDUn'
REFRESH_TOKEN = '4/rwAUW2bL702WiHFumTpKCf_urJXGrkMWvxNk8QjQNXS6MgejukvGUGM'

# AdWords API information.
DEVELOPER_TOKEN = '1aNcSAOfsu4oOuMibCYDMw'
USER_AGENT = 'Chicos Programando'
CLIENT_CUSTOMER_ID = '927-413-9299'

KEYWORDS = ['best home security system' ,'home security systems','home security companies','home security system','home alarm monitoring']

def main(client_id, client_secret, refresh_token, developer_token, user_agent,
         client_customer_id):
  oauth2_client = oauth2.GoogleRefreshTokenClient(
      client_id, client_secret, refresh_token)
  
  print(oauth2_client)

  adwords_client = adwords.AdWordsClient(
      developer_token, oauth2_client, user_agent,
      client_customer_id=client_customer_id)
   
  print(adwords_client)

  targeting_service = adwords_client.GetService('TargetingIdeaService', version='v201809')

  print(targeting_service)

  print('You are logged in.')

if __name__ == '__main__':
  main(CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN, DEVELOPER_TOKEN, USER_AGENT,
       CLIENT_CUSTOMER_ID)

selector = {
    ideaType: 'KEYWORD',
    requestType: 'STATS',
    requestedAttributeTypes: ['SEARCH_VOLUME', 'AVERAGE_CPC','TARGETED_MONTHLY_SEARCHES'],
    paging: {startIndex: 0, numberResults: 1000},
}

targeting_service.get(selector)
