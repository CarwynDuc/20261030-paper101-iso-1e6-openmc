"""Job S2_0p005cm_20keV: mẫu S2, bề dày 0.005 cm, năng lượng 20 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S2", thickness_cm=0.005, energy_kev=20.0, primaries=@PRIMARIES@)
