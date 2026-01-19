import requests
from bs4 import BeautifulSoup
import csv
import time

base_url = "https://www.cars45.com/listing"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}


def scrape_detail_page(car_url):

    try:
        full_url = f"https://www.cars45.com{car_url}"

        response = requests.get(full_url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')

        general_info = soup.find('div', class_='general-info')

        if not general_info:
            return {}

        info_items = general_info.find_all('div')

        details = {}
        for item in info_items:
            # Each item has: <p class="general-info__name">Value</p> and <span class="general-info__value">Label</span>
            name_elem = item.find('p', class_='general-info__name')
            value_elem = item.find('span', class_='general-info__value')

            if name_elem and value_elem:
                label = value_elem.text.strip()
                value = name_elem.text.strip()
                details[label] = value

        return details

    except Exception as e:
        print(f"Error scraping detail page: {e}")
        return {}


num_pages = 145
all_cars = []

for page_num in range(1, num_pages + 1):
    print(f"\n Scraping page {page_num}...")

    if page_num == 1:
        url = base_url
    else:
        url = f"{base_url}?page={page_num}"

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    car_links = soup.find_all('a', class_='car-feature')

    print(f"Found {len(car_links)} cars on page {page_num}")

    for idx, car_link in enumerate(car_links, 1):
        try:
            details_div = car_link.find('div', class_='car-feature__details')

            car_name = details_div.find('p', class_='car-feature__name').text.strip()
            price = details_div.find('p', class_='car-feature__amount').text.strip()
            location = details_div.find('p', class_='car-feature__region').text.strip()

            detail_url = car_link.get('href')

            print(f"  {idx}. Scraping details for: {car_name[:50]}...")

            detailed_specs = scrape_detail_page(detail_url)

            car_data = {
                'name': car_name,
                'price': price,
                'location': location,
                'detail_url': detail_url,
                **detailed_specs
            }

            all_cars.append(car_data)

            time.sleep(1)

        except Exception as e:
            print(f"Error extracting car: {e}")
            continue

print(f"\n Total cars scraped: {len(all_cars)}")

csv_filename = 'cars45_detailed_data.csv'

if all_cars:
    with open(csv_filename, 'w', newline='', encoding='utf-8') as file:
        all_fieldnames = set()
        for car in all_cars:
            all_fieldnames.update(car.keys())

        fieldnames = sorted(all_fieldnames)

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_cars)

    print(f"saved to {csv_filename}")
    print(f"Columns: {', '.join(fieldnames)}")