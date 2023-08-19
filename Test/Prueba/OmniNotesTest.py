from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

# Configuración de capacidades del dispositivo y la aplicación
def conector():  
    desired_caps = {
        "deviceName": "emulator-5554",
        "platformName": "android",
        "appPackage": "it.feio.android.omninotes",
        "appActivity": "it.feio.android.omninotes.MainActivity",
        "noReset": True
    }

    # Inicialización del driver de Appium
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# Busca y elimina un nota especifica.
def searchNote(driver, title):
        wait = WebDriverWait(driver, 20)
        
        # Interacciones con elementos en la aplicación móvil
        findSearch = wait.until(EC.presence_of_all_elements_located((By.ID, "it.feio.android.omninotes:id/menu_search")))
        search = wait.until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Search")))
        search.click()
        
        # Interacciones con la barra de busqueda
        findSearchText = wait.until(EC.presence_of_all_elements_located((By.ID, "it.feio.android.omninotes:id/search_src_text")))
        searchText = wait.until(EC.presence_of_element_located((By.ID, "it.feio.android.omninotes:id/search_src_text")))
        searchText.send_keys(title)
        
        # Boton de buscar en el teclado
        buttom = TouchAction(driver)
        buttom.tap(x=1322, y=2823).perform()
        
        # Encontrar y hacer clic en el botón de apertura del menú lateral
        el7 = driver.find_element(By.ACCESSIBILITY_ID, "drawer open")
        el7.click()
        
        # Tiempo de espera 
        time.sleep(10)

# Elimina una nota con titulo especifico.        
def deleteNote(driver):
        wait = WebDriverWait(driver, 20)
        
        # Boton de buscar en el teclado
        buttom = TouchAction(driver)
        buttom.tap(x=1322, y=2823).perform()
        
        # Simular un toque en las coordenadas (912, 491)
        buttonAction = TouchAction(driver)
        buttonAction.tap(x=912, y=491).perform()
            
        # Interacciones con elementos en la aplicación móvil
        findMoreOption = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//android.widget.ImageView[@content-desc='More options']")))
        moreOption = wait.until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "More options")))
        moreOption.click()
        
        # Eliminar nota    
        findButtonDelete = wait.until(EC.presence_of_all_elements_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[6]/android.widget.LinearLayout")))
        buttonDelete = wait.until(EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[6]/android.widget.LinearLayout")))
        buttonDelete.click()
        
        # Tiempo de espera 
        time.sleep(10)
        

def createNoteTest(driver, validation):
        # Encontrar y hacer clic en el botón de expansión de menú
        el3 = driver.find_element(By.ID, "it.feio.android.omninotes:id/fab_expand_menu_button")
        el3.click()

        # Encontrar y hacer clic en el botón para crear una nueva nota
        el4 = driver.find_element(By.ID, "it.feio.android.omninotes:id/fab_note")
        el4.click()

        # Encontrar y enviar texto al campo de título de la nota
        el5 = driver.find_element(By.ID, "it.feio.android.omninotes:id/detail_title")
        el5.send_keys("Dia 17")

        # Encontrar y enviar texto al campo de contenido de la nota
        el6 = driver.find_element(By.ID, "it.feio.android.omninotes:id/detail_content")
        el6.send_keys("Hola 17")

        # Encontrar y hacer clic en el botón de apertura del menú lateral
        el7 = driver.find_element(By.ACCESSIBILITY_ID, "drawer open")
        el7.click()

        # Encontrar y hacer clic en un elemento específico en la jerarquía utilizando XPath
        el8 = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout")
        el8.click()

        elemento = driver.find_element(By.ID, "it.feio.android.omninotes:id/detail_title")

        # Obtener el texto del elemento
        texto_elemento = elemento.text

        # Valor con el cual deseas comparar
        valor_esperado = validation

        # Comparar el texto del elemento con el valor esperado
        if texto_elemento == valor_esperado:
            return True
        else :
            return False
      

def main():
    driver = conector()
    deleteNote(driver)
    # Cerrar la aplicación al finalizar
    driver.quit()


if __name__ == "__main__":
    main()





