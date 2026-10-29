"""Job S8_3cm_15000keV: mẫu S8, bề dày 3 cm, năng lượng 15000 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S8", thickness_cm=3.0, energy_kev=15000.0, primaries=@PRIMARIES@)
