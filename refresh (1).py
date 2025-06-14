def schedule_refresh(root, update_func, delay=4000):
    def refresher():
        if root.winfo_exists():
            update_func()
            root.after(delay, refresher)
    if root.winfo_exists():
        root.after(delay, refresher)
