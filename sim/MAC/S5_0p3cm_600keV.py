"""Job S5_0p3cm_600keV: mẫu S5, bề dày 0.3 cm, năng lượng 600 keV. Số hạt lấy từ project.yaml (primaries)."""
from model import run

run(sample="S5", thickness_cm=0.3, energy_kev=600.0, primaries=@PRIMARIES@)
