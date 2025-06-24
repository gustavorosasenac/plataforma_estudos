from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("mysql+pymysql://root:1234#abcd@localhost:3306/plataforma_estudos")
#engine = create_engine('sqlite:///banco.db', echo=True)

try:
    connection = engine.connect()
    print("\n✅ Conexão bem-sucedida!")
    connection.close()
except Exception as e:
    print(f"❌ Falha na conexão: {e}")
    
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()