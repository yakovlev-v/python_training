from selenium import webdriver


class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")

    def login(self, username, password):
        driver = self.driver
        self.open_home_page()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def open_groups_page(self):
        driver = self.driver
        driver.find_element_by_link_text("groups").click()

    def create_group(self, group):
        driver = self.driver
        # открыть страницу групп
        self.open_groups_page()
        driver.find_element_by_name("new").click()
        # ввод данных группы
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").click()
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(group .header)
        driver.find_element_by_name("group_footer").click()
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(group.footer)
        driver.find_element_by_xpath("//form[@action='/addressbook/group.php']").click()
        driver.find_element_by_name("submit").click()
        self.open_groups_page()

    def logout(self):
        driver = self.driver
        driver.find_element_by_link_text("Logout").click()

    def destroy(self):
        self.driver.quit()