import time
from datetime import datetime as dt


host_path = r"C:\Windows\System32\drivers\etc\hosts"  

redirect = "127.0.0.1"  # Localhost IP

# List of websites to block
blocked_websites = [
    "www.facebook.com",
    "facebook.com",
    "www.twitter.com",
    "twitter.com",

]

def block_websites(start_hour, end_hour):
    while True:
        if dt(dt.now().year, dt.now().month, dt.now().day, start_hour) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, end_hour):
            print("Working hours...")
            with open(host_path, "r+") as file:
                content = file.read()
                for site in blocked_websites:
                    if site in content:
                        pass
                    else:
                        file.write(redirect + " " + site + "\n")
        else:
            print("Fun hours...")
            with open(host_path, "r+") as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not any(site in line for site in blocked_websites):
                        file.write(line)
                file.truncate()
        time.sleep(5)  # Check every 5 seconds


start_hour = 8 
end_hour = 17  


block_websites(start_hour, end_hour)
