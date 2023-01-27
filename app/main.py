from datetime import datetime
from fastapi import FastAPI, HTTPException, Query, status

from app.db import Statistic, database
from app.selectors import order_items_by_field

app = FastAPI()


@app.delete("/statistics/reset")
async def statistic_reset():
    statistic_count = await Statistic.objects.count()
    if statistic_count==0:
        return f"Sorry, we do not have enough stastic to delete"
    await Statistic.objects.delete(each=True)
    return f"Succesfully deleted {statistic_count} statistic objects"

@app.post("/statistics/create/")
async def statistic_create(statistic: Statistic):
    statistic.cpc = round(statistic.cost / statistic.clicks, 2)
    statistic.cpm = round(statistic.cost / statistic.views * 1000, 2)
    try:
        await statistic.save()
    except Exception as e:
        raise HTTPException(status_code=400, detail="Failed to create item")
    return {"message": "Succesfully created!"}

@app.get("/statistics/")
async def statistic_get(field_name: str = Query(None, alias='field')):
    return await order_items_by_field(field_name=field_name)

@app.get('/statistics/{start_date}/{end_date}/')
async def statistic_get_by_range(start_date: str, end_date: str):
    start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
    end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
    return await Statistic.objects.filter(date__gte=start_date, date__lte=end_date).all()


@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()

@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()
