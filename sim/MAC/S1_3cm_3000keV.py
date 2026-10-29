"""Job S1_3cm_3000keV: mẫu S1, bề dày 3 cm, năng lượng 3000 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S1", thickness_cm=3.0, energy_kev=3000.0, primaries=@PRIMARIES@)
