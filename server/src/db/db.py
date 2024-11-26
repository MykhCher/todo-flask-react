from sqlalchemy import String, create_engine
from sqlalchemy.orm import mapped_column, declarative_base, Mapped

from ..constants.index import DB_PORT, DB_NAME, DB_PASS, DB_USER

Base = declarative_base()



class Todo(Base):
    __tablename__ = "todo"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))

engine = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@localhost:{DB_PORT}/{DB_NAME}")
Base.metadata.create_all(engine)

connection = engine.connect()