import initialization
from facebookads.adobjects.campaign import Campaign

AD_ACCOUNT_ID = initialization.account_id
parent_id = AD_ACCOUNT_ID
campaign = Campaign(parent_id=parent_id)
campaign.update({
    Campaign.Field.name: 'Test Campaign',
    Campaign.Field.objective: Campaign.Objective.link_clicks,
})

campaign.remote_create(params={
    'status': Campaign.Status.paused,
})
