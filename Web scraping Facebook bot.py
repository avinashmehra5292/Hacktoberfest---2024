import requests
import json

# Replace with your App ID, App Secret, and Access Token

#1. Create a Facebook Developer Account
#Sign in with your Facebook account and create an app.
#Once the app is created, you will receive an App ID and App Secret.

#2. Get an Access Token
#You will need an access token to authenticate API requests. You can use the Facebook Graph API Explorer to generate an access token for testing purposes.

#3. Install the Required Python Libraries
#You will need the requests library to make HTTP requests and the json library to handle the response data. Install these libraries using pip:
ACCESS_TOKEN = 'your_access_token_here'

def get_facebook_page_data(page_id):
    """
    Fetches the public posts from a Facebook Page using the Graph API.
    """
    url = f"https://graph.facebook.com/v13.0/{page_id}/posts"
    params = {
        'access_token': ACCESS_TOKEN
    }

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        # Convert the response to JSON
        data = response.json()
        return data
    else:
        print(f"Failed to fetch data. Status Code: {response.status_code}")
        return None

def main():
    # Replace 'page_id_here' with the Facebook page ID or username you want to scrape
    page_id = 'page_id_here'
    
    page_data = get_facebook_page_data(page_id)
    
    if page_data:
        print(json.dumps(page_data, indent=4))  # Pretty print the JSON response

if __name__ == "__main__":
    main()
