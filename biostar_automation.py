import requests
import json
import urllib3

# Hidden unsecure HTTPS (Self-signed Log) file errors
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ==========================================
# SETTINGS
# ==========================================
IP_ADDRESS = "192.168.1.11"   
PORT = "443"                  
USERNAME = "admin"            
PASSWORD = "Isuru2003423" 

# ==========================================
# MAIN SCRIPT
# ==========================================

def login_and_fetch_data():
    base_url = f"https://{IP_ADDRESS}:{PORT}"
    
    print(f"\n Connecting to BioStar 2 Server at {IP_ADDRESS}...")

    # 1. LOGIN (Authentication)
    login_url = f"{base_url}/api/login"
    login_payload = json.dumps({
        "User": {
            "login_id": USERNAME,
            "password": PASSWORD
        }
    })
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(login_url, headers=headers, data=login_payload, verify=False)
        
        if response.status_code != 200:
            print(f"Unsuccess Login! Status: {response.status_code}")
            print(f"Error: {response.text}")
            return

        # Get session ID
        auth_token = response.headers.get('bs-session-id')
        print("Success Login! (Login Successful)")
        print(f" Session ID: {auth_token}")

        # 2. GET USER DATA (Fetching Users)
        print("\n Fetching Users...")
        
        user_headers = {
            'bs-session-id': auth_token,
            'Content-Type': 'application/json'
        }
        
        # Call User List API 
        user_url = f"{base_url}/api/users?limit=10"
        user_response = requests.get(user_url, headers=user_headers, verify=False)

        if user_response.status_code == 200:
            users_data = user_response.json()
            user_list = users_data.get('UserCollection', {}).get('rows', [])
            
            print(f"\n Number of Users: {len(user_list)}")
            print("-" * 40)
            print(f"{'ID':<10} | {'Name':<20} | {'Email'}")
            print("-" * 40)
            
            for user in user_list:
                uid = user.get('user_id', 'N/A')
                name = user.get('name', 'N/A')
                email = user.get('email', '')
                print(f"{uid:<10} | {name:<20} | {email}")
            
            print("-" * 40)
            print(" Mission Complete")
            
        else:
            print(f"Mission incomplete: {user_response.status_code}")

    except Exception as e:
        print(f"\n Connection Error: {e}")
        print("Tip: See your VM is ping with Host.")

# Code Run 
if __name__ == "__main__":
    login_and_fetch_data()