import requests
import re
import json

def get_following(user):
    url = f"https://www.instagram.com/{user}/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    # Ambil HTML profil
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        print("Gagal mengambil data. Status:", r.status_code)
        return []

    # Cari JSON embedded di halaman
    shared_data_match = re.search(r"window\._sharedData = (.*?);</script>", r.text)
    if not shared_data_match:
        print("Gagal menemukan data JSON di HTML.")
        return []

    data = json.loads(shared_data_match.group(1))

    # Ambil user ID target
    try:
        user_id = data["entry_data"]["ProfilePage"][0]["graphql"]["user"]["id"]
    except KeyError:
        print("Tidak bisa menemukan user ID.")
        return []

    # Endpoint GraphQL untuk ambil following
    query_hash = "d04b0a864b4b54837c0d870b0e77e076"  # untuk following
    variables = {"id": user_id, "include_reel": True, "fetch_mutual": False, "first": 50}

    api_url = f"https://www.instagram.com/graphql/query/?query_hash={query_hash}&variables={json.dumps(variables)}"
    res = requests.get(api_url, headers=headers)
    if res.status_code != 200:
        print("Gagal mengambil daftar following.")
        return []

    following_data = res.json()["data"]["user"]["edge_follow"]["edges"]
    usernames = [edge["node"]["username"] for edge in following_data]
    return usernames


# Contoh penggunaan
target = "nvntii_"  # akun publik
following_list = get_following(target)

print(f"Following {target}:")
for u in following_list:
    print("-", u)
