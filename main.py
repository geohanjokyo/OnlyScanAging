import unittest
import os
from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction



class OnlyScanAging(unittest.TestCase):

    def setUp(self):
        # Set up appium
        self.driver = webdriver.Remote(
            command_executor='http://localhost:4723/wd/hub',
            desired_capabilities={
                "platformName": "Android",
                "platformVersion": "11",# 실행할 폰에 맞추어 정보 수정 필요
                "deviceName": "A40",# 실행할 폰에 맞추어 정보 수정 필요
                "automationName": "Appium",
                "newCommandTimeout": 3000,
                "appPackage": "com.koamtac.ktsync",
                "appActivity": "com.koamtac.ktsync.MainActivity",
                "udid": "R59M702GR4B",# 실행할 폰에 맞추어 정보 수정 필요
                "noReset": "True"  # app 데이터 유지
            })


    def test_search_field(self):
        # appiun의 webdriver를 초기화 합니다.
        driver = self.driver
        # KTSync 실행하고 10초 대기
        sleep(10)
        # Aging Delay 선언
        delay = 1
        #설정한 Delay 주기로 고정된 좌표를 반목 tap
        while True:
            self.driver.tap([(530,1900)])
            sleep(delay)


def tearDown(self):
    self.driver.quit()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(OOnlyScanAgin)
    unittest.TextTestRunner(verbosity=2).run(suite)
