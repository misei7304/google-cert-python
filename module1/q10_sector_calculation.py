# 문제 10: 16GB 디스크에서 섹터 수 계산
disk_size = 16 * 1024 * 1024 * 1024  # 16GB를 바이트로
sector_size = 512                   # 1 섹터 = 512바이트
sector_amount = disk_size // sector_size
print(sector_amount)  # 출력: 33554432