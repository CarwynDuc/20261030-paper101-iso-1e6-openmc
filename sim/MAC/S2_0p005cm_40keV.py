"""Job S2_0p005cm_40keV: mẫu S2, bề dày 0.005 cm, năng lượng 40 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S2", thickness_cm=0.005, energy_kev=40.0, primaries=@PRIMARIES@)
