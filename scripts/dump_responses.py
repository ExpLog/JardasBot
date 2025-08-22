# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pandas",
# ]
# ///
import sqlite3

from database.DBhelpers import db_select_all
from responses import (
    BomDia,
    Cheats,
    Custom,
    DarkJokes,
    event_reminders,
Fortunes,
Friendly,
Generic,
Huggies,
Mentions,
Nuke,
Offerings,
Piropos,
Roasting,
ShowerThoughts,
Thanks,
Warning,
Wronged,
)
import pandas as pd

RESPONSES = {
    "good_morning": BomDia.arr_wake,
    "cheats": Cheats.arr_cheats,
    "communism": Custom.arr_communism,
    "euskara": Custom.arr_euskara,
    "french": Custom.arr_french,
    "german": Custom.arr_german,
    "japanese": Custom.arr_japanese,
    "latin": Custom.arr_latin,
    "girl_power": Custom.arr_girlpower,
    "scam": Custom.arr_scam,
    "dark_joke": DarkJokes.arr_darkjokes,
    "event_reminder": event_reminders.PHRASES,
    "fortune_cookie": Fortunes.arr_fortune,
    "friendly": Friendly.arr_friendly,
    "generic_often": Generic.arr_high,
    "generic_sometimes": Generic.arr_medium,
    "generic_seldom": Generic.arr_low,
    "hug": Huggies.arr_huggies,
    "mention": Mentions.arr_mention,
    "nuke": Nuke.arr_nuke,
    "vocabulary_added": Offerings.arr_offerings,
    "catcall": Piropos.arr_piropo,
    "roast": Roasting.arr_roast,
    "shower_thought": ShowerThoughts.arr_shower,
    "thanks": Thanks.arr_thanks,
    "warning": Warning.arr_warn,
    "wronged": Wronged.arr_wronged
}


def load_user_added_responses() -> list[str]:
    conn = sqlite3.connect("wordstats.db")
    with conn:
        cursor = conn.cursor()
        cursor.execute("SELECT vocabulary FROM vocabulary_table")
        data = cursor.fetchall()
    conn.close()
    return [d[0] for d in data]


def main():
    data = []
    for message_group, group_responses in RESPONSES.items():
        for text in group_responses:
            record = {"message_group": message_group, "text": text}
            data.append(record)

    for text in load_user_added_responses():
        record = {"message_group": "legacy_user_added", "text": text}
        data.append(record)

    df = pd.DataFrame.from_records(data)
    df.to_csv("responses.csv", index=False)


if __name__ == '__main__':
    main()
