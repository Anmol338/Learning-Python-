class Information:

    def __init__(self, name, location):
        self.name = name
        self.location = location


    def __str__(self):
        return f"{self.name} lives in {self.location}"

info = Information("Ram", "Kathmandu")
info2 = Information("Shyam", "Lalitpur")

print(info)
info.location="Kavre"
print(info)