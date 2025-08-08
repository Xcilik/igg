import instaloader

# Inisialisasi
L = instaloader.Instaloader()

# Login (supaya bisa akses daftar following akun yang private / banyak datanya)
username = "farid_srydi"
password = "@Cilik423"
L.login(username, password)

# Username target yang mau diambil daftar following-nya
target_username = "nvntii_"

# Ambil profil target
profile = instaloader.Profile.from_username(L.context, target_username)

print(f"Daftar following {target_username}:")
for following in profile.get_followees():
    print(following.username)
