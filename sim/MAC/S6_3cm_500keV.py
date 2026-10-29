"""Job S6_3cm_500keV: mẫu S6, bề dày 3 cm, năng lượng 500 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S6", thickness_cm=3.0, energy_kev=500.0, primaries=@PRIMARIES@)
