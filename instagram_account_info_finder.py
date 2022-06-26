import instaloader

# Created an instance of the Instaloader class
bot = instaloader.Instaloader()

# Load a profile from instagram handle
profile_name = input("Enter the user name: ")
profile = instaloader.Profile.from_username(bot.context, profile_name)

print("\nUsername: ", profile.username)

print("User ID: ", profile.userid)

print("Post count: ", profile.mediacount)

print("Bio: ", profile.biography)

print("Profile pic URL: ", profile.profile_pic_url)
