import webbrowser
import time
import random

while True:
    sites = random.choice(['google.com/search?q=what+is+big+pp&sxsrf=ALeKk00um-wz7nsF1a0syoU7FB2rMTEBuQ%3A1618489527488&ei=tzB4YL-cHcGWjgb4v5DgCA&oq=what+is+big+pp&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEMsBMgUIABDLATIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB46BwgAEEcQsAM6BwgAELADEEM6BAgjECc6BAgAEEM6AggAOgUIABDJAzoFCC4QsQNQvCtYwjpgmT1oAnACeAOAAasDiAHmEJIBCTMuMy4xLjEuMpgBAKABAaoBB2d3cy13aXrIAQrAAQE&sclient=gws-wiz&ved=0ahUKEwj_0-6qn4DwAhVBi8MKHfgfBIwQ4dUDCA4&uact=5', 'youtube.com/watch?v=JXAyEUkfWoE', 'y8.com/games/bad_ice_cream_3','www.youtube.com/watch?v=dQw4w9WgXcQ'])
    visit = "http://{}".format(sites)
    webbrowser.open(visit)
    seconds = random.randrange(5, 20)
    time.sleep(seconds)