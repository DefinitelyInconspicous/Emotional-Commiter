import random
import requests

API_KEY = "0ada710641715dc14c1be04c6b615fa7"
CITY = input("Which CITY are you in?\n")

emotions = [
    "existential", "melancholic", "deliriously calm", "whimsically hollow",
    "moderately unbothered", "slightly panicked", "hyper-aware", "cautiously optimistic",
    "spiritually offline", "ambiguously anxious", "ironically motivated",
    "functionally confused", "cryptically inspired", "emotionally deprecated",
    "soft-crashed", "mentally paginated", "debugging my soul", "compiling feelings",
    "accidentally confident", "tragically hopeful", "quietly combusting",
    "philosophically drained", "bravely exhausted", "digitally burnt-out",
    "chaotically aligned", "reluctantly productive", "mentally forked",
    "half-documented", "temporarily zen", "sarcastically efficient",
    "overclocked and undercaffeinated", "mood: rubber ducking myself",
    "partially present", "autocompleted my emotions", "commented out of reality",
    "awkwardly optimistic", "recursively sad", "emotionally hard-reset",
    "deprecated but still running", "feeling semicolon-dependent", "buffering in 140p"
]


verbs = [
    "Fixed bug", "Refactored method", "Updated docs", "Improved logic",
    "Tweaked UI", "Deleted something important", "Renamed a file again",
    "Wrote code caffeinated", "Undid the undo", "Hotfixed the hotfix",
    "Added temporary fix (permanent)", "Blamed the internet", "Added TODOs (ignored them)",
    "Implemented... something", "Sacrificed code to the python gods",
    "Tried something weird", "Deleted half the project", "Git push and prayed",
    "Fixed merge conflict with past self", "Left NO comments whatsoever",
    "Debugged with print statements", "Forgot what I was doing",
    "Blamed previous developer (it was me)", "Wrote feature, broke 3 others",
    "Added logs, forgot to remove them", "Fixed one bug, created two more",
    "Disabled test, problem solved", "StackOverflowed entire solution",
    "Wrote code that should work", "Code now compiles. Probably.",
    "Added a workaround to the workaround", "Turned it off and on again",
    "Confirmed bug is real", "Moved code around for no reason",
    "Improvised, adapted, overcame", "Commented out critical line",
    "Accidentally genius", "Why am I awake", "Vibecoded",
    "Yelled at computer", "Blamed Pip", "Made things worse",
    "Sacrificed performance for elegance", "Forgot semicolon;",
    "Implemented dark magic", "It works, don’t touch", "Switched tabs and lost track",
    "Pushed to production by mistake", "Wrote code during meeting",
    "Commit message placeholder", "Prayed to Linus Torvalds", "Crashed my Xcode"
]


def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        res = requests.get(url)
        data = res.json()
        description = data["weather"][0]["description"]
        return description
    except:
        return "whatever weather you see outside your Non-Existent window."

def generate_commit():
    mood = random.choice(emotions)
    verb = random.choice(verbs)
    weather = get_weather(CITY)
    return f'{verb} while feeling {mood} during {weather}.'


message = generate_commit()
print(f'git commit -m "{message}"')