
#users 테이블 관련
def mem_register():
    sql = """INSERT INTO users(user_id, nickname, email, password)
    VALUES (%s, %s, %s, %s)"""
    return sql

def select_nickname_from_users():
    sql ="""
    SELECT nickname from users where nickname = %s
    """
    return sql

def select_user_id_from_users():
    sql ="""
    SELECT user_id from users where user_id = %s
    """
    return sql

def select_nickname_by_id():
    sql ="""
    SELECT nickname from users where user_id = %s
    """
    return sql

def select_password_from_users():
    sql ="""
    SELECT password from users where nickname = %s
    """
    return sql





#recipes 테이블 관련
def select_foodname_by_type(): # 음식의 카테고리별로 음식 이름 조회
    sql=""" 
    SELECT rec_name from recipes where rec_type = %s
    """
    return sql

def select_descrip_by_type(): # 음식의 카테고리별로 음식 설명 조회 
    sql=""" 
    SELECT rec_descrip from recipes where rec_type = %s
    """
    return sql

def select_detail_by_type(): # 음식의 카테고리별로 음식 레시피(조리법) 조회회
    sql=""" 
    SELECT rec_detail from recipes where rec_type = %s
    """
    return sql

def select_ing_by_type(): # 음식의 카테고리별로 음식 사진 조회
    sql=""" 
    SELECT rec_img from recipes where rec_type = %s
    """
    return sql




#user_ingredients 테이블 관련
def delete_all_u_i():
    sql = """
    TRUNCATE TABLE user_ingredients
    """
    return sql

# def insert_ingredient_for_user(): # user_ingredients 테이블에 재료 입력하는 쿼리 (존재하지 않는 재료도 삽입)
#     sql = """
#     INSERT INTO user_ingredients (user_id, ing_id) 
#     VALUES (%s, %s)
#     """
#     return sql

# def select_recipes_by_ingredients(): # recipe_ingredients 테이블에서 특정 재료들을 사용하는 레시피 찾기 (일치하는 재료가 n개 이상인 레시피)
#     sql = """
#     SELECT DISTINCT r.rec_name
#     FROM recipes r
#     JOIN recipe_ingredients ri ON r.rec_id = ri.rec_id
#     WHERE ri.ing_id IN (%s)  -- IN 절을 사용해 여러 재료를 처리
#     GROUP BY r.rec_name
#     HAVING COUNT(DISTINCT ri.ing_id) >= %s  -- 사용자가 가진 재료 수와 겹치는 재료가 n개 이상인 레시피
#     """
#     return sql

# def insert_new_ingredient(): # ingredients 테이블에 없는 재료를 새로 삽입하는 쿼리
#     sql = """
#     INSERT INTO ingredients (ing_name) 
#     VALUES (%s)
#     """
#     return sql

def select_ingredients_by_user():
    sql = """
    SELECT ing_id FROM user_ingredients WHERE user_id = %s
    """
    return sql
