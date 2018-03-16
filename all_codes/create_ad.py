from facebookads.adobjects.ad import Ad
import initialization

AD_ACCOUNT_ID = initialization.account_id
AD_SET_ID = <YOUR_AD_SET_ID>

ad = Ad(parent_id=AD_ACCOUNT_ID)
ad[Ad.Field.name] = 'My Ad'
ad[Ad.Field.adset_id] = AD_SET_ID
ad[Ad.Field.creative] = {
    'creative_id': <YOUR_CREATIVE_ID>,
}
ad.remote_create(params={
    'status': Ad.Status.paused,
})
