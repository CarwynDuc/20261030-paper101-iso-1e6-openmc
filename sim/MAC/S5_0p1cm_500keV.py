"""Job S5_0p1cm_500keV: mẫu S5, bề dày 0.1 cm, năng lượng 500 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S5", thickness_cm=0.1, energy_kev=500.0, primaries=@PRIMARIES@)
