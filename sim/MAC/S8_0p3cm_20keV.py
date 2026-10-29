"""Job S8_0p3cm_20keV: mẫu S8, bề dày 0.3 cm, năng lượng 20 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S8", thickness_cm=0.3, energy_kev=20.0, primaries=@PRIMARIES@)
