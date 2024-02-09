import datetime



class Date:

    def __init__(self, day, month, year):

        self.day = day
        self.month = month
        self.year = year

    
    def __lt__(self, other):
        if self.year < other.year:
            return True
        elif self.year == other.year and self.month < other.month:
            return True
        elif self.year == other.year and self.month == other.month and self.day < other.day:
            return True
        else:
            return False
        
    
    def __add__(self, days):
        # current_date = datetime(self.year, self.month, self.day)
        new_date = self.day + datetime.timedelta(days=days)
        return Date(new_date.day, new_date.month, new_date.year)






d1 = Date(14,12,2023)
d2 = Date(14,12,2007)


print(d1 + 40)
print(d1 < d2)



