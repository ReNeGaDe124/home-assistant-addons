from homeassistant.components.text import TextEntity
from homeassistant.helpers.entity import DeviceInfo
import async_timeout
import logging
from .const import DOMAIN, DEVICE_NAME

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, entry, async_add_entities):
    config = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([SubsroSearchInput(config, entry)])

class SubsroSearchInput(TextEntity):
    _attr_has_entity_name = True
    def __init__(self, config, entry):
        self._config, self._entry = config, entry
        self._attr_name = "Search & Download Subtitles"
        self._attr_unique_id = "subsro_search_and_download_subtitles"
        self._attr_icon, self._attr_mode = "mdi:magnify", "text"
        self._attr_native_value = ""

    @property
    def device_info(self) -> DeviceInfo:
        return DeviceInfo(identifiers={(DOMAIN, self._entry.entry_id)}, name=DEVICE_NAME)

    async def async_set_value(self, value: str) -> None:
        self._attr_native_value = value
        self.async_write_ha_state()
        if not value: return

        headers = {"X-Auth-Token": self._config["secret"], "Content-Type": "application/json"}
        try:
            async with async_timeout.timeout(10):
                await self._config["session"].post(
                    f"{self._config['url']}/search_and_download_subtitles", 
                    json={"keywords": value}, 
                    headers=headers
                )
        except Exception as e:

            _LOGGER.error("Eroare căutare: %s", e)




