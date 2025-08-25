from dataclasses import asdict

from sqlalchemy import select

from todo_list.models import User


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(
            username='test', password='password', email='teste@test'
        )
        session.add(new_user)
        session.commit()

    user = session.scalar(select(User).where(User.username == 'test'))

    assert asdict(user) == {
        'id': 1,
        'username': 'test',
        'password': 'password',
        'email': 'teste@test',
        'created_at': time,
        'updated_at': time,
    }
