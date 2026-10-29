"""Job S5_0p005cm_15keV: mẫu S5, bề dày 0.005 cm, năng lượng 15 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S5", thickness_cm=0.005, energy_kev=15.0, primaries=@PRIMARIES@)
