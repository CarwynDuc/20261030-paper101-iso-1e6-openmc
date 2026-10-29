"""Job S7_0p5cm_15000keV: mẫu S7, bề dày 0.5 cm, năng lượng 15000 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S7", thickness_cm=0.5, energy_kev=15000.0, primaries=@PRIMARIES@)
