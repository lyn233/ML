import urllib2
from BeautifulSoup import *
from urlparse import urljoin

ignorewords = set(['the', 'of', 'to', 'and', 'a', 'in', 'is','it'])

class crawler:
    def __init__(self,dbname):
        pass

    def __del__(self):
        pass

    def dbcommit(self):
        pass

    def getentryid(self, table, field, value, creatnew = True):
        return None

    def addtoindex(self, url ,soup):
        print 'Indexing %s' %url

    def gettextonly(self, soup):
        return None

    def separatewords(self, text):
        return None

    def  isindexed(self, url):
        return False

    def  addlinkref(self, urlForm, urlTo, linkText):
        pass

    def createindextables(self):
        pass

    def crawl(self, pages, depth=2):
       for i in range(depth):
            newspages = set()
            for page in pages:
                try:
                    c = urllib2.urlopen(page)
                except:
                    print "Could not open %s" %page
                    continue
                soup = BeautifulSoup(c.read())
                self.addtoindex(page, soup)

                links = soup('a')
                for link in links:
                    if ('href' in dict(link.attrs)):
                        url = urljoin(page, link['href'])
                        if url.find(" '' ") != -1:
                            continue
                        url = url.split( '#')[0]
                        if url[0:4] == 'http' and not self.isindexed(url):
                            newspages.add(url)
                        linkText = self.gettextonly(link)
                        self.addlinkref(page,url,linkText)
                self.dbcommit()

            pages = newspages
