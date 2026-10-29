"""Job S8_2p5cm_50keV: mẫu S8, bề dày 2.5 cm, năng lượng 50 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S8", thickness_cm=2.5, energy_kev=50.0, primaries=@PRIMARIES@)
