class modules_loader(object):

    def on_select_timeout(self):
        self._load_modules()
