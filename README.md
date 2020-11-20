# 멋쟁이사자처럼 미니해커톤 I’ll VEGAN🥗

> 비건을 위한 통합 웹 서비스 플랫폼

<p align="center"><img src="https://user-images.githubusercontent.com/60457112/99776737-a1661080-2b54-11eb-827e-1062f68f6d75.gif" width="500px"/></p>


### [📷 화면기획서](https://docs.google.com/document/d/1mkqI7aCQx13PNN2kWhbGz3nv6JC-981JZwqimzR3byE/edit)
### [📋 팀 회의록](https://docs.google.com/document/d/1GNcKvoggR6rB3anN0DjmuASfJxnLRIMeCaIC2mQmEzk/edit)

## 📖 서비스 설명
```
채식주의 시장에 대한 관심과 수요의 증가에도 불구하고 아직 관련 정보를 쉽게 찾기 힘들다는 점에서 가치 창출의 기회를 포착했습니다. 
채식주의에도 여러 종류가 있는데 이에 대한 구분이 제대로 되어있지 않고, 많은 채식주의자들이 정보를 얻기 어려워 하고 있었습니다.
저희 I’ll VEGAN은 이용자들을 목적과 니즈에 따라 분류하고, 적절한 식당 위치정보와 리뷰, 레시피와 식료품 정보와 커뮤니티를 제공합니다. 
이를 통해 채식주의에 대한 진입장벽을 낮추고, 비건(Vegan)같은 완전 채식주의자뿐만 아니라 플렉시테리언(Flexitarian)처럼 건강 유지와 
환경 보호를 위해 채식 위주의 식사도 하면서 고기도 먹는 채식주의자들의 수요까지 기대할 수 있는 플랫폼을 개발하는 것을 목표로 합니다. 
```

## 📚 주요 기능
#### 1. 회원가입시 선호하는 채식주의 분석 및 선택 가능
#### 2. google 및 kakao 소셜 로그인 구현
#### 3. 비건 식당 검색 및 별점 부여, 소셜 공유 기능 구현
#### 4. 비건 식당 및 화장품 추천, 비건 레시피 제공 등 비건 관련 정보들을 제공
#### 5. 이용자들이 자유롭게 글을 생성하고 댓글을 달 수 있는 게시판 기능 구현

## ✔️ 기술 스택
#### Front : HTML, CSS
#### Backend : Django

## 📺 실행 화면
### 1. 메인 화면
<p><img src="https://user-images.githubusercontent.com/60457112/99776946-f30e9b00-2b54-11eb-8d37-a835562bca88.png" width="500px"/></p>

### 2. 비건 식당 목록 
<p><img src="https://user-images.githubusercontent.com/60457112/99777227-55679b80-2b55-11eb-92a9-5579180f73f9.png" width="500px"/></p>

### 3. 비건 식품 목록
<p><img src="https://user-images.githubusercontent.com/60457112/99777333-79c37800-2b55-11eb-9e7c-a5387064ee44.png" width="500px"/></p>

### 4. 비건 관련 정보 제공
<p><img src="https://user-images.githubusercontent.com/60457112/99777387-89db5780-2b55-11eb-952b-edc2e4911ed2.png" width="500px"/></p>

### 5. 게시판
<p><img src="https://user-images.githubusercontent.com/60457112/99777469-ad060700-2b55-11eb-96cf-046f6246c20e.png" width="500px"/></p>

## ⚒️ Installation

Use the package manager [pipenv shell](https://pipenv-fork.readthedocs.io/en/latest/install.html) to install pipenv

```bash
git clone https://github.com/dooking/team2_miniton.git
cd team2_miniton
pipenv shell
pipenv install
python manage.py runserver
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
