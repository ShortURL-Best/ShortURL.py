from .client import Client
from aiohttp import ClientSession
from json import dumps, loads


class HTTPClient:
    def __init__(self, client: Client, **kwargs) -> None:
        self.api_token: str = client.api_token
        self.base_url: str = "https://shorturl.best/api/"
        
    async def __request(self, method, endpoint, data = None):
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json",
        }

        if data != None:
            data = dumps(data)

        async with ClientSession() as session:
            if method == "get":
                async with session.get(self.base_url + endpoint) as resp:
                    return loads(await resp.content.read())

            elif method == "post":
                async with session.post(self.base_url + endpoint, headers = headers, data = data) as resp:
                    return loads(await resp.content.read())
            
            elif method == "put":
                async with session.put(self.base_url + endpoint, headers = headers, data = data) as resp:
                    return loads(await resp.content.read())

            elif method == "delete":
                async with session.delete(self.base_url + endpoint) as resp:
                    return loads(await resp.content.read())

            else:
                raise Exception("Invalid method provided.")

    # Account
    async def get_account(self):
        return self.__request("get", "account")

    async def update_account(self, email, password):
        data = {"email": email, "password": password}
        return self.__request("put", "account/update", data)

    # Branded domains
    async def list_branded_domains(self, limit, page):
        return self.__request("get", f"domains?limit={limit}&page={page}")

    async def create_domain(self, domain, redirect_root, redirect_404):
        data = {"domain": domain, "redirectroot": redirect_root, "redirect404": redirect_404}
        return self.__request("post", "domain/add", data)

    async def update_domain(self, id, redirect_root, redirect_404):
        data = {"redirectroot": redirect_root, "redirect404": redirect_404}
        return self.__request("put", f"domain/:{id}/update", data)

    async def delete_domain(self, id):
        return self.__request("delete", f"domain/:{id}/delete")

    # CTA Overlays
    async def list_cta_overlays(self, limit, page):
        return self.__request("get", f"overlay?limit={limit}&page={page}")

    # Campaigns
    async def list_campaigns(self, limit, page):
        return self.__request("get", f"campaigns?limit={limit}&page={page}")

    async def create_campaign(self, name, slug, public):
        data = {"name": name, "slug": slug, "public": public}
        return self.__request("post", "campaign/add", data)

    ## Make sure method if correct for this one
    async def assign_campaign(self, campaign, link):
        return self.__request("put", f"campaign/:{campaign}/assign/:{link}")

    async def update_campaign(self, id, name, slug, public):
        data = {"name": name, "slug": slug, "public": public}
        return self.__request("put", f"campaign/:{id}/update", data)

    async def delete_campaign(self, id):
        return self.__request("delete", f"campaign/:{id}/delete")
