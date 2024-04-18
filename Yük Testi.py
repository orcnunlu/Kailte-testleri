import requests
import time
import matplotlib.pyplot as plt

def load_test(url, num_requests):
    successes = 0
    failures = 0
    start_time = time.time()

    for _ in range(num_requests):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                successes += 1
            else:
                failures += 1
        except Exception as e:
            print("Error:", e)
            failures += 1

    end_time = time.time()
    total_time = end_time - start_time
    print("Total requests:", num_requests)
    print("Successful requests:", successes)
    print("Failed requests:", failures)
    print("Total time:", total_time)
    print("Requests per second:", num_requests / total_time)

    # Plotting
    labels = ['Successful', 'Failed']
    data = [successes, failures]
    plt.bar(labels, data, color=['green', 'red'])
    plt.title('Request Performance')
    plt.xlabel('Request Status')
    plt.ylabel('Number of Requests')
    plt.show()

url = "http://mb-elbe.de/"
num_requests = 300  # Adjust as needed

load_test(url, num_requests)
