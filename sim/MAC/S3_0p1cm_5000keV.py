"""Job S3_0p1cm_5000keV: mẫu S3, bề dày 0.1 cm, năng lượng 5000 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S3", thickness_cm=0.1, energy_kev=5000.0, primaries=@PRIMARIES@)
