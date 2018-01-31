#coding=utf-8
from toapi import XPath, Item, Api, Settings


class MySettings(Settings):
    web = {
        "with_ajax": True,
        "request_config": {},
        "headers": None
    }

api = Api('https://sh.2boss.cn/estate/house', settings=MySettings)

class RabbitDoc(Item):
    url = XPath('//div[@class="content_box2"]/a/@href')
    title = XPath('//div[@class="content_box2"]/a/div/h2/text()')

    class Meta:
        source = XPath('//div[@class="clearfix content_box estate_external"]')
        route = {'/House?Community=:community': '/:community/s5'}

api.register(RabbitDoc)

api.serve()