import threading
from collections import defaultdict

lock = threading.Lock()
log_counts = defaultdict(int)

def process_chunk(lines):
    global log_counts
    local_counts = defaultdict(int)

    for line in lines:
        parts = line.strip().split()
        if len(parts) < 2:
            continue
        level = parts[1]
        local_counts[level] += 1

    # thread-safe merge
    with lock:
        for k, v in local_counts.items():
            log_counts[k] += v


def chunkify(file_path, chunk_size=50):
    with open(file_path, "r") as f:
        chunk = []
        for line in f:
            chunk.append(line)
            if len(chunk) == chunk_size:
                yield chunk
                chunk = []
        if chunk:
            yield chunk


def main():
    threads = []

    for chunk in chunkify("app.log", 100):
        t = threading.Thread(target=process_chunk, args=(chunk,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Log Level Counts:", dict(log_counts))


if __name__ == "__main__":
    main()
