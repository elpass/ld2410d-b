"""The hlk2410d_b integration models."""

from dataclasses import dataclass

from ld2410_ble import LD2410BLE

from homeassistant.config_entries import ConfigEntry

from .coordinator import HLK2410DBCoordinator

type HLK2410DBConfigEntry = ConfigEntry[HLK2410DBData]


@dataclass
class HLK2410DBData:
    """Data for the hlk2410d_b integration."""

    title: str
    device: LD2410BLE
    coordinator: HLK2410DBCoordinator
