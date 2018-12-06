from googleads import adwords
from googleads import oauth2

CLIENT_ID = '200039730421-3ouk3goh4qlpa1lc83moi0d44okdg6e7.apps.googleusercontent.com'
CLIENT_SECRET = 'Q_4Vlw1GhJF8n2-Vw_DVsROu'
REFRESH_TOKEN = '4/qwAsAg4y-THyo-YoKSs2rL90bCHyk3efvvmuutw9aVgAOPU0fH01QXc'

# AdWords API information.
DEVELOPER_TOKEN = 'aouTC9qranwKJC7KsTprCw'
USER_AGENT = 'ConsumerAffairs'
CLIENT_CUSTOMER_ID = '573-256-9423'


def main(client_id, client_secret, refresh_token, developer_token, user_agent,
         client_customer_id):
  oauth2_client = oauth2.GoogleRefreshTokenClient(
      client_id, client_secret, refresh_token)

  adwords_client = adwords.AdWordsClient(
      developer_token, oauth2_client, user_agent,
      client_customer_id=client_customer_id)

  customer_service = adwords_client.GetService('CustomerService',
                                               version='v201809')
  customers = customer_service.getCustomers()

  print('You are logged in as a user with access to the following customers:')

  for customer in customers:
    print('\t%s' % customer['customerId'])


if __name__ == '__main__':
  main(CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN, DEVELOPER_TOKEN, USER_AGENT,
       CLIENT_CUSTOMER_ID)