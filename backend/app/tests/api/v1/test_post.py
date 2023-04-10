import pytest

from httpx import AsyncClient


@pytest.mark.anyio
async def test_get_uncorrect_post_id(client: AsyncClient):
    uncorrect_id_letters = "no_id"
    # local restriction 1 <= and >= 100_000
    uncorrect_id_big_number = 100_001
    uncorrect_id_small_number = -1

    res = await client.get(url=f"/api/v1/post?id={uncorrect_id_letters}")
    assert res.status_code == 422

    res = await client.get(url=f"/api/v1/post?id={uncorrect_id_big_number}")
    assert res.status_code == 422

    res = await client.get(url=f"/api/v1/post?id={uncorrect_id_small_number}")
    assert res.status_code == 422
