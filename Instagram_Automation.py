from instabot import Bot
bot = Bot()

username = input("Enter Your username for LOGIN : ")
passwd = input("Enter your password for LOGIN : ")

bot.login(username=username,  password=passwd)

def Follow_and_unfollow():
    while True:
        check = input("Do you want to follow or unfollow a person? (follow/unfollow): ").lower()
        if check == "follow":
            user_name = input("Enter a username to follow: ")
            bot.follow(user_name)
            break
        elif check == "unfollow":
            user_name = input("Enter a username to unfollow: ")
            bot.unfollow(user_name)
            break
        else:
             print("Please enter either 'follow' or 'unfollow'")

           
def Upload_picture_vedio_story():
    while True:
        check = input("what you want to upload picture(P) Story(S) Vedio(V): ").lower()

        if check == "p":
            path = input("Enter a path : ")
            caption = input("Enter a caption: ")
            bot.upload_photo(path,caption=caption)
            break

        elif check == "v":
            path = input("Enter a path : ")
            caption = input("Enter a caption: ")
            bot.upload_video(path,caption=caption)
            break

        elif check == "s":
            path = input("Enter a path : ")
            caption = input("Enter a caption: ")
            bot.upload_story_photo(path)
            break

        else:
             print("Make sure you type (p/s/v)")

def Send_message():
    user_id = input("Enter a id you want to send a message: ")
    msg =  input("Enter a msg: ")
    bot.send_message(msg, user_ids=user_id) #you can add many id in usin python list



def Retrieving_profile_information():
    user_name = input("Enter a username for checking account information: ")
    user_info = bot.get_user_info(user_name)
    
    if user_info is not None:
        print("User Information:")
        for key, value in user_info.items():
            print(f"{key}: {value}")
    else:
        print("User information not found or error occurred.")


if __name__ == "__main__":
    Send_message()
    Retrieving_profile_information()