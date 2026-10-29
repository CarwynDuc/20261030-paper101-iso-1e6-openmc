"""Job S3_1p5cm_15keV: mẫu S3, bề dày 1.5 cm, năng lượng 15 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S3", thickness_cm=1.5, energy_kev=15.0, primaries=@PRIMARIES@)
