import scrapy
from scrapy.http import Request

class ImdbSpider(scrapy.Spider):
   
    name = "imdb_spider"
       
    start_urls = [
        "https://www.imdb.com/title/tt0241527/"    
    ]


    def parse(self,response):
        url= response.url + "fullcredits/"
        yield Request(url,callback = self.parse_full_credits)
      
    def parse_full_credits(self,response):
        links = response.css("td.primary_photo").css("a")
        actorname = [link.attrib["href"] for link in links]
        for i in actorname:
            url ="https://www.imdb.com/"+ i
            yield Request(url,callback = self.parse_actor_page)
    

    def parse_actor_page(self,response):
        actor = response.css("span.itemprop::text").get()
        boxes = response.css("div#content-2-wide.redesign")
        Movie = boxes.css('div.filmo-row[id^="actor"]').css('b').css('a::text').extract()
                
        for m in Movie:
            yield{
                "actor":actor,
                "Movie_or_TV_name":m
            }

    def parse_start_url(self,response):
        return self.parse(response)