import databases
import ormar
import sqlalchemy
import datetime

from app.config import settings

database = databases.Database(settings.db_url)
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database
    auto_create = True


class Statistic(ormar.Model):
    class Meta(BaseMeta):
        tablename = "statistics"

    id: int = ormar.Integer(primary_key=True)
    date: ormar.Date = ormar.Date(default=datetime.datetime.now().date())
    clicks: int = ormar.Integer(minimum=0, default=0, nullable=False)
    views: int = ormar.Integer(minimum=0, default=0)
    cost: float = ormar.Float(minimum=0.0, default=0.0)
    cpc: float = ormar.Float(default=0)
    cpm: float = ormar.Float(default=0)


engine = sqlalchemy.create_engine(settings.db_url)
metadata.create_all(engine)