"""Job S5_2p5cm_600keV: mẫu S5, bề dày 2.5 cm, năng lượng 600 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S5", thickness_cm=2.5, energy_kev=600.0, primaries=@PRIMARIES@)
