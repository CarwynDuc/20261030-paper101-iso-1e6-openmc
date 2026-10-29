"""Job S6_1cm_40keV: mẫu S6, bề dày 1 cm, năng lượng 40 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S6", thickness_cm=1.0, energy_kev=40.0, primaries=@PRIMARIES@)
