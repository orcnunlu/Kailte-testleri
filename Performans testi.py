import requests
import time
import matplotlib.pyplot as plt

def performans_testi(url, num_requests):
    total_time = 0
    response_times = []

    for _ in range(num_requests):
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()
        request_time = end_time - start_time
        total_time += request_time
        response_times.append(request_time)

    average_time = total_time / num_requests
    print("Toplam istek sayısı:", num_requests)
    print("Ortalama yanıt süresi:", average_time, "saniye")

    # Plotting
    plt.plot(response_times, marker='o', linestyle='-')
    plt.title('Response Times')
    plt.xlabel('Request Number')
    plt.ylabel('Response Time (seconds)')
    plt.grid(True)
    plt.show()

url = "http://mb-elbe.de/"
num_requests = 10  # Yapılacak istek sayısı

performans_testi(url, num_requests)
