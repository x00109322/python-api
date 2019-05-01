import multiprocessing

entrypoint: gunicorn -c gunicorn.conf.py -b :$PORT
workers = multiprocessing.cpu_count() * 2 + 1
