import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
unittest.TestLoader.sortTestMethodsUsing = None

class SwagTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Safari()
        cls.driver.get("https://www.saucedemo.com/v1/index.html")
        user_name_element = WebDriverWait(cls.driver,10).until(EC.presence_of_element_located((By.ID,
         "user-name")))
        user_name_element.send_keys("standard_user")
        #cls.driver.fullscreen_window()
        cls.driver.set_window_rect(0, 0, 1400, 1024)
        sleep(2)
        action = ActionChains(cls.driver)
        action.click(on_element=user_name_element)
        action.perform() # performs the click action

        pass_element = cls.driver.find_element(By.ID,"password")
        pass_element.send_keys("secret_sauce")
        action.reset_actions()
        action.click(on_element = pass_element)
        action.perform() # performs the click action
        sleep(2)
        # Clicking the LOGIN button
        login_element = cls.driver.find_element(By.ID,"login-button")
        action.reset_actions()
        action.click(on_element = login_element)
        action.perform() # performs the click action
        sleep(2)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()    #closes the browser window
    

    def test_01_count_items(self):
        """ Checks the number of items displayed on the main page"""
        item_list = self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        self.assertEqual(6,len(item_list))

    def test_02_add_to_cart(self):
        """Checks if element is added to the cart"""
        element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,
         "/html/body/div/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/button")))
        action = ActionChains(self.driver)
        action.click(on_element=element)
        action.perform() # performs the click action
        sleep(3)
        itemCountElement = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,
         "/html/body/div/div[2]/div[1]/div[2]/a/span")))
        self.assertEqual(itemCountElement.text,"1")

    def test_03_remove_from_cart(self):
        """Checks if element is removed from the cart"""
        element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,
         "/html/body/div/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/button")))
        action = ActionChains(self.driver)
        action.click(on_element=element)
        action.perform() # performs the click action
        sleep(2)
        self.assertEqual(element.text,"ADD TO CART")


    def test_04_back_button(self):
        """Testing the back button"""
        element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,
        "/html/body/div/div[2]/div[2]/div/div[2]/div/div[4]/div[2]/a/div")))
        action = ActionChains(self.driver)
        action.click(on_element=element)
        action.perform() # performs the click action
        sleep(3)

        # Finding and clicking the back button
        element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,
        "/html/body/div/div[2]/div[2]/div/button")))
        action.reset_actions()
        action.click(on_element=element)
        action.perform() # performs the click action
        sleep(3)

        item_list = self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        self.assertEqual(6,len(item_list))

    def test_05_logout(self):
        """Test if user can log out"""
        element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,
        "bm-burger-button")))
        action = ActionChains(self.driver)
        action.click(on_element=element)
        action.perform() # performs the click action
        sleep(3)

        element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,
        "logout_sidebar_link")))
        action.reset_actions()
        action.click(on_element=element)
        action.perform() # performs the click action
        sleep(3)

        
if __name__ == '__main__':
    unittest.main()   # execution of the tests from command line