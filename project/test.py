import pytest
import asyncio
from app import Application


data = [
    {
        "id": 1,
        "identifier": "u1",
        "values": [100, 81, 64],
        "weight": 2,
        "meta": {"category": "A"}
    },
    {
        "id": 2,
        "identifier": "u2",
        "values": [25, 36, 49],
        "weight": 3,
        "meta": {"category": "B"}
    }
]


@pytest.mark.asyncio
async def test_bootstrap():
    app = Application(data)
    results = await app.bootstrap()
    assert isinstance(results, list)
    assert len(results) == 2


@pytest.mark.asyncio
async def test_top_user():
    app = Application(data)
    top = await app.top_user()
    assert top["id"] == "u1"
