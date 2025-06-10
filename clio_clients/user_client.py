from clio_clients.base import AuthenticatedClient
from clio_clients.models.usershow import UserShow

async def user_who_am_i(client: AuthenticatedClient) -> UserShow:
    url = "/users/who_am_i"
    response = await client.get(url)
    response.raise_for_status()
    return UserShow.model_validate(response.json())