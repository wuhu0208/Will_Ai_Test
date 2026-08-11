---
schema_version: will-ai-question-bank/v1
source_pdf: SBR-FVP001-02-C1N.pdf
source_sha256: d81073fb510dc5cb1f22ce0b5105c76278bce8c676b33c3ae6d8f2c7ffed1447
source_pages: 22
question_bank_version: V1
product_scope: FVP/FVH
---

# SBR-FVP001-02-C1N 题库与判定标准

## 1. Source Information

- Source PDF: `SBR-FVP001-02-C1N.pdf`
- SHA-256: `d81073fb510dc5cb1f22ce0b5105c76278bce8c676b33c3ae6d8f2c7ffed1447`
- Physical pages: 22
- Product: KOSMEK FVP/FVH 油压复动式分体式夹钳
- Product printed pages: 1-16
- Included common-caution printed pages: 17-20
- Included accessory: BZL0101-B 低压用回油节流速度控制阀
- Included cover and sales-reference physical pages: 1 and 22 (unnumbered)
- Source-evidence policy: PDF page images control visual facts; extracted text is a navigation aid and is not source truth.

## 2. Scope

### 2.1 Product and document scope

This bank covers the FVP pusher and FVH support families of hydraulic
double-acting split clamps. It includes product positioning, operating principles,
model grammar, specifications, force relationships, allowable load/displacement,
dimensions, mounting and platen design, hydraulic circuits, installation,
maintenance, safety cautions, and the BZL0101-B meter-out speed-control accessory
included in the PDF.

Commercial warranty and sales-network material remain in the source inventory but
are excluded from core capability questions. Common hydraulic installation,
speed-control, operation, and maintenance cautions must use `DOCUMENT_COMMON`
binding with a page-bounded local scope so they cannot be confused with
FVP/FVH-local requirements.

### 2.2 Model Grammar

The printed model fields use the following orders. The FVP and FVH product
families have no option suffix in this PDF.

#### FVP pusher family

`FVP<SizeCode><DesignNo>`

| Field | Legal values | Meaning and constraint |
|---|---|---|
| SizeCode | `060` | Body-width class; the printed body width is 60 mm. |
| DesignNo | `0` | Product-series/design number listed by this PDF. |

#### FVH support family

`FVH<SizeCode><DesignNo>`

| Field | Legal values | Meaning and constraint |
|---|---|---|
| SizeCode | `060` | Body-width class; the printed body width is 60 mm. |
| DesignNo | `0` | Product-series/design number listed by this PDF. |

The prefixes are functional family boundaries: FVP is the pusher type that
advances under clamp-side pressure, while FVH is the support type whose internal
wedge mechanism holds the slide after it contacts the workpiece.

#### BZL low-pressure speed-control accessory

`BZL0<ThreadCode><DesignNo>-<ControlMethod>`

| Field | Legal values | Meaning and constraint |
|---|---|---|
| ThreadCode | `10` | G1/8A thread. |
| DesignNo | `1` | Product-version/design number listed by this PDF. |
| ControlMethod | `B` | Meter-out control; the hyphen before `B` is required. |

`BZL0101-B` is listed for `FVP0600` and is explicitly not compatible with
`FVH0600`.

Positive grammar cases:

- `FVP0600`
- `FVH0600`
- `BZL0101-B`

Negative grammar cases and reasons:

- `FVP0601`: FVP design number `1` is not listed; the printed design number is `0`.
- `FVH1000`: FVH size code `100` is not listed; the printed size code is `060`.
- `FVP0600-B`: FVP has no printed option or control-method suffix.
- `BZL0101`: the required hyphenated meter-out control field `-B` is missing.
- `BZL0101-A`: control method `A` is not listed.
- `BZL0100-B`: BZL design number `0` is not listed; the printed design number is `1`.
- `BZL0201-B`: BZL thread code `20` is not listed in this PDF.

### 2.3 Source-first inventory and initial dispositions

`HIGH` and `MEDIUM` items remain open until their mapped questions and
construction audits are complete. The disposition column identifies planned
Work Packages and does not claim coverage in advance.

| Inventory ID | Physical / printed page | Local scope | Evidence type | Priority | Testable object | Initial disposition |
|---|---|---|---|---|---|---|
| FVP-FVH-SI-001 | 2 / 1 | FVP/FVH overview | TEXT + DRAWING | HIGH | Split-clamp placement freedom, workpiece-following positioning, and contrast with self-centering clamps | WP2 `FACT`; product-series scope |
| FVP-FVH-SI-002 | 3 / 2 | Features and application examples | TEXT + TABLE + DRAWING | MEDIUM | 8 mm stroke, 75 mm maximum platen height, 50 mm allowable eccentricity, family combinations, and representative applications | WP2 `FACT` / `TABLE`; avoid application-drawing duplicates |
| FVP-FVH-SI-003 | 4 / 3 | FVP pusher operation and construction | STATE_DIAGRAM + DRAWING + TEXT | HIGH | Release/clamp port behavior, slide direction, continuous pushing action, opposed-use synchronization, and internal construction | WP2 `FACT`; WP3 `PROCEDURE` / `CAUTION` |
| FVP-FVH-SI-004 | 5 / 4 | FVH support operation and construction | STATE_DIAGRAM + DRAWING + TEXT | HIGH | Release, platen advance, wedge locking, holding-force state, FVP/FVH sequencing, and approximately 50 N spring force during release | WP2 `FACT`; WP3 `PROCEDURE` / `CAUTION` |
| FVP-FVH-SI-005 | 6 / 5 | Product model designation and specifications | TABLE + DRAWING | HIGH | FVP/FVH model fields, family boundary, stroke, force/support values, platen-height range, eccentricity, capacities, pressure, temperature, fluid, and mass | Grammar and representative model question in Section 2.2 / `FVP-FVH-Q-0001`; WP2 `TABLE` |
| FVP-FVH-SI-006 | 7 / 6 | Force and load/displacement relationships | FORMULA + TABLE + CHART + DRAWING | HIGH | FVP height-dependent pusher-force formulae, FVH support-force formula, pressure limits, and FVH load/displacement curve | WP2 `TABLE`; WP3 `CALCULATION` / `CHART` |
| FVP-FVH-SI-007 | 8-11 / 7-10 | FVP/FVH dimensions, mounting, and platen design | DRAWING + TABLE + TEXT | HIGH | External dimensions, oil/air/lubrication ports, mounting surfaces, Rz6.3 sealing face, fastener paths, platen geometry, load position, and positive/negative platen-height orientation | WP2 `TABLE`; WP3 `PROCEDURE` / `CAUTION`; repeated dimension grids remain direct lookup evidence |
| FVP-FVH-SI-008 | 12 / 11 | Product design cautions | TEXT + TABLE + DRAWING | HIGH | Circuit design, simultaneous-pressure prohibition, opposed-use sequencing, collision avoidance, platen-height/eccentricity limits, bolt-position selection, continuous air cleaning, and FVH equal-pressure requirement | WP3 `CAUTION` / `PROCEDURE` |
| FVP-FVH-SI-009 | 13 / 12 | Reference hydraulic circuits | STATE_DIAGRAM + TEXT | HIGH | Opposed FVP synchronization and FVP/FVH sequence-valve circuit order | WP3 `PROCEDURE`; preserve circuit-local conditions |
| FVP-FVH-SI-010 | 14 / 13 | Product installation and speed adjustment | TEXT + TABLE + DRAWING | HIGH | Fluid selection, platen/body fastener strength and torque, gap-free installation, 0.5-1 s stroke target, low-flow startup, abnormal-pressure check, air effects, and temperature adjustment | WP2 `TABLE`; WP3 `PROCEDURE` / `CAUTION` |
| FVP-FVH-SI-011 | 15 / 14 | Product maintenance and inspection | TEXT + TABLE + DRAWING | HIGH | FVP/FVH lubrication frequencies, 1 mL amount, molybdenum-disulfide grease, excess-grease consequences, and cleaning | WP2 `TABLE`; WP3 `PROCEDURE` / `CAUTION` |
| FVP-FVH-SI-012 | 16 / 15 | BZL0101-B model and specifications | MODEL + TABLE + DRAWING | MEDIUM | BZL field grammar, meter-out symbol, pressure/temperature/flow specifications, tightening torque, FVP compatibility, and FVH exclusion | Grammar in Section 2.2; WP2 `MODEL` / `TABLE` |
| FVP-FVH-SI-013 | 17 / 16 | BZL0101-B flow curves, dimensions, and cautions | CHART + DRAWING + TEXT | MEDIUM | Adjusted flow versus turns/pressure loss, pre-adjustment flow, port orientation, dimensions, circuit-design warning, and low-pressure air bleeding | WP3 `CHART` / `CAUTION`; dimensions remain direct lookup evidence |
| FVP-FVH-SI-014 | 18 / 17 | Common hydraulic installation and fluid reference | TEXT + TABLE + DRAWING | HIGH | Fluid selection, contamination control, sealing tape, air-bleeding sequence and 2 MPa limit, tightening checks, and ISO-VG32 oil table | WP3 `PROCEDURE` / `CAUTION`; page-bounded `DOCUMENT_COMMON` |
| FVP-FVH-SI-015 | 19 / 18 | Common hydraulic speed-control circuits | STATE_DIAGRAM + TEXT | HIGH | Double-acting meter-out requirement, meter-in instability, single/double-acting circuit separation, back-pressure coupling, and internal-pressure controls | WP3 `PROCEDURE` / `CAUTION`; page-bounded `DOCUMENT_COMMON` |
| FVP-FVH-SI-016 | 20 / 19 | Common operation and maintenance safety | TEXT + DRAWING | HIGH | Qualified staff, fall/unintended-motion protection, pressure/power isolation, zero-pressure checks, cooldown, restart inspection, no-touch, and no-modification requirements | WP3 `CAUTION`; page-bounded `DOCUMENT_COMMON` |
| FVP-FVH-SI-017 | 21 / 20 | Warranty | TEXT | LOW | Warranty term, coverage, and exclusions | Exclude from core capability bank; commercial policy |
| FVP-FVH-SI-018 | 1 and 22 / unnumbered | Cover, catalog metadata, and sales network | TEXT + DRAWING | NON-TEST | Product identity, catalog number, publication history, contact details, and sales geography | Product identity retained; commercial/contact material excluded |
| FVP-FVH-SI-019 | 2-21 / 1-20 | Navigation and repeated sidebars | TEXT | NON-TEST | Repeated section navigation, accessory links, and caution navigation | Exclude as navigation chrome; inventory follows the local technical content |

## 3. Question Statistics

- Total: 1
- MODEL: 1

## 4. Questions

## FVP-FVH-Q-0001

**Type: MODEL**

### Target

- Binding: MODEL_FAMILY
- Product: FVP/FVH 油压复动式分体式夹钳
- Model / Scope: FVP0600 pusher family and FVH0600 support family

### Question

按 PDF 的型号字段顺序分别解读 `FVP0600` 与 `FVH0600`。说明两个前缀的
功能边界、`060` 和末位 `0` 的含义，并判断这两个型号是否合法以及是否带有
任何选项后缀。

### Standard Answer

`FVP` 表示推紧型分体式夹钳，夹紧侧供压时滑块追随工件前进并持续施加推力；
`FVH` 表示支撑型分体式夹钳，滑块接触工件后由内置楔型机构锁紧并保持位置。
两个型号中的 `060` 都表示本体宽度为 60 mm，末位 `0` 都是本 PDF 列出的
设计编号。`FVP0600` 和 `FVH0600` 的字段顺序与取值均合法；本 PDF 未为
FVP 或 FVH 定义任何选项后缀。

### Scoring Standard

- P1 [15]: 正确说明 `FVP` 是推紧型分体式夹钳。
- P2 [15]: 正确说明 FVP 在夹紧侧供压时前进并持续施加推力。
- P3 [15]: 正确说明 `FVH` 是支撑型分体式夹钳。
- P4 [15]: 正确说明 FVH 接触工件后由内置楔型机构锁紧并保持位置。
- P5 [15]: 正确说明两个型号的 `060` 都表示 60 mm 本体宽度。
- P6 [10]: 正确说明两个型号末位 `0` 都是设计编号。
- P7 [10]: 正确判断 `FVP0600` 和 `FVH0600` 均为合法型号。
- P8 [5]: 正确说明本 PDF 未为 FVP/FVH 定义选项后缀。

### Accepted Variants

- `推紧型` 可写为 `pusher type`。
- `支撑型` 可写为 `support type`。
- `内置楔型机构` 可写为语义等价的 `internal wedge mechanism`。

### Forbidden Errors

- 交换 FVP 与 FVH 的推紧/支撑功能。
- 将 `060` 解释为 60 kN、60 MPa 或 60 mm 行程。
- 将末位 `0` 解释为行程编号、压力等级或选项。
- 声称 `FVP0600` 或 `FVH0600` 非法。
- 为 FVP/FVH 添加 PDF 未定义的 `-L`、`-B` 或其他选项后缀。

### Tolerance

- Exact family meanings, 60 mm body-width class, design number `0`, and no-option conclusion are required.

### Source

- PDF: SBR-FVP001-02-C1N.pdf
- Physical page: 4-6
- Printed page: 3-5
- Section: 动作说明 / 型号表示 / 规格
- Local scope path: FVP 推紧型与 FVH 支撑型动作说明；型号表示 FVP0600 / FVH0600；尺寸代码 060 与设计编号 0
- Evidence type: STATE_DIAGRAM + TABLE + DRAWING + TEXT
- Evidence: FVP 动作页定义推紧型持续推力，FVH 动作页定义楔型锁紧保持；型号表示页给出 FVP0600/FVH0600 的字段顺序，并将 060 定义为 60 mm 本体宽度、0 定义为设计编号。
