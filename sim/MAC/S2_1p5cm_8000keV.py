"""Job S2_1p5cm_8000keV: mẫu S2, bề dày 1.5 cm, năng lượng 8000 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S2", thickness_cm=1.5, energy_kev=8000.0, primaries=@PRIMARIES@)
