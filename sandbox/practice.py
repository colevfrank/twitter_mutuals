import requests
from util import get_keys
import json

# Twitter sample code:
# https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/master/Follows-Lookup/followers_lookup.py
    


    
#resp = requests.get(query_url)
#data_lsts = resp.json()

def get_user_id(username):
    """
    Given a twitter user name
    Return user id
    https://developer.twitter.com/en/docs/twitter-api/users/lookup/quick-start
    """
    bearer_token = get_keys.get_bearer_token()
    base_url = f"https://api.twitter.com/2/users/by?usernames={username}"
    params = {"user.fields": "created_at"}
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    response = requests.request("GET", base_url, headers=headers, params=params)
    return response.json()


def create_url():
    # Replace with user ID below
    user_id = 2244994945
    return "https://api.twitter.com/2/users/{}/following".format(user_id)


def get_params():
    return {"user.fields": "created_at", "max_results": 1, "pagination_token": None}


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def connect_to_endpoint(url, headers, params):
    response = requests.request("GET", url, headers=headers, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()

def main():
    bearer_token = get_keys.get_bearer_token()
    url = create_url()
    headers = create_headers(bearer_token)
    params = get_params()
    json_response = connect_to_endpoint(url, headers, params)
    new_params = params
    new_params["pagination_token"] = json_response['meta']['next_token']
    json_response = connect_to_endpoint(url, headers, params)

    return json_response
    #print(type(json_response))
    #print(json.dumps(json_response, indent=4, sort_keys=True))