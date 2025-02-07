<script type="module">
  // Import the functions you need from the SDKs you need
  import { initializeApp } from "https://www.gstatic.com/firebasejs/11.3.0/firebase-app.js";
  import { getAnalytics } from "https://www.gstatic.com/firebasejs/11.3.0/firebase-analytics.js";
  // TODO: Add SDKs for Firebase products that you want to use
  // https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  const firebaseConfig = {
    apiKey: "AIzaSyAzWxU0YWSogrIaE47fsFBG2PIMDiVBjSo",
    authDomain: "todays-best-recipe-signup.firebaseapp.com",
    projectId: "todays-best-recipe-signup",
    storageBucket: "todays-best-recipe-signup.firebasestorage.app",
    messagingSenderId: "931084422641",
    appId: "1:931084422641:web:9bb87895790162dae94850",
    measurementId: "G-LJRKJS7NY7"
  };

// Firebase 초기화
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

// 회원가입 함수
window.signup = function () {
    const nickname = document.getElementById("nickname").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirm-password").value;

    // 닉네임, 이메일, 비밀번호 확인
    if (!nickname || !email || !password || !confirmPassword) {
        alert("모든 필드를 입력하세요.");
        return;
    }

    if (password !== confirmPassword) {
        alert("비밀번호가 일치하지 않습니다.");
        return;
    }

    // Firebase에 회원가입 요청
    createUserWithEmailAndPassword(auth, email, password)
        .then(() => {
            alert("회원가입 성공! 로그인 페이지로 이동합니다.");
            window.location.href = "login.html"; // 로그인 페이지로 이동
        })
        .catch(error => {
            alert("회원가입 실패: " + error.message);
        });
};
