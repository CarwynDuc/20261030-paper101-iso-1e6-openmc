"""Job S4_0p3cm_4000keV: mẫu S4, bề dày 0.3 cm, năng lượng 4000 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S4", thickness_cm=0.3, energy_kev=4000.0, primaries=@PRIMARIES@)
