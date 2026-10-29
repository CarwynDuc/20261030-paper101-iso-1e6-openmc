"""Job S2_1p5cm_80keV: mẫu S2, bề dày 1.5 cm, năng lượng 80 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S2", thickness_cm=1.5, energy_kev=80.0, primaries=@PRIMARIES@)
