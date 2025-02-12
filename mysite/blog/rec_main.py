import rec_fn as rfunc
import os
import blog.query_sql as q
import rec_conn as rdb
import getpass # 비밀번호 입력 시 *로 입력받기 위함임'

#로그인 변수
login_val = 0
user_id = ""
conn=rdb.mysql_rdb_conn() 

def fmenu(): #기능을 위한 선택지(기능만 이해 및 사용하고 틀은 이용할 필요 X) ,fmenu는 first페이지라는 뜻
            print("""
             레시피 추천 !
  1.회원 가입        2.로그인             
                """)
            
def menu(): #기능을 위한 선택지(기능만 이해 및 사용하고 틀은 이용할 필요 X)
            print("""
             레시피 추천 !
  1.음식 종류 선택    2.식재료로 추천받기
  3.출력창 정리       4.종료                  
                """)
            
            
def regi():
    try:
        with conn.cursor() as curs:
            while(True):
                # 아이디 입력 및 중복 확인
                user_id = input("사용할 아이디를 입력하세요 : ")
                user_chk = q.select_user_id_from_users()
                curs.execute(user_chk, (user_id,))
                if curs.fetchone() is not None:
                    print("이미 사용 중인 아이디입니다. 다른 아이디를 입력해주세요.")
                    continue
                
                # 닉네임 입력 및 중복 확인
                nickname = input("사이트에서 사용할 닉네임을 입력하세요 : ")
                nick_chk = q.select_nickname_from_users()
                curs.execute(nick_chk, (nickname,))
                if curs.fetchone() is not None:
                    print("이미 사용 중인 닉네임입니다. 다른 닉네임을 입력해주세요.")
                    continue
                
                # 이메일 유효성 검사
                email = input("이메일을 입력하세요: ")
                if "@" not in email:
                    print("올바른 이메일 형식을 입력해주세요. ('@'가 포함되어야 합니다)")
                    continue  # 이메일이 잘못되면 처음으로 돌아감
                
                # 비밀번호 입력 및 불일치 검사
                password = getpass.getpass("비밀번호를 입력하세요: ")                     # 비밀번호 입력 시 *로 입력받기 위함임
                confirm_password = getpass.getpass("비밀번호 다시 입력해주세요: ")        # 비밀번호 입력 시 *로 입력받기 위함
                
                if password != confirm_password:
                    print("비밀번호가 일치하지 않습니다. 다시 입력해주세요.")
                    continue  # 비밀번호 불일치 시 처음으로 돌아감
                
                regi_data = (user_id,nickname,email,password)
                regi_insert = q.mem_register()
                curs.execute(regi_insert,regi_data)
                conn.commit()
                print()
                print("성공 ! 회원 가입 완료 !")
                break
    except Exception as e:
        print(f"Unexpected error: {e}")

        
def login():
    try:
        with conn.cursor() as curs:
            while(True):
                global user_id
                user_id = input("아이디를 입력하세요 : ")
                user_chk = q.select_user_id_from_users()
                curs.execute(user_chk, (user_id,))
                if curs.fetchone() is not None:
                    pass
                else:
                    print("아이디가 없습니다")
                    continue
                
                password = getpass.getpass("비밀번호를 입력하세요 : ")
                user_chk = q.select_password_from_users()
                curs.execute(user_chk, (password, user_id))
                if curs.fetchone() is not None:
                    pass
                else:
                    print("비밀번호가 다릅니다")
                    continue
                
                #로그인 변수에 1추가 => 로그인 됨됨
                global login_val
                login_val += 1
                
                nick_sql = q.select_nickname_by_id()
                curs.execute(nick_sql,(user_id,))
                result_nickname = curs.fetchone()
                
                print()
                print(result_nickname[0],"님 반갑습니다 !")
                print("로그인 되었습니다 !")
                print()
                
                break
    except Exception as e:
        print(f"Unexpected error: {e}")
        
def recomm_by_ing():
    pass


def select_category():
        while True:
            print("""
        카테고리 선택
  1. 한식          2. 양식
  3. 중식          4. 일식
  5. 디저트        6. 종료
                """)
            cho = input("선택하세요: ")
            if cho == "1":
                rfunc.select_food_by_category("한식")
            elif cho == "2":
                rfunc.select_food_by_category("양식")
            elif cho == "3":
                rfunc.select_food_by_category("중식")
            elif cho == "4":
                rfunc.select_food_by_category("일식")
            elif cho == "5":
                rfunc.select_food_by_category("디저트")
            elif cho=="6":
                break
            else:
                print("잘못 입력했습니다. 다시 입력해주세요")


def main():
    try:
        #첫 페이지(로그인, 회원가입)
        while (login_val == 0):
            fmenu()
            choice = input("선택하세요: ")
            if choice == "1":
                regi()
            elif choice == "2":
                login()
            else:
                print("잘못 입력했습니다. 다시 입력해주세요")
        
        #진짜 메뉴   
        while True:
            menu()
            choice = input("선택하세요: ")
            if choice == "1":
                select_category()
            elif choice == "2":
                rfunc.recomm_by_ing(user_id)
                rfunc.delete_user_ing()
            elif choice == "3":
                os.system("cls")
            elif choice == "4":
                print("Program ended")
                break
            else:
                print("잘못 입력했습니다. 다시 입력해주세요")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("System ended")

    
if __name__=="__main__":
    main()