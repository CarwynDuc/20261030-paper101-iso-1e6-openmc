"""Job S8_1cm_3000keV: mẫu S8, bề dày 1 cm, năng lượng 3000 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S8", thickness_cm=1.0, energy_kev=3000.0, primaries=@PRIMARIES@)
