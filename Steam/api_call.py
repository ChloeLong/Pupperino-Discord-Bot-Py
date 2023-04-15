from Steam.special import Special
from datetime import datetime
import requests

class Steam_API_Call:
    def callSteamAPI():
        steam_game_deals = []
        
        url = 'https://store.steampowered.com/api/featuredcategories'
        r = requests.get(url)
        data = r.json()

        for item in data['specials']['items']:
            steam_game_deals.append(Steam_API_Call.makeObjectsSpecial(item))
            
        return steam_game_deals
    

    def makeObjectsSpecial(item):
        newSpecial = Special()
        newSpecial.title = item['name']
        newSpecial.original_price = "${:.2f}".format(item['original_price'] / 100)
        newSpecial.sale_price = "${:.2f}".format(item['final_price'] / 100)
        newSpecial.header_image = item['header_image']
        newSpecial.store_link = f"https://store.steampowered.com/app/{item['id']}"

        return newSpecial