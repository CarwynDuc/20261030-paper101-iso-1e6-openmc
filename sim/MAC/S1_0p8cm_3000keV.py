"""Job S1_0p8cm_3000keV: mẫu S1, bề dày 0.8 cm, năng lượng 3000 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S1", thickness_cm=0.8, energy_kev=3000.0, primaries=@PRIMARIES@)
