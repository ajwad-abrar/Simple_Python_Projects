import instaloader

# Created an instance of the Instaloader class
instagram = instaloader.Instaloader()

instagram_profile_name = input("Enter username: ")

instagram.download_profile(instagram_profile_name, profile_pic_only=False)
