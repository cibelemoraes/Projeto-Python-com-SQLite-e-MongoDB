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
inspetor_engine = inspect(engine)
print(inspetor_engine.has_table("user_account"))
print(inspetor_engine.get_table_names())
print(inspetor_engine.default_schema_name)


#inserindo dados no banco de dados
with Session(engine) as session:
    juliana = User(
        name = 'Juliana',
        fullname= 'Juliana Mascarenhas',
        address=[Address(email_address='julianam"email.com')]
        
    )
    
    sandy = User(
        name = 'Sandy',
        fullname= 'Sandy Cardoso',
        address=[Address(email_address='sandyam"email.com'),
                 Address(email_address='sandyc@email.org')]
    )
    
    patrick = User (name='patrick', fullname='Patrick Cardoso')
    
    
    #enviandopara o BD (persistência de dados)
    session.add_all([juliana, sandy, patrick])
    
    session.commit()
    
    stmt = select(User).where(User.name.in_(["juliana", 'sandy']))
    print('Recuperando usuários a partir de condições de filtragem')
    for user in session.scalars(stmt):
        print(user)
        
    stmt_address = select(Address).where(Address.user_id.in_([2]))
    print('\nRecuperando os endereços de email de Sandy')
    for address in session.scallars(stmt_address):
        print(address)
        
    stmt_order = select(User).order_by(User.fullname.desc())
    print("\nRecuperando info de maneira ordenada")
    for result in session.scalars(stmt_order):
        print(result)
        
    stmt_join = select(User.fullname, Address.email_address).join_from(Address, User)
    print("\n")
    for result in session.scalars(stmt_join):
        print(result)
        
    #print(select(User.fullname, Address.email_address).join_from(Address, User))
    
    connection = engine.connect()
    result = connection.execute(stmt_join).fetchall()
    print("\nExecutando statement a partirda connection")
    for result in results:
        print(result)
        
    stmt_count = select(func.count('*')).select_from(User)
    print('\nTotal de instâncias em User')
    for result in session.scalars(stmt_count):
        print(result)
        
        
    # encerrando de fato a session
    session.closed()
    
    