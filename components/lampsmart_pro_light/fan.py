import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import fan
from esphome.const import (
    CONF_DURATION,
    CONF_GROUP,
    CONF_ID,
)

CONF_FANS = "fans"
CONF_LIGHTS = "lights"

AUTO_LOAD = ["esp32_ble"]
DEPENDENCIES = ["esp32"]

lampsmartpro_ns = cg.esphome_ns.namespace('lampsmartpro')
LampSmartProFan = lampsmartpro_ns.class_('LampSmartProFan', cg.Component, fan.Fan)


CONFIG_SCHEMA = fan.fan_schema(LampSmartProFan).extend(
    {
        cv.Optional(CONF_DURATION, default=100): cv.positive_int,
        cv.Optional(CONF_GROUP, default=0x0): cv.hex_uint8_t,
    }
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await fan.register_fan(var, config)

    cg.add(var.set_tx_duration(config[CONF_DURATION]))
    cg.add(var.set_group_id(config[CONF_GROUP]))
