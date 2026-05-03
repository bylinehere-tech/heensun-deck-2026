# DESIGN TOKENS — 희앤썬 Deck

22개 슬라이드 모두에 동일하게 적용된 디자인 시스템.
한 곳에서 변경하면 모든 슬라이드에 반영해야 일관성 유지.

---

## 색상 팔레트 (CSS 변수)

```css
:root {
  /* Navy — 주 색상 (Header, Title, Hero) */
  --navy: #0F1E3D;        /* 기본 네이비 */
  --navy-deep: #0a1628;   /* 깊은 네이비 (Cover, 섹션 디바이더) */
  --navy-soft: #1a2540;   /* 연한 네이비 (보조) */

  /* Gold — 강조·구분선·아이콘 */
  --gold: #B8945A;        /* 기본 골드 */
  --gold-soft: #C5A572;   /* 부드러운 골드 (보조) */

  /* Cream — 배경·카드 */
  --cream: #FAF7F2;       /* 슬라이드 기본 배경 */
  --cream-deep: #F0EBE0;  /* 카드 배경 (강조) */
  --cream-warm: #F5EBD8;  /* Pass / Toolkit 키트 톤 (Slide 18, 23) */

  /* Line / Border */
  --line: #D9D3C5;        /* 기본 보더 */

  /* Text */
  --ink: #1A1A1A;         /* 본문 (검정에 가까움) */
  --gray: #6B6B6B;        /* 서브 텍스트 */
  --gray-light: #A8A29A;  /* 가장 약한 텍스트 (페이지 번호 등) */
}
```

### 색상 사용 규칙

| 영역 | 색상 |
|---|---|
| 슬라이드 배경 | `--cream` (기본) / `--navy` (Cover, 섹션 디바이더) |
| Title | `--navy` (cream 배경 위) / `--cream` (navy 배경 위) |
| Subtitle | `--gray` |
| Section tag | `--gold` |
| 보더·구분선 | `--line` (얇은) / `--gold` (강조) |
| Hero italic 카피 | `--navy` (cream 위) / `--cream` (navy 위) |
| 한국어 본문 | `--ink` |
| 카드 배경 | `#fff` (white) |
| 키트 영역 (Welcome Pass / Viral Toolkit) | `--cream-warm` + 이중 골드 보더 |

---

## 타이포그래피

### Google Fonts Import

```html
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;600;700;900&family=Cormorant+Garamond:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

### 폰트 역할

| 폰트 | 역할 | 예시 |
|---|---|---|
| **Cormorant Garamond** | 영문 hero / italic 강조 / 영문 hook | _More Than Hotels._ / _Premium Select._ |
| **Noto Sans KR** | 한국어 모든 영역 / 카드 타이틀 | 호텔이 아니라, 라이프스타일을 운영합니다. |
| **Inter** | 영문 UI / 태그 / 메타 / 캡션 | SECTION TAG / FOOTER / 페이지 번호 |

### 폰트 사이즈 (1280×720 슬라이드 기준)

| 요소 | 폰트 | 사이즈 | weight | letter-spacing |
|---|---|---|---|---|
| Slide Title (32) | Noto Sans KR | 32px | 700 | -0.02em |
| Slide Title (long) | Noto Sans KR | 30px | 700 | -0.02em |
| Slide Subtitle | Noto Sans KR | 13.5px | 400 | -0.01em |
| Section Tag | Inter | 11px | 500 | 0.3em (UPPERCASE) |
| Hero italic (English) | Cormorant Garamond italic | 18-30px | 500 | -0.02em |
| Card Title (Cormorant) | Cormorant Garamond italic | 18-22px | 500-600 | -0.01em |
| Card 한국어 hook | Noto Sans KR | 11.5-12.5px | 700 | -0.01em |
| Card 본문 | Noto Sans KR | 10.5px | 400 | -0.01em |
| Caption / Tag | Inter | 8.5-10px | 600 | 0.18-0.25em (UPPERCASE) |
| 페이지 번호 | Inter | 11px | 500 | 0.2em |
| Footer brand | Inter | 10px | 500 | 0.25em (UPPERCASE) |
| Closing italic | Cormorant Garamond italic | 20px | 500 | -0.01em |

---

## 슬라이드 구조 (모든 슬라이드 공통)

### HTML 골조

```html
<div class="slide" id="sN">
  <div class="pad" style="height:100%">

    <!-- Header block -->
    <div class="header-block">
      <div class="section-tag">XX · Section — Topic</div>
      <h2 class="slide-title">한국어 타이틀.</h2>
      <p class="slide-subtitle">서브 카피 — <strong>강조</strong>.</p>
    </div>

    <!-- Zone 1, 2, 3, ... -->
    <!-- 페이지별 컨텐츠 -->

    <!-- Closing -->
    <div class="closing-line">
      <span class="quote">"English Closing."</span>
      <span class="sep">—</span>
      <strong>한국어 closing echo.</strong>
    </div>

  </div>
  <div class="footer-brand">희앤썬 · Marketing Strategy 2026</div>
  <div class="page-num">N</div>
</div>
```

### 패딩

- `.pad`: `padding: 38-42px 56px` — 슬라이드 외각 여백
- `.header-block`: `margin-bottom: 10-14px`

### 페이지 번호 / Footer 위치 (고정)

```css
.page-num{position:absolute; bottom:32px; right:48px;}
.footer-brand{position:absolute; bottom:32px; left:48px;}
```

---

## 카드 패턴 (Two Signature / Two Tier)

여러 슬라이드 (s11, s17, s18, s20, s22) 에서 반복되는 _두 카드 병렬_ 패턴:

```css
.sig-grid{
  display:grid;
  grid-template-columns:1fr 1fr;
  gap:14px;
  height:284-340px;
}

.sig-card{
  background:#fff;
  border-top:2px solid var(--gold);  /* 일반 */
  /* 또는 */
  border-top:3px solid var(--gold);  /* 강조 (★) */
}

.sig-hero{
  height:90-96px;
  padding:13-14px 20-22px;
  /* hero gradient — 페이지마다 다른 무드 */
}

.sig-name{
  font-family:'Cormorant Garamond';
  font-style:italic;
  font-size:28-30px;
  color:#fff;
}
```

### Hero Gradient 컬렉션

| 슬라이드 | 카드 | Gradient |
|---|---|---|
| s17 Pool Suite | Pool Room | `linear-gradient(135deg,#9bb8c4 0%,#6a8a98 60%,#3a5a68 100%)` (시안) |
| s17 Pool Suite | Pool Suite ★ | `linear-gradient(135deg,#1a2540 0%,#0a1628 60%,#000812 100%)` + gold 보더 |
| s18 Palace | Light Stay | `linear-gradient(135deg,#e8d8b8 0%,#c8a878 100%)` (베이지) |
| s18 Palace | Long Living | `linear-gradient(135deg,#c8a878 0%,#8a6848 60%,#5a3a28 100%)` (브론즈) |
| s20 Kitchen | Daily Anchor | `linear-gradient(135deg,#c8b898 0%,#9a8868 100%)` (매트 베이지) |
| s20 Kitchen | Seasonal Festa | `linear-gradient(135deg,#B8945A 0%,#8a3a4a 50%,#3a1828 100%)` (골드~버건디) |
| s22 KLOUD | Live Rooftop | `linear-gradient(135deg,#2a2858 0%,#1a1838 60%,#0a0828 100%)` (딥 네이비) |
| s22 KLOUD | Themed Nights | `linear-gradient(135deg,#c8a878 0%,#6a3878 60%,#2a0848 100%)` (골드~보라) |

---

## 키트 영역 패턴 (cream-warm)

Slide 18 (Welcome to Gangnam Pass), Slide 23 (Viral Toolkit) 에서 사용:

```css
.kit-band{
  background:var(--cream-warm);
  padding:13px 22px 14px;
  border-top:2px solid var(--gold);
  border-bottom:2px solid var(--gold);
  position:relative;
}
.kit-band::before{
  content:'';
  position:absolute;
  top:5px; left:5px; right:5px; bottom:5px;
  border:1px dashed rgba(184,148,90,.3);
  pointer-events:none;
}
```

→ _봉투·티켓·키트_ 무드. 그룹 자산 카테고리 시각 ring.

---

## 시즌 컬러 (Always Celebrated)

| 시즌 | 메인 컬러 | 사용처 |
|---|---|---|
| **Bloom** (Spring · 가족·기념일) | 파스텔 핑크/그린 | 봄 캠페인 |
| **Splash** (Summer · Pool·호캉스) | 시안 / 블루 | s25 working calendar Splash bar |
| **Encore** (Autumn · 컬처·콜라보) | 갈색 / 카퍼 | s25 working calendar Encore bar |
| **Toast** (Winter · 송년·미식) | 와인 / 버건디 | s25 working calendar Toast bar |

---

## 슬라이드 dimension 고정값

```css
.slide{
  width: 1280px;
  height: 720px;
  background: var(--cream);
  position: relative;
  overflow: hidden;
}
```

- **변경 금지** — PPT 16:9 (1280×720) 표준에 맞춰져 있음.
- 모든 페이지 PNG 렌더링 시 1280×720 기준.

---

## 반응형 스케일 (preview용)

```css
@media (max-width: 1340px){.slide{transform: scale(.72)}}
@media (max-width: 900px){.slide{transform: scale(.45)}}
@media (max-width: 600px){.slide{transform: scale(.28)}}
```

→ 작은 화면에서도 1280×720 비율 유지하며 축소 표시.

---

## 변경 시 주의

| 변경 | 영향 |
|---|---|
| `--gold` 변경 | 모든 슬라이드의 강조·보더·아이콘에 영향. 22개 일괄 sed 필요. |
| `--navy` 변경 | Cover, Section divider, Title 색에 영향. 대대적 수정. |
| 폰트 변경 (Cormorant / Noto / Inter 외) | 카피의 시각 톤 자체가 바뀜. 디자인 합의 필요. |
| 슬라이드 dimension 변경 | render_pngs.py / build_pptx.py 수정도 필요. |
| 패딩 / 마진 변경 | 카드 grid 자동 재계산. 다른 zone에 overflow 가능. |
