import requests

def retrieveRecipe():
    request = requests.get("https://api.edamam.com/search?q=desert&appid=2fa1798f&app_key=300dd34142d127ca021b1779d7e4518e&from=0&to=3")
    json_file = request.json()
    json_file