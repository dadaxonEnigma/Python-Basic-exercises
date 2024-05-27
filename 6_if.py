india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

user_city = input('City: ').lower()
if user_city in india:
    print(f'Your city {user_city} located in india')
if user_city in pakistan:
    print(f'Your city {user_city} located in pakistan')
if user_city in bangladesh:
    print(f'Your city {user_city} located in bangladesh')
    