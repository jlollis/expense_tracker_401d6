def includeme(config):
    config.add_static_view('static', 'expense_tracker:static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('detail', '/expense/{id:\d+}')
