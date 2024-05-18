from models import Holidays_base, User

users: dict[str, User] = {
    "User1": User(name="User1", holidays_id=[1]), 
    "User2": User(name="User2", holidays_id=[]),
    "User3": User(name="User3", holidays_id=[2]),
}


holidays_all: dict[int, Holidays_base] = {
    1: Holidays_base(**{
        "user_name": "User1",
        "start": "01.01.2022",
        "end": "02.01.2022",
    }),
    2: Holidays_base(**{
        "user_name": "User3",
        "start": "01.03.2022",
        "end": "02.03.2022",
    }),
}


calendar: dict[str, int] = {
    "01.01.2022": 1,
    "02.01.2022": 1,
    "01.03.2022": 1,
    "02.03.2022": 1,    
}
