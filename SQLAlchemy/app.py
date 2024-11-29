from models import Address,User
from database import session
from database import Base,engine

Base.metadata.create_all(engine)

user1 = User(name='John Doe',age=52)
user2 = User(name='Jane Smith',age=34)

address1 = Address(city='New York',state='NY',zip_code='1001')
address2 = Address(city='Los Angeles',state='CA',zip_code='90001')
address3 = Address(city='Chicago',state='IL',zip_code='60601')

user1.addresses.extend([address1,address2])
user2.addresses.append(address3)

session.add(user1)
session.add(user2)
session.commit()

print(f'{user1.addresses}')
print(f'{user2.addresses}')
print(f'{address1.user}')
