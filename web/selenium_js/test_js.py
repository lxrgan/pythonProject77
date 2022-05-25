# -*- coding: utf-8 -*-



class TestJS(Base):

    def test_js_scroll(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("kw").send_key("selenium测试")
        element=self.driver.execute_script("return document.getElementById('su')")
        element.click()
        sleep(5)

