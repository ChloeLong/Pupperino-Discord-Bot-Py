class Special:
    def __init__(self, title=None, original_price=None, sale_price=None, header_image=None, store_link=None):
        self.title = title
        self.original_price = original_price
        self.sale_price = sale_price
        self.header_image = header_image
        self.store_link = store_link
    
    def get_title(self):
        return self.title
    
    def set_title(self, title):
        self.title = title
    
    def get_original_price(self):
        return self.original_price
    
    def set_original_price(self, original_price):
        self.original_price = original_price
    
    def get_sale_price(self):
        return self.sale_price
    
    def set_sale_price(self, sale_price):
        self.sale_price = sale_price
    
    def get_header_image(self):
        return self.header_image
    
    def set_header_image(self, header_image):
        self.header_image = header_image

    def get_store_link(self):
        return self.store_link
    
    def set_header_image(self, store_link):
        self.store_link = store_link