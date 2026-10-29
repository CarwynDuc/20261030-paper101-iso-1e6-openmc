"""Job S6_0p1cm_100keV: mẫu S6, bề dày 0.1 cm, năng lượng 100 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S6", thickness_cm=0.1, energy_kev=100.0, primaries=@PRIMARIES@)
