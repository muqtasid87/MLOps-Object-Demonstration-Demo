from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import os
import schedule
import time
from datetime import datetime, timedelta

counter = 0

def scrape_images():
    
    print("Started Scraping Images")
    global counter
    
    edge_driver_path = 'src\\utils\\scraper\\driver\\msedgedriver.exe'
    edge_options = Options()
    edge_options.add_argument('--disable-gpu')
    edge_options.add_argument("--start-minimized")
    edge_options.add_argument('--ignore-certificate-errors')
    edge_options.add_argument('--headless')  # Uncomment if you want to run headless
    edge_options.add_argument("--window-size=1920,1080")
    edge_options.add_argument("--log-level=3") 
    edge_options.add_experimental_option("detach", True)
    service = Service(edge_driver_path)
    driver = webdriver.Edge(service=service, options=edge_options)
    # driver.maximize_window()    
    driver.get('https://www.llm.gov.my/awam/cctv')

    # Interact with the dropdown
    dropdown = driver.find_element(By.ID, "cctvhighway")
    select = Select(dropdown)
    select.select_by_index(9)
    time.sleep(2)
    
    save_dir = "src\\utils\\scraper\\scraped_images"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        
    images = driver.find_elements(By.XPATH, "//img[@class='border']")[3:]
    toll_plazas = ["Chenor", "Gambang", "Jabor", "Karak", "Kuantan","Lanchang", "Maran", "Temerloh"]
    for index, img in enumerate(images):
        src = img.get_attribute('src')
        if src:
            filename = os.path.join(save_dir, toll_plazas[index] + '.png')
            with open(filename, 'wb') as f:
                f.write(driver.find_element(By.XPATH, f"//img[@src='{src}']").screenshot_as_png)
        


    driver.quit()

def get_time_until_next_run(next_run):
    now = datetime.now()
    countdown = next_run - now
    return countdown

file = "src\\utils\\scraper\\scraped_images\\timer\\timer.txt"

# Schedule the task to run every 30 seconds
schedule.every(30).seconds.do(scrape_images)

while True:
    # Get the next job in the schedule
    job = schedule.next_run()
    if job:
        time_until_next_task = get_time_until_next_run(job)
        with open(file, 'w') as f:
            f.write(str(time_until_next_task.seconds))
    # Run pending jobs
    schedule.run_pending()

    # Sleep for a short time to avoid busy-waiting
    time.sleep(1)
