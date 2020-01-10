class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0

    def describe_restaurant(self):
        print("The restaurant name is "+self.restaurant_name)
        print(self.restaurant_name+" supply "+self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name+" is open")

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=['orange','watermelon','apple','pear']

    def show_icecream_type(self):
        print(self.restaurant_name+"supply "+self.flavors[0]+" ice cream")
        print(self.restaurant_name + "supply " + self.flavors[1] + " ice cream")
        print(self.restaurant_name + "supply " + self.flavors[2] + " ice cream")
        print(self.restaurant_name + "supply " + self.flavors[3] + " ice cream")

icecreamstand=IceCreamStand('summer cool','ice cream')
icecreamstand.show_icecream_type()