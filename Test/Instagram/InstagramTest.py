from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuración de capacidades del dispositivo y la aplicación
def conector():  
    desired_caps = {
        "deviceName": "emulator-5554",
        "platformName": "Android",
        "appPackage": "com.instagram.android",
        "appActivity": "com.instagram.mainactivity.MainActivity",
        "noReset": True
    }

    # Inicialización del driver de Appium
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# Prueba para enviar un mensaje a algun usuario. 
def sendImbox(driver, nombre_usuario, mensaje): 
    try:
        # Esperar a que aparezcan los elementos antes de interactuar con ellos
        wait = WebDriverWait(driver, 20)
        
        # Interacciones con elementos en la aplicación móvil
        
        # Encontrar y hacer clic en el icono de la bandeja de entrada
        els1 = wait.until(EC.presence_of_all_elements_located((By.ID, "com.instagram.android:id/action_bar_inbox_button")))
        el1 = wait.until(EC.presence_of_element_located((By.ID, "com.instagram.android:id/action_bar_inbox_button")))
        el1.click()
        
        # Encontrar y hacer clic en la barra de búsqueda
        els2 = wait.until(EC.presence_of_all_elements_located((By.ID, "com.instagram.android:id/search_edit_text")))
        el2 = wait.until(EC.presence_of_element_located((By.ID, "com.instagram.android:id/search_edit_text")))
        el2.click()
        
        # Ingresar texto en el campo de búsqueda
        el3 = wait.until(EC.presence_of_element_located((By.ID, "com.instagram.android:id/search_bar_real_field")))
        el3.send_keys(nombre_usuario)
        
        # Encontrar y seleccionar un elemento de la lista de resultados de búsqueda
        els3 = wait.until(EC.presence_of_all_elements_located((By.XPATH, "\t/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.GridView/android.widget.LinearLayout[1]\n")))
        el4 = wait.until(EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.GridView/android.widget.LinearLayout[1]")))
        el4.click()
        
        # Encontrar y hacer clic en el campo de composición de mensaje
        els4 = wait.until(EC.presence_of_all_elements_located((By.ID, "com.instagram.android:id/row_thread_composer_edittext")))
        el5 = wait.until(EC.presence_of_element_located((By.ID, "com.instagram.android:id/row_thread_composer_edittext")))
        el5.click()
        
        # Ingresar mensaje en el campo de composición
        el5.send_keys(mensaje)
        
        # Encontrar y hacer clic en el botón de enviar
        els5 = wait.until(EC.presence_of_all_elements_located((By.ID, "com.instagram.android:id/row_thread_composer_button_send")))
        el6 = wait.until(EC.presence_of_element_located((By.ID, "com.instagram.android:id/row_thread_composer_button_send")))
        el6.click()
        
        # Esperar 5 segundos
        time.sleep(10)

    finally:
        # Cerrar la aplicación al finalizar
        driver.quit()
        print("Prueba terminada")

#Prueba dar like a una fotografia.
def like(driver):
    try:
        # Esperar a que aparezcan los elementos antes de interactuar con ellos
        wait = WebDriverWait(driver, 20)
        
        # Interacciones con elementos en la aplicación móvil
        
        # Encontrar todos los elementos con el ID especificado
        els1 = wait.until(EC.presence_of_all_elements_located((By.ID, "com.instagram.android:id/row_feed_photo_media_tag_hints")))
        
        # Encontrar el primer elemento con el ID especificado y hacer clic
        el1 = wait.until(EC.presence_of_element_located((By.ID, "com.instagram.android:id/row_feed_photo_media_tag_hints")))
        
        #Da doble click
        el1.click()
        el1.click()
    
    finally:
        # Cerrar la aplicación al finalizar
        driver.quit()
        print("Prueba terminada")

def main():
    driver = conector()
    print("Selecciona una opción:")
    print("1. Enviar mensaje a un usuario")
    print("2. Dar like a una fotografía")
    print("3. Salir")
    
    opcion = input("Ingresa el número de la opción deseada: ")
    
    if opcion == "1":
        nombre_usuario = input("Ingresa el nombre de usuario: ")
        mensaje = input("Ingresa el mensaje: ")
        sendImbox(driver, nombre_usuario, mensaje)
    elif opcion == "2":
        like(driver)
    elif opcion == "3":
        exit()
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()





