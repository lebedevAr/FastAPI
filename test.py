import random

import pytest
from httpx import ASGITransport, AsyncClient

from app.app import app, get_user_data


@pytest.mark.asyncio
async def test_root():
    response = await get_user_data(1)
    print(response)
    assert response.status_code == 200
    assert response.json()['name'] == 'Leanne Graham'

async def make_random_request():
    resp = await get_user_data(random.randint(3, 10))
    return resp.status_code

@pytest.mark.asyncio
async def test_root_many_requests():
    r_status_code = await make_random_request()
    assert r_status_code == 200
    r_status_code = await make_random_request()
    assert r_status_code == 200
    r_status_code = await make_random_request()
    assert r_status_code == 200
    r_status_code = await make_random_request()
    assert r_status_code == 200
    r_status_code = await make_random_request()
    assert r_status_code == 200
    r_status_code = await make_random_request()
    assert r_status_code == 200

@pytest.mark.asyncio
async def test_empty_id():
    response = await get_user_data(15)
    print(response)
    assert response.status_code == 404
