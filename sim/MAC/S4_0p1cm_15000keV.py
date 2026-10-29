"""Job S4_0p1cm_15000keV: mẫu S4, bề dày 0.1 cm, năng lượng 15000 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S4", thickness_cm=0.1, energy_kev=15000.0, primaries=@PRIMARIES@)
