import requests
import json
import urllib3

# Disable insecure request warnings for self-signed certificates
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ==========================================
# MULTI-SITE SETTINGS (SERVER LIST)
# ==========================================
# Add all your servers here
SERVERS = [
    {"name": "Site A (Head Office)", "ip": "192.168.1.11"},
    {"name": "Site B (Branch)",      "ip": "192.168.1.12"}
]

PORT = "443"
USERNAME = "admin"
PASSWORD = "Isuru2003423"  

# ==========================================
# AUTOMATION SCRIPT
# ==========================================

def fetch_data_from_server(server_name, ip):
    base_url = f"https://{ip}:{PORT}"
    print(f"\nConnecting to {server_name} [{ip}]...")

    # 1. LOGIN
    try:
        login_response = requests.post(
            f"{base_url}/api/login",
            headers={'Content-Type': 'application/json'},
            data=json.dumps({"User": {"login_id": USERNAME, "password": PASSWORD}}),
            verify=False
        )

        if login_response.status_code != 200:
            print(f"Login Failed on {server_name}")
            return None

        session_id = login_response.headers.get('bs-session-id')
        print(f"Login Success! (Session: {session_id[:10]}...)")

        # 2. FETCH USERS
        headers = {'bs-session-id': session_id, 'Content-Type': 'application/json'}
        user_response = requests.get(f"{base_url}/api/users?limit=10", headers=headers, verify=False)
        
        if user_response.status_code == 200:
            users = user_response.json().get('UserCollection', {}).get('rows', [])
            print(f"Found {len(users)} users on {server_name}")
            return users
        else:
            print(f"Could not fetch users from {server_name}")
            return None

    except Exception as e:
        print(f"Connection Error with {server_name}: {e}")
        return None

# --- Main Execution ---
all_site_data = []

print("Starting Multi-Site Data Sync...")
print("=" * 50)

for server in SERVERS:
    data = fetch_data_from_server(server["name"], server["ip"])
    if data:
        # Tag data with the source server name
        for user in data:
            user['source_server'] = server["name"]
            all_site_data.append(user)

print("=" * 50)
print(f"Total Data Count: {len(all_site_data)} Users gathered.")

# 3. SAVE TO FILE (HR SYSTEM SIMULATION)
filename = "global_hr_data.json"
with open(filename, 'w') as f:
    json.dump(all_site_data, f, indent=4)

print(f"All data saved to '{filename}'.")
print("Mission Complete: Multi-Site Sync Finished!")