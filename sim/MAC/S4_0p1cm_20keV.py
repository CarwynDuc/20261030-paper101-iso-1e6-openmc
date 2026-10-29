"""Job S4_0p1cm_20keV: mẫu S4, bề dày 0.1 cm, năng lượng 20 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S4", thickness_cm=0.1, energy_kev=20.0, primaries=@PRIMARIES@)
