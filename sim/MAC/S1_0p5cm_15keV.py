"""Job S1_0p5cm_15keV: mẫu S1, bề dày 0.5 cm, năng lượng 15 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S1", thickness_cm=0.5, energy_kev=15.0, primaries=@PRIMARIES@)
