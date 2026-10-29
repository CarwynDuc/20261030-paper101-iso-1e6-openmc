"""Job S5_1cm_2000keV: mẫu S5, bề dày 1 cm, năng lượng 2000 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S5", thickness_cm=1.0, energy_kev=2000.0, primaries=@PRIMARIES@)
