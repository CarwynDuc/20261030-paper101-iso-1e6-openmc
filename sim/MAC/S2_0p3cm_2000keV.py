"""Job S2_0p3cm_2000keV: mẫu S2, bề dày 0.3 cm, năng lượng 2000 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S2", thickness_cm=0.3, energy_kev=2000.0, primaries=@PRIMARIES@)
