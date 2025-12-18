from dataclasses import asdict

from sqlalchemy import select

from backend_todo.models import User


def test_create_user(session, mock_db_time):

    with mock_db_time(model=User) as time:
        new_user = User(username='test', email='test@test', password='test')
        session.add(new_user)
        session.commit()
        session.refresh(new_user)

    user = session.scalar(select(User).where(User.username == 'test'))

    assert asdict(user) == {
        'id': 1,
        'username': 'test',
        'password': 'test',
        'email': 'test@test',
        'created_at': time,
    }
