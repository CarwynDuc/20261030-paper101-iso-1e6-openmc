"""Job S5_0p1cm_30keV: mẫu S5, bề dày 0.1 cm, năng lượng 30 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S5", thickness_cm=0.1, energy_kev=30.0, primaries=@PRIMARIES@)
