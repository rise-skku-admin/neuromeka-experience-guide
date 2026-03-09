# 웹페이지 관리
## 활성화
### GitHub Pages 웹 페이지 활성화 방법

GitHub Pages를 이용하여 웹 페이지를 배포하는 기본 절차입니다.

---

### 1. Public Repository 생성

GitHub에서 웹 페이지 업로드를 위한 **Public Repository**를 생성합니다.

---

### 2. GitHub Pages 설정

Repository에서 아래 메뉴로 이동합니다.

Settings → Pages

다음 항목을 설정합니다.

Source : GitHub Actions

---

### 3. 웹 페이지 내용 작성 또는 복사

웹 페이지에 사용할 파일들을 작성하거나 템플릿을 복사하여 Repository에 추가합니다.

예시 파일 구조
```
.github/
workflows/
docs/
index.md
_config.yml
```
---

### 4. GitHub Actions 권한 설정 확인

.github/workflows 디렉토리에 있는 workflow 파일에서 아래 권한이 설정되어 있는지 확인합니다.
```
permissions:
  contents: read
  pages: write
  id-token: write
```
이 설정은 GitHub Actions가 Pages에 웹 페이지를 배포할 수 있도록 하는 권한입니다.

---

### 5. 변경 사항 Push

웹 페이지 내용을 작성한 후 Repository에 push 합니다.
```
git add .
git commit -m "update webpage"
git push
```
Push가 완료되면 GitHub Actions가 자동으로 실행되어 페이지가 빌드 및 배포됩니다.

---

### 6. Actions 실행 상태 확인

Repository 상단 메뉴에서 **Actions** 탭을 확인합니다.

- 초록색 체크 표시 → 정상 배포 완료  
- 실패한 경우  
  - 실행된 workflow 클릭  
  - 로그를 확인하여 오류 원인을 확인

---

### 웹 페이지 주소

배포가 완료되면 아래 주소에서 웹 페이지를 확인할 수 있습니다.

https://`<github-username>`.github.io/`<repository-name>`/

예시

https://username.github.io/robotics-in-practice/

---

## 현재 폴더 구조

- `source/`: Sphinx 소스 문서
- `build/`: 로컬 빌드 산출물(업로드 대상 아님)
- `.github/workflows/sphinx.yml`: GitHub Actions 배포 워크플로우
- `.gitignore`: 업로드 제외 항목 관리

## 로컬 실행/빌드

### Requirements
- Python 3.11+

### 1) 의존성 설치

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2) 문서 빌드
문서 빌드는 로컬에서 해당 페이지가 잘 생성되는지 확인을 하기위한 용도이므로, 업로드시 삭제 혹은 .gitignore에 포함 시켜야 한다.
```bash
make html
```

빌드 결과:

- `build/html`

## GitHub Action 배포 흐름

`.github/workflows/sphinx.yml`은 `main` 브랜치 푸시 시 다음 순서로 동작합니다.

1. Python 3.11 설정
2. Sphinx 설치
3. `sphinx-build -b html source _site`
4. `_site/.nojekyll` 생성
5. Pages 아티팩트 업로드
6. GitHub Pages 배포

배포를 위해 GitHub 저장소에서 다음 설정을 확인합니다.

- Settings > Pages > Source: `GitHub Actions`
- Actions 권한 및 Pages 쓰기 권한 허용

## `.gitignore` 정책

`git ignore`는 다음 항목을 업로드에서 제외하도록 구성되어 있습니다.

- 가상환경: `.venv/`, `venv/`, `env/`, `ENV/`
- Python 캐시/중간 산출물: `__pycache__/`, `.pytest_cache/`, `.mypy_cache/`, `.ruff_cache/`, `.tox/`, `.coverage`, `htmlcov/`
- 빌드 산출물: `build/`, `_build/`, `_site/`
- 에디터/시스템 파일: `.vscode/`, `.idea/`, `.DS_Store`, `Thumbs.db`, `*.swp`
- 환경 변수/시크릿 파일: `.env*`

## 문서 유지보수 가이드

이 저장소는 레포지토리에서 지속적으로 관리하려면 `source/` 기준으로 문서를 업데이트하는 방식만 유지하면 됩니다.  

1. 새 문서는 `source/`에 `.rst`로 작성
2. 메뉴(사이드바)는 `source/index.rst`의 `toctree`로 연결
3. 필요 시 `source/conf.py`에서 전역 옵션을 조정

### 1) 새 문서 페이지 추가 (`.rst`)

- 새 파일 생성 예시
  - `source/operations.rst`
- 파일 규칙
  - UTF-8 저장
  - 제목(underlines)은 `=` 또는 `-`로 통일
  - 이미지/정적파일은 `source/_static` 또는 문서 폴더로 분리

예시(`source/operations.rst`)

```rst
로봇 운용 가이드
=================

.. contents::
   :depth: 2

개요
----

운용 절차를 여기에 작성한다.
```

### 2) 메뉴(사이드바) 등록: `source/index.rst`

- `index.rst`의 `.. toctree::`에 파일명만 추가합니다.  
- 파일 확장자(`.rst`)는 쓰지 않습니다.
- depth는 항목 노출 레벨을 제어합니다.

현재 구조:

```rst
.. toctree::
   :maxdepth: 2
   :caption: Contents

   documents
   overview
   as_manual
```

새 페이지를 추가하려면 아래처럼 한 줄만 추가:

```rst
   operations
```

### 3) 기존 페이지를 하위 메뉴로 묶기

단일 문서 그룹이 커지면 폴더 단위 구조를 추천합니다.

- 예: `source/maintenance/index.rst`, `source/maintenance/checklist.rst`
- 상위(폴더) `index.rst`의 toctree로 하위 페이지를 묶고, 최상위 `source/index.rst`에는 `maintenance/index`만 추가
- 폴더 내 이미지도 함께 둬서 운영 주기 확보

`source/maintenance/index.rst` 예시

```rst
정비 가이드
==========

.. toctree::
   :maxdepth: 2

   checklist
   troubleshooting
```

상위 메뉴 등록(`source/index.rst`)

```rst
   maintenance/index
```

### 4) `conf.py`에서 자주 조정하는 항목

현재 설정은 최소 구성입니다. 유지보수 시 아래 항목만 자주 바꿉니다.

- 사이드바/탐색 깊이
  - `html_theme_options['navigation_depth'] = 4`
- 자동 목차 생성
  - `extensions`에 `sphinx.ext.autosectionlabel` 추가 시 섹션 이름 재사용 가능
  - `extensions = ['sphinx.ext.autosectionlabel']`
- 복수 소스 언어/특수 기능
  - `extensions`에 기능별 확장 추가

예시 (`source/conf.py`)

```python
# -- General configuration --
extensions = ['sphinx.ext.autosectionlabel']
autosectionlabel_prefix_document = True

# -- HTML options --
html_theme_options = {
    'collapse_navigation': False,
    'navigation_depth': 4,
    'titles_only': False,
}
```

### 5) 정적 자원(이미지/문서 자료) 규칙

- 이미지: `source/_static` 또는 하위 폴더(`source/overview/`, `source/as_manual/`)에 두고 상대경로로 참조
- 문서 내부 표기 예

```rst
.. image:: _static/logo.png
   :width: 300px
   :align: center
```

폴더 안에 둘 경우(권장)

```rst
.. image:: overview/ind7_overview.png
```

### 6) 배포 전 체크리스트

```bash
make html
```

- `source/index.rst`에 새 파일이 모두 연결됐는지
- 링크 깨짐 경고 없는지
- `build/html/index.html`에서 새 메뉴 노출 확인
- 결과 확인 후 main 브랜치 푸시


