# Öklid formülü d = √(x₂-x₁)²+(y₂-y₁)²
# Fonksiyonlar ve döngüler kullanılacak

import math
# Math kütüphanesi ile matematiksel işlemler yapılabilir.

points =[(1,3), (2,4), (2,5), (3,3), (4,1), (4,5)]
# 1 ile 5  arasında değerler alan tuplelardan liste oluşturuldu.

def euclideanDistance (point_1,point_2):        # iki nokta arasındaki uzaklığı hesaplama
    (x1, y1) = point_1   #point1'in ilk elemanı x1'e ikinci elemanı y1'e atanır.
    (x2, y2) = point_2
    oklid_mesafe=math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    return oklid_mesafe

# Döngü ile mesafelerin hesaplanması

distances = [] 
# points listesindeki noktalar arası uzaklıklar hesaplanıp bu boş listeye eklenecek.

for i in range(len(points)) : # i değeri sırayla point listesinin elemanlarına eşitlenir.
    
    for j in range(i+1, len(points)):   # j değeri i+1.değişkenden başlayarak sırayla point listesinin elemanlarına eşitlenir.

        mesafe = euclideanDistance(points[i], points[j])
        distances.append(mesafe) 

min_mesafe = min(distances)
#distance listesinden minimum 
print("İki nokta arasındaki minimum mesafe: ", min_mesafe)






