from sqlalchemy import  create_engine

engine = create_engine("mysql+pymsql://root:password@localhost:3306/")

conn = engine.connect()
