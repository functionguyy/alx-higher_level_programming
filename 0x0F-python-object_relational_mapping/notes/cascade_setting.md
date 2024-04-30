# Cascade behaviour setting for one-to-many relationship

Setting the `cascade` option of a`relationship()` construct to
`delete-orphan` is appropriate for related objects which only exit as long as they
are attached to their parents, and otherwise deleted

```python
class User(Base):
    # ...

    addresses = relationship("Address", cascade="all, delete-orphan")
```
The above indicates that 
- when the "parent"(User) object is marked for
deletion, its "child"(Address) objects should also be marked for deletion
- If the child object is deassociated from the parent object, it should be 
deleted  

For `relationship()`, `delete-orphan` cascade is normally configured only on
the "one" side of a one-to-many relationship, and not on the "many" side of a
many-to-one or many-to-many relationship.

```python
class A(Base):
    __tablename__ = "a"

    id = Column(Integer, primary_key=True)

    bs = relationship("B", back_ref="a", cascade="all, delete-orphan")


class B(Base):
    __tablename__ = "b"
    id = Column(Integer, primary_key=True)
    a_id = Column(ForeignKey("a.id"))

```
