import unittest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
import time

class SearchNote(unittest.TestCase):
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

    # Busca una nota en especifico y valida que el titulo sea igual al texto que se ingresó en la barra de buscar.
    def test_search(self):
        # Interacciones con elementos en la aplicación móvil
        search = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Search")
        search.click()

        # Interacciones con la barra de búsqueda
        searchText = self.driver.find_element(MobileBy.ID, "it.feio.android.omninotes:id/search_src_text")
        searchText.send_keys("Prueba 1")

        # Boton de buscar en el teclado
        button = TouchAction(self.driver)
        button.tap(x=1319, y=2832).perform()
        
        time.sleep(2)

        # Encontrar y hacer clic en el botón de apertura del menú lateral
        button = TouchAction(self.driver)
        button.tap(x=541, y=666).perform()

        # Encontrar el elemento con el ID 'it.feio.android.omninotes:id/detail_title'
        detail_title_element = self.driver.find_element(MobileBy.ID, "it.feio.android.omninotes:id/detail_title")
        texto_actual = detail_title_element.text

        # Texto esperado para la comparación
        texto_esperado = "Prueba 1"

        # Realizar la comparación
        self.assertEqual(texto_actual, texto_esperado, f"El texto actual no coincide con el texto esperado: {texto_actual}")

if __name__ == '__main__':
    unittest.main()
