"""Job S7_1p5cm_40keV: mẫu S7, bề dày 1.5 cm, năng lượng 40 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S7", thickness_cm=1.5, energy_kev=40.0, primaries=@PRIMARIES@)
