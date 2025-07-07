
import requests
import webbrowser
import urllib.parse
client_id = input("🔑 Enter your LinkedIn Client ID: ").strip()
client_secret = input("🔐 Enter your LinkedIn Client Secret: ").strip()
post_text = input("📝 What do you want to post on LinkedIn? ").strip()
redirect_uri = "http://localhost:8000"
auth_url = (
    f"https://www.linkedin.com/oauth/v2/authorization"
    f"?response_type=code&client_id={client_id}"
    f"&redirect_uri={urllib.parse.quote(redirect_uri)}"
    f"&scope=w_member_social"
)
webbrowser.open(auth_url)
auth_code = input("\n🔁 After authorizing, paste the 'code' from the redirected URL here:\ncode = ").strip()
print("🔄 Getting access token...")
token_url = "https://www.linkedin.com/oauth/v2/accessToken"
token_data = {
    "grant_type": "authorization_code",
    "code": auth_code,
    "redirect_uri": redirect_uri,
    "client_id": client_id,
    "client_secret": client_secret
}
token_response = requests.post(token_url, data=token_data)
if token_response.status_code != 200:
    print("❌ Failed to get access token:", token_response.text)
    exit()
access_token = token_response.json()["access_token"]
print("✅ Access token received!")
print("🔍 Getting your LinkedIn profile ID...")
headers = {
    "Authorization": f"Bearer {access_token}",
    "X-Restli-Protocol-Version": "2.0.0"
}
me_response = requests.get("https://api.linkedin.com/v2/me", headers=headers)
if me_response.status_code != 200:
    print("❌ Failed to fetch profile ID:", me_response.text)
    exit()
urn = me_response.json()["id"]
author = f"urn:li:person:{urn}"
print("📤 Posting to LinkedIn...")
post_url = "https://api.linkedin.com/v2/ugcPosts"
headers["Content-Type"] = "application/json"
post_data = {
    "author": author,
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {"text": post_text},
            "shareMediaCategory": "NONE"
        }
    },
    "visibility": {
        "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
    }
}
post_response = requests.post(post_url, headers=headers, json=post_data)
if post_response.status_code == 201:
    print("✅ Post successfully shared on your LinkedIn!")
else:
    print("❌ Failed to post:", post_response.text)
