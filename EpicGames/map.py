from EpicGames.game import Game
from datetime import datetime

class Map:
    def convertDate(dateStr):
        date_format = "%Y-%m-%dT%H:%M:%S.%fZ"
        return int(datetime.strptime(dateStr, date_format).timestamp())

    def makeObjectsCurrent(item):
        newGame = Game()
        newGame.title = item['title']
        newGame.desc = item['description']
        newGame.price = "${:.2f}".format(item['price']['totalPrice']['originalPrice'] / 100)
        newGame.startTime = Map.convertDate(item['promotions']['promotionalOffers'][0]['promotionalOffers'][0]['startDate'])
        newGame.endTime = Map.convertDate(item['promotions']['promotionalOffers'][0]['promotionalOffers'][0]['endDate'])
        newGame.image_url = item['keyImages'][0]['url']

        return newGame

    def makeObjectsUpcoming(item):
        newGame = Game()
        newGame.title = item['title']
        newGame.desc = item['description']
        newGame.price = "${:.2f}".format(item['price']['totalPrice']['originalPrice'] / 100)
        newGame.startTime = Map.convertDate(item['promotions']['upcomingPromotionalOffers'][0]['promotionalOffers'][0]['startDate'])
        newGame.endTime = Map.convertDate(item['promotions']['upcomingPromotionalOffers'][0]['promotionalOffers'][0]['endDate'])
        newGame.image_url = item['keyImages'][0]['url']
        
        return newGame
    
