"""Job S5_0p5cm_4000keV: mẫu S5, bề dày 0.5 cm, năng lượng 4000 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S5", thickness_cm=0.5, energy_kev=4000.0, primaries=@PRIMARIES@)
