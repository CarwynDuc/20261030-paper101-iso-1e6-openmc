"""Job S6_0p5cm_100keV: mẫu S6, bề dày 0.5 cm, năng lượng 100 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S6", thickness_cm=0.5, energy_kev=100.0, primaries=@PRIMARIES@)
