# Local Code Imports
from EpicGames.game import Game

# Outside Packages
from datetime import datetime
import requests

class Epic_API_Call:
    def callEpicAPI():
        game_deals = [[],[]]
        
        # Calls the Epic store API and stores the raw data.
        url = 'https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=en-US&country=US&allowCountries=US'
        r = requests.get(url)
        data = r.json()

        # Fills the game_deals list, it is split into 2 dimensions to store upcoming and current so they can be displayed in order.
        for item in data['data']['Catalog']['searchStore']['elements']:
            if item['offerType'] == 'BASE_GAME':
                if item['price']['totalPrice']['originalPrice'] == item['price']['totalPrice']['discountPrice'] or item['price']['totalPrice']['originalPrice'] == item['price']['totalPrice']['discount']:
                    if len(item['promotions']['promotionalOffers']) == 0:
                        game_deals[1].append(Epic_API_Call.makeObjectsUpcoming(item))
                    else:
                        game_deals[0].append(Epic_API_Call.makeObjectsCurrent(item))
        
        return game_deals
    
    # This function converts the raw API dates/times into UTC >> Epoch format, this is needed to make use of Discord's timestamp markup.
    def convertDate(dateStr):
        date_format = "%Y-%m-%dT%H:%M:%S.%fZ"
        return int(datetime.strptime(dateStr, date_format).timestamp())

    # Using the Game class it creates objects for each free game and maps the data returned from the API
    def makeObjectsCurrent(item):
        newGame = Game()
        newGame.title = item['title']
        newGame.desc = item['description']
        newGame.price = "${:.2f}".format(item['price']['totalPrice']['originalPrice'] / 100)
        newGame.startTime = Epic_API_Call.convertDate(item['promotions']['promotionalOffers'][0]['promotionalOffers'][0]['startDate'])
        newGame.endTime = Epic_API_Call.convertDate(item['promotions']['promotionalOffers'][0]['promotionalOffers'][0]['endDate'])
        newGame.image_url = item['keyImages'][0]['url']
        newGame.status = 'Current'

        return newGame

    # Additional function is because the raw data for the date information is different.
    def makeObjectsUpcoming(item):
        newGame = Game()
        newGame.title = item['title']
        newGame.desc = item['description']
        newGame.price = "${:.2f}".format(item['price']['totalPrice']['originalPrice'] / 100)
        newGame.startTime = Epic_API_Call.convertDate(item['promotions']['upcomingPromotionalOffers'][0]['promotionalOffers'][0]['startDate'])
        newGame.endTime = Epic_API_Call.convertDate(item['promotions']['upcomingPromotionalOffers'][0]['promotionalOffers'][0]['endDate'])
        newGame.image_url = item['keyImages'][0]['url']
        newGame.status = 'Upcoming'
        
        return newGame