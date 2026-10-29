"""Job S4_1p5cm_800keV: mẫu S4, bề dày 1.5 cm, năng lượng 800 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S4", thickness_cm=1.5, energy_kev=800.0, primaries=@PRIMARIES@)
