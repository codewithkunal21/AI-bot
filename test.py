import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import pandas as pd  # Excel banane ke liye
import time

driver = uc.Chrome()

try:
    driver.get("https://www.yellowpages.com/search?search_terms=Software&geo_location_terms=Delhi")
    time.sleep(10) 

    cards = driver.find_elements(By.CLASS_NAME, "result")
    
    # 1. Ek khali list banayein data store karne ke liye
    all_leads = []

    for card in cards[:15]: # Pehli 15 leads
        try:
            name = card.find_element(By.CLASS_NAME, "business-name").text
            phone = card.find_element(By.CLASS_NAME, "phones").text
            address = card.find_element(By.CLASS_NAME, "adr").text

            # 2. Data ko ek dictionary mein dalkar list mein add karein
            lead_info = {
                "Company Name": name,
                "Phone Number": phone,
                "Address": address
            }
            all_leads.append(lead_info)
            print(f"Saved: {name}")

        except:
            continue

    # 3. Jab loop khatam ho jaye, Excel file banayein
    df = pd.DataFrame(all_leads)
    df.to_csv("my_leads.csv", index=False) # CSV file ban jayegi
    print("\n✅ Mubarak ho! Aapki 'my_leads.csv' file ban gayi hai.")

except Exception as e:
    print(f"Galti: {e}")

finally:
    driver.quit()