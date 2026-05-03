# 희앤썬 · Marketing Strategy 2026 — Handoff Package

이 패키지는 **Claude의 새 프로젝트에서 deck을 계속 디벨롭** 하기 위한 작업 자산이다.

## 패키지 구성

```
heensun-deck-handoff/
├── README.md                    ← 본 문서 · 시작 가이드
├── PROJECT_BRIEF.md             ← 새 Claude 프로젝트 시스템 프롬프트 (복붙)
├── DESIGN_TOKENS.md             ← 모든 슬라이드 공통 CSS / 폰트 / 패턴
├── SLIDE_INDEX.md               ← 22 슬라이드 카피·자산·결합 인덱스
├── slides/                      ← 22 슬라이드 HTML 소스 (편집 대상)
│   ├── slide-01-cover.html
│   ├── slide-03-the-brief.html
│   ├── ...
│   └── slide-25-working-calendar.html
└── scripts/                     ← 최종 export 스크립트
    ├── render_pngs.py           ← HTML → PNG (1280×720 @2x)
    ├── build_pptx.py            ← PNG → PowerPoint
    └── build_deck_html.py       ← PNG → 단일 HTML
```

## 새 Claude 프로젝트 시작 방법

### 1. 새 프로젝트 생성

Claude.ai에서 새 프로젝트 만들기 → 프로젝트 이름: `희앤썬 Deck V2` (또는 원하는 이름)

### 2. 시스템 프롬프트 설정

`PROJECT_BRIEF.md` 파일 내용을 복사해서 새 프로젝트의 **Custom Instructions** 영역에 붙여넣기. 이 문서가 Claude에게:
- 프로젝트 컨텍스트 (희앤썬 그룹 · 4 브랜드)
- FIXED FACTS (변경 금지 사항)
- 작업 방식 (spec 제안 → 합의 → str_replace 수정)
- 톤·매너
를 한 번에 전달한다.

### 3. 슬라이드 HTML 업로드

새 프로젝트의 **Knowledge** 영역에 22개 HTML 파일을 업로드한다. 또는 ZIP으로 묶어서 첫 대화에 첨부.

### 4. 작업 시작

새 대화에서 Claude에게 다음과 같이 시작:

> "희앤썬 deck 디벨롭 이어서 진행. SLIDE_INDEX.md와 22개 HTML 모두 가지고 있어.
> Slide 17 (Pool Rooms Two Tiers)의 The First Page Suite 패키지 5개 항목 중
> 'KORRES 듀오'를 'AC 시그니처 어메니티 듀오'로 바꿔줘."

Claude가:
1. 해당 HTML 파일을 view로 열고
2. str_replace로 정확한 부분만 수정
3. present_files로 결과 보여줌

### 5. 최종 export (작업 완료 후)

수정 작업이 충분히 쌓이면, 다음 스크립트로 PPT/통합 HTML을 다시 빌드:

```bash
# 1. HTML → PNG 렌더링 (Playwright 필요)
python scripts/render_pngs.py

# 2. PowerPoint 빌드
python scripts/build_pptx.py

# 3. 단일 HTML 빌드
python scripts/build_deck_html.py
```

또는 Claude에게 **"deck 다시 빌드해줘"** 하면 코드 환경에서 자동 실행.

---

## 슬라이드 편집 규칙

### ✓ 안전한 편집 (Claude에게 부탁)

- 카피 변경 (Title / Subtitle / Hook / Closing)
- 가격·시간·숫자 데이터 업데이트
- 카드 내 본문 행 (sig-row, content-desc 등) 추가/수정
- 색상 변수 변경 (`--gold`, `--navy` 등 — 한 번에 모든 슬라이드 반영)
- 새 zone 추가 (예: 페이지 하단에 KPI 띠 추가)

### ⚠ 주의가 필요한 편집

- **레이아웃 grid 변경** — 다른 zone에 영향. spec 합의 후 진행.
- **새 슬라이드 추가** — Section 구조와 흐름 영향. 어느 위치에 들어갈지 합의 필요.
- **DESIGN_TOKENS.md 변경** — 한 슬라이드만 바꾸면 일관성 깨짐. 모든 슬라이드 반영해야 함.

### ✗ 하지 말아야 할 편집

- 슬라이드 파일 이름 변경 (스크립트가 정해진 파일명을 찾음)
- 폰트 import URL 변경 (Cormorant Garamond / Noto Sans KR / Inter 외)
- `.slide` 컨테이너 크기 변경 (1280×720 고정)

---

## 워크플로우 예시

### 사례 1 · 한 줄 카피 수정

> 사용자: "Slide 22 KLOUD의 Closing 카피를 _Play It Loud, Daily and Themed._ 에서 _Loud, Always._ 로 바꿔줘"

→ Claude:
1. `view slide-22-kloud-brand-definition.html`
2. `str_replace`로 해당 부분만 교체
3. `present_files`로 결과 표시

### 사례 2 · 새 Section 추가

> 사용자: "Section 02 Closer 페이지 추가하자. Hotel Brief 7장의 한 줄 요약 + Closing"

→ Claude:
1. SLIDE_INDEX.md 참조해서 Section 02 슬라이드 7장 (s9~s16) 카피 추출
2. 새 페이지 spec 제안 (zone 구성 + 카피)
3. 합의 후 새 HTML 파일 생성 → `slide-16b-section02-closer.html`
4. 다음 export 시 이 파일도 자동 포함

### 사례 3 · 일괄 색상 변경

> 사용자: "전체 deck의 골드를 #B8945A → #C5A572로 (한 톤 밝게)"

→ Claude:
1. DESIGN_TOKENS.md에서 변수 확인
2. 22개 HTML 모두 `--gold:#B8945A` → `--gold:#C5A572` 일괄 sed
3. 변경 영향 페이지 list로 확인

---

## 자주 묻는 작업

| 작업 | 명령 예시 |
|---|---|
| 한 슬라이드 카피 수정 | "Slide N의 [카피] 부분을 [새 카피]로" |
| 새 슬라이드 추가 | "Section X에 [주제] 페이지 추가하자" |
| 슬라이드 순서 변경 | "Slide A와 B 순서 바꾸자" |
| 색상 일괄 변경 | "전체 골드 톤 한 단계 밝게" |
| 폰트 사이즈 조정 | "Slide N의 Title 폰트 사이즈 한 단계 줄여" |
| 최종 export | "deck PPT랑 HTML로 다시 빌드해줘" |

---

## 알려진 제약

- **PPTX는 PNG 이미지 슬라이드** — PowerPoint에서 직접 텍스트 편집 불가. 텍스트 수정은 항상 HTML 소스에서.
- **폰트 라이센스** — Google Fonts (Cormorant Garamond, Noto Sans KR, Inter) 사용. 상업 deliverable 시 폰트 라이센스 확인.
- **Mermaid 다이어그램** — 현재 deck에는 없음. 추가하려면 Mermaid 렌더링 단계 필요.

---

## 작업 자산 백업

이 패키지는 **단일 진실 원본 (Single Source of Truth)** 이다. 패키지 자체를 Git/Drive에 정기 백업 권장:

- `slides/` 22개 HTML
- 4개 가이드 문서 (`README.md`, `PROJECT_BRIEF.md`, `DESIGN_TOKENS.md`, `SLIDE_INDEX.md`)

---

**Built with Claude · 희앤썬 Marketing Strategy 2026**
