import requests

def get_zone_id(email, api_key, zone_name):
    url = f'https://api.cloudflare.com/client/v4/zones?name={zone_name}'

    headers = {
        'X-Auth-Email': email,
        'X-Auth-Key': api_key,
        'Content-Type': 'application/json',
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    if response.status_code == 200 and data.get('result'):
        return data['result'][0]['id']
    else:
        print(f'Failed to get zone ID. Status code: {response.status_code}, Error: {response.text}')
        return None

def get_record_id(email, api_key, zone_id, record_name):
    url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records?type=A&name={record_name}'

    headers = {
        'X-Auth-Email': email,
        'X-Auth-Key': api_key,
        'Content-Type': 'application/json',
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    if response.status_code == 200 and data.get('result'):
        return data['result'][0]['id']
    else:
        print(f'Failed to get record ID. Status code: {response.status_code}, Error: {response.text}')
        return None

def update_dns_record(email, api_key, zone_name, record_name, record_type, content, ttl):
    zone_id = get_zone_id(email, api_key, zone_name)
    if not zone_id:
        return

    record_id = get_record_id(email, api_key, zone_id, record_name)
    if not record_id:
        return

    url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{record_id}'

    headers = {
        'X-Auth-Email': email,
        'X-Auth-Key': api_key,
        'Content-Type': 'application/json',
    }

    data = {
        'type': record_type,
        'name': record_name,
        'content': content,
        'ttl': ttl,
    }

    response = requests.put(url, headers=headers, json=data)

    if response.status_code == 200:
        print('DNS record updated successfully.')
    else:
        print(f'Failed to update DNS record. Status code: {response.status_code}, Error: {response.text}')

# Replace these with your Cloudflare credentials and DNS record details
email = 'lzt1399@gmail.com'
api_key = 'f91863182686c1cab99d191dd75428d6298e9'
zone_name = 'hajistock.ir'
subdomain = 'xs'  # Replace with your subdomain
record_name = f'{subdomain}.{zone_name}'  # Full record name including subdomain
record_type = 'A'
content = '15.5.5.5'
ttl = 1

update_dns_record(email, api_key, zone_name, record_name, record_type, content, ttl)
