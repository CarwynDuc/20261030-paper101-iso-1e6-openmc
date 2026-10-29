"""Job S5_0p1cm_2000keV: mẫu S5, bề dày 0.1 cm, năng lượng 2000 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S5", thickness_cm=0.1, energy_kev=2000.0, primaries=@PRIMARIES@)
