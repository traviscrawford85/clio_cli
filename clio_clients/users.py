from clio_clients.base import AuthenticatedClient
from clio_clients.models.usershow import UserShow
import httpx


async def user_who_am_i(client: AuthenticatedClient) -> UserShow:
    url = "/users/who_am_i"
    response = await client.get(url)
    response.raise_for_status()
    print(f"[user_who_am_i] Response: {response.status_code} - {response.text}")
    return UserShow.parse_obj(response.json())
