"""Job S1_1p5cm_400keV: mẫu S1, bề dày 1.5 cm, năng lượng 400 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S1", thickness_cm=1.5, energy_kev=400.0, primaries=@PRIMARIES@)
