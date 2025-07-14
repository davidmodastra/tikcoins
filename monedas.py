import time
import pickle
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import flask
#         user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options)
driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
    'source': '''
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        })
    '''
})


cookies_file = "cookies_tiktok.pkl"
espera_carga = 5
espera_en_live = 10
espera_cofre = 5
max_lives = 5
contador_lives = 0


def guardar_cookies():
    with open(cookies_file, "wb") as f:
        pickle.dump(driver.get_cookies(), f)
        print("💾 Cookies guardadas.")

def cargar_cookies():
    if os.path.exists(cookies_file):
        with open(cookies_file, "rb") as f:
            cookies = pickle.load(f)
            for cookie in cookies:
                driver.ºadd_cookie(cookie)
        print("✅ Cookies cargadas.")

def intentar_abrir_cofre():
    try:
        print("🔎 Buscando cofre...")
        cofre = driver.find_element(By.XPATH, '//div[contains(@class, "DivTreasureBoxContainer")]')
        abrir_btns = cofre.find_elements(By.XPATH, './/div[contains(@class, "DivTreasureBoxOpenedButton")]')
        if abrir_btns:
            abrir_btns[0].click()
            print("🎁 ¡Cofre abierto y monedas recogidas!")
            return True
        else:
            print("⏳ Cofre encontrado, pero no disponible aún.")
            return False
    except:
        print("❌ No se encontró cofre.")
        return False


try:
    
    driver.get("https://www.tiktok.com/")
    time.sleep(espera_carga)

   
    if os.path.exists(cookies_file):
        cargar_cookies()
        driver.refresh()
        time.sleep(espera_carga)
    else:
        input("🔐 Inicia sesión manualmente en TikTok y presiona ENTER cuando hayas terminado...")
        guardar_cookies()

    
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(@class,"navbar")]'))
        )
        print("✅ Sesión iniciada correctamente.")
    except:
        print("⚠️ No se detectó sesión iniciada. Revisa manualmente si estás dentro de tu cuenta.")

    
    driver.get("https://www.tiktok.com/live")
    time.sleep(espera_carga)

    
    while contador_lives < max_lives:
        try:
            lives = driver.find_elements(By.XPATH, '//div[contains(@class, "DivLiveCardContainer")]')
            if not lives:
                print("❌ No hay Lives disponibles.")
                break

            print(f"🚀 Entrando al Live #{contador_lives + 1}")
            lives[contador_lives % len(lives)].click()
            time.sleep(espera_carga)

            
            tiempo_viendo = 0
            while tiempo_viendo < espera_en_live:
                if intentar_abrir_cofre():
                    break
                time.sleep(espera_cofre)
                tiempo_viendo += espera_cofre

            
            body = driver.find_element(By.TAG_NAME, 'body')
            body.send_keys(Keys.ESCAPE)
            print("✅ Salí del Live.")
            time.sleep(3)
            contador_lives += 1

        except Exception as e:
            print(f"⚠️ Error en Live: {e}")
            break

    print(f"🏁 Bot terminado. Lives visitados: {contador_lives}")

finally:
    input("🖥️ El navegador sigue abierto. Presiona ENTER para cerrarlo manualmente...")

with open(cookies_file, "wb") as f: 
    pickle.dump(driver.get_cookies(), f)

  # --- Configuración ---------------------------------------------------------
cookies_file   = "cookies_tiktok.pkl"
espera_carga   = 5
espera_en_live = 10
espera_cofre   = 5
max_lives      = 5
contador_lives = 0

# ▼ NUEVO: selectores para el cofre ▼
SELECTOR_COFRE_CONTENEDOR = 'div.tiktok-chest.ephr5mm1'
SELECTOR_COFRE_BOTON      = 'div.tiktok-chest.ephr5mm1 button'  # ajusta si el botón cambia
# --------------------------------------------------------------------------

# ---si falla  --------------------------------------------------------------

import subprocess
import os
import sys
def ejecutar_codigo_principal():
    # Aquí va el código principal que puede fallar
    raise Exception("Error simulado")  # Simulación de error

try:
    ejecutar_codigo_principal()

except Exception as e:
    print("Ha ocurrido un error:", e)

    ruta_codigo_alternativo = r"S:\mejorado.py"  # Cambia esto según el archivo real

    if os.path.exists(ruta_codigo_alternativo):
        # Ejecutar el script alternativo con Python
        subprocess.run(["python", ruta_codigo_alternativo])
    else:
        print("El código alternativo no se encontró en:", ruta_codigo_alternativo)
# --- Fin de la configuración ------------------------------------------------

exec(open("bolsas de obsequios.py").read())  # Ejecuta el código principal del bot
# --- Flujo Principal ---
try:
    driver.get("https://www.tiktok.com/")
    time.sleep(espera_carga)

    if os.path.exists(cookies_file):
        cargar_cookies()
        driver.refresh()
        time.sleep(espera_carga)
    else:
        input("🔐 Inicia sesión manualmente en TikTok y presiona ENTER cuando hayas terminado...")
        guardar_cookies()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(@class,"navbar")]'))
        )
        print("✅ Sesión iniciada correctamente.")
    except:
        print("⚠️ No se detectó sesión iniciada. Revisa manualmente si estás dentro de tu cuenta.")

    driver.get("https://www.tiktok.com/live")
    time.sleep(espera_carga)

    while contador_lives < max_lives:
        try:
            lives = driver.find_elements(By.XPATH, '//div[contains(@class, "DivLiveCardContainer")]')
            if not lives:
                print("❌ No hay Lives disponibles.")
                break

            print(f"🚀 Entrando al Live #{contador_lives + 1}")
            lives[contador_lives % len(lives)].click()
            time.sleep(espera_carga)

            tiempo_viendo = 0
            while tiempo_viendo < espera_en_live:
                if intentar_abrir_cofre():
                    break
                time.sleep(espera_cofre)
                tiempo_viendo += espera_cofre

            body = driver.find_element(By.TAG_NAME, 'body')
            body.send_keys(Keys.ESCAPE)
            print("✅ Salí del Live.")
            time.sleep(8) 
            contador_lives += 1

        except Exception as e:
            print(f"⚠️ Error en Live: {e}")
            break

    print(f"🏁 Bot terminado. Lives visitados: {contador_lives}")
finally:
    input("🖥️ El navegador sigue abierto. Presiona ENTER para cerrarlo manualmente...")
    guardar_cookies()
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Ejecutar en segundo plano
    open("cookies_tiktok.pkl", "wb").close()  # Limpia el archivo de cookiesdriver
    print ("🗑️ Cookies limpiadas.")