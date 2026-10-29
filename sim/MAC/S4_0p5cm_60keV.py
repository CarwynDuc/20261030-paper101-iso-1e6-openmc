"""Job S4_0p5cm_60keV: mẫu S4, bề dày 0.5 cm, năng lượng 60 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S4", thickness_cm=0.5, energy_kev=60.0, primaries=@PRIMARIES@)
