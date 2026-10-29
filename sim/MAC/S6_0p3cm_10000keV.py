"""Job S6_0p3cm_10000keV: mẫu S6, bề dày 0.3 cm, năng lượng 10000 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S6", thickness_cm=0.3, energy_kev=10000.0, primaries=@PRIMARIES@)
