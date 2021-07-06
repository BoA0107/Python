# -*-coding:utf-8-*-
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

# 占位符：_
for country, _ in traveler_ids:
    print(country)
