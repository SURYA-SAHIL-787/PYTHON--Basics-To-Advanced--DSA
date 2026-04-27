import threading
import requests

lock = threading.Lock()
results = {}

def fetch_url(url):
    global results
    try:
        response = requests.get(url, timeout=5)
        content_length = len(response.text)
    except Exception:
        content_length = 0

    with lock:
        results[url] = content_length


def main():
    threads = []

    with open("urls.txt", "r") as f:
        urls = [line.strip() for line in f]

    for url in urls:
        t = threading.Thread(target=fetch_url, args=(url,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Scraping Results:")
    for k, v in results.items():
        print(k, "->", v, "chars")


if __name__ == "__main__":
    main()
