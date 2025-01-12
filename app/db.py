from sqlmodel import create_engine, SQLModel, Session, select
from app.models import User

DATABASE_URL = "sqlite:///db.sqlite"

engine = create_engine(
    DATABASE_URL,
    echo=True,
)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


def add_user(session: Session, user: User):
    # check both existing user (email and provider match)
    # check if previous signup (email and different provider)
    existing_user = session.exec(select(User).where(User.email == user.email)).first()
    if existing_user:
        return user
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
