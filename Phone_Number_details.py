import phonenumbers
from phonenumbers import timezone,geocoder,carrier

User_Number = input("Enter the number to check details: (start with '+__'): ")

def Number():
    Number_detail = phonenumbers.parse(User_Number)
    return Number_detail    


def Number_details():

    Time_zone = timezone.time_zones_for_number(Number())
    carr = carrier.name_for_number(Number(), "en")
    registartion = geocoder.description_for_number(Number(), "en")

    print("\n*********Number Details*******\n")
    print(Number(),"\n")
    print("Time Zone: ",Time_zone)
    print("SIM: ",carr)
    print("registration: ",registartion,"\n\n")


if __name__ == "__main__":
    Number_details()