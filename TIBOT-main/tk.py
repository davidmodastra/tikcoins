import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# RUTA A TU PERFIL FIREFOX
firefox_profile_path = r"C:\Users\DAVID\AppData\Roaming\Mozilla\Firefox\Profiles\wx8f8rj8.default-release"

def open_tiktok_live_firefox(account):
    print("[INFO] Configurando opciones de Firefox...")
    options = Options()
    options.set_preference("profile", firefox_profile_path)
    options.set_preference("dom.webdriver.enabled", False)

    print("[INFO] Iniciando driver de Firefox...")
    driver = webdriver.Firefox(options=options)

    try:
        url = f"https://www.tiktok.com/@{account}/live"
        print(f"[INFO] Abriendo URL: {url}")
        driver.get(url)
        time.sleep(10)

        print("[INFO] Buscando botón de monedas...")
        coin_button = driver.find_element("xpath", '//button[@aria-label="Coin"]')
        coin_button.click()
        print("[OK] Monedas recolectadas correctamente.")
    except Exception as e:
        print(f"[ERROR] No se pudo recolectar monedas: {e}")
    finally:
        time.sleep(3)
        driver.quit()
        print("[INFO] Driver cerrado.")

if __name__ == "__main__":
    cuenta = input("Ingresa el nombre de usuario de TikTok: ").strip()
    open_tiktok_live_firefox(cuenta)
