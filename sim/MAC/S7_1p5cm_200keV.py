"""Job S7_1p5cm_200keV: mẫu S7, bề dày 1.5 cm, năng lượng 200 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S7", thickness_cm=1.5, energy_kev=200.0, primaries=@PRIMARIES@)
