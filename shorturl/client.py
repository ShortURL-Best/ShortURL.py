from .http import HTTPClient


class Client:
    def __init__(self, api_token: str, **kwargs) -> None:
        if self.api_token == None:
            raise Exception("No Bearer Token set.")
        self.api_token = api_token
        self.http = HTTPClient(self, **kwargs)

    async def get_account(self):
        return HTTPClient.get_account(self)

    async def update_account(self, email = None, password = None):
        return HTTPClient.update_account(self, email, password)

    async def list_branded_domains(self, limit = None, page = None):
        return HTTPClient.list_branded_domains(self, limit)

    async def create_domain(self, domain, redirect_root = None, redirect_404 = None):
        return HTTPClient.create_domain(self, domain, redirect_root, redirect_404)

    async def update_domain(self, id, redirect_root = None, redirect_404 = None):
        return HTTPClient.update_domain(self, id, redirect_root, redirect_404)

    async def delete_domain(self, id):
        return HTTPClient.delete_domain(self, id)

    async def list_cta_overlays(self, limit = None, page = None):
        return HTTPClient.list_cta_overlays(self, limit, page)

    async def list_campaigns(self, limit = None, page = None):
        return HTTPClient.list_campaigns(self, limit, page)

    async def create_campaign(self, name = None, slug = None, public: bool = True):
        return HTTPClient.create_campaign(self, name, slug, public)

    async def assign_campaign(self, campaign = None, link = None):
        return HTTPClient.assign_campaign(self, campaign, link)

    async def update_campaign(self, id, name = None, slug = None, public: bool = True):
        return HTTPClient.update_campaign(self, id, name, slug, public)

    async def delete_campaign(self, id):
        return HTTPClient.delete_campaign(self, id)