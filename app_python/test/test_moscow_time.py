from datetime import datetime

import pytz

from app_python.moscow_time import app, moscow_time


def test_moscow_time():
    with app.app_context():
        tz = pytz.timezone('Europe/Moscow')
        now = datetime.now(tz)  # current date and time
        time = now.strftime("%H:%M:%S")

        assert moscow_time() == f'Current time in Moscow: { time }'
