import pytest
from aioresponses import aioresponses
from textoria import Textoria


@pytest.fixture
def api_url():
    return "http://localhost:8000"


@pytest.fixture
def textoria_client(api_url):
    return Textoria(api_url)


@pytest.mark.asyncio
async def test_get_all_keys(textoria_client, api_url):
    mocked_data = {"key1": "value1", "key2": "value2"}

    with aioresponses() as m:
        m.get(f"{api_url}/get_all_keys", payload=mocked_data)

        response = await textoria_client.get_all_keys()
        assert response == mocked_data


@pytest.mark.asyncio
async def test_create_key(textoria_client, api_url):
    new_key = "new_key"
    new_value = "new_value"
    mocked_data = {new_key: new_value}

    with aioresponses() as m:
        m.post(f"{api_url}/create_key?new_key={new_key}&new_value={new_value}", payload=mocked_data)

        response = await textoria_client.create_key(new_key, new_value)
        assert response == mocked_data


@pytest.mark.asyncio
async def test_update_key(textoria_client, api_url):
    key = "key1"
    new_value = "updated_value"
    mocked_data = {key: new_value}

    with aioresponses() as m:
        m.put(f"{api_url}/update_key?key={key}&new_value={new_value}", payload=mocked_data)

        response = await textoria_client.update_key(key, new_value)
        assert response == mocked_data


@pytest.mark.asyncio
async def test_delete_key(textoria_client, api_url):
    key = "key1"
    mocked_data = {"detail": f"Key '{key}' deleted."}

    with aioresponses() as m:
        m.delete(f"{api_url}/delete_key?key={key}", payload=mocked_data)

        response = await textoria_client.delete_key(key)
        assert response == mocked_data
