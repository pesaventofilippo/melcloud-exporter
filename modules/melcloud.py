import aiohttp
import pymelcloud


class MELCloud:
    READ_PROPS = (
        "RoomTemperature", "OutdoorTemperature", "SetTemperature",
        "ActualFanSpeed", "FanSpeed", "AutomaticFanSpeed",
        "VaneVerticalDirection", "VaneVerticalSwing", "VaneHorizontalDirection", "VaneHorizontalSwing",
        "OperationMode", "InStandbyMode", "CurrentEnergyConsumed"
    )

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self._session = aiohttp.ClientSession()
        self._devices = None

    async def login(self):
        token = await pymelcloud.login(self.username, self.password, self._session)
        devices = await pymelcloud.get_devices(token, self._session)
        self._devices = devices[pymelcloud.DEVICE_TYPE_ATA]

    async def get_device_data(self) -> dict[str, dict]:
        if not self._devices:
            await self.login()

        res = {}
        for dev in self._devices:
            raw = dev._device_conf
            name = raw.get("DeviceName")
            data = raw.get("Device")
            res[name] = {prop: data[prop] for prop in self.READ_PROPS}

        return res
