---
schema_version: will-ai-question-bank/v1
source_pdf: LSA_LSE_R00_2023KW_C1N.pdf
source_sha256: fc60d3fccd1cd784233e95c31b708a2ac877e03874e892b9f9cfc617582f865c
source_pages: 34
question_bank_version: V1
product_scope: LSA/LSE
---

# LSA_LSE_R00_2023KW_C1N 题库与判定标准

## 1. Source Information

- Source PDF: `LSA_LSE_R00_2023KW_C1N.pdf`
- SHA-256: `fc60d3fccd1cd784233e95c31b708a2ac877e03874e892b9f9cfc617582f865c`
- Physical pages: 34
- Product: KOSMEK LSA/LSE 油压复动式侧向夹紧器
- Product printed pages: 947-958
- Included common-reference printed pages: 1725-1730
- Included control-valve printed pages: 1257-1262 and 1265-1272
- Included sales-reference physical pages: 33-34 (unnumbered)
- Source-evidence policy: PDF page images control visual facts; extracted text is a navigation aid and is not source truth.

## 2. Scope

### 2.1 Product and document scope

This bank covers the LSA standard side-clamp family and LSE high-power side-clamp
family: product positioning, model grammar, specifications, clamp-force and holding-
force relationships, dimensions, mounting, hydraulic circuits, speed adjustment,
installation, maintenance, safety, and the applicable direct-mounted valves included
in the PDF.

Commercial warranty and sales-network material remain in the source inventory but
are excluded from core capability questions. Common hydraulic installation,
speed-control, operation, maintenance, notation, and ancillary-valve facts must use
page-bounded local scope and the appropriate binding so they cannot be confused with
LSA/LSE-local requirements.

### 2.2 Model Grammar

The LSA and LSE printed field order is:

`<Family><BodySize><DesignNo>-<Piping><PlateDirection>`

| Field | Legal values | Meaning and constraint |
|---|---|---|
| Family | `LSA`, `LSE` | `LSA` is the standard side-clamp family; `LSE` is the high-power side-clamp family with a mechanical self-lock mechanism. |
| BodySize | `036` | Clamp-body outside-diameter class, phi 36 mm. |
| DesignNo | `0` | Product version/design number listed by this PDF. |
| Piping | `C` | Manifold/plate piping with supplied G-thread plugs; a separately purchased direct-mounted speed-control valve can be installed. |
| PlateDirection | `L`, `C`, `R` | Left, center, or right plate direction when facing the oil-supply ports. |

The two families share body-size, design, piping, and direction grammar, but they
do not share all operating limits or speed-control rules. In particular, the PDF
requires an inlet-metering BZL-A valve for LSE.

Positive grammar cases:

- `LSA0360-CL`
- `LSA0360-CC`
- `LSA0360-CR`
- `LSE0360-CL`
- `LSE0360-CC`
- `LSE0360-CR`

Negative grammar cases and reasons:

- `LSA0400-CR`: body-size code `040` is not listed for LSA in this PDF.
- `LSE0361-CR`: design number `1` is not listed.
- `LSA0360-SR`: piping value `S` is not listed.
- `LSE0360-CB`: plate direction `B` is not listed.
- `LSA0360-RC`: piping and direction fields are out of order.
- `LSE0360-CR-A`: the BZL control method is not a suffix of the LSE product model.

### 2.3 Source-first inventory and initial dispositions

`HIGH` and `MEDIUM` items remain open until their mapped questions and construction
audits are complete. The disposition column identifies planned work and does not
claim coverage in advance. Each physical-page pair is one repeated two-page printed
spread; the inventory records the pair once rather than treating the duplicate render
as new evidence.

| Inventory ID | Physical / printed page | Local scope | Evidence type | Priority | Testable object | Initial disposition |
|---|---|---|---|---|---|---|
| LSA-LSE-SI-001 | 1-2 / 947-948 | LSA overview and features | TEXT + DRAWING | HIGH | Side-push positioning, zero top interference, installation commonality, 2.8 kN headline force, and direct speed-control mounting | WP2 `FACT`; preserve drawing-local claims |
| LSA-LSE-SI-002 | 3-4 / 949-950 | LSA model, specifications, and force relationship | MODEL + TABLE + FORMULA + CHART | HIGH | Four-field grammar, phi 36 body, stroke/capacity/pressure/temperature/fluid/mass, `F = 0.394 x P`, pressure-force table, and unusable-range consequence | Grammar and `LSA-LSE-Q-0001`; WP2 `TABLE`; WP3 `CALCULATION` / `CHART` |
| LSA-LSE-SI-003 | 5-6 / 951-952 | LSA dimensions, design, installation, and speed control | DRAWING + TABLE + TEXT | HIGH | Ports, mounting geometry, simultaneous-pressure prohibition, welding/dry-environment controls, M4 torque, pin handling, and speed adjustment | WP2 `TABLE`; WP3 `PROCEDURE` / `CAUTION`; repeated dimensions remain direct lookup evidence |
| LSA-LSE-SI-004 | 7-8 / 953-954 | LSE overview and high-power mechanism | TEXT + DRAWING | HIGH | Side-push positioning, 1.5-times LSA force comparison, mechanical self-lock, holding-force role, and BZL-A requirement | WP2 `FACT`; WP3 `CAUTION`; visual mechanism retained for selective verification |
| LSA-LSE-SI-005 | 9-10 / 955-956 | LSE model, specifications, and force/holding relationships | MODEL + TABLE + FORMULA + CHART | HIGH | Shared four-field grammar, stroke/capacity/pressure limits, `F = 0.601 x P`, `Fk = 0.953 x P`, 3.62 kN holding cap, and reaction-force cautions | Grammar and `LSA-LSE-Q-0001`; WP2 `TABLE`; WP3 `CALCULATION` / `CHART` / `CAUTION` |
| LSA-LSE-SI-006 | 11-12 / 957-958 | LSE dimensions, design, installation, and speed control | DRAWING + TABLE + TEXT | HIGH | Direction variants, mounting geometry, simultaneous-pressure prohibition, M4 torque, inlet-metering adjustment, air removal, multi-clamp control, and loaded release | WP2 `TABLE`; WP3 `PROCEDURE` / `CAUTION`; preserve LSE-local circuit exceptions |
| LSA-LSE-SI-007 | 13-14 / 1725-1726 | Common hydraulic installation and speed-control circuits | TEXT + TABLE + STATE_DIAGRAM | HIGH | ISO-VG32 oil list, cleanliness, sealing tape, air bleeding, tightening checks, single/double-acting circuit rules, and LSE exception | WP3 `PROCEDURE` / `CAUTION`; page-bounded `DOCUMENT_COMMON` |
| LSA-LSE-SI-008 | 15-16 / 1727-1728 | Common operation, maintenance, and warranty | TEXT + DRAWING | HIGH | Personnel qualifications, isolation/zero pressure/cooldown, restart checks, no-touch/no-modification, cleaning, inspection, storage, and overhaul | WP3 `CAUTION`; warranty content LOW and excluded; page-bounded scope |
| LSA-LSE-SI-009 | 17-18 / 1729-1730 | Common notation references | TABLE | MEDIUM | Surface-roughness notation and O-ring material/hardness notation mappings | WP2 `TABLE`; page-bounded `DOCUMENT_COMMON` |
| LSA-LSE-SI-010 | 19-20 / 1257-1258 | Direct-mounted control-valve family overview | TEXT + DRAWING + TABLE | MEDIUM | BZL/BZT/BZX/JZG/BZS purposes, direct-mount relationship, and pressure classes | WP2 `FACT` / `TABLE`; ancillary product scope |
| LSA-LSE-SI-011 | 21-22 / 1259-1260 | BZL low-pressure speed-control models and compatibility | MODEL + TABLE + TEXT | HIGH | Thread/design/control-method grammar, A/B circuit meanings, pressure/temperature/torque values, compatibility, reuse warning, and LSA/LSE mapping | WP2 `MODEL` / `TABLE`; WP3 `CAUTION` |
| LSA-LSE-SI-012 | 23-24 / 1261-1262 | BZL flow curves, dimensions, and cautions | CHART + DRAWING + TEXT | MEDIUM | Adjusted/pre-adjustment flow versus turns and pressure loss, port orientation, low-pressure air bleeding, and machining dimensions | WP3 `CHART` / `CAUTION`; genuine visual read required |
| LSA-LSE-SI-013 | 25-26 / 1265-1266 | BZX exhaust valve | MODEL + TABLE + DRAWING + TEXT | MEDIUM | Thread grammar, 35 MPa limit, torque, compatibility, plug-loosening limit, and low-pressure bleeding | WP2 `MODEL` / `TABLE`; WP3 `CAUTION`; ancillary scope |
| LSA-LSE-SI-014 | 27-28 / 1267-1268 | JZG G-thread plug with bleeding function | MODEL + TABLE + DRAWING + TEXT | MEDIUM | Thread grammar, 35 MPa limit, torque/material rule, compatibility, and low-pressure bleeding | WP2 `MODEL` / `TABLE`; WP3 `CAUTION`; ancillary scope |
| LSA-LSE-SI-015 | 29-30 / 1269-1270 | BZS direct-mounted sequence valve model and specifications | MODEL + TABLE + DRAWING + TEXT | HIGH | Thread/design grammar, pressure ranges, paths, torque, compatibility, contamination, pressure-difference, reuse, and flow controls | WP2 `MODEL` / `TABLE`; WP3 `CAUTION` |
| LSA-LSE-SI-016 | 31-32 / 1271-1272 | BZS dimensions, setup, and operating sequence | DRAWING + TABLE + CHART + PROCEDURE | HIGH | Adjustment range, port directions, pressure setting, locking torque, operating sequence, multiple-valve differential, air, and commissioning | WP3 `PROCEDURE` / `CHART` / `CAUTION`; selective visual verification only where layout matters |
| LSA-LSE-SI-017 | 33-34 / unnumbered | Sales addresses and network | TEXT + DRAWING | NON-TEST | Contact details and sales geography | Exclude; not durable LSA/LSE technical knowledge |
| LSA-LSE-SI-018 | 1-32 / all included printed pages | Repeated navigation and paired spread renders | TEXT | NON-TEST | Sidebar navigation, section tabs, page duplication, and cross-reference chrome | Exclude as navigation/render duplication; inventory follows local technical content |

## 3. Question Statistics

- Total: 1
- MODEL: 1

## 4. Questions

## LSA-LSE-Q-0001

**Type: MODEL**

### Target

- Binding: MODEL_FAMILY
- Product: LSA/LSE 油压复动式侧向夹紧器
- Model / Scope: LSA0360-C□ standard family and LSE0360-C□ high-power family

### Question

按 PDF 的型号字段顺序解读 `LSA0360-CL` 与 `LSE0360-CR`。说明两个前缀的
产品系列边界、`036`、末位 `0`、`C` 以及 `L`/`R` 的含义，并判断两个型号
是否合法。

### Standard Answer

`LSA` 表示标准侧向夹紧器系列；`LSE` 表示带机械自锁机构的高能力侧向夹紧器
系列。两个型号中的 `036` 都表示夹紧器本体夹紧部分外径为 phi 36 mm，末位
`0` 是本 PDF 列出的设计编号，`C` 表示板式配管型并配有 G 螺纹堵头。面向
供油口观察时，`L` 表示压板向左，`R` 表示压板向右。因此 `LSA0360-CL` 和
`LSE0360-CR` 的字段顺序与取值均合法。

### Scoring Standard

- P1 [10]: 正确说明 `LSA` 是标准侧向夹紧器系列。
- P2 [15]: 正确说明 `LSE` 是带机械自锁机构的高能力侧向夹紧器系列。
- P3 [15]: 正确说明 `036` 表示夹紧器本体夹紧部分外径 phi 36 mm。
- P4 [10]: 正确说明末位 `0` 是设计编号。
- P5 [15]: 正确说明 `C` 为配有 G 螺纹堵头的板式配管型。
- P6 [10]: 正确限定压板方向的观察视角为面向供油口。
- P7 [10]: 正确说明 `L` 为左、`R` 为右。
- P8 [15]: 正确判断两个示例型号的字段顺序和取值均合法。

### Accepted Variants

- `phi 36 mm` 可写为 `φ36 mm`、`Φ36 mm` 或 `直径 36 mm`。
- `板式配管型` 可写为 `板式连接型` 或 `manifold connection`。
- `机械自锁机构` 可写为语义等价的 `mechanical self-lock mechanism`。

### Forbidden Errors

- 交换 LSA 与 LSE 的标准/高能力系列边界。
- 将 `036` 解释为行程、压力或夹紧力。
- 将末位 `0` 解释为方向或控制方式。
- 将 `C` 解释为压板中央方向。
- 不限定观察视角，或交换 `L` 与 `R`。
- 声称任一示例型号的字段顺序或取值非法。

### Tolerance

- Exact family boundary, phi 36 mm body class, design number `0`, piping value `C`, and direction meanings are required.

### Source

- PDF: LSA_LSE_R00_2023KW_C1N.pdf
- Physical page: 3-4, 7-10
- Printed page: 949-950, 953-956
- Section: LSA/LSE 特点 / 型号表示 / 规格
- Local scope path: LSA 标准侧向夹紧器与 LSE 高能力自锁侧向夹紧器；LSA0360-C□ / LSE0360-C□ 型号字段
- Evidence type: TEXT + MODEL + TABLE + DRAWING
- Evidence: LSA/LSE 特点页区分标准和高能力自锁系列；型号页给出 Family-036-0-C-Direction 顺序，将 036 定义为 phi 36 mm 本体尺寸、0 定义为设计编号、C 定义为配有 G 螺纹堵头的板式配管，并以面向供油口的视角定义 L/C/R。
