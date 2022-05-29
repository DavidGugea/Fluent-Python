from concurrent import futures

from flags import save_flag, get_flag, show, main

MAX_WORKERS = 20  # Maximum number of threads to be used in the ThreadPoolExecutor


def download_one(cc):
    """
    Function to download a single image; this is what each thread will execute.
    """
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc


def download_many(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))  # Set the number of worker threads: sue the smaller number between the maximum we want to allow (MAX_WORKERS) and the actual items to be processed, so no unnecessary threads are created.
    with futures.ThreadPoolExecutor(workers) as executor:  # Instantiate the ThreadPoolExecutor with that number of worker threads; teh executor.__exit__ method will call executor.shutdown(wait=True, which will block untill ahl threads are done
        res = executor.map(download_one, sorted(cc_list))  # The map method is similar to the map built-in, except that the download_one function will be called concurrently from multiple threads; it returns a generator that can be iterated over to retrieve the value returned by each function
        return len(list(res))  # Return the number of results obtained; if any of the threaded calls raised an exception, that exception would be raised here as the implicit next() call tried to retrieve the corresponding return value from the iterator.


if __name__ == '__main__':
    main(download_many)