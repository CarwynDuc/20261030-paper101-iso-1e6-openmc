"""Job S7_1p5cm_4000keV: mẫu S7, bề dày 1.5 cm, năng lượng 4000 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S7", thickness_cm=1.5, energy_kev=4000.0, primaries=@PRIMARIES@)
