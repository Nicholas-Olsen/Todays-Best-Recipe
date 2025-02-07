import { auth } from "./app.js"; // Firebase 인증 객체 가져오기
import { createUserWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/11.3.0/firebase-auth.js";

window.signup = function () {
    const nickname = document.getElementById("nickname").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirm-password").value;

    // 입력값 확인
    if (!nickname || !email || !password || !confirmPassword) {
        alert("모든 필드를 입력하세요.");
        return;
    }

    if (password !== confirmPassword) {
        alert("비밀번호가 일치하지 않습니다.");
        return;
    }

    // Firebase 회원가입 요청
    createUserWithEmailAndPassword(auth, email, password)
        .then(() => {
            alert("회원가입 성공! 로그인 페이지로 이동합니다.");
            window.location.href = "index.html"; // 로그인 페이지로 이동
        })
        .catch(error => {
            alert("회원가입 실패: " + error.message);
        });
};
