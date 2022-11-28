class MobilePhone:

    def __init__(self, manufacter: str, screen_size: float, num_cores: int):
        self.manufacter = manufacter
        self.screen_size = screen_size
        self.num_cores = num_cores
        self.status = 0
        self.apps = []

    def power_on(self):
        self.status = True

    def power_off(self):
        self.status = False

    def install_app(self, app: str):
        self.apps.append(app)

    def install_apps(self, *apps: str):
        self.apps.extend(apps)

    def uninstall_app(self, app: str):
        self.apps.remove(app)


huawei_40_pro = MobilePhone("Huawei", 6.5, 24)
print(huawei_40_pro.manufacter)
huawei_40_pro.power_on()
print(huawei_40_pro.status)
huawei_40_pro.power_off()
print(huawei_40_pro.status)
huawei_40_pro.install_app("Telegram")
huawei_40_pro.install_app("WhatsApp")
huawei_40_pro.install_app("Facebook")
huawei_40_pro.install_apps("Gmail", "Google")
print(huawei_40_pro.apps)
huawei_40_pro.uninstall_app("Facebook")
print(huawei_40_pro.apps)

iphone_13_pro = MobilePhone("Apple", 6.1, 16)
print(iphone_13_pro.manufacter)
iphone_13_pro.install_app("Apple Store")
print(iphone_13_pro.apps)


def install_multiple_apps(self, *apps):
    for app in apps:
        self.apps.append(app)


def uninstall_multiple_apps(self, *apps):
    for app in apps:
        self.apps.remove(app)


iphone_13_pro.install_multiple_apps = install_multiple_apps
iphone_13_pro.install_multiple_apps(iphone_13_pro, "Facebook", "Gmail")
print(iphone_13_pro.apps)

iphone_13_pro.uninstall_multiple_apps = uninstall_multiple_apps
iphone_13_pro.uninstall_multiple_apps(iphone_13_pro, "Facebook", "Gmail")
print(iphone_13_pro.apps)
