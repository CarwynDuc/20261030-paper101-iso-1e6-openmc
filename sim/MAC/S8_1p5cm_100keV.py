"""Job S8_1p5cm_100keV: mẫu S8, bề dày 1.5 cm, năng lượng 100 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S8", thickness_cm=1.5, energy_kev=100.0, primaries=@PRIMARIES@)
