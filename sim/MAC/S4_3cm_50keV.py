"""Job S4_3cm_50keV: mẫu S4, bề dày 3 cm, năng lượng 50 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S4", thickness_cm=3.0, energy_kev=50.0, primaries=@PRIMARIES@)
