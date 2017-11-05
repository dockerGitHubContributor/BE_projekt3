from urllib.request import urlopen
from html.parser import HTMLParser
from random import randrange


class MyHTMLParser(HTMLParser):
    
    
    
    def __init__(self, category, subcategory):
        HTMLParser.__init__(self)
        self.__category = category
        self.__subcategory = subcategory
        self.__result = ""
    
    __category = ""
    __subcategory = ""
    __link = ""
    __name = ""
    __price = ""
    __result = ""
    __isSrc = False
    __isAlt = False
    
    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            for attr in attrs:
                if (attr[0] == 'data-price'):
                    self.__price = attr[1]
                    if self.__isSrc and self.__isAlt:
                        self.__name = self.__name.replace(";", "-")
                        self.__link = self.__link.replace("medium.jpg", "main.jpg")
                        self.__result = ';1;' + self.__name + ';'
                        self.__result += self.__subcategory + ';'
                        self.__result += self.__price + ';;;0;;;;;;;;;;;;;;;;'
                        self.__result += str(randrange(1000)) + ';0;;;;;;;;;;;;;;1;;;1;'
                        self.__result += self.__link + ';' + self.__name + ';0;;0;;0;0;0;;0\n'
                        self.__result = self.__result.replace("&amp", "")
                        self.__result = self.__result.replace(" ;", ";")
                        
                        output.write(self.__result)
                           
                        
                        self.__isSrc = False
                        self.__isAlt = False
                        self.__name = ""
                        self.__link = ""
                    self.__price = ""

                        
        if tag == 'img':
            for attr in attrs:
                if attr[0] == 'src':
                    self.__link = attr[1]
                    self.__isSrc = True
                if attr[0] == 'alt' and attr[1] != "" and attr[1] != "Strona główna Leroy Merlin":
                    self.__name = attr[1] 
                    self.__isAlt = True
            if self.__isAlt == False or self.__isSrc == False:
                self.__name = ""
                self.__link = ""
                self.__isAlt = False
                self.__isSrc = False
                
    def handle_endtag(self, tag):
        return
    
    def handle_startendtag(self, tag, attrs):
        if tag == 'img':
            for attr in attrs:
                if attr[0] == 'src':
                    self.__link += attr[1]
                    self.__isSrc = True
                if attr[0] == 'alt' and attr[1] != "" and attr[1] != "Strona główna Leroy Merlin":
                    self.__name = attr[1]
                    self.__isAlt = True
                    
            if self.__isAlt == False or self.__isSrc == False:
                self.__link = ""
                self.__name = ""
                self.__isAlt = False
                self.__isSrc = False
                    
                
    def handle_data(self, data):
        return
       
    def handle_comment(self, data):
        return
        
    def handle_entityref(self, name):
        return
        
    def handle_charref(self, name):
        return 
        
    def handle_decl(self, data):
        return
        

#lista stron z których pobierane są produkty wraz z kategorią i podkategorią
websites = [
    ("Materiały budowlane", "Stan surowy", "https://www.leroymerlin.pl/materialy-budowlane/materialy-budowlane-stan-surowy,a156.html"),
    ("Materiały budowlane", "Stan surowy", "https://www.leroymerlin.pl/materialy-budowlane/materialy-budowlane-stan-surowy,a156,strona-2.html"),
    ("Materiały budowlane", "Stan surowy", "https://www.leroymerlin.pl/materialy-budowlane/materialy-budowlane-stan-surowy,a156,strona-3.html"),
    ("Materiały budowlane", "Stan surowy", "https://www.leroymerlin.pl/materialy-budowlane/materialy-budowlane-stan-surowy,a156,strona-4.html"),
    ("Materiały budowlane", "Stan surowy", "https://www.leroymerlin.pl/materialy-budowlane/materialy-budowlane-stan-surowy,a156,strona-5.html"),
    ("Materiały budowlane", "Zaprawy i tynki", "https://www.leroymerlin.pl/materialy-budowlane/zaprawy-i-tynki,a157.html"),
    ("Materiały budowlane", "Zaprawy i tynki", "https://www.leroymerlin.pl/materialy-budowlane/zaprawy-i-tynki,a157,strona-2.html"),
    ("Materiały budowlane", "Zaprawy i tynki", "https://www.leroymerlin.pl/materialy-budowlane/zaprawy-i-tynki,a157,strona-3.html"),
    ("Materiały budowlane", "Zaprawy i tynki", "https://www.leroymerlin.pl/materialy-budowlane/zaprawy-i-tynki,a157,strona-4.html"),
    ("Materiały budowlane", "Zaprawy i tynki", "https://www.leroymerlin.pl/materialy-budowlane/zaprawy-i-tynki,a157,strona-5.html"),
    ("Materiały budowlane", "Zaprawy i tynki", "https://www.leroymerlin.pl/materialy-budowlane/zaprawy-i-tynki,a157,strona-6.html"),
    ("Materiały budowlane", "Zaprawy i tynki", "https://www.leroymerlin.pl/materialy-budowlane/zaprawy-i-tynki,a157,strona-7.html"),
    ("Materiały budowlane", "Zaprawy i tynki", "https://www.leroymerlin.pl/materialy-budowlane/zaprawy-i-tynki,a157,strona-8.html"),
    ("Materiały budowlane", "Grunty i inpregnaty", "https://www.leroymerlin.pl/materialy-budowlane/grunty-i-impregnaty,a160.html"),
    ("Materiały budowlane", "Grunty i inpregnaty", "https://www.leroymerlin.pl/materialy-budowlane/grunty-i-impregnaty,a160,strona-2.html"),
    ("Materiały budowlane", "Grunty i inpregnaty", "https://www.leroymerlin.pl/materialy-budowlane/grunty-i-impregnaty,a160,strona-3.html"),
    ("Materiały budowlane", "Grunty i inpregnaty", "https://www.leroymerlin.pl/materialy-budowlane/grunty-i-impregnaty,a160,strona-4.html"),
    ("Materiały budowlane", "Kleje i zaprawy klejowe", "https://www.leroymerlin.pl/materialy-budowlane/kleje-i-zaprawy-klejowe,a163.html"),
    ("Materiały budowlane", "Kleje i zaprawy klejowe", "https://www.leroymerlin.pl/materialy-budowlane/kleje-i-zaprawy-klejowe,a163,strona-2.html"),
    ("Materiały budowlane", "Kleje i zaprawy klejowe", "https://www.leroymerlin.pl/materialy-budowlane/kleje-i-zaprawy-klejowe,a163,strona-3.html"),
    ("Materiały budowlane", "Kleje i zaprawy klejowe", "https://www.leroymerlin.pl/materialy-budowlane/kleje-i-zaprawy-klejowe,a163,strona-4.html"),
    ("Izolacja budynków", "Wełna mineralna i styropian", "https://www.leroymerlin.pl/izolacja-budynkow/welna-mineralna-styropian,a167.html"),
    ("Izolacja budynków", "Wełna mineralna i styropian", "https://www.leroymerlin.pl/izolacja-budynkow/welna-mineralna-styropian,a167,strona-2.html"),
    ("Izolacja budynków", "Wełna mineralna i styropian", "https://www.leroymerlin.pl/izolacja-budynkow/welna-mineralna-styropian,a167,strona-3.html"),
    ("Izolacja budynków", "Wełna mineralna i styropian", "https://www.leroymerlin.pl/izolacja-budynkow/welna-mineralna-styropian,a167,strona-4.html"),
    ("Izolacja budynków", "Kleje uszczelniające izolację", "https://www.leroymerlin.pl/izolacja-budynkow/kleje-uszczelniacze-izolacje,a395.html"),
    ("Izolacja budynków", "Kleje uszczelniające izolację", "https://www.leroymerlin.pl/izolacja-budynkow/kleje-uszczelniacze-izolacje,a395,strona-2.html"),
    ("Izolacja budynków", "Kleje uszczelniające izolację", "https://www.leroymerlin.pl/izolacja-budynkow/kleje-uszczelniacze-izolacje,a395,strona-3.html"),
    ("Izolacja budynków", "Kleje uszczelniające izolację", "https://www.leroymerlin.pl/izolacja-budynkow/kleje-uszczelniacze-izolacje,a395,strona-4.html"),
    ("Izolacja budynków", "Kleje uszczelniające izolację", "https://www.leroymerlin.pl/izolacja-budynkow/kleje-uszczelniacze-izolacje,a395,strona-5.html"),
    ("Izolacja budynków", "Kleje uszczelniające izolację", "https://www.leroymerlin.pl/izolacja-budynkow/kleje-uszczelniacze-izolacje,a395,strona-6.html"),
    ("Izolacja budynków", "Kleje uszczelniające izolację", "https://www.leroymerlin.pl/izolacja-budynkow/kleje-uszczelniacze-izolacje,a395,strona-7.html"),
    ("Izolacja budynków", "Kleje uszczelniające izolację", "https://www.leroymerlin.pl/izolacja-budynkow/kleje-uszczelniacze-izolacje,a395,strona-8.html"),
    ("Izolacja budynków", "Kleje uszczelniające izolację", "https://www.leroymerlin.pl/izolacja-budynkow/kleje-uszczelniacze-izolacje,a395,strona-9.html"),
    ("Izolacja budynków", "Kleje uszczelniające izolację", "https://www.leroymerlin.pl/izolacja-budynkow/kleje-uszczelniacze-izolacje,a395,strona-10.html"),
    ("Dachy i akcesoria", "Pokrycie dachowe", "https://www.leroymerlin.pl/dachy-i-akcesoria/pokrycia-dachowe,a196.html"),
    ("Dachy i akcesoria", "Pokrycie dachowe", "https://www.leroymerlin.pl/dachy-i-akcesoria/pokrycia-dachowe,a196,strona-2.html"),
    ("Dachy i akcesoria", "Pokrycie dachowe", "https://www.leroymerlin.pl/dachy-i-akcesoria/pokrycia-dachowe,a196,strona-3.html"),
    ("Dachy i akcesoria", "Pokrycie dachowe", "https://www.leroymerlin.pl/dachy-i-akcesoria/pokrycia-dachowe,a196,strona-4.html"),
    ("Dachy i akcesoria", "Pokrycie dachowe", "https://www.leroymerlin.pl/dachy-i-akcesoria/pokrycia-dachowe,a196,strona-5.html"),
    ("Dachy i akcesoria", "Pokrycie dachowe", "https://www.leroymerlin.pl/dachy-i-akcesoria/pokrycia-dachowe,a196,strona-6.html"),
    ("Dachy i akcesoria", "Odprowadzanie wody deszczowej", "https://www.leroymerlin.pl/dachy-i-akcesoria/odprowadzanie-wody-deszczowej,a199.html"),
    ("Dachy i akcesoria", "Odprowadzanie wody deszczowej", "https://www.leroymerlin.pl/dachy-i-akcesoria/odprowadzanie-wody-deszczowej,a199,strona-2.html"),
    ("Dachy i akcesoria", "Odprowadzanie wody deszczowej", "https://www.leroymerlin.pl/dachy-i-akcesoria/odprowadzanie-wody-deszczowej,a199,strona-3.html"),
    ("Dachy i akcesoria", "Odprowadzanie wody deszczowej", "https://www.leroymerlin.pl/dachy-i-akcesoria/odprowadzanie-wody-deszczowej,a199,strona-4.html"),
    ("Dachy i akcesoria", "Odprowadzanie wody deszczowej", "https://www.leroymerlin.pl/dachy-i-akcesoria/odprowadzanie-wody-deszczowej,a199,strona-5.html"),
    ("Dachy i akcesoria", "Odprowadzanie wody deszczowej", "https://www.leroymerlin.pl/dachy-i-akcesoria/odprowadzanie-wody-deszczowej,a199,strona-6.html"),
    ("Dachy i akcesoria", "Odprowadzanie wody deszczowej", "https://www.leroymerlin.pl/dachy-i-akcesoria/odprowadzanie-wody-deszczowej,a199,strona-7.html"),
    ("Dachy i akcesoria", "Odprowadzanie wody deszczowej", "https://www.leroymerlin.pl/dachy-i-akcesoria/odprowadzanie-wody-deszczowej,a199,strona-8.html"),
    ("Dachy i akcesoria", "Farby i uszczelniacze dachowe", "https://www.leroymerlin.pl/dachy-i-akcesoria/farby-i-uszczelniacze-dachowe,a203.html"),
    ("Dachy i akcesoria", "Farby i uszczelniacze dachowe", "https://www.leroymerlin.pl/dachy-i-akcesoria/farby-i-uszczelniacze-dachowe,a203,strona-2.html"),
    ("Dachy i akcesoria", "Farby i uszczelniacze dachowe", "https://www.leroymerlin.pl/dachy-i-akcesoria/farby-i-uszczelniacze-dachowe,a203,strona-3.html"),
    ("Dachy i akcesoria", "Farby i uszczelniacze dachowe", "https://www.leroymerlin.pl/dachy-i-akcesoria/farby-i-uszczelniacze-dachowe,a203,strona-4.html"),
    ]

output = open('products.csv', 'w')
for site in websites:
    print(site[2])
    sock = urlopen(site[2])
    htmlSource = sock.read()
    sock.close()
    source = str(htmlSource, 'utf-8')

    parser = MyHTMLParser(site[0], site[1])
    parser.feed(source)
    
output.close()




