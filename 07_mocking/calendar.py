from datetime import datetime
from unittest.mock import Mock


tuesday = datetime(2019, 1, 1)
saturday = datetime(2019, 1, 5)
datetime = Mock()
print(dir(datetime))


def is_weekday():
    today = datetime.today()
    day_of_the_week = today.weekday()
    return 0 <= day_of_the_week < 5


datetime.today.return_value = saturday
assert is_weekday(), "Today is not weekday"
