import datetime

class User:
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday

        name_split = full_name.split(' ')
        self.first_name = name_split[0]
        self.last_name = name_split[-1]

    def age(self):
        today = datetime.date(2020, 3, 18)

        years = int(self.birthday[0:4])
        months = int(self.birthday[4:6])
        days = int(self.birthday[6:8])

        birth_data = datetime.date(years, months, days)
        how_old_in_days = (today - birth_data).days
        how_old_in_years = how_old_in_days / 365

        return int(how_old_in_years)
        

user = User('shang ruyan', '20010503')

print(user.first_name, user.last_name)
print(user.birthday)
print(user.age())