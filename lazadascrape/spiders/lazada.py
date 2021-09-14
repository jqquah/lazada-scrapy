import scrapy
from bs4 import BeautifulSoup


class LazadaSpider(scrapy.Spider):
    name = "lazada"
    allowed_domains = ["lazada.com.my"]
    start_urls = [""]

    def parse(self, response):
        soup = BeautifulSoup(response.text, features="lxml")
        if soup.find("meta", {"property": "og:type"}):
            img_url = soup.find("meta", {"property": "og:image"})["content"]
            if img_url[:2] == "//":
                img_url = "https:" + img_url
            yield {
                'url': soup.find("meta", {"property": "og:url"})["content"],
                'title':  soup.find("meta", {"property": "og:title"})["content"],
                'type': soup.find("meta", {"property": "og:type"})["content"],
                'description': soup.find("meta", {"property": "og:description"})["content"],
                'image': img_url
            }
        else:
            img_url = soup.find("meta", {"name": "og:image"})["content"]
            if img_url[:2] == "//":
                img_url = "https:" + img_url
            yield {
                'url': soup.find("meta", {"name": "og:url"})["content"],
                'title':  soup.find("meta", {"name": "og:title"})["content"],
                'type': soup.find("meta", {"name": "og:type"})["content"],
                'description': soup.find("meta", {"name": "og:description"})["content"],
                'image': img_url
            }


# # input_url = "https://www.lazada.com.my/products/rorec-white-rice-beauty-moisturizing-facial-mask-i520004656-s1008020131.html?spm=a2o4k.home.flashSale.3.75f82e7eQYSdvq&search=1&mp=1&c=fs&clickTrackInfo=rs%3A0.0%3Babid%3A238030%3Bitem_id%3A520004656%3Bpvid%3A0384bb21-3b78-4d6c-af9d-8a9753aec212%3Bmt%3Ahot%3Bdata_type%3Aflashsale%3Bscm%3A1007.17760.238030.%3Bchannel_id%3A0000%3Bcampaign_id%3A139038&scm=1007.17760.238030.0"


# soup = BeautifulSoup(response.text, features="lxml")


# response.xpath('/html/head/meta[7]') # This is the og:url
# response.xpath('/html/head/meta[8]') # This is the og:title
# response.xpath('/html/head/meta[9]') # This is the og:type - product / website
# response.xpath('/html/head/meta[10]') # This is the og:description
# response.xpath('/html/head/meta[11]') # This is the og:image
