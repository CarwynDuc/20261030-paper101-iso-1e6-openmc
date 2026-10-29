"""Job S3_2p5cm_500keV: mẫu S3, bề dày 2.5 cm, năng lượng 500 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S3", thickness_cm=2.5, energy_kev=500.0, primaries=@PRIMARIES@)
