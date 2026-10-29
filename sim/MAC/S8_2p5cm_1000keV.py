"""Job S8_2p5cm_1000keV: mẫu S8, bề dày 2.5 cm, năng lượng 1000 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S8", thickness_cm=2.5, energy_kev=1000.0, primaries=@PRIMARIES@)
