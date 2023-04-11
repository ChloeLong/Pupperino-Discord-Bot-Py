class Game:
    def __init__(self, title=None, desc=None, price=None, startTime=None, endTime=None, image_url=None):
        self.title = title
        self.desc = desc
        self.price = price
        self.startTime = startTime
        self.endTime = endTime
        self.image_url = image_url
        
    # Getter methods
    def get_title(self):
        return self.title
    
    def get_desc(self):
        return self.desc
    
    def get_price(self):
        return self.price
    
    def get_startTime(self):
        return self.startTime
    
    def get_endTime(self):
        return self.endTime
    
    def get_image_url(self):
        return self.image_url
    
    # Setter methods
    def set_title(self, title):
        self.title = title
    
    def set_desc(self, desc):
        self.desc = desc
    
    def set_price(self, price):
        self.price = price
    
    def set_startTime(self, startTime):
        self.startTime = startTime
    
    def set_endTime(self, endTime):
        self.endTime = endTime

    def set_image_url(self, image_url):
        self.image_url = image_url