"""Job S5_1p5cm_800keV: mẫu S5, bề dày 1.5 cm, năng lượng 800 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S5", thickness_cm=1.5, energy_kev=800.0, primaries=@PRIMARIES@)
