import blog.query_sql as q
import rec_conn as rdb
from tabulate import tabulate

conn=rdb.mysql_rdb_conn()

def select_food_by_category(category):
    try:
        with conn.cursor() as curs:
            query = q.select_food_by_type()
            curs.execute(query, (category,))
            res = curs.fetchall()

            if res:
                headers = ["번호", "음식명"]
                table = [(i + 1, row[0]) for i, row in enumerate(res)]
                print(tabulate(table, headers=headers, tablefmt="plain"))
                print()
            else:
                print(f"{category} 카테고리에 추천할 음식이 없습니다.")
    except Exception as e:
        conn.rollback()
        print("에러ㅠㅠㅠ", "에러에오... ->", e)
        
def recomm_by_ing(user_id):
    try:
        with conn.cursor() as curs:
            # 1. 사용자가 보유한 재료를 입력받음
            ingredients = input("가지고 있는 식재료를 입력해주세요!(띄어쓰기로 식재료 구분): ").split()
            
            if not ingredients:
                print("입력되지 않았습니다. 다시 입력해주세요.")
                return

            # 2. 입력받은 재료들을 user_ingredients 테이블에 저장
            for ingredient in ingredients:
                # ingredient는 식재료의 이름이므로 ing_id를 얻기 위해 ingredients 테이블을 조회
                curs.execute("SELECT ing_id FROM ingredients WHERE ing_name = %s", (ingredient,))
                ing_id = curs.fetchone()
                
                if ing_id:
                    # 이미 ing_id가 존재하면 user_ingredients에 삽입
                    curs.execute(q.insert_ingredient_for_user(), (user_id, ing_id[0]))
                else:
                    # 만약 존재하지 않는 재료라면 ingredients 테이블에 새로 삽입
                    curs.execute(q.insert_new_ingredient(), (ingredient,))
                    # 새로 삽입된 재료의 ing_id를 가져옴
                    curs.execute("SELECT ing_id FROM ingredients WHERE ing_name = %s", (ingredient,))
                    ing_id = curs.fetchone()
                    curs.execute(q.insert_ingredient_for_user(), (user_id, ing_id[0]))
                    print(f"식재료 '{ingredient}'가 새로 등록되었습니다.")
            
            print()
            conn.commit()
            print("식재료가 등록되었습니다.")

            # 3. 사용자가 가진 재료로 만들 수 있는 레시피를 찾음
            curs.execute(q.select_ingredients_by_user(), (user_id,))
            user_ingredients = [row[0] for row in curs.fetchall()]

            if not user_ingredients:
                print("보유한 재료가 없습니다.")
                return
            
            # 재료들을 인자로 사용하여 레시피를 찾음
            ingredients_str = ",".join(map(str, user_ingredients))
            num_ingredients = len(user_ingredients)
            min_required_ingredients = num_ingredients // 2  # 예시로 전체 재료 수의 절반 이상이 일치하면 추천

            curs.execute(q.select_recipes_by_ingredients(), (ingredients_str, min_required_ingredients))

            recipes = curs.fetchall()

            if recipes:
                print("추천 레시피:")
                for i, recipe in enumerate(recipes, 1):
                    print(f"{i}. {recipe[0]}")
            else:
                print("보유한 재료로 만들 수 있는 레시피가 없습니다.")
    except Exception as e:
        conn.rollback()
        print("에러ㅠㅠㅠ", "에러에오... ->", e)

def delete_user_ing():
    with conn.cursor() as curs:
        curs.execute(q.delete_all_u_i())
        conn.commit
    