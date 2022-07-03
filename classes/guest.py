class Guest:

    def __init__(self, name):
        self.name = name['name']
        self.memb_ship = name['membership']
        self.cash = name['cash']
            
    def check_you_can_add_guest(self):
        new_guest = self.name
        return new_guest
    
    def check_membership(self):
        membership = self.memb_ship
        if membership == True:
            return True
        else:
            return False

    def check_guest_can_enter_venue(self):
        free_pass = self.check_membership()
        money_enough = self.cash 
        if free_pass == True or money_enough >= 20:
            return True
        else:
            return False