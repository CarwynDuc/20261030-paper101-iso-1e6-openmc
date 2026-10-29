"""Job S1_2cm_2000keV: mẫu S1, bề dày 2 cm, năng lượng 2000 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S1", thickness_cm=2.0, energy_kev=2000.0, primaries=@PRIMARIES@)
