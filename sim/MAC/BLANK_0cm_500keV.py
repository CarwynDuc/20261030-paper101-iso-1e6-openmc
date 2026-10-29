"""Job BLANK_0cm_500keV: mẫu BLANK, bề dày 0 cm, năng lượng 500 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="BLANK", thickness_cm=0.0, energy_kev=500.0, primaries=@PRIMARIES@)
