"""Job S8_0p3cm_30keV: mẫu S8, bề dày 0.3 cm, năng lượng 30 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S8", thickness_cm=0.3, energy_kev=30.0, primaries=@PRIMARIES@)
