
sospechosa (+) arbolito (genA 1)

= <evaluamos sospechosa>

foldA (whatTF (+)) (const Hoja) arbolito (genA 1)

= <evaluamos arbolito>

foldA (whatTF (+)) (const Hoja) (Rama 1 (Rama 2 Hoja (Rama 3 Hoja Hoja)) Hoja) (genA 1)

= <evaluamos foldA>

whatTF (+) 1 (foldA whatTF (+) (const Hoja) (Rama 2 Hoja (Rama 3 Hoja Hoja))) (foldA whatTF (+) (const Hoja) Hoja) (genA 1)

= <evaluamos genA>

whatTF (+) 1 (foldA whatTF (+) (const Hoja) (Rama 2 Hoja (Rama 3 Hoja Hoja))) (foldA whatTF (+) (const Hoja) Hoja) 
(Rama 1 (genA 2) (genA 3))

= <evaluamos whatTF>

Rama ((+) 1 1) ((foldA whatTF (+) (const Hoja) (Rama 2 Hoja (Rama 3 Hoja Hoja))) (genA 2)) 
               ((foldA whatTF (+) (const Hoja) Hoja) (genA 3))

= <evaluamos la suma>

Rama (2) ((foldA whatTF (+) (const Hoja) (Rama 2 Hoja (Rama 3 Hoja Hoja))) (genA 2)) 
         ((foldA whatTF (+) (const Hoja) Hoja) (genA 3))

= <evaluamos foldA>

Rama (2) ((whatTF (+) 2 (foldA whatTF (+) (const Hoja) Hoja) (foldA whatTF (+) (const Hoja) (Rama 3 Hoja Hoja))) (genA 2))
		 ((foldA whatTF (+) (const Hoja) Hoja) (genA 3))


= <evaluamos genA>

Rama (2) (whatTF (+) 2 (foldA whatTF (+) (const Hoja) Hoja) (foldA whatTF (+) (const Hoja) (Rama 3 Hoja Hoja)) 
	     (Rama 2 (genA 4) (genA 6)))
		 ((foldA whatTF (+) (const Hoja) Hoja) (genA 3))

= <evaluamos whatTF>

Rama (2) (Rama ((+) 2 2) 
	       ((foldA whatTF (+) (const Hoja) Hoja) (genA 4)) ((foldA whatTF (+) (const Hoja) (Rama 3 Hoja Hoja)) (genA 6)))
		 ((foldA whatTF (+) (const Hoja) Hoja) (genA 3))

= <evaluamos la suma>

Rama (2) (Rama (4) 
	       ((foldA whatTF (+) (const Hoja) Hoja) (genA 4)) ((foldA whatTF (+) (const Hoja) (Rama 3 Hoja Hoja)) (genA 6)))
		 ((foldA whatTF (+) (const Hoja) Hoja) (genA 3))

= <evaluamos foldA>

Rama (2) (Rama (4) ((const Hoja) (genA 4)) ((foldA whatTF (+) (const Hoja) (Rama 3 Hoja Hoja)) (genA 6)))
		 ((foldA whatTF (+) (const Hoja) Hoja) (genA 3))

= <evaluamos const>

Rama (2) (Rama (4) Hoja ((foldA whatTF (+) (const Hoja) (Rama 3 Hoja Hoja)) (genA 6)))
		 ((foldA whatTF (+) (const Hoja) Hoja) (genA 3))

= <evaluamos foldA>

Rama (2) (Rama (4) Hoja ((whatTF (+) 3 (foldA whatTF (+) (const Hoja) Hoja) (foldA whatTF (+) (const Hoja) Hoja)) (genA 6)))
		 ((foldA whatTF (+) (const Hoja) Hoja) (genA 3))

= <evaluamos genA>

Rama (2) (Rama (4) Hoja (whatTF (+) 3 (foldA whatTF (+) (const Hoja) Hoja) (foldA whatTF (+) (const Hoja) Hoja) 
						 (Rama 6 (genA 12) (genA 18))))
		 ((foldA whatTF (+) (const Hoja) Hoja) (genA 3))

= <evaluamos whatTF>

Rama (2) (Rama (4) Hoja (Rama ((+) 3 6) ((foldA whatTF (+) (const Hoja) Hoja) (genA 12)) 
	                                    ((foldA whatTF (+) (const Hoja) Hoja) (genA 18))))
		 ((foldA whatTF (+) (const Hoja) Hoja) (genA 3))

= <evaluamos la suma>

Rama (2) (Rama (4) Hoja (Rama (9) ((foldA whatTF (+) (const Hoja) Hoja) (genA 12)) 
	                              ((foldA whatTF (+) (const Hoja) Hoja) (genA 18))))
		 ((foldA whatTF (+) (const Hoja) Hoja) (genA 3))

= <evaluamos foldA>

Rama (2) (Rama (4) Hoja (Rama (9) ((const Hoja) (genA 12)) 
	                              ((foldA whatTF (+) (const Hoja) Hoja) (genA 18))))
		 ((foldA whatTF (+) (const Hoja) Hoja) (genA 3))

= <evaluamos const>

Rama (2) (Rama (4) Hoja (Rama (9) Hoja ((foldA whatTF (+) (const Hoja) Hoja) (genA 18))))
                                       ((foldA whatTF (+) (const Hoja) Hoja) (genA 3))

= <evaluamos foldA>

Rama (2) (Rama (4) Hoja (Rama (9) Hoja ((const Hoja) (genA 18))))
                                       ((foldA whatTF (+) (const Hoja) Hoja) (genA 3))

= <evaluamos const>

Rama (2) (Rama (4) Hoja (Rama (9) Hoja Hoja)) ((foldA whatTF (+) (const Hoja) Hoja) (genA 3))

= <evaluamos foldA>

Rama (2) (Rama (4) Hoja (Rama (9) Hoja Hoja)) ((const Hoja) (genA 3))

= <evaluamos const>

Rama (2) (Rama (4) Hoja (Rama (9) Hoja Hoja)) Hoja

