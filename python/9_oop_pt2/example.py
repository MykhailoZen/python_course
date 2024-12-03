import abc


class Device:

    def __init__(self, id):
        self._id = id

    @property
    def get_id(self):
        return self._id

    def __increment(self):
        self._id = +1


class MobileDevice(Device):

    def call(self, number):
        print(f"calling {number}")

    def open_store(self):
        print("default")


class Android(MobileDevice):

    def __init__(self, id, google_account):
        super().__init__(id)
        self.__google_account = google_account

    def open_store(self):
        if self.__google_account:
            print(f"opening google market using {self.__google_account}")


class IOS(MobileDevice):

    def __init__(self, id, apple_id, is_tablet=False):
        super().__init__(id)
        self.__apple_id = apple_id
        self.__is_tablet = is_tablet

    def open_store(self):
        print("opening app store")

    def call(self, number):
        if self.__apple_id:
            print("offer to call with facetime")
        else:
            super().call(number)


# Polymorphism


class DeviceFarm:

    def __init__(self, devices):
        self.__devices = devices

    def open_store_on_all_devices(self):
        for device in self.__devices:
            device.open_store()

    def __len__(self):
        return len(self.__devices)


devices = [
    IOS("111", "AA", False),
    Android("222", "322@gamil"),
    Android("333", "555@gamil"),
]
device_farm = DeviceFarm(devices)
device_farm.open_store_on_all_devices()


# Abstraction


class BaseDbClient:

    def connect(self):
        pass

    def query_all(self):
        pass
