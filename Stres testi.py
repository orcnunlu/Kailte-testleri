import threading
import requests

# İstek gönderme fonksiyonu
def send_requests(url):
    while True:
        try:
            response = requests.get(url)
            print(response.status_code)
            # Sınıra gelindiğinde "Sınır burada" mesajını göster
            if response.status_code != 200:
                print("Sınır burada!")
                break
        except Exception as e:
            print("Error:", e)

# Stres testi fonksiyonu
def stress_test(url, num_threads):
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=send_requests, args=(url,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

url = "http://mb-elbe.de/"
num_threads = 10  # Eşzamanlı istek sayısı (thread sayısı) - isteğinizi kontrol altında tutun

stress_test(url, num_threads)
