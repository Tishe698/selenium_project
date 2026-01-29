from selenium.webdriver.common.by import By

button_basket_loc = (By.CSS_SELECTOR, 'input[value="12"] + a')
product_img_two_loc = (By.XPATH, '//img[contains(@alt, "[FURN_1118")]')
modal_header_loc = (By.XPATH, '//h4[text()="Add to cart"]')
search_input_loc = (By.XPATH, '//input[@data-search-type="products"]')
