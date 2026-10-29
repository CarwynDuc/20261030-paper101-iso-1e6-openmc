"""Job S1_3cm_5000keV: mẫu S1, bề dày 3 cm, năng lượng 5000 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S1", thickness_cm=3.0, energy_kev=5000.0, primaries=@PRIMARIES@)
