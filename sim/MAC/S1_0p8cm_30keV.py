"""Job S1_0p8cm_30keV: mẫu S1, bề dày 0.8 cm, năng lượng 30 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S1", thickness_cm=0.8, energy_kev=30.0, primaries=@PRIMARIES@)
