from sqlalchemy import Column, Integer, String, DateTime, Time, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType, PasswordType, EmailType
import uuid
from database import Base


available = Table(
    "available",
    Base.metadata,
    Column("store_id", UUIDType(binary=False), ForeignKey("store.store_id"), primary_key=True),
    Column("item_id", UUIDType(binary=False), ForeignKey("item.item_id"), primary_key=True),
)

item_to_allergy = Table(
    "item_to_allergy",
    Base.metadata,
    Column("item_id", UUIDType(binary=False), ForeignKey("item.item_id"), primary_key=True),
    Column("allergy_id", Integer, ForeignKey("allergy.allergy_id"), primary_key=True),
)

customer_to_allergy = Table(
    "customer_to_allergy",
    Base.metadata,
    Column("customer_id", UUIDType(binary=False), ForeignKey("customer.customer_id"), primary_key=True),
    Column("allergy_id", Integer, ForeignKey("allergy.allergy_id"), primary_key=True),
)



class Organization(Base):
    __tablename__ = "organization"

    organization_id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    name = Column(String(256), nullable=False)
    email = Column(EmailType, nullable=False, unique=True)
    password = Column(PasswordType(schemes=["pbkdf2_sha512", "md5_crypt"], deprecated=["md5_crypt"]), nullable=False)

    stores = relationship("Store", back_populates="organization")
    items = relationship("Item", back_populates="organization")

class Store(Base):
    __tablename__ = "store"

    store_id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    organization_id = Column(UUIDType(binary=False), ForeignKey("organization.organization_id"), nullable=False)
    name = Column(String(256), nullable=False)
    email = Column(EmailType, nullable=False, unique=True)
    password = Column(PasswordType(schemes=["pbkdf2_sha512", "md5_crypt"], deprecated=["md5_crypt"]), nullable=False)
    address = Column(String(256), nullable=False)
    latitude = Column(String(11), nullable=False)
    longitude = Column(String(11), nullable=False)
    open_time = Column(Time, nullable=False)
    close_time = Column(Time, nullable=False)

    organization = relationship("Organization", back_populates="stores")
    items = relationship("Item", secondary=available, back_populates="store")

class Item(Base):
    __tablename__ = "item"

    item_id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    name = Column(String(256), nullable=False)
    organization_id = Column(UUIDType(binary=False), ForeignKey("organization.organization_id"), nullable=False)
    size = Column(String(256), nullable=True)
    price = Column(Integer, nullable=False)
    description = Column(String(256), nullable=True)

    organization = relationship("Organization", back_populates="items")
    order_details = relationship("OrderDetail", back_populates="item")
    store = relationship("Store", secondary=available, back_populates="items")
    allergy = relationship("Allergy", secondary=item_to_allergy, back_populates="item")

class Customer(Base):
    __tablename__ = "customer"

    customer_id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    name = Column(String(256), nullable=False)
    email = Column(EmailType, nullable=False, unique=True)
    password = Column(PasswordType(schemes=["pbkdf2_sha512", "md5_crypt"], deprecated=["md5_crypt"]), nullable=False)
    points = Column(Integer, nullable=False)

    orders = relationship("Order", back_populates="customer")
    point_history = relationship("PointHistory", back_populates="customer")
    allergy = relationship("Allergy", secondary=customer_to_allergy, back_populates="customer")

class Order(Base):
    __tablename__ = "order"

    order_id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    customer_id = Column(UUIDType(binary=False), ForeignKey("customer.customer_id"), nullable=False)

    customer = relationship("Customer", back_populates="orders")
    payment = relationship("Payment", back_populates="order", uselist=False)
    order_details = relationship("OrderDetail", back_populates="order")

class OrderDetail(Base):
    __tablename__ = "order_detail"

    order_detail_id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    order_id = Column(UUIDType(binary=False), ForeignKey("order.order_id"), nullable=False)
    item_id = Column(UUIDType(binary=False), ForeignKey("item.item_id"), nullable=False)
    number_of_purchase = Column(Integer, nullable=False)

    order = relationship("Order", back_populates="order_details")
    item = relationship("Item", back_populates="order_details")

class Payment(Base):
    __tablename__ = "payment"

    payment_id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    order_id = Column(UUIDType(binary=False), ForeignKey("order.order_id"), nullable=False)
    total = Column(Integer, nullable=False)
    status = Column(Integer, nullable=False) # todo
    timestamp = Column(DateTime, nullable=False)

    order = relationship("Order", back_populates="payment", uselist=False)

class PointHistory(Base):
    __tablename__ = "point_history"

    point_history_id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    customer_id = Column(UUIDType(binary=False), ForeignKey("customer.customer_id"), nullable=False)
    charge = Column(Integer, nullable=False)
    timestamp = Column(DateTime, nullable=False)

    customer = relationship("Customer", back_populates="point_history")

class Allergy(Base):
    __tablename__ = "allergy"

    allergy_id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)

    item = relationship("Item", secondary=item_to_allergy, back_populates="allergy")
    customer = relationship("Customer", secondary=customer_to_allergy, back_populates="allergy")

class Session(Base):
    __tablename__ = "session"

    session_id = Column(String(128), primary_key=True)
    user_id = Column(UUIDType(binary=False), nullable=False)
    user_type = Column(Integer, nullable=False) # 1: customer 2: org 3: store