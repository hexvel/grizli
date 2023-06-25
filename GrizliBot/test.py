from DB.BaseRequests.BaseRequests import Base


db = Base()

a = db.all_base({"a": 1})
print(a)