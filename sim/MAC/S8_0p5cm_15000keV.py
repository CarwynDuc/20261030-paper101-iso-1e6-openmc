"""Job S8_0p5cm_15000keV: mẫu S8, bề dày 0.5 cm, năng lượng 15000 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S8", thickness_cm=0.5, energy_kev=15000.0, primaries=@PRIMARIES@)
