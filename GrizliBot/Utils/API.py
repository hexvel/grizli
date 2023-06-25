import aiohttp
from constants import DATA


class VK:
    async def apia(self, method, **params):
        async with aiohttp.ClientSession() as session:
            async with session.post("https://api.vk.com/method/" + method + \
                                    f"?access_token={DATA.TOKEN}&v=5.131", params=params) as response:
                return await response.json()