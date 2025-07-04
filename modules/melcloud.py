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

    async def get_device_data(self) -> dict[str, dict]:
        with aiohttp.ClientSession() as session:
            token = await pymelcloud.login(self.username, self.password, session)
            devices = await pymelcloud.get_devices(token, session)

        res = {}
        for dev in devices[pymelcloud.DEVICE_TYPE_ATA]:
            raw = dev._device_conf
            name = raw.get("DeviceName")
            data = raw.get("Device")
            res[name] = {prop: data[prop] for prop in self.READ_PROPS}

        return res
