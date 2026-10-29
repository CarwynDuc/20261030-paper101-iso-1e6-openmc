"""Job S2_0p8cm_10000keV: mẫu S2, bề dày 0.8 cm, năng lượng 10000 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S2", thickness_cm=0.8, energy_kev=10000.0, primaries=@PRIMARIES@)
