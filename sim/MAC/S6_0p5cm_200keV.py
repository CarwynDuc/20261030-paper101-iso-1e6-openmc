"""Job S6_0p5cm_200keV: mẫu S6, bề dày 0.5 cm, năng lượng 200 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S6", thickness_cm=0.5, energy_kev=200.0, primaries=@PRIMARIES@)
