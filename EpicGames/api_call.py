from EpicGames.map import Map
import requests

class API_Call:
    def callEpicAPI():
        game_deals = [[],[]]
        
        url = 'https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=en-US&country=US&allowCountries=US'
        r = requests.get(url)
        data = r.json()

        for item in data['data']['Catalog']['searchStore']['elements']:
            if item['offerType'] == 'BASE_GAME':
                if item['price']['totalPrice']['originalPrice'] == item['price']['totalPrice']['discountPrice'] or item['price']['totalPrice']['originalPrice'] == item['price']['totalPrice']['discount']:
                    if len(item['promotions']['promotionalOffers']) == 0:
                        game_deals[1].append(Map.makeObjectsUpcoming(item))
                    else:
                        game_deals[0].append(Map.makeObjectsCurrent(item))
        
        return game_deals