from fastapi import FastAPI
import httpx
import asyncio


app = FastAPI()


async def get_api_data(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response


@app.get("/get_user_data")
async def get_user_data(id):
    api_url = f"https://jsonplaceholder.typicode.com/users/{id}"
    resp = await get_api_data(api_url)
    # return {'name': resp.json()["name"], 'email': resp.json()["email"], 'status_code': resp.status_code}
    return resp
