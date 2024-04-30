## declarative_base()

`declarative_base()` sets a default constructor on its subclasses which enables
them to take keyword arguments, and assigns them to the named attributes in the
subclass. 

So take for instance you have a class `User()` that inherits from a declarative
base class:
```python
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# create instance of declarative base class
Base = declarative_base()

# declare a class user
class User(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	fullname = Column(String)
	nickname = Column(String)
```

As `User()` is declared as a subclass of `base_declarative()`, a default
constructor has been set in `User()` that allows it to take keyword arguments
and assign to its named attributes(name, fullname, nickname)
```python
# create an instance of User()
ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
```
