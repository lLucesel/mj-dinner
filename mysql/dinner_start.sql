use dinner;
SELECT food_type, name, ingredient, spice, recipe, calorie, carbohydrate, protein, vitamin
FROM food
JOIN food_type ON food.food_type_id = food_type.id;

            SELECT name
            FROM food JOIN food_type ON food.food_type_id = food_type.id
            WHERE food_type = '반찬' ;
            
            
             INSERT INTO food (food_type_id, name, ingredient, spice, recipe,
    calorie, carbohydrate, protein, vitamin)
    VALUES ('1',
        '테스트메뉴3', '등갈비, 김치', '고춧가루', '넣고 끓인다.',
        '890', '6', '7', '8');
--             
--          DELETE food FROM food
--          INNER JOIN food_type ON food.food_type_id = food_type.id
--          WHERE name = '테스트메뉴1'