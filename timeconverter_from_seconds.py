import math

class TimeConverter:
    def __init__(self, seconds):
        self.seconds = seconds
    
    def convert_to_hours(self):        
        return math.floor(self.seconds / 3600)
    
    def convert_to_minutes(self):
        if self.convert_to_hours() >= 1:
            return math.floor((self.seconds - self.convert_to_hours() * 3600) / 60)
        return self.seconds / 60
    
    def convert_to_seconds(self):
        return (self.seconds - self.convert_to_hours() * 3600 - self.convert_to_minutes() * 60)
    
time_obj = TimeConverter(5432)
print(time_obj.convert_to_hours())
print(time_obj.convert_to_minutes())
print(time_obj.convert_to_seconds())