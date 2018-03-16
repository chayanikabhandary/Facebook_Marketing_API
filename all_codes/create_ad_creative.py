from facebookads.adobjects.adcreative import AdCreative
from facebookads.adobjects.adcreativelinkdata import AdCreativeLinkData
from facebookads.adobjects.adcreativeobjectstoryspec \
    import AdCreativeObjectStorySpec
import initialization
import create_adimage

IMAGE_HASH = create_adimage.image_hash
AD_ACCOUNT_ID = initialization.account_id
PAGE_ID = <YOUR_PAGE_ID>

link_data = AdCreativeLinkData()
link_data[AdCreativeLinkData.Field.message] = 'try it out'
link_data[AdCreativeLinkData.Field.link] = 'www.facebook.com'
link_data[AdCreativeLinkData.Field.image_hash] = IMAGE_HASH

object_story_spec = AdCreativeObjectStorySpec()
object_story_spec[AdCreativeObjectStorySpec.Field.link_data] = link_data
object_story_spec[AdCreativeObjectStorySpec.Field.page_id] = PAGE_ID

creative = AdCreative(parent_id=AD_ACCOUNT_ID)
creative[AdCreative.Field.name] = 'AdCreative for Link Ad'
creative[AdCreative.Field.object_story_spec] = object_story_spec
creative.remote_create()

print(creative)
