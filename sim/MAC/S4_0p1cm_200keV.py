"""Job S4_0p1cm_200keV: mẫu S4, bề dày 0.1 cm, năng lượng 200 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S4", thickness_cm=0.1, energy_kev=200.0, primaries=@PRIMARIES@)
