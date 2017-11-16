
# coding: utf-8

# In[9]:


from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.http.request import Request
import sys 
sys.path.append(r'F:\python2.7\workspace\musicLikeScrapy\musicLikeScrapy')
from items import MusiclikescrapyItem


# In[18]:


class MusicLikeSpider(Spider):
    name = "MusicLike"
    allowed_domains = ["163.com"]
    #设置爬取速度
    #download_delay = 1
    # def start_requests(self):
    #    for i in range(1001,1004):
    #        for j in range(65,91):
    #            #获得A-Z歌手信息
    #            yield Request("http://music.163.com/#/discover/artist/cat?id=%d&initial=%d" %(i,j),callback=self.parse,dont_filter=True)
    #        #获得 “其他” 歌手信息
    #        yield Request("http://music.163.com/#/discover/artist/cat?id=%d&initial=0" %i, callback=self.parse,dont_filter=True)
    start_urls = [
        # 第一个网页地址
        # "http://music.163.com/#/playlist?id=142570652"]
        'http://music.163.com/#/playlist?id=142570652']
    def parse(self,response):
        info=MusiclikescrapyItem()
        sel=Selector(response)
        # artist_ids = response.xpath('//a[contains(@href, "/artist?id=")][@class="nm nm-icn f-thide s-fc0"]').re(r'/artist\?id=\s*(\d*)"')
        # artist_names = response.xpath('//a[contains(@href, "/artist?id=")][@class="nm nm-icn f-thide s-fc0"]/text()').extract()
        # print "------------------>"+str(len(artist_ids))
        # print "------------------>"+str(len(artist_names))
        # for i in range(len(artist_ids)):
        #     print '----------->'+str(artist_ids[i].encode("utf-8"))
        #     print '----------->'+str(artist_names[i].encode("utf-8"))
        _users=sel.xpath("//h2[@class='f-ff2 f-brk']/text()").extract()
        # print "-------------->"+str(len(_users))
        _songs=sel.xpath('//a[contains(@href,"/song?id=")]/b/@title').extract()
        _artists=sel.xpath('//div[@class="text"]/span/@title').extract()
        # print '----------->'+str(len(_songs))
        # print '----------->'+str(len(_artists))
        for i in range(len(_artists)):
            # print '----------->'+str(_songs[i].encode("utf-8"))
            # print '----------->'+str(_artists[i].encode("utf-8"))
            info["user"]=_users[0].encode('utf-8')
            info['artist_name']=_artists[i].encode('utf-8')
            info['song_name']=_songs[i].encode('utf-8')
            yield info
if __name__ == '__main__':
    a = MusicLikeSpider()
    a.parse()
