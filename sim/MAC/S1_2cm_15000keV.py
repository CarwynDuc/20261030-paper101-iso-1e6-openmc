"""Job S1_2cm_15000keV: mẫu S1, bề dày 2 cm, năng lượng 15000 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S1", thickness_cm=2.0, energy_kev=15000.0, primaries=@PRIMARIES@)
