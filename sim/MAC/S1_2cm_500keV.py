"""Job S1_2cm_500keV: mẫu S1, bề dày 2 cm, năng lượng 500 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S1", thickness_cm=2.0, energy_kev=500.0, primaries=@PRIMARIES@)
