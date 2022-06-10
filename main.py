from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
import database

options = ChromeOptions()
options.add_argument('--window-size=1920,1080')

driver = Chrome('chromedriver.exe', options=options)
driver.minimize_window()

def next_page():
    driver.find_element(By.CLASS_NAME, 'pager-next').click()


def get_blocks():
    elements = driver.find_elements(By.CLASS_NAME, 'model-short-block')
    return elements


def get_info_from_block(block):
    name = block.find_element(By.CLASS_NAME, 'u').text
    link = block.find_element(By.CLASS_NAME, 'no-u').get_attribute('href')

    img = block.find_element(By.CLASS_NAME, 'list-img')\
        .find_element(By.TAG_NAME, 'img')\
        .get_attribute('src')

    print(name, link, img)
    database.add_item(name, link, img)


def main():
    driver.get('https://ek.ua/list/298/')
    while True:
        # sleep(2)
        blocks = get_blocks()
        for block in blocks:
            get_info_from_block(block)
        try:
            next_page()
        except:
            driver.close()
            break

    database.commit()




if __name__ == "__main__":
    main()