from facebookads.adobjects.customaudience import CustomAudience
from facebookads.adobjects.adaccount import AdAccount
import initialization

fbid = initialization.account_id
ad_account = AdAccount(fbid=fbid)
name = 'Test Audience'
description = 'Only testing'
params = {
    CustomAudience.Field.subtype: CustomAudience.Subtype.custom,
    CustomAudience.Field.name: name,
    CustomAudience.Field.description: description
}
custom_audience = ad_account.create_custom_audience(params=params)
CUSTOM_AUDIENCE_ID = custom_audience[CustomAudience.Field.id]
