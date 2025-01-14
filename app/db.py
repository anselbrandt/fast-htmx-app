from sqlmodel import create_engine, SQLModel, Session, select
from app.user_models import User

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
    statement = select(User).where(
        (User.email == user.email) & (User.provider_id == user.provider_id)
    )
    existing_user = session.exec(statement).first()
    if existing_user:
        return existing_user
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
