# for executing sql queries without setting each field as a argument for a function.
cpu_specs = [
    "name",
    "manufacturer",
    "model",
    "socket",
    "cores",
    "threads",
    "base_clock",
    "boost_clock",
    "tdp",
    "integrated_graphics",
    "lithography",
    "unlocked",
    "cache_l1",
    "cache_l2",
    "cache_l3",
    "max_memory",
    "pcie_version",
    "max_pcie_lanes",
    "release_date"
    #"test_field" <- future implementation of a dynamic function which adds new columns to the database table with ease, without causing data loss
]


gpu_specs = [
    "name",
    "brand",
    "manufacturer",
    "model",
    "vram",
    "vram_type",
    "base_clock",
    "boost_clock",
    "tdp",
    "slot_size",
    "interface",  # e.g., PCIe 4.0 x16
    "ray_tracing",
    "dlss_fsr_xess_support",
    "hdmi",
    "display_port",
    "release_date",
    "architecture",
    "cuda_cores",
    "stream_processors",
    "xmx_engines"
]

mobo_specs = [
    "name",
    "manufacturer",
    "model",
    "socket",
    "chipset",
    "form_factor",
    "memory_slots",
    "max_memory",
    "memory_type",
    "memory_speed_supported",
    "pcie_slots",
    "m2_slots",
    "m2_keys",
    "sata_ports",
    "usb_ports",
    "ethernet_speed",
    "wifi",
    "bluetooth",
    "audio_codec",
    "bios_features",
    "release_date"
]

psu_specs = [
    "name",
    "manufacturer",
    "model",
    "wattage",
    "efficiency_rating",
    "modular",  # Full / Semi / Non
    "form_factor",
    "pcie_connectors",
    "cpu_connectors",
    "sata_connectors",
    "release_date",
    "atx_3_0_compliant"
]

ram_specs = [
    "name",
    "manufacturer",
    "model",
    "type",  # DDR4 / DDR5
    "speed",
    "capacity",
    "modules",  # e.g., 2x16GB
    "ecc",
    "rgb",
    "cas_latency",
    "voltage"
]

case_specs = [
    "name",
    "manufacturer",
    "model",
    "form_factor_support",
    "gpu_clearance",
    "cpu_cooler_clearance",
    "psu_clearance",
    "drive_bays",
    "fan_mounts",
    "radiator_support",
    "front_panel_io",
    "psu_shroud",
    "side_panel_type",
    "rgb",
    "dimensions"
]

mouse_specs = [
    "name",
    "manufacturer",
    "model",
    "sensor",
    "dpi_range",
    "polling_rate",
    "connection_type",  # Wired / Wireless / Bluetooth
    "weight",
    "programmable_buttons",
    "rgb",
    "battery_life"
]

keyboard_specs = [
    "name",
    "manufacturer",
    "model",
    "switch_type",
    "form_factor",
    "connection_type",
    "key_rollover",
    "backlight",
    "programmable_keys",
    "wireless_range",
    "battery_life"
]

monitor_specs = [
    "name",
    "manufacturer",
    "model",
    "size",
    "resolution",
    "refresh_rate",
    "panel_type",
    "response_time",
    "sync_tech",  # G-Sync / FreeSync
    "aspect_ratio",
    "ports",
    "hdr_support",
    "curved",
    "height_adjustable"
]

headset_specs = [
    "name",
    "manufacturer",
    "model",
    "driver_size",
    "connection_type",  # 3.5mm / USB / Wireless
    "mic_type",
    "surround_sound",
    "noise_cancellation",
    "battery_life",
    "rgb",
    "impedance",
    "frequency_response"
]

m2_specs = [
    "name",
    "manufacturer",
    "model",
    "capacity",
    "interface",  # NVMe / SATA
    "form_factor",  # 2280 / 22110 etc.
    "read_speed",
    "write_speed",
    "nand_type",
    "controller",
    "dram_cache",
    "endurance_tbw"
]

hdd_specs = [
    "name",
    "manufacturer",
    "model",
    "capacity",
    "rpm",
    "cache",
    "form_factor",
    "interface",  # SATA / SAS
    "reliability_rating",
    "warranty"
]

sata_ssd_specs = [
    "name",
    "manufacturer",
    "model",
    "capacity",
    "form_factor",
    "read_speed",
    "write_speed",
    "nand_type",
    "dram_cache",
    "interface"
]

mouse_pad_specs = [
    "name",
    "manufacturer",
    "model",
    "size",
    "material",
    "rgb",
    "thickness",
    "anti_slip_base"
]

table_specs = {
    "cpu": {spec: "TEXT" for spec in cpu_specs},
    "gpu": {spec: "TEXT" for spec in gpu_specs},
    "mobo": {spec: "TEXT" for spec in mobo_specs},
    "psu": {spec: "TEXT" for spec in psu_specs},
    "ram": {spec: "TEXT" for spec in ram_specs},
    "pc_case": {spec: "TEXT" for spec in case_specs},
    "mouse": {spec: "TEXT" for spec in mouse_specs},
    "keyboard": {spec: "TEXT" for spec in keyboard_specs},
    "monitor": {spec: "TEXT" for spec in monitor_specs},
    "headset": {spec: "TEXT" for spec in headset_specs},
    "m2": {spec: "TEXT" for spec in m2_specs},
    "hdd": {spec: "TEXT" for spec in hdd_specs},
    "sata_ssd": {spec: "TEXT" for spec in sata_ssd_specs},
    "mouse_pad": {spec: "TEXT" for spec in mouse_pad_specs}
}