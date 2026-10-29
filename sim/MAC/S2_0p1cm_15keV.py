"""Job S2_0p1cm_15keV: mẫu S2, bề dày 0.1 cm, năng lượng 15 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S2", thickness_cm=0.1, energy_kev=15.0, primaries=@PRIMARIES@)
