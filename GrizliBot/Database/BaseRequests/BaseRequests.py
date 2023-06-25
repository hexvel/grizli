import json
import requests

from typing import Optional

base = '127.0.0.1:8088'


class Base:
    def requester(self, url: Optional[str], params: Optional[dict]) -> Optional[dict]:
        try:
            return requests.get(url=url, params=params).json()
        except Exception as error:
            return {'running': False, 'data': error}

    def create_template(self, params: Optional[dict], bases: Optional[str]) -> dict:
        # log.info(f'crt -> From[ params | {params}], bases | {bases}')
        data: Optional[dict] = {'params': json.dumps(params), 'bases': bases}
        url: Optional[str] = f'http://{base}/createTemplate/'
        return self.requester(url, data)

    def base_update(self, filters: Optional[dict], params: Optional[dict], bases: Optional[str]) -> Optional[dict]:
        # log.info(f'Updates -> From[ filter | {filters} params | {params}]')
        data: Optional[dict] = {'filters': json.dumps(filters), 'params': json.dumps(params), 'bases': bases}
        url: Optional[str] = f'http://{base}/updater/'
        return self.requester(url, data)

    def base_getter(self, filters: Optional[dict], bases: Optional[str]):
        # log.info(f'Getter -> From[ filter | {filters}]')
        data: Optional[dict] = {'filters': json.dumps(filters), 'bases': bases}
        url: Optional[str] = f'http://{base}/getter/'
        return self.requester(url, data)

    def base_create(self, filters: Optional[dict], params: Optional[dict], bases: Optional[str]) -> dict:
        # log.info(f'creater -> From[ filter | {filters} params | {params}], bases | {bases}')
        data: Optional[dict] = {'filters': json.dumps(filters), 'params': json.dumps(params), 'bases': bases}
        url: Optional[str] = f'http://{base}/creaters'
        return self.requester(url, data)

    def base_delete(self, filters: Optional[dict], bases: Optional[str]) -> dict:
        data: Optional[dict] = {'filters': json.dumps(filters), 'bases': bases}
        url: Optional[str] = f'http://{base}/deleter'
        return self.requester(url, data)
        
    def all_base(self, data):
        url: Optional[str] = f'http://{base}/all/'
        return self.requester(url, data)