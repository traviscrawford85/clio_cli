from sqlalchemy import Column, Float, Integer, String

from .db import Base


class ClioToken(Base):
    __tablename__ = "clio_tokens"

    id = Column(Integer, primary_key=True, index=True)
    clio_user_id = Column(String, unique=True, index=True)
    access_token = Column(String)
    refresh_token = Column(String)
    expires_at = Column(Float)
    client_id = Column(String)
    client_secret = Column(String)
