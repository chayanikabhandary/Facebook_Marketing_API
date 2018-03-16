from facebookads.adobjects.customaudience import CustomAudience
import initialization

CUSTOM_AUDIENCE_ID = <YOUR_CUSTOM_AUDIENCE_ID>

schema = [
    CustomAudience.Schema.MultiKeySchema.email
]

users = [
    ['testa@a.com'],
    ['testb@b.com']
]
audience = CustomAudience(CUSTOM_AUDIENCE_ID)
audience.add_users(schema, users, is_raw=True)
