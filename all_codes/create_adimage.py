from facebookads.adobjects.adimage import AdImage
import initialization

AD_ACCOUNT_ID = initialization.account_id
image = AdImage(parent_id=AD_ACCOUNT_ID)
image[AdImage.Field.filename] = '../other_resources/image.png'
image.remote_create()
image_hash = image[AdImage.Field.hash]
