import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
import time

class DeleteNoteTest(unittest.TestCase):
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

    # Elimina la nota y valida que se haya eliminado correctamente y no exista ninguna otra nota con ese nombre
    def test2(self):
        el1 = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Search")
        el1.click()

        el2 = self.driver.find_element(MobileBy.ID, "it.feio.android.omninotes:id/search_src_text")
        el2.send_keys("Dia 17")

        button = TouchAction(self.driver)
        button.tap(x=1324, y=2808).perform()
        
        time.sleep(2)

        button = TouchAction(self.driver)
        button.tap(x=541, y=666).perform()
      
        el4 = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "More options")
        el4.click()

        buttonDelete = self.driver.find_element(MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[6]/android.widget.LinearLayout")
        buttonDelete.click()
        
        el1 = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Search")
        el1.click()

        el2 = self.driver.find_element(MobileBy.ID, "it.feio.android.omninotes:id/search_src_text")
        el2.send_keys("Dia 17")
        
        button = TouchAction(self.driver)
        button.tap(x=1324, y=2808).perform()
        
        time.sleep(2)

        # Encontrar el elemento con el ID 'it.feio.android.omninotes:id/detail_title'
        detail_empty = self.driver.find_element(MobileBy.ID, "it.feio.android.omninotes:id/empty_list")
        texto_actual = detail_empty.text
        texto_esperado = "Nothing here!"
        
        # Realizar la comparación
        self.assertEqual(texto_actual, texto_esperado, f"El texto actual no coincide con el texto esperado: {texto_actual}")
        
if __name__ == '__main__':
    print("Ejecutando la prueba 2, eliminar una nota...")
    unittest.main()
