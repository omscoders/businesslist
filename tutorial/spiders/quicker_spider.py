import scrapy
import csv
import os
import math
import re
import sys
reload(sys);
sys.setdefaultencoding("utf8")


class QuickerItem(scrapy.Item):
    district = scrapy.Field()
    area = scrapy.Field()
    pin = scrapy.Field()
    category = scrapy.Field()
    sub_cat = scrapy.Field()
    b_name = scrapy.Field()
    b_address = scrapy.Field()
    mobile = scrapy.Field()

class QuickerSpider(scrapy.Spider):
    name = "quicker"
    cat_name =""
    dist_name = ""
    countmaker = re.compile( '([0-9]+)' )
    nospace = re.compile( '\s+' )
    writer = ""

    def start_requests(self):
        urls = [
            {"u":"https://www.quickerala.com/abrasives/ct-479","n":"Abrasives"},
            {"u":"https://www.quickerala.com/accounting/ct-1","n":"Accounting"},
            {"u":"https://www.quickerala.com/accreditation/ct-489","n":"Accreditation"},
            {"u":"https://www.quickerala.com/acoustic-consultants/ct-1191","n":"Acoustic Consultants"},
            {"u":"https://www.quickerala.com/acupressurist/ct-1479","n":"Acupressurist"},
            {"u":"https://www.quickerala.com/adhesives/ct-3","n":"Adhesives"},
            {"u":"https://www.quickerala.com/advertising/ct-2","n":"Advertising"},
            {"u":"https://www.quickerala.com/advocates/ct-863","n":"Advocates"},
            {"u":"https://www.quickerala.com/agriculture/ct-5","n":"Agriculture"},
            {"u":"https://www.quickerala.com/air-conditioning-refrigeration/ct-7","n":"Air Conditioning/Refrigeration"},
            {"u":"https://www.quickerala.com/akshaya-services/ct-1688","n":"Akshaya Services"},
            {"u":"https://www.quickerala.com/aluminium-products-and-services/ct-669","n":"Aluminium Products and Services"},
            {"u":"https://www.quickerala.com/ambulance-service/ct-11","n":"Ambulance Service"},
            {"u":"https://www.quickerala.com/ammunition/ct-1394","n":"Ammunition"},
            {"u":"https://www.quickerala.com/amplifiers/ct-840","n":"Amplifiers"},
            {"u":"https://www.quickerala.com/animation/ct-640","n":"Animation"},
            {"u":"https://www.quickerala.com/aquarium/ct-14","n":"Aquarium"},
            {"u":"https://www.quickerala.com/art-and-culture/ct-1888","n":"Art and Culture"},
            {"u":"https://www.quickerala.com/associations/ct-527","n":"Associations"},
            {"u":"https://www.quickerala.com/attestation/ct-1024","n":"Attestation"},
            {"u":"https://www.quickerala.com/audio-video/ct-514","n":"Audio/Video"},
            {"u":"https://www.quickerala.com/auditorium/ct-1026","n":"Auditorium"},
            {"u":"https://www.quickerala.com/automatic-lath-company/ct-972","n":"Automatic Lath Company"},
            {"u":"https://www.quickerala.com/automation/ct-545","n":"Automation"},
            {"u":"https://www.quickerala.com/automotive/ct-1880","n":"Automotive"},
            {"u":"https://www.quickerala.com/baby-care/ct-27","n":"Baby care"},
            {"u":"https://www.quickerala.com/bags/ct-46","n":"Bags"},
            {"u":"https://www.quickerala.com/bakery/ct-29","n":"Bakery"},
            {"u":"https://www.quickerala.com/bank/ct-1605","n":"Bank"},
            {"u":"https://www.quickerala.com/batteries/ct-53","n":"Batteries"},
            {"u":"https://www.quickerala.com/beautycare/ct-1930","n":"Beautycare"},
            {"u":"https://www.quickerala.com/blood-banks/ct-57","n":"Blood Banks"},
            {"u":"https://www.quickerala.com/book/ct-36","n":"Book"},
            {"u":"https://www.quickerala.com/branding/ct-1942","n":"Branding"},
            {"u":"https://www.quickerala.com/builders-developers/ct-554","n":"Builders & Developers"},
            {"u":"https://www.quickerala.com/building-and-construction/ct-68","n":"Building and Construction"},
            {"u":"https://www.quickerala.com/business/ct-495","n":"Business"},
            {"u":"https://www.quickerala.com/business-consultants/ct-1464","n":"Business Consultants"},
            {"u":"https://www.quickerala.com/cable-tv/ct-58","n":"Cable TV"},
            {"u":"https://www.quickerala.com/calligraphy/ct-920","n":"Calligraphy"},
            {"u":"https://www.quickerala.com/candle/ct-973","n":"Candle"},
            {"u":"https://www.quickerala.com/cargo-services/ct-86","n":"Cargo Services"},
            {"u":"https://www.quickerala.com/cds-tapes-and-records/ct-76","n":"CDs, Tapes and Records"},
            {"u":"https://www.quickerala.com/cemeteries-and-crematories/ct-96","n":"Cemeteries and Crematories"},
            {"u":"https://www.quickerala.com/certificate-attestation-company/ct-1023","n":"Certificate Attestation Company"},
            {"u":"https://www.quickerala.com/certification-body/ct-1872","n":"Certification Body"},
            {"u":"https://www.quickerala.com/charitable-trust/ct-1543","n":"Charitable Trust"},
            {"u":"https://www.quickerala.com/chemicals/ct-629","n":"Chemicals"},
            {"u":"https://www.quickerala.com/cleaning-service/ct-1418","n":"Cleaning Service"},
            {"u":"https://www.quickerala.com/clubs/ct-1875","n":"Clubs"},
            {"u":"https://www.quickerala.com/coconut-products/ct-1932","n":"Coconut Products"},
            {"u":"https://www.quickerala.com/cold-storage/ct-769","n":"Cold Storage"},
            {"u":"https://www.quickerala.com/communication-media/ct-67","n":"Communication / Media"},
            {"u":"https://www.quickerala.com/computer/ct-70","n":"Computer"},
            {"u":"https://www.quickerala.com/consultants/ct-485","n":"Consultants"},
            {"u":"https://www.quickerala.com/consumer-products/ct-1245","n":"Consumer Products"},
            {"u":"https://www.quickerala.com/counselling-services/ct-561","n":"Counselling Services"},
            {"u":"https://www.quickerala.com/courier-services/ct-524","n":"Courier Services"},
            {"u":"https://www.quickerala.com/crane-and-recovery-service/ct-635","n":"Crane and Recovery Service"},
            {"u":"https://www.quickerala.com/currency/ct-1085","n":"Currency"},
            {"u":"https://www.quickerala.com/cycle-showrooms/ct-558","n":"Cycle Showrooms"},
            {"u":"https://www.quickerala.com/dairy/ct-99","n":"Dairy"},
            {"u":"https://www.quickerala.com/dance-and-music/ct-100","n":"Dance and Music"},
            {"u":"https://www.quickerala.com/data-entry-works/ct-649","n":"Data Entry Works"},
            {"u":"https://www.quickerala.com/day-care-play-school/ct-28","n":"Day Care/Play School"},
            {"u":"https://www.quickerala.com/defence/ct-1165","n":"Defence"},
            {"u":"https://www.quickerala.com/detectives-and-investigation-agencies/ct-111","n":"Detectives and Investigation Agencies"},
            {"u":"https://www.quickerala.com/disposable-consumables/ct-120","n":"Disposable Consumables"},
            {"u":"https://www.quickerala.com/document-writing/ct-1119","n":"Document Writing"},
            {"u":"https://www.quickerala.com/dress-apparel/ct-622","n":"Dress/Apparel"},
            {"u":"https://www.quickerala.com/drinking-mineral-water-supply/ct-1049","n":"Drinking / Mineral Water Supply"},
            {"u":"https://www.quickerala.com/driver/ct-1207","n":"Driver"},
            {"u":"https://www.quickerala.com/driving-schools/ct-128","n":"Driving Schools"},
            {"u":"https://www.quickerala.com/eco-friendly-products/ct-1889","n":"Eco friendly Products"},
            {"u":"https://www.quickerala.com/education/ct-1263","n":"Education"},
            {"u":"https://www.quickerala.com/electrical-and-electronics/ct-759","n":"Electrical and Electronics"},
            {"u":"https://www.quickerala.com/electrician/ct-1401","n":"Electrician"},
            {"u":"https://www.quickerala.com/emporiums/ct-162","n":"Emporiums"},
            {"u":"https://www.quickerala.com/energy-environment/ct-667","n":"Energy & Environment"},
            {"u":"https://www.quickerala.com/entertaintment/ct-526","n":"Entertaintment"},
            {"u":"https://www.quickerala.com/equipments-and-supplies/ct-1877","n":"Equipments and Supplies"},
            {"u":"https://www.quickerala.com/event-management/ct-537","n":"Event Management"},
            {"u":"https://www.quickerala.com/exporters-importers/ct-1102","n":"Exporters & Importers"},
            {"u":"https://www.quickerala.com/eye-care/ct-1943","n":"Eye care"},
            {"u":"https://www.quickerala.com/family-counselling-centre/ct-1344","n":"Family Counselling Centre"},
            {"u":"https://www.quickerala.com/farm/ct-1944","n":"Farm"},
            {"u":"https://www.quickerala.com/finance-and-banking/ct-1876","n":"Finance and Banking"},
            {"u":"https://www.quickerala.com/fire-and-safety/ct-194","n":"Fire and Safety"},
            {"u":"https://www.quickerala.com/fire-works-and-explosives/ct-196","n":"Fire Works and Explosives"},
            {"u":"https://www.quickerala.com/fishery/ct-1058","n":"Fishery"},
            {"u":"https://www.quickerala.com/flats-apartments/ct-1923","n":"Flats/Apartments"},
            {"u":"https://www.quickerala.com/flavours-and-fragrance/ct-200","n":"Flavours and Fragrance"},
            {"u":"https://www.quickerala.com/florist/ct-203","n":"Florist"},
            {"u":"https://www.quickerala.com/food/ct-1549","n":"Food"},
            {"u":"https://www.quickerala.com/footwear/ct-208","n":"Footwear"},
            {"u":"https://www.quickerala.com/franchisee/ct-1139","n":"Franchisee"},
            {"u":"https://www.quickerala.com/freelancer/ct-1189","n":"Freelancer"},
            {"u":"https://www.quickerala.com/fruits-shop/ct-938","n":"Fruits Shop"},
            {"u":"https://www.quickerala.com/fuel/ct-1931","n":"Fuel"},
            {"u":"https://www.quickerala.com/funeral-services/ct-966","n":"Funeral Services"},
            {"u":"https://www.quickerala.com/gadgets/ct-870","n":"Gadgets"},
            {"u":"https://www.quickerala.com/garage/ct-214","n":"Garage"},
            {"u":"https://www.quickerala.com/general-labours-and-workers/ct-608","n":"General labours And Workers"},
            {"u":"https://www.quickerala.com/generator/ct-227","n":"Generator"},
            {"u":"https://www.quickerala.com/gifts-and-fancy/ct-1933","n":"Gifts and Fancy"},
            {"u":"https://www.quickerala.com/government-offices/ct-1100","n":"Government Offices"},
            {"u":"https://www.quickerala.com/gps-tracking-solution/ct-1934","n":"GPS Tracking Solution"},
            {"u":"https://www.quickerala.com/graphics-and-designs/ct-232","n":"Graphics and Designs"},
            {"u":"https://www.quickerala.com/handicraft/ct-1563","n":"Handicraft"},
            {"u":"https://www.quickerala.com/hardware/ct-241","n":"Hardware"},
            {"u":"https://www.quickerala.com/healthcare/ct-1937","n":"Healthcare"},
            {"u":"https://www.quickerala.com/helpline/ct-539","n":"Helpline"},
            {"u":"https://www.quickerala.com/hill-products/ct-1006","n":"Hill Products"},
            {"u":"https://www.quickerala.com/hiring/ct-1945","n":"Hiring"},
            {"u":"https://www.quickerala.com/hologram/ct-1912","n":"Hologram"},
            {"u":"https://www.quickerala.com/home-appliances/ct-623","n":"Home Appliances"},
            {"u":"https://www.quickerala.com/home-care/ct-499","n":"Home Care"},
            {"u":"https://www.quickerala.com/home-nursing/ct-581","n":"Home Nursing"},
            {"u":"https://www.quickerala.com/hostels/ct-260","n":"Hostels"},
            {"u":"https://www.quickerala.com/hotel-accommodation/ct-1938","n":"Hotel/Accommodation"},
            {"u":"https://www.quickerala.com/household-products/ct-1878","n":"Household Products"},
            {"u":"https://www.quickerala.com/human-resource-solutions/ct-1936","n":"Human Resource Solutions"},
            {"u":"https://www.quickerala.com/identity-cards/ct-580","n":"Identity Cards"},
            {"u":"https://www.quickerala.com/immigration-checks/ct-815","n":"IMMIGRATION CHECKS"},
            {"u":"https://www.quickerala.com/individual-workers/ct-1232","n":"Individual Workers"},
            {"u":"https://www.quickerala.com/industrial-estates/ct-280","n":"Industrial Estates"},
            {"u":"https://www.quickerala.com/industrial-goods-and-services/ct-1940","n":"Industrial Goods and Services"},
            {"u":"https://www.quickerala.com/information-technology/ct-1680","n":"Information Technology"},
            {"u":"https://www.quickerala.com/infrastructure/ct-483","n":"Infrastructure"},
            {"u":"https://www.quickerala.com/insurance/ct-285","n":"Insurance"},
            {"u":"https://www.quickerala.com/interior-design-and-work/ct-1602","n":"Interior Design And Work"},
            {"u":"https://www.quickerala.com/internet/ct-1443","n":"Internet"},
            {"u":"https://www.quickerala.com/internet-and-digital-service/ct-504","n":"Internet and Digital Service"},
            {"u":"https://www.quickerala.com/inverter-battery-and-ups/ct-1941","n":"Inverter, Battery and UPS"},
            {"u":"https://www.quickerala.com/investigations-and-detective-services/ct-1105","n":"Investigations And Detective Services"},
            {"u":"https://www.quickerala.com/investments/ct-741","n":"Investments"},
            {"u":"https://www.quickerala.com/jewellers/ct-293","n":"Jewellers"},
            {"u":"https://www.quickerala.com/job/ct-1162","n":"Job"},
            {"u":"https://www.quickerala.com/kerala-ministry/ct-1095","n":"Kerala Ministry"},
            {"u":"https://www.quickerala.com/ksrtc-bus-station/ct-531","n":"KSRTC Bus Station"},
            {"u":"https://www.quickerala.com/laboratory/ct-771","n":"Laboratory"},
            {"u":"https://www.quickerala.com/laundry/ct-315","n":"Laundry"},
            {"u":"https://www.quickerala.com/legal-services/ct-318","n":"Legal Services"},
            {"u":"https://www.quickerala.com/liaison-public-relations/ct-1022","n":"Liaison & Public Relations"},
            {"u":"https://www.quickerala.com/life-guard-services/ct-323","n":"Life Guard Services"},
            {"u":"https://www.quickerala.com/light-house/ct-325","n":"Light house"},
            {"u":"https://www.quickerala.com/lights-and-sound-service/ct-329","n":"Lights and Sound Service"},
            {"u":"https://www.quickerala.com/lottery/ct-939","n":"Lottery"},
            {"u":"https://www.quickerala.com/mall/ct-1425","n":"Mall"},
            {"u":"https://www.quickerala.com/manufacturing-distribution/ct-879","n":"Manufacturing & Distribution"},
            {"u":"https://www.quickerala.com/marketing/ct-1196","n":"Marketing"},
            {"u":"https://www.quickerala.com/media/ct-752","n":"Media"},
            {"u":"https://www.quickerala.com/mills/ct-1276","n":"Mills"},
            {"u":"https://www.quickerala.com/mobile-mortuary/ct-1654","n":"Mobile Mortuary"},
            {"u":"https://www.quickerala.com/mobile-phone/ct-1666","n":"Mobile Phone"},
            {"u":"https://www.quickerala.com/modeling/ct-1146","n":"Modeling"},
            {"u":"https://www.quickerala.com/monastry/ct-1169","n":"Monastry"},
            {"u":"https://www.quickerala.com/mortuary/ct-1856","n":"Mortuary"},
            {"u":"https://www.quickerala.com/multimedia/ct-354","n":"Multimedia"},
            {"u":"https://www.quickerala.com/music/ct-350","n":"Music"},
            {"u":"https://www.quickerala.com/notary/ct-362","n":"Notary"},
            {"u":"https://www.quickerala.com/office-automation/ct-1925","n":"Office Automation"},
            {"u":"https://www.quickerala.com/old-age-home/ct-1857","n":"Old Age Home"},
            {"u":"https://www.quickerala.com/online-service/ct-631","n":"Online Service"},
            {"u":"https://www.quickerala.com/organic-products/ct-818","n":"Organic Products"},
            {"u":"https://www.quickerala.com/orphange/ct-1032","n":"Orphange"},
            {"u":"https://www.quickerala.com/outsourcing-agencies/ct-376","n":"Outsourcing agencies"},
            {"u":"https://www.quickerala.com/overseas-migration/ct-1840","n":"Overseas Migration"},
            {"u":"https://www.quickerala.com/packaged-drinking-water/ct-552","n":"Packaged Drinking water"},
            {"u":"https://www.quickerala.com/packers-and-movers/ct-379","n":"Packers and Movers"},
            {"u":"https://www.quickerala.com/packing/ct-833","n":"Packing"},
            {"u":"https://www.quickerala.com/paint-and-hardware/ct-1949","n":"Paint and Hardware"},
            {"u":"https://www.quickerala.com/pan-card-services/ct-1487","n":"Pan Card Services"},
            {"u":"https://www.quickerala.com/paper-products/ct-508","n":"Paper Products"},
            {"u":"https://www.quickerala.com/parcel-service/ct-1270","n":"Parcel Service"},
            {"u":"https://www.quickerala.com/passport-office/ct-385","n":"Passport office"},
            {"u":"https://www.quickerala.com/pest-control/ct-1947","n":"Pest Control"},
            {"u":"https://www.quickerala.com/pets-kennels/ct-301","n":"Pets/Kennels"},
            {"u":"https://www.quickerala.com/photo-video/ct-502","n":"Photo/Video"},
            {"u":"https://www.quickerala.com/photostat/ct-866","n":"Photostat"},
            {"u":"https://www.quickerala.com/plastic-products/ct-548","n":"Plastic Products"},
            {"u":"https://www.quickerala.com/plumber-electrician/ct-1204","n":"Plumber/Electrician"},
            {"u":"https://www.quickerala.com/police-control-room/ct-528","n":"Police Control Room"},
            {"u":"https://www.quickerala.com/press/ct-505","n":"Press"},
            {"u":"https://www.quickerala.com/printing-and-publishing/ct-1421","n":"Printing and Publishing"},
            {"u":"https://www.quickerala.com/printing-photostat-fax/ct-1893","n":"Printing, Photostat,Fax"},
            {"u":"https://www.quickerala.com/professionals/ct-1939","n":"Professionals"},
            {"u":"https://www.quickerala.com/project-handling/ct-1772","n":"Project Handling"},
            {"u":"https://www.quickerala.com/provision-store/ct-912","n":"Provision Store"},
            {"u":"https://www.quickerala.com/quarries/ct-401","n":"Quarries"},
            {"u":"https://www.quickerala.com/railway-reservation/ct-538","n":"Railway Reservation"},
            {"u":"https://www.quickerala.com/real-estate/ct-1027","n":"Real Estate"},
            {"u":"https://www.quickerala.com/recycling-services/ct-406","n":"Recycling Services"},
            {"u":"https://www.quickerala.com/refrigeration/ct-405","n":"Refrigeration"},
            {"u":"https://www.quickerala.com/religious-services/ct-571","n":"Religious Services"},
            {"u":"https://www.quickerala.com/research-and-development/ct-410","n":"Research and Development"},
            {"u":"https://www.quickerala.com/restaurant/ct-412","n":"Restaurant"},
            {"u":"https://www.quickerala.com/saw-mills/ct-418","n":"Saw mills"},
            {"u":"https://www.quickerala.com/scrap/ct-547","n":"Scrap"},
            {"u":"https://www.quickerala.com/security-systems/ct-1517","n":"Security Systems"},
            {"u":"https://www.quickerala.com/self-defence/ct-1039","n":"Self Defence"},
            {"u":"https://www.quickerala.com/service-personality-development/ct-1108","n":"Service & Personality Development"},
            {"u":"https://www.quickerala.com/service-and-repair/ct-1384","n":"Service and Repair"},
            {"u":"https://www.quickerala.com/shipping/ct-496","n":"Shipping"},
            {"u":"https://www.quickerala.com/shipping-company/ct-593","n":"Shipping Company"},
            {"u":"https://www.quickerala.com/shops-and-stores/ct-511","n":"Shops and Stores"},
            {"u":"https://www.quickerala.com/smart-cards/ct-1476","n":"Smart Cards"},
            {"u":"https://www.quickerala.com/soaps-and-perfumes/ct-1918","n":"Soaps and Perfumes"},
            {"u":"https://www.quickerala.com/societies/ct-1030","n":"Societies"},
            {"u":"https://www.quickerala.com/software-and-web-development/ct-1427","n":"Software And Web Development"},
            {"u":"https://www.quickerala.com/solar-products/ct-501","n":"Solar Products"},
            {"u":"https://www.quickerala.com/sports/ct-428","n":"Sports"},
            {"u":"https://www.quickerala.com/stainless-steel/ct-980","n":"Stainless Steel"},
            {"u":"https://www.quickerala.com/stamps-and-coins/ct-1010","n":"Stamps and Coins"},
            {"u":"https://www.quickerala.com/stationery/ct-486","n":"Stationery"},
            {"u":"https://www.quickerala.com/steel-fabrication/ct-1186","n":"Steel Fabrication"},
            {"u":"https://www.quickerala.com/steel-products/ct-523","n":"Steel Products"},
            {"u":"https://www.quickerala.com/swimming-pool/ct-842","n":"Swimming Pool"},
            {"u":"https://www.quickerala.com/tailoring/ct-433","n":"Tailoring"},
            {"u":"https://www.quickerala.com/tanks/ct-1924","n":"Tanks"},
            {"u":"https://www.quickerala.com/taxi-services/ct-430","n":"Taxi services"},
            {"u":"https://www.quickerala.com/telecom-service/ct-519","n":"Telecom Service"},
            {"u":"https://www.quickerala.com/theatres/ct-436","n":"Theatres"},
            {"u":"https://www.quickerala.com/tools/ct-1929","n":"Tools"},
            {"u":"https://www.quickerala.com/tours-and-travel/ct-440","n":"Tours and Travel"},
            {"u":"https://www.quickerala.com/transport/ct-1184","n":"Transport"},
            {"u":"https://www.quickerala.com/transportation/ct-1935","n":"Transportation"},
            {"u":"https://www.quickerala.com/upholstery/ct-521","n":"Upholstery"},
            {"u":"https://www.quickerala.com/visual-aids/ct-452","n":"Visual Aids"},
            {"u":"https://www.quickerala.com/warehouse/ct-456","n":"Warehouse"},
            {"u":"https://www.quickerala.com/waste-disposal/ct-457","n":"Waste Disposal"},
            {"u":"https://www.quickerala.com/waste-recycling/ct-458","n":"Waste recycling"},
            {"u":"https://www.quickerala.com/watch/ct-459","n":"Watch"},
            {"u":"https://www.quickerala.com/water-and-wastewater-treatment/ct-1825","n":"Water And Wastewater Treatment"},
            {"u":"https://www.quickerala.com/water-service/ct-1907","n":"Water Service"},
            {"u":"https://www.quickerala.com/waterproof/ct-1946","n":"waterproof"},
            {"u":"https://www.quickerala.com/wedding-arrangements/ct-493","n":"Wedding Arrangements"},
            {"u":"https://www.quickerala.com/wind-mill/ct-1439","n":"Wind Mill"},
            {"u":"https://www.quickerala.com/wood-and-wood-products/ct-473","n":"Wood and Wood Products"},
        ]
        dist = [
            #("1" , "Alleppey" ),
            # ("2","Calicut" ),
            # ("3","Ernakulam" ),
            # ("4","Idukki" ),
            # ("5","Kannur" ),
            # ("6","Kasargode" ),
            # ("7","Kollam" ),
            # ("8","Kottayam" ),
            # ("9","Malappuram" ),
            ("10","Palakkad" ),
            # ("11","Pathanamthitta" ),
            # ("12","Trivandrum" ),
            # ("13","Thrissur" ),
            # ("14","Wayanad"),
         ]
        for did,dnm in dist:
            self.dist_name = dnm
            for url in urls:
                 ftrg = '%s/?count=30&districtId=%s' % (url['u'], did)
                 request = scrapy.Request(url=ftrg, callback=self.parse)
                 self.cat_name = url['n']
                 yield request

    def parse(self, response):
        urlparts = response.url.split("?")
        check_data = response.css('div.row div.listHeader h1 span::text').extract_first()
        if check_data is not None:
            total = self.countmaker.search(check_data)
            self.log('Data Text : %s : %s' % ( total.group(), self.dist_name ))
            page = int(math.ceil(float(total.group())/float(30)))
            for x in range(1,page+1):
                self.log("Next URL :"+urlparts[0]+"p-"+str(x)+"/?"+urlparts[1])
                yield response.follow(urlparts[0]+"p-"+str(x)+"/?"+urlparts[1],callback=self.parse_list)
        # with open(filename, 'wb') as f:
        #     f.write('Category = %s ; Title = %s' % (cat_name, response.css('title::text').extract_first()))
        #self.log('Saved file %s' % filename)

    def parse_list(self, response):
        for items in response.css('#collapseWrapper > div.col-lg-9.col-md-9.col-sm-12.col-xs-12.listingArea > div > div.row > div.col-lg-12.col-md-6.col-sm-12.col-xs-12'):
            yield response.follow(items.css('a::attr(href)').extract_first(), callback=self.parse_data)

    def parse_data(self, response):
        self.log('------------------------------------')
        area = response.css('h3 span[itemprop="addressLocality"]::text').extract_first()
        pin = response.css('h3 span[itemprop="postalCode"]::text').extract_first()
        sub_cat = response.css('div.clearfix p[title="Subcategories"] a::text').extract_first()
        main_cat = response.css('div.brtop-10 p[itemprop="brand"] a::text').extract_first()
        b_name = response.css('h1[itemprop="name"]::text').extract_first()
        street = response.css('h3 span[itemprop="streetAddress"]::text').extract_first()
        b_address = re.sub(r'\s+',' ',response.css('h3[itemprop="address"]::text').extract_first())
        if street is not None:
            b_address = b_address + "," + street
        if area is not None:
            b_address = b_address + "," + area
        mobile = re.sub(r'\s+',' ',response.css('h4[itemprop="telephone"]::text').extract_first())
        self.log("Area : %s" % area);
        self.log("Pin : %s" % pin);
        self.log("Sub Cat : %s" % sub_cat);
        self.log("Name : %s" % b_name);
        self.log("Address : %s" % b_address);
        self.log("Mobile : %s" % mobile);
        self.log("District : %s" % self.dist_name);
        self.log("Category : %s" % main_cat);
        item = QuickerItem()
        item['district'] = self.dist_name
        item['area'] = area
        item['pin'] = pin
        item['category'] = main_cat
        item['sub_cat'] = sub_cat
        item['b_name'] = b_name
        item['b_address'] = b_address
        item['mobile'] = mobile
        yield item
        # with open('/var/www/pyth/tutorial/out/%s.csv' % (self.dist_name), 'ab') as csvfile:
        #     fieldnames = ['district','area','pin', 'category', 'sub_cat', 'b_name', 'b_address','mobile' ]
        #     self.writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #     self.writer.writeheader()
        #     self.log("Mobile")
        #     self.writer.writerow({'district':self.dist_name,
        #                 'area':area,
        #                 'pin':pin,
        #                 'category':self.cat_name,
        #                 'sub_cat':sub_cat,
        #                 'b_name':b_name,
        #                 'mobile':mobile,
        #                 'b_address':b_address})
        self.log('Loop Completed')
            #writer.writerow({'category': cat_name, 'title': response.css('title::text').extract_first()})
