"""Job S7_0p8cm_2000keV: mẫu S7, bề dày 0.8 cm, năng lượng 2000 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S7", thickness_cm=0.8, energy_kev=2000.0, primaries=@PRIMARIES@)
