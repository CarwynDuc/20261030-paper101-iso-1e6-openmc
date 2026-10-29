"""Job S2_1p5cm_4000keV: mẫu S2, bề dày 1.5 cm, năng lượng 4000 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S2", thickness_cm=1.5, energy_kev=4000.0, primaries=@PRIMARIES@)
