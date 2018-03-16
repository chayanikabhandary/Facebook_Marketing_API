from facebookads.adobjects.targetingsearch import TargetingSearch
import initialization
params = {
    'q': 'un',
    'type': 'adgeolocation',
    'location_types': ['country'],
}

resp = TargetingSearch.search(params=params, api=None)
print(resp)
