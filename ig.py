import instaloader

# Inisialisasi tanpa login
L = instaloader.Instaloader()

# Username target (akun publik)
target_username = "nvntii_"

# Ambil profil target
profile = instaloader.Profile.from_username(L.context, target_username)

print(f"Daftar following {target_username}:")
for following in profile.get_followees():
    print(following.username)
