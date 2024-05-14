"""
    Meu Primeiro progama de integração com banco de dados
    utilizando SQLAlchemy e modelo ORM
    """
    
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import select
from sqlalchemy import func
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey


Base = declarative_base()

class User(Base):
    __tablename__ = "user_account"
    #atributos
    id = Column(Integer, primary_Key=True)
    name = Column(String)
    fullname = Column(String)
    
    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orpham"
    )

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname})"
    
class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)
    
    user = relationship("user", back_populates="address")
    
    def __repr__(self):
        return f"Address(id={self.id}, email_address={self.email_address})"
    
    
print(User.__tablename__)
print(Address.__tablename__)

# conexão com banco de dados
engine = create_engine("sqlite://")

#criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)

#depreciado -  será removido em futuro release
# print(engine.table_name())

#investigando o esquema de banco de dados 
