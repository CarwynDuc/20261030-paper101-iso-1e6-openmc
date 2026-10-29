"""Job S4_3cm_30keV: mẫu S4, bề dày 3 cm, năng lượng 30 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S4", thickness_cm=3.0, energy_kev=30.0, primaries=@PRIMARIES@)
