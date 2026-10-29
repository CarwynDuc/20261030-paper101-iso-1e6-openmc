"""Job S4_1p5cm_40keV: mẫu S4, bề dày 1.5 cm, năng lượng 40 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S4", thickness_cm=1.5, energy_kev=40.0, primaries=@PRIMARIES@)
