"""Job S3_0p5cm_40keV: mẫu S3, bề dày 0.5 cm, năng lượng 40 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S3", thickness_cm=0.5, energy_kev=40.0, primaries=@PRIMARIES@)
