"""Job S3_1cm_100keV: mẫu S3, bề dày 1 cm, năng lượng 100 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S3", thickness_cm=1.0, energy_kev=100.0, primaries=@PRIMARIES@)
