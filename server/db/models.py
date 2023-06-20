import datetime
import uuid
from sqlalchemy import UUID, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from db.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    isy = Column(Integer, nullable=False, unique=True)
    full_name = Column(String, nullable=False, unique=False)
    permissions = Column(String, nullable=True, unique=False)
    education = Column(String, nullable=False, unique=False)
    graduate = Column(String, nullable=True, unique=False)
    role_id = Column(Integer, ForeignKey("roles.id"))
    publications = relationship("Publication", backref="user")


class Publication(Base):
    __tablename__ = "publications"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.isy"))
    type_ = Column(String, nullable=False, unique=False)
    data = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())


class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    number_of_theme = Column(Integer, nullable=False, unique=True)
    type_ = Column(String, nullable=False)
    title = Column(String(255), nullable=False)
    key_words = Column(String, nullable=True, unique=False)
    register_card = Column(String, nullable=True, unique=False)
    customer = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    end_at = Column(DateTime)
    role_id = Column(Integer, ForeignKey("roles.id"))
    user_id = Column(Integer, ForeignKey("users.isy"))
    division = Column(Integer, ForeignKey("divisions.cvc"))


class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    rang = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    user_id = Column(Integer, ForeignKey("users.isy"))
    role_id = Column(Integer, ForeignKey("roles.id"))
    type_category = Column(String, ForeignKey("categories.event_category"))


class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey("users.isy"))
    users = relationship("User", backref="role")


class Division(Base):
    __tablename__ = "divisions"
    id = Column(Integer, primary_key=True)
    cvc = Column(Integer, nullable=False, unique=True)
    title = Column(String(255), nullable=False)
    divisions = relationship("Division", backref="division")


class EventCategory(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    event_category = Column(String, nullable=False, unique=True)
    be_something = Column(String(255), nullable=False)
    categories = relationship("EventCategory", backref="category")
