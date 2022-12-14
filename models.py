from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey

from database import Base


class CommonUser(Base):
    __tablename__ = "commonuser"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    student_id = Column(String, nullable=True)
    permission = Column(Integer, nullable=False)
    otp_key = Column(String, nullable=True)
    create_date = Column(DateTime, nullable=False)


class Booth(Base):
    __tablename__ = "booth"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    mapx = Column(String, nullable=True)
    mapy = Column(String, nullable=True)


class AdminUser(Base):
    __tablename__ = "adminuser"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    permission = Column(Integer, nullable=False)
    booth_id = Column(Integer, ForeignKey("booth.id"), nullable=True)


class Visit(Base):
    __tablename__ = "visit"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("commonuser.id"))
    booth_id = Column(Integer, ForeignKey("booth.id"))
    start_time = Column(DateTime, nullable=True)
    end_time = Column(DateTime, nullable=True)
