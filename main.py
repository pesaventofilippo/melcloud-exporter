import asyncio
from time import sleep
import prometheus_client as prom
from modules.env import env
from modules import melcloud

melcloud = melcloud.MELCloud(env.MEL_USERNAME, env.MEL_PASSWORD)
METRICS = {
    "RoomTemperature": prom.Gauge(
        name="room_temperature", documentation="Room Temperature",
        namespace=env.PROMETHEUS_PREFIX, labelnames=["device_name"]
    ),
    "OutdoorTemperature": prom.Gauge(
        name="outdoor_temperature", documentation="Outdoor Temperature",
        namespace=env.PROMETHEUS_PREFIX, labelnames=["device_name"]
    ),
    "SetTemperature": prom.Gauge(
        name="set_temperature", documentation="Set Temperature",
        namespace=env.PROMETHEUS_PREFIX, labelnames=["device_name"]
    ),
    "ActualFanSpeed": prom.Gauge(
        name="actual_fan_speed", documentation="Actual Fan Speed",
        namespace=env.PROMETHEUS_PREFIX, labelnames=["device_name"]
    ),
    "FanSpeed": prom.Gauge(
        name="fan_speed", documentation="Fan Speed",
        namespace=env.PROMETHEUS_PREFIX, labelnames=["device_name"]
    ),
    "AutomaticFanSpeed": prom.Gauge(
        name="automatic_fan_speed", documentation="Automatic Fan Speed",
        namespace=env.PROMETHEUS_PREFIX, labelnames=["device_name"]
    ),
    "VaneVerticalDirection": prom.Gauge(
        name="vane_vertical_direction", documentation="Vane Vertical Direction",
        namespace=env.PROMETHEUS_PREFIX, labelnames=["device_name"]
    ),
    "VaneVerticalSwing": prom.Gauge(
        name="vane_vertical_swing", documentation="Vane Vertical Swing",
        namespace=env.PROMETHEUS_PREFIX, labelnames=["device_name"]
    ),
    "VaneHorizontalDirection": prom.Gauge(
        name="vane_horizontal_direction", documentation="Vane Horizontal Direction",
        namespace=env.PROMETHEUS_PREFIX, labelnames=["device_name"]
    ),
    "VaneHorizontalSwing": prom.Gauge(
        name="vane_horizontal_swing", documentation="Vane Horizontal Swing",
        namespace=env.PROMETHEUS_PREFIX, labelnames=["device_name"]
    ),
    "OperationMode": prom.Gauge(
        name="operation_mode", documentation="Operation Mode",
        namespace=env.PROMETHEUS_PREFIX, labelnames=["device_name"]
    ),
    "InStandbyMode": prom.Gauge(
        name="in_standby_mode", documentation="In Standby Mode",
        namespace=env.PROMETHEUS_PREFIX, labelnames=["device_name"]
    ),
    "CurrentEnergyConsumed": prom.Gauge(
        name="current_energy_consumed", documentation="Current Energy Consumed",
        namespace=env.PROMETHEUS_PREFIX, labelnames=["device_name"]
    )
}


async def update_metrics():
    data = await melcloud.get_device_data()
    for device_name, props in data.items():
        for prop, value in props.items():
            METRICS[prop].labels(device_name=device_name).set(value)


if __name__ == "__main__":
    prom.disable_created_metrics()
    prom.REGISTRY.unregister(prom.GC_COLLECTOR)
    prom.REGISTRY.unregister(prom.PROCESS_COLLECTOR)
    prom.REGISTRY.unregister(prom.PLATFORM_COLLECTOR)

    _, web_thread = prom.start_http_server(addr="0.0.0.0", port=env.PROMETHEUS_PORT)
    while True:
        asyncio.run(update_metrics())
        sleep(60)
