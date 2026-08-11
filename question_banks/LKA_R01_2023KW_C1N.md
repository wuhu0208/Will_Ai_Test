---
schema_version: will-ai-question-bank/v1
source_pdf: LKA_R01_2023KW_C1N.pdf
source_sha256: 9fb2ad70cb85984c8d3e76f52b0b7e7072635c8e120685fa1af71bdaaa9082c5
source_pages: 58
question_bank_version: V1
product_scope: LKA
---

# LKA_R01_2023KW_C1N 题库与判定标准

## 1. Source Information

- Source PDF: `LKA_R01_2023KW_C1N.pdf`
- SHA-256: `9fb2ad70cb85984c8d3e76f52b0b7e7072635c8e120685fa1af71bdaaa9082c5`
- Physical pages: 58
- Product: KOSMEK LKA 油压杠杆式夹紧器
- Product printed pages: 749-786
- Included control-valve printed pages: 1257-1266, 1269-1272
- Included manifold-block printed pages: 1697-1700
- Included sales-reference printed pages: 947-948
- Source-evidence policy: PDF page images control visual facts; OCR is a navigation aid and is not source truth.

## 2. Scope

### 2.1 Product and document scope

This bank covers the LKA hydraulic double-acting link-clamp series: operating
principle, body sizes, model grammar, specifications, clamp-force and allowable-
eccentricity curves, dimensions, action-confirmation variants, clamp-arm design,
installation, hydraulic circuits, cautions, maintenance, and the applicable control
valves and manifold blocks included in the PDF.

Commercial warranty and sales-network material remain in the source inventory but
are excluded from core capability questions. Common hydraulic cautions and notation
references must use `DOCUMENT_COMMON` binding with a page-bounded local scope so
they cannot be confused with product-local LKA requirements.

### 2.2 Model Grammar

The printed field order is:

`LKA<BodySize>0-<Piping><ArmDirection><Confirmation?>-<Option?>`

An unmarked optional field is blank. Fields must remain in the printed order and
follow these rules.

| Field | Legal values | Meaning and constraint |
|---|---|---|
| BodySize | `036`, `040`, `048`, `055`, `065`, `075`, `090`, `105` | Indicates clamp-body outside diameter phi 36, 40, 48, 55, 65, 75, 90, or 105 mm. |
| DesignNo | `0` | Product version/design number listed by this PDF. |
| Piping | `C`, `S` | `C` is manifold connection with a supplied G-thread plug; the separately purchased direct-mounted speed-control valve may be installed and BZL-B is recommended. `S` is external piping with an Rc thread and no manifold port. |
| ArmDirection | `L`, `C`, `R` | Left, center, or right clamp-arm direction when viewed with the piping port at the front. |
| Confirmation | blank, `D`, `M`, `N`, `NC`, `NL`, `NR` | Blank is standard without action confirmation. `D` is probe dual-rod type. `M` is air-sensor manifold connection. `N` is air-sensor external piping at the standard phase; `NC`, `NL`, and `NR` select the other printed air-port phases. |
| Option | blank, `A`, `H`, `K` | Blank is standard. `A` is quick-change clamp-arm type A. `H` is high-strength link-plate type. `K` is flanged-pin C-retaining-ring type. |

Additional model constraints:

- Option `H` is available only for body sizes `036`, `040`, `048`, `055`, `065`, and `075`; it is unavailable for `090` and `105`.
- The PDF directs users to inquire separately for detailed compatibility among options. A combination not explicitly established by source evidence must not be treated as legal merely because each individual field value exists.
- The printed example `LKA0480-CR--` uses blank Confirmation and Option fields and is a valid standard configuration.

Positive grammar case:

- `LKA0480-CR--`

Negative grammar cases and reasons:

- `LKA0500-CR--`: body code `050` is not listed.
- `LKA0481-CR--`: design number `1` is not listed.
- `LKA0480-XR--`: piping value `X` is not listed.
- `LKA0480-CX--`: arm direction `X` is not listed.
- `LKA1050-CR--H`: option `H` is unavailable for body size `105`.

### 2.3 Source-first inventory and initial dispositions

`HIGH` and `MEDIUM` items remain open until their mapped questions and construction
audits are complete. The disposition column identifies planned Work Packages and
does not claim coverage in advance.

| Inventory ID | Physical / printed page | Local scope | Evidence type | Priority | Testable object | Initial disposition |
|---|---|---|---|---|---|---|
| LKA-SI-001 | 1 / 749 | Product family introduction > LKA identity and operating principle | TEXT + DRAWING | HIGH | LKA position in the link-clamp family, release/clamp motion, and representative applications | WP2 `FACT`; WP3 `PROCEDURE` |
| LKA-SI-002 | 2 / 750 | Product-family examples | TEXT + DRAWING | LOW | Contextual examples of other link-clamp models | Context only; exclude facts not bound to LKA |
| LKA-SI-003 | 3-4 / 751-752 | Product lineup and accessory overview | TABLE + DRAWING | MEDIUM | Product-type boundaries, variant selection, and accessory relationships | WP2 `FACT` / `TABLE`; retain only LKA-relevant facts |
| LKA-SI-004 | 5 / 753 | Table of contents | TEXT | NON-TEST | Navigation map for LKA product, common cautions, valves, and manifold blocks | Navigation only |
| LKA-SI-005 | 6 / 754 | LKA features and cross-section | TEXT + DRAWING | HIGH | Compact body, integrated fulcrum, coolant protection, eccentric-load allowance, arm directions, and direct speed-control mounting | WP2 `FACT`; WP3 `CAUTION` |
| LKA-SI-006 | 7 / 755 | Model designation | TABLE + DRAWING | HIGH | Six-field order, legal body/piping/arm/confirmation/option values, and H-option size restriction | Started with `LKA-Q-0001`; expand and audit in WP2/WP4 |
| LKA-SI-007 | 8 / 756 | Specifications | TABLE + FORMULA | HIGH | Clamp area, clamp-force formula, capacities, strokes, pressure, temperature, fluid, and weight for eight body sizes and confirmation variants | WP2 `TABLE` / `SPEC_LOOKUP`; WP3 `CALCULATION` |
| LKA-SI-008 | 9-12 / 757-760 | Clamp-force capability curves | CHART + FORMULA | HIGH | Pressure/arm-length/clamp-force relationships with and without action confirmation | WP3 `CHART` / `CALCULATION` |
| LKA-SI-009 | 13-16 / 761-764 | Allowable eccentricity curves | CHART + DRAWING | HIGH | Standard versus high-strength-link eccentricity limits and consequences of exceeding them | WP3 `CHART` / `CAUTION` |
| LKA-SI-010 | 17 / 765 | Standard model dimensions | DRAWING + TABLE | HIGH | External, mounting, port, arm, and interference dimensions | WP2 `TABLE` / `SPEC_LOOKUP`; WP3 `CAUTION` |
| LKA-SI-011 | 18-19 / 766-767 | Probe dual-rod confirmation type `D` | DRAWING + TABLE | HIGH | Model-specific construction, confirmation interface, and dimensions | WP2 `FACT` / `TABLE` |
| LKA-SI-012 | 20-21 / 768-769 | Air-sensor manifold confirmation type `M` | DRAWING + TABLE | HIGH | Model-specific air interface, construction, and dimensions | WP2 `FACT` / `TABLE`; WP3 `PROCEDURE` |
| LKA-SI-013 | 22-23 / 770-771 | Air-sensor external-piping types `N/NC/NL/NR` | DRAWING + TABLE | HIGH | Four port phases, external piping, and dimensions | WP2 `MODEL` / `TABLE`; WP3 `PROCEDURE` |
| LKA-SI-014 | 24-25 / 772-773 | Quick-change arm option `A` | DRAWING + TABLE + TEXT | HIGH | Quick-change construction, dimensions, installation, and fastening | WP2 `FACT` / `TABLE`; WP3 `PROCEDURE` |
| LKA-SI-015 | 26 / 774 | Link-plate and flanged-pin options | DRAWING + TABLE + TEXT | HIGH | Option-specific model and dimensional constraints for `H` and `K` | WP2 `MODEL` / `TABLE`; WP3 `CAUTION` |
| LKA-SI-016 | 27 / 775 | Air-sensor connection and confirmation | TEXT + DRAWING + TABLE | HIGH | Differential-pressure confirmation, sensor connection limit, exhaust protection, arm alignment, and O-ring grease controls | WP3 `PROCEDURE` / `CAUTION` |
| LKA-SI-017 | 28 / 776 | Air-sensor circuit and process charts | STATE_DIAGRAM + CHART | HIGH | Clamp/release sensing sequence, pressure/stroke states, and sensor-output conditions | WP3 `PROCEDURE` / `CHART` |
| LKA-SI-018 | 29 / 777 | Clamp-arm design | DRAWING + FORMULA + CHART | HIGH | Arm dimensions, clamp-point distance, force-curve selection, and geometric limits | WP3 `CALCULATION` / `PROCEDURE` / `CAUTION` |
| LKA-SI-019 | 30 / 778 | Blank arm and fastening kit | DRAWING + TABLE + TEXT | MEDIUM | Blank-arm selection, machining, fastener kit, and compatibility constraints | WP2 `TABLE`; WP3 `PROCEDURE` |
| LKA-SI-020 | 31 / 779 | LKA-specific design and installation cautions | TEXT + DRAWING | HIGH | Hydraulic circuit, simultaneous pressure prohibition, axial loading, eccentricity, contamination, parallel clamping, pins, mounting, and sensor references | WP3 `CAUTION` / `PROCEDURE` |
| LKA-SI-021 | 32 / 780 | LKA-specific operation and adjustment | TEXT + DRAWING + TABLE | HIGH | Quick-change fastening, action time, air bleeding, speed adjustment, fulcrum adjustment, and probe installation | WP3 `PROCEDURE` / `CAUTION` |
| LKA-SI-022 | 33 / 781 | Common hydraulic installation cautions | TEXT + DRAWING | HIGH | Oil selection, cleaning, sealing tape, air bleeding, and fastener checks | WP3 `PROCEDURE` / `CAUTION`; bind as page-bounded `DOCUMENT_COMMON` |
| LKA-SI-023 | 34 / 782 | Common hydraulic speed-control circuits | STATE_DIAGRAM + TEXT | HIGH | Single/double-acting circuit differences, meter-out/meter-in behavior, air instability, circuit separation, and back pressure | WP3 `PROCEDURE` / `CAUTION`; bind as page-bounded `DOCUMENT_COMMON` |
| LKA-SI-024 | 35 / 783 | Common operation and maintenance cautions | TEXT | HIGH | Qualified staff, energy isolation, restart checks, moving-part avoidance, modification prohibition, inspection, storage, and overhaul | WP3 `CAUTION` / `PROCEDURE`; bind as page-bounded `DOCUMENT_COMMON` |
| LKA-SI-025 | 36 / 784 | Warranty | TEXT | LOW | Warranty term, coverage, and exclusions | Exclude from core capability bank; commercial policy |
| LKA-SI-026 | 37-38 / 785-786 | Common notation references | TABLE | MEDIUM | Surface-roughness and O-ring old/new notation mappings | WP2 `TABLE`; bind as page-bounded `DOCUMENT_COMMON` |
| LKA-SI-027 | 39 / 1257 | Control-valve family introduction | TEXT + DRAWING | MEDIUM | BZL/BZT/BZX/JZG/BZS family purpose and direct-mount relationship | WP2 `FACT`; ancillary scope |
| LKA-SI-028 | 40 / 1258 | Control-valve type comparison | TABLE + DRAWING | MEDIUM | Pressure classes and functions of speed, exhaust, plug, and sequence-valve types | WP2 `TABLE` / `SPEC_LOOKUP`; ancillary scope |
| LKA-SI-029 | 41-44 / 1259-1262 | BZL/BZT speed-control valves | TABLE + CHART + DRAWING | MEDIUM | Model grammar, specifications, compatible threads, flow curves, dimensions, and circuit cautions | WP2 `MODEL` / `TABLE`; WP3 `CHART` / `CAUTION` |
| LKA-SI-030 | 45-48 / 1263-1266 | BZX exhaust valves and JZG plugs | TABLE + DRAWING + TEXT | MEDIUM | Model grammar, pressure/specification limits, compatibility, dimensions, and exhaust safety | WP2 `MODEL` / `TABLE`; WP3 `CAUTION` |
| LKA-SI-031 | 49-52 / 1269-1272 | BZS direct-mounted sequence valves | TABLE + CHART + DRAWING + TEXT | HIGH | Model grammar, operating/setting pressure, compatibility, dimensions, pressure-flow behavior, contamination, air, and adjustment cautions | WP2 `MODEL` / `TABLE`; WP3 `CHART` / `PROCEDURE` / `CAUTION` |
| LKA-SI-032 | 53-56 / 1697-1700 | Manifold blocks | TABLE + DRAWING + TEXT | MEDIUM | WHZ/LZY/LZ/TMZ/DZ families, applicable models, dimensions, machining, height adjustment, and bolt cautions | WP2 `MODEL` / `TABLE`; WP3 `CAUTION`; ancillary scope |
| LKA-SI-033 | 57-58 / 947-948 | Sales addresses and network | TEXT + DRAWING | NON-TEST | Contact details, sales geography, and certification marks | Exclude; not durable LKA technical knowledge |

## 3. Question Statistics

- Total: 1
- MODEL: 1

## 4. Questions

## LKA-Q-0001

**Type: MODEL**

### Target

- Binding: EXACT_MODEL
- Product: LKA 油压杠杆式夹紧器
- Model / Scope: LKA0480-CR--

### Question

请按 PDF 的型号字段顺序解读 `LKA0480-CR--`：说明主体尺寸、设计编号、
配管方式、从配管口正面观察时的压板方向、动作确认方式和选配项，并判断
该型号表示是否合法。

### Standard Answer

`048` 表示夹紧器主体夹紧部分的外径为 phi 48 mm，设计编号为 `0`。`C`
表示板式连接型，附带 G 螺纹堵头，并可安装另购的直装式速度控制阀，推荐
型号为 BZL-B。`R` 表示配管口位于身前观察时，压板夹紧方向为右。动作确认
字段为空，表示无动作确认的标准型；选配字段也为空，表示无选配的标准型。
该型号与 PDF 的印刷示例一致，字段顺序和取值均合法。

### Scoring Standard

- P1 [15]: 正确说明 `048` 表示夹紧器主体夹紧部分外径 phi 48 mm。
- P2 [10]: 正确说明设计编号为 `0`。
- P3 [15]: 正确说明 `C` 为板式连接型。
- P4 [10]: 正确说明 `C` 型附带 G 螺纹堵头。
- P5 [10]: 正确说明可另购直装式速度控制阀，且推荐 BZL-B。
- P6 [15]: 正确说明 `R` 是从配管口正面观察时向右夹紧。
- P7 [10]: 正确说明空白动作确认字段表示无动作确认的标准型。
- P8 [10]: 正确说明空白选配字段表示无选配的标准型。
- P9 [5]: 明确判断该型号字段顺序和取值合法。

### Accepted Variants

- `phi 48 mm` 可写为 `φ48 mm`、`Φ48 mm` 或 `直径 48 mm`。
- `板式连接型` 可写为 `manifold connection` 或 `板式配管`。
- `无动作确认`、`无选配` 可分别表述为对应字段为空或标准配置。

### Forbidden Errors

- 将 `048` 解释为活塞杆直径、行程或夹紧力。
- 将 `C` 解释为外配管型，或声称它使用 Rc 螺纹且无板式连接口。
- 将 `R` 解释为从压板端或任意未规定视角观察的方向。
- 将任一空白字段解释为 `D`、`M`、`N`、`A`、`H` 或 `K`。
- 将合法的印刷示例判定为非法。

### Tolerance

- Exact field meanings, phi 48 mm, right-hand viewing convention, and blank-field semantics are required.

### Source

- PDF: LKA_R01_2023KW_C1N.pdf
- Physical page: 7
- Printed page: 755
- Section: 型号表示
- Local scope path: 型号表示 > LKA0480-CR-- 印刷示例；主体尺寸 / 设计编号 / 配管方式 / 压板方向 / 动作确认方式 / 选配项
- Evidence type: TABLE + DRAWING
- Evidence: 印刷示例按主体尺寸、设计编号、配管、压板方向、动作确认和选配排列字段；同页定义 048、0、C、R 以及两个无符号字段的含义。
