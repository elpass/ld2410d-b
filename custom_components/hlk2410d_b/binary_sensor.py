"""HLK2410D-B integration binary sensor platform."""

from typing import override

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
    BinarySensorEntityDescription,
)
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from . import LD2410BLE, HLK2410DBCoordinator
from .models import HLK2410DBConfigEntry

ENTITY_DESCRIPTIONS = (
    BinarySensorEntityDescription(
        key="is_moving",
        device_class=BinarySensorDeviceClass.MOTION,
    ),
    BinarySensorEntityDescription(
        key="is_static",
        device_class=BinarySensorDeviceClass.OCCUPANCY,
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: HLK2410DBConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up the platform for HLK2410D-B."""
    data = entry.runtime_data
    async_add_entities(
        HLK2410DBBinarySensor(data.coordinator, data.device, entry.title, description)
        for description in ENTITY_DESCRIPTIONS
    )


class HLK2410DBBinarySensor(
    CoordinatorEntity[HLK2410DBCoordinator], BinarySensorEntity
):
    """Moving/static sensor for HLK2410D-B."""

    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: HLK2410DBCoordinator,
        device: LD2410BLE,
        name: str,
        description: BinarySensorEntityDescription,
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._coordinator = coordinator
        self._key = description.key
        self._device = device
        self.entity_description = description
        self._attr_unique_id = f"{device.address}_{self._key}"
        self._attr_device_info = DeviceInfo(
            name=name,
            connections={(dr.CONNECTION_BLUETOOTH, device.address)},
        )
        self._attr_is_on = getattr(self._device, self._key)

    @callback
    @override
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        self._attr_is_on = getattr(self._device, self._key)
        self.async_write_ha_state()

    @property
    @override
    def available(self) -> bool:
        """Unavailable if coordinator isn't connected."""
        return self._coordinator.connected and super().available
