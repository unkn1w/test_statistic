from app.db import Statistic


async def order_items_by_field(field_name: str):
    if field_name is None:
        return await Statistic.objects.order_by('date').all()
    return await Statistic.objects.order_by(field_name).all()
