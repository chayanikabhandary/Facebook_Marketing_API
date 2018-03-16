# Facebook_Marketing_API
Pre-requisites:
_________________
    1. Create a Facebook account (<YOUR_ACCOUNT_ID> is the Facebook account ID)
    2. Register on 'developers.facebook.com' and create an App.
    
    
Steps required to run codes in this repository:
___________________________________________________
    1. Clone the repo
    2. Create a virtual environment
        python -m virtualenv env
    3. Activate the virtual environment
        source env/bin/activate
    4. Install all required packages
        pip install -r requirements.txt
    5. Substitute the actual values of the variables in initialization.py
        a. YOUR_APP_ID with the APP ID that is found in https://developers.facebook.com/apps/ 
        b. YOUR_APP_SECRET with the App secret found in https://developers.facebook.com/apps/<YOUR_APP_ID>/settings/basic/
        c. YOUR_ACCESS_TOKEN with the access token generated in https://developers.facebook.com/apps/<YOUR_APP_ID>/marketing-api/tools/
        d. YOUR_ACCOUNT_ID with the Facebook account ID
