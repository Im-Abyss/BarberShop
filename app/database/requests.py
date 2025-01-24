from app.database.models import async_session
from app.database.models import User, Barber, Service, Reserve, Manager
from sqlalchemy import select, update


def connection(func):
    async def wrapper(*args, **kwargs):
        async with async_session() as session:
            return await func(session, *args, **kwargs)
    return wrapper


@connection
async def set_user(session, tg_id):
    user = await session.scalar(select(User).where(User.tg_id == tg_id))

    if not user:
        session.add(User(tg_id=tg_id, name="", phone_number=""))
        await session.commit()
        return False
    else:
        return user
    

@connection
async def set_admin(session, tg_id):
    admin = await session.scalar(select(Manager).where(Manager.tg_id == tg_id))
    
    if not admin:
        return False
    else:
        return admin


@connection
async def update_user(session, tg_id, name, contact):
    await session.execute(update(User).where(User.tg_id == tg_id).values(name=name, phone_number=contact))
    await session.commit()


@connection
async def get_barbers(session):
    return await session.scalars(select(Barber))


@connection
async def get_services(session):
    return await session.scalars(select(Service))


@connection
async def get_reserve(session):
    return await session.scalars(select(User))


@connection
async def set_reserve(session, tg_id, barber, service):
    user = await session.scalar(select(User).where(User.tg_id == tg_id))
    session.add(Reserve(user_name=user.name, user_number=user.phone_number, barber_name=barber, service_name=service))
    await session.commit()