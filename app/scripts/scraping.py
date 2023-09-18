import os
from bs4 import BeautifulSoup
from db_connection import collection
from selenium import webdriver
from selenium.webdriver.edge.service import Service

edge_driver_path = 'C:\\Drivers\\msedgedriver.exe'

os.environ['PATH'] += ';' + edge_driver_path

def scrape_property_details(city):
    base_url = f"https://www.99acres.com/search/property/buy/{city}?keyword={city}&preference=S&area_unit=1&budget_min=0&res_com=R&isPreLeased=N"
    
    driver = webdriver.Edge(service=Service(edge_driver_path), options=webdriver.EdgeOptions())


    try:
        driver.get(base_url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        properties = soup.find_all('div', class_='srpTuple__cardWrap tupleCardWrap')

        for property in properties:
            property_name = property.find('h2', class_='srpTuple__tupleTitleOverflow')
            property_cost = property.find('td', class_='srpTuple__col title_semiBold', id="srp_tuple_price")
            property_type = property.find('td', class_='srpTuple__col title_semiBold', id="srp_tuple_bedroom")
            property_area = property.find('td', class_='srpTuple__col title_semiBold', id="srp_tuple_primary_area")
            property_locality = property.find('td', class_='srpTuple__propertyPremiumHeading srpTuple__spacer10 srpTuple__tdClasstwoPremium', id="srp_tuple_society_heading")

            if all([property_name, property_cost, property_type, property_area, property_locality]):
                property_name = property_name.text.strip()
                property_cost = property_cost.text.strip()
                property_type = property_type.text.strip()
                property_area = property_area.text.strip()
                property_locality = property_locality.text.strip()
                property_city = city

                property_data = {
                    'property_name': property_name,
                    'property_cost': property_cost,
                    'property_type': property_type,
                    'property_area': property_area,
                    'property_locality': property_locality,
                    'property_city': property_city,
                }
                collection.insert_one(property_data)
    finally:
        driver.quit()
