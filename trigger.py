"""Orchestration script responsible for triggering script.py once a day """
import time
import json
import schedule
import script

with open("config.json", 'r', encoding="utf8") as f:
    config = json.loads(f.read())

def job():
    """Runs script.py"""
    script.main()

schedule.every().day.at(config["ScheduleTime"]).do(job)

while True:
    schedule.run_pending()
    time.sleep(60)
