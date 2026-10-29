"""Job S8_2cm_2000keV: mẫu S8, bề dày 2 cm, năng lượng 2000 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S8", thickness_cm=2.0, energy_kev=2000.0, primaries=@PRIMARIES@)
