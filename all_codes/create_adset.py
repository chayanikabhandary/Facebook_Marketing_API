import datetime
import initialization
from facebookads.adobjects.adaccount import AdAccount
from facebookads.adobjects.adset import AdSet

today = datetime.date.today()
start_time = str(today + datetime.timedelta(weeks=1))
end_time = str(today + datetime.timedelta(weeks=2))

AD_ACCOUNT_ID = initialization.account_id
CAMPAIGN_ID = <YOUR_CAMPAIGN_ID>

ad_account = AdAccount(fbid=AD_ACCOUNT_ID)

params = {
    AdSet.Field.name: 'My Ad Set',
    AdSet.Field.campaign_id: CAMPAIGN_ID,
    AdSet.Field.daily_budget: 20000,
    AdSet.Field.billing_event: AdSet.BillingEvent.impressions,
    AdSet.Field.optimization_goal: AdSet.OptimizationGoal.reach,
    AdSet.Field.bid_amount: 150,
    AdSet.Field.start_time: start_time,
    AdSet.Field.end_time: end_time,
    AdSet.Field.targeting: {
        'geo_locations': {
            'countries': ['US'],
        },
        'user_device': [
            'galaxy s6',
            'one m9',
        ],
        'user_os': ['android'],
    },
    AdSet.Field.status: AdSet.Status.paused,
}
adset = ad_account.create_ad_set(params=params)
