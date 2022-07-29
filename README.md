# 이제누가공지해주냐
홍익대학교 공지 추천 서비스

## 팀원
<table>
    <tr align="center">
        <td><B>기획 / 디자인 / 프론트<B></td>
        <td><B>PM / 기획 / 백엔드<B></td>
        <td><B>백엔드<B></td>
        <td><B>DE & ML<B></td>
        <td><B>DE & ML<B></td>
    </tr>
    <tr align="center">
        <td><B>김도현<B></td>
        <td><B>안재현<B></td>
        <td><B>조상욱<B></td>
        <td><B>전지수<B></td>
        <td><B>박준서<B></td>
    </tr>
    <tr align="center">
        <td>
            <img src="https://github.com/swoooon.png" width="100">
            <br>
            <a href="https://github.com/swoooon"><I>swoooon</I></a>
        </td>
        <td>
            <img src="https://github.com/uwoobeat.png" width="100">
            <br>
            <a href="https://github.com/uwoobeat"><I>uwoobeat</I></a>
        </td>
        <td>
            <img src="https://github.com/Sangwook02.png" width="100">
            <br>
            <a href="https://github.com/Sangwook02"><I>Sangwook02</I></a>
        </td>
        <td>
            <img src="https://github.com/Jeon-jisu.png" width="100">
            <br>
            <a href="https://github.com/Jeon-jisu"><I>Jeon-jisu</I></a>
        </td>
        <td>
            <img src="https://github.com/Pjunn.png" width="100">
            <br>
            <a href="https://github.com/pjunn"><I>pjunn</I></a>
        </td>
    </tr>
</table>
            
## Getting Started
Step1) "python -m venv venv"를 통해 가상환경 생성
<br>
Step2) 가상환경이 생성된 디렉토리에서 다음의 명령어를 순서대로 입력하여 가상환경에 진입

<ul>
    <li>"cd venv"</li>
    <li>"cd Scripts"</li>
    <li>"activate"</li>
</ul>
Step3) 다음의 명령어를 순서대로 입력하여 manage.py가 있는 폴더로 이동
<br>
<ul>
    <li>"cd 2022-2NuGong-2NuGong"</li>
    <li>"cd backend"</li>
</ul>
Step4) "pip install -r requirements.txt"을 입력하여 dependencies 다운로드
<br>
Step5) 다음의 명령어를 순서대로 입력하여 migrate
<br>
<ul>
    <li>"python manage.py makemigrations"</li>
    <li>"python manage.py migrate"</li>
</ul>

Step6) "python manage.py runserver"로 실행
