"""Job S8_3cm_600keV: mẫu S8, bề dày 3 cm, năng lượng 600 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S8", thickness_cm=3.0, energy_kev=600.0, primaries=@PRIMARIES@)
