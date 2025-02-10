// import { auth } from "./app.js"; // app.js에서 auth 가져오기
// import { signInWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/11.3.0/firebase-auth.js";

// // 로그인 함수
// window.login = function () {
//     const email = document.getElementById("email").value;
//     const password = document.getElementById("password").value;

//     if (!email || !password) {
//         alert("이메일과 비밀번호를 입력하세요.");
//         return;
//     }

//     signInWithEmailAndPassword(auth, email, password)
//         .then(() => {
//             alert("로그인 성공!");
//             window.location.href = "main.html"; // 로그인 후 이동
//         })
//         .catch(error => {
//             alert("로그인 실패: " + error.message);
//         });
// };
