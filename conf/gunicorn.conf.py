import multiprocessing
workers = 2 * multiprocessing.cpu_count()
worker_class = "gthread"
bind = ["0.0.0.0:8000"]
reload = True
loglevel = "info"
accesslog = None  # `"-"` means stdout.
## if one needs information of the request that gunicorn receives
# access_log_format = '%({x-forwarded-for}i)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
errorlog = "-"  # command line option: `--log-file`
