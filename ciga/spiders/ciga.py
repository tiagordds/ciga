import scrapy

from ciga.alerter import send_alert_email
from ciga.db import is_same_as_saved, save_to_db


class CigaSpider(scrapy.Spider):
    name = "ciga"
    allowed_domains = ["portal.institutolegalle.org.br"]
    start_urls = ["https://portal.institutolegalle.org.br/edital/ver/68"]

    def parse(self, response):
        posts = response.css("#arquivos .list-group-item")
        if not posts:
            self.logger.warning("No posts found in ARQUIVOS DISPONÍVEIS")
            return

        item = posts[0].css("p").xpath("normalize-space(.)").get()
        if not item:
            self.logger.warning("The first available post has no title")
            return

        same = is_same_as_saved(item)
        print("__ SAME AS SAVED:", same)

        if not same:
            send_alert_email(item)
            print("__ EMAIL SENT")

        save_to_db(item)
        print("__", item)
