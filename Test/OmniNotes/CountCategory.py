import unittest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

class CountCategory(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            "deviceName": "emulator-5554",
            "platformName": "android",
            "appPackage": "it.feio.android.omninotes",
            "appActivity": "it.feio.android.omninotes.MainActivity",
            "noReset": True
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_category(self):
        el2 = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "drawer open")
        el2.click()

        el3 = self.driver.find_element(MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.ListView[2]/android.widget.LinearLayout[1]/android.widget.TextView[1]")

        titulo_categoria = el3.text

        if titulo_categoria == "Dev":
            cantidad = self.driver.find_element(MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.ListView[2]/android.widget.LinearLayout[1]/android.widget.TextView[2]")

            cantidad_notas = int(cantidad.text)
            cantidad_esperada = 3

            self.assertEqual(cantidad_notas, cantidad_esperada, f"La cantidad actual no coincide con la cantidad esperada: {cantidad_notas}")
        else:
            print("No es la categoría dev")

if __name__ == '__main__':
    print("Ejecutando prueba 4")
    unittest.main()
