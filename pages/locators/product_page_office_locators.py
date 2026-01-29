from selenium.webdriver.common.by import By

product_name_loc = (By.XPATH, "//h1[text() = 'Office Design Software']")
add_product_loc = (By.XPATH, "//a[@aria-label='Add one']")
quantity_product = (By.XPATH, "//input[@name = 'add_qty']")
remove_product_loc = (By.XPATH, "//a[@aria-label='Remove one']")
