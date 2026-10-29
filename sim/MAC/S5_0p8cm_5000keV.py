"""Job S5_0p8cm_5000keV: mẫu S5, bề dày 0.8 cm, năng lượng 5000 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S5", thickness_cm=0.8, energy_kev=5000.0, primaries=@PRIMARIES@)
