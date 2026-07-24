import scrapy

from ciga.alerter import send_alert_email
from ciga.db import is_same_as_saved, save_to_db


class CigaSpider(scrapy.Spider):
    name = "ciga"
    allowed_domains = ["consorciociga.gov.br"]
    start_urls = ["https://consorciociga.gov.br/concursos/"]

    def parse(self, response):
        whole_table = response.css("div.su-table.su-table-responsive")
        item = whole_table.css("tbody tr:first-child td:nth-child(2)::text").get()

        same = is_same_as_saved(item)
        print("__ SAME AS SAVED:", same)

        if not same:
            send_alert_email(item)
            print("__ EMAIL SENT")

        save_to_db(item)
        print("__", item)
