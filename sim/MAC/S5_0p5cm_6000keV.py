"""Job S5_0p5cm_6000keV: mẫu S5, bề dày 0.5 cm, năng lượng 6000 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S5", thickness_cm=0.5, energy_kev=6000.0, primaries=@PRIMARIES@)
