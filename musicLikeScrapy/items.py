
import scrapy


class MusiclikescrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    user=scrapy.Field()
    artist_name=scrapy.Field()
    song_name=scrapy.Field()
    pass


