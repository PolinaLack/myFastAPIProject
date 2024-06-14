from models.holiday import Holiday_base
from models.user import User

users_table: dict[str, User] = {
    "User1": User(name="User1", holis_ids=[1, 3]), 
    "User2": User(name="User2", holis_ids=[]),
    "User3": User(name="User3", holis_ids=[2]),
}

holis_table: dict[int, Holiday_base] = {
    1: Holiday_base(**{
        "user_name": "User1",
        "start": "01.01.2022",
        "end_date": "02.01.2022",
    }),
    2: Holiday_base(**{
        "user_name": "User3",
        "start": "01.03.2022",
        "end_date": "02.03.2022",
    }),
    3: Holiday_base(**{
        "user_name": "User1",
        "start": "07.03.2022",
        "end_date": "09.03.2022",
    }),
}

# calendar: dict[str, int] = {
#     "01.01.2022": 1,
#     "02.01.2022": 1,
#     "01.03.2022": 1,
#     "02.03.2022": 1,    
# }
