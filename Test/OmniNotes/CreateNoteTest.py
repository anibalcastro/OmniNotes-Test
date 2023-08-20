import unittest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy  # Agregamos la importación que faltaba

class CreateNoteTest(unittest.TestCase):
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

    # Crea una nota, y verifica que el texto creado sea igual al texto que se espera.
    def test1(self):
        # Cambiamos `driver.find_element` a `self.driver.find_element`
        el3 = self.driver.find_element(MobileBy.ID, "it.feio.android.omninotes:id/fab_expand_menu_button")
        el3.click()

        el4 = self.driver.find_element(MobileBy.ID, "it.feio.android.omninotes:id/fab_note")
        el4.click()

        el5 = self.driver.find_element(MobileBy.ID, "it.feio.android.omninotes:id/detail_title")
        el5.send_keys("Hola esto es una prueba")

        el6 = self.driver.find_element(MobileBy.ID, "it.feio.android.omninotes:id/detail_content")
        el6.send_keys("Hola mundo")

        el7 = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "drawer open")
        el7.click()

        el8 = self.driver.find_element(MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[2]")
        el8.click()

        # Cambiamos `driver.find_element` a `self.driver.find_element`
        elemento = self.driver.find_element(MobileBy.ID, "it.feio.android.omninotes:id/detail_title")

        texto_actual = elemento.text
        texto_esperado = "Hola mundo"  # Cambiamos el valor esperado a "Hola mundo"

        self.assertEqual(texto_actual, texto_esperado, f"El texto actual no coincide con el texto esperado: {texto_actual}")

if __name__ == '__main__':
    print("Ejecutando prueba 1, creando una nota y buscando la nota recien creada...")
    unittest.main()
