"""Job S4_0p8cm_800keV: mẫu S4, bề dày 0.8 cm, năng lượng 800 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S4", thickness_cm=0.8, energy_kev=800.0, primaries=@PRIMARIES@)
