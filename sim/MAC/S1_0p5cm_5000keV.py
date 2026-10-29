"""Job S1_0p5cm_5000keV: mẫu S1, bề dày 0.5 cm, năng lượng 5000 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S1", thickness_cm=0.5, energy_kev=5000.0, primaries=@PRIMARIES@)
