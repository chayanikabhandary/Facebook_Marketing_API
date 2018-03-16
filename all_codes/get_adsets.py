from facebookads.adobjects.adaccount import AdAccount
import initialization

fbid = initialization.account_id
ad_account = AdAccount(fbid=fbid)
print ad_account.get_ad_sets()
