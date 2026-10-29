"""Job S1_1cm_4000keV: mẫu S1, bề dày 1 cm, năng lượng 4000 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S1", thickness_cm=1.0, energy_kev=4000.0, primaries=@PRIMARIES@)
