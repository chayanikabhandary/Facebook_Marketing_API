from facebookads.api import FacebookAdsApi

my_app_id = <YOUR_APP_ID>
my_app_secret = <YOUR_APP_SECRET>
my_access_token = <YOUR_ACCESS_TOKEN>
account_id = 'act_' + <YOUR_ACCOUNT_ID>
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token, account_id)
