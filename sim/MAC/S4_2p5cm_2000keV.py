"""Job S4_2p5cm_2000keV: mẫu S4, bề dày 2.5 cm, năng lượng 2000 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S4", thickness_cm=2.5, energy_kev=2000.0, primaries=@PRIMARIES@)
