class UnifiConfig(object):
    def __init__(self, instance) -> None:
        # Use self.instance to read the check configuration
        self.url = instance.get("url", "")
        self.user = instance.get("user", "")
        self.password = instance.get("pwd", "")
        self.site = instance.get("site", "default")
        self.version = instance.get("version", "")
        self.tags = [f"url:{self.url}", f"site:{self.site}"] + instance.get("tags", [])
