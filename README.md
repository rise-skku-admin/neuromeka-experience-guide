
## 폴더 구조

- `source/`: Sphinx 소스 문서
- `build/`: 로컬 빌드 산출물(업로드 대상 아님)
- `.github/workflows/sphinx.yml`: GitHub Actions 배포 워크플로우
- `.gitignore`: 업로드 제외 항목 관리

## 로컬 실행/빌드

### 1) 의존성 설치

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2) 문서 빌드

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


