"""Job S3_0p1cm_6000keV: mẫu S3, bề dày 0.1 cm, năng lượng 6000 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S3", thickness_cm=0.1, energy_kev=6000.0, primaries=@PRIMARIES@)
