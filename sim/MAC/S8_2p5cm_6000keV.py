"""Job S8_2p5cm_6000keV: mẫu S8, bề dày 2.5 cm, năng lượng 6000 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S8", thickness_cm=2.5, energy_kev=6000.0, primaries=@PRIMARIES@)
