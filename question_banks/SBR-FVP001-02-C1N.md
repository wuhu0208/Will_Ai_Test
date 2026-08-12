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

### 2.3 Source inventory and coverage

The inventory maps durable source objects to representative questions or an explicit
coverage disposition. Repeated numeric grids, illustrations, and ancillary material
remain direct source evidence where a standalone question would add little
discrimination.

| Inventory ID | Physical / printed page | Local scope | Evidence type | Priority | Testable object | Coverage disposition |
|---|---|---|---|---|---|---|
| FVP-FVH-SI-001 | 2 / 1 | FVP/FVH overview | TEXT + DRAWING | HIGH | Split-clamp placement freedom, workpiece-following positioning, and contrast with self-centering clamps | Product positioning and workpiece-following behavior in `FVP-FVH-Q-0002` |
| FVP-FVH-SI-002 | 3 / 2 | Features and application examples | TEXT + TABLE + DRAWING | MEDIUM | 8 mm stroke, 75 mm maximum platen height, 50 mm allowable eccentricity, family combinations, and representative applications | Headline envelope in `FVP-FVH-Q-0002`; repeated application drawings remain illustrative context rather than duplicate questions |
| FVP-FVH-SI-003 | 4 / 3 | FVP pusher operation and construction | STATE_DIAGRAM + DRAWING + TEXT | HIGH | Release/clamp port behavior, slide direction, continuous pushing action, opposed-use synchronization, and internal construction | FVP action sequence in `FVP-FVH-Q-0012` and opposed-use controls in `FVP-FVH-Q-0013`; labeled internal parts remain explanatory drawing context |
| FVP-FVH-SI-004 | 5 / 4 | FVH support operation and construction | STATE_DIAGRAM + DRAWING + TEXT | HIGH | Release, platen advance, wedge locking, holding-force state, FVP/FVH sequencing, and approximately 50 N spring force during release | FVH action, wedge locking, family boundary, and 50 N release behavior in `FVP-FVH-Q-0012`; opposed sequence in `FVP-FVH-Q-0013` |
| FVP-FVH-SI-005 | 6 / 5 | Product model designation and specifications | TABLE + DRAWING | HIGH | FVP/FVH model fields, family boundary, stroke, force/support values, platen-height range, eccentricity, capacities, pressure, temperature, fluid, and mass | Grammar and family boundary in Section 2.2 and `FVP-FVH-Q-0001`; shared limits in `FVP-FVH-Q-0003`; capacities/mass in `FVP-FVH-Q-0004`; formulas in `FVP-FVH-Q-0005`; listed fluid remains direct selection evidence |
| FVP-FVH-SI-006 | 7 / 6 | Force and load/displacement relationships | FORMULA + TABLE + CHART + DRAWING | HIGH | FVP height-dependent pusher-force formulae, FVH support-force formula, pressure limits, and FVH load/displacement curve | Formula table in `FVP-FVH-Q-0005`, deterministic calculations in `FVP-FVH-Q-0009` and `FVP-FVH-Q-0010`, and genuine chart read in `FVP-FVH-Q-0011` |
| FVP-FVH-SI-007 | 8-11 / 7-10 | FVP/FVH dimensions, mounting, and platen design | DRAWING + TABLE + TEXT | HIGH | External dimensions, oil/air/lubrication ports, mounting surfaces, Rz6.3 sealing face, fastener paths, platen geometry, load position, and positive/negative platen-height orientation | Fastener paths in `FVP-FVH-Q-0006` and platen geometry/load-position controls in `FVP-FVH-Q-0018`; repeated external, port, and sealing-face dimension grids remain direct design lookup evidence |
| FVP-FVH-SI-008 | 12 / 11 | Product design cautions | TEXT + TABLE + DRAWING | HIGH | Circuit design, simultaneous-pressure prohibition, opposed-use sequencing, collision avoidance, platen-height/eccentricity limits, bolt-position selection, continuous air cleaning, and FVH equal-pressure requirement | Hydraulic, opposed-use, air-cleaning, and equal-pressure controls in `FVP-FVH-Q-0013`; platen limits and bolt positions in `FVP-FVH-Q-0018`; collision illustration remains direct handling context |
| FVP-FVH-SI-009 | 13 / 12 | Reference hydraulic circuits | STATE_DIAGRAM + TEXT | HIGH | Opposed FVP synchronization and FVP/FVH sequence-valve circuit order | Opposed FVP synchronization and FVH-before-FVP order in `FVP-FVH-Q-0013`; connection-count and piping-dependent timing remains an equipment-specific commissioning adjustment |
| FVP-FVH-SI-010 | 14 / 13 | Product installation and speed adjustment | TEXT + TABLE + DRAWING | HIGH | Fluid selection, platen/body fastener strength and torque, gap-free installation, 0.5-1 s stroke target, low-flow startup, abnormal-pressure check, air effects, and temperature adjustment | Fasteners and gap-free mounting in `FVP-FVH-Q-0006`; complete speed adjustment in `FVP-FVH-Q-0014`; fluid list remains direct installation selection evidence |
| FVP-FVH-SI-011 | 15 / 14 | Product maintenance and inspection | TEXT + TABLE + DRAWING | HIGH | FVP/FVH lubrication frequencies, 1 mL amount, molybdenum-disulfide grease, excess-grease consequences, and cleaning | Lubrication schedule/material in `FVP-FVH-Q-0007`; excess-grease and contamination consequences in `FVP-FVH-Q-0021` |
| FVP-FVH-SI-012 | 16 / 15 | BZL0101-B model and specifications | MODEL + TABLE + DRAWING | MEDIUM | BZL field grammar, meter-out symbol, pressure/temperature/flow specifications, tightening torque, FVP compatibility, and FVH exclusion | BZL grammar in Section 2.2; specifications and compatibility in `FVP-FVH-Q-0008`; installation torque consequence in `FVP-FVH-Q-0017` |
| FVP-FVH-SI-013 | 17 / 16 | BZL0101-B flow curves, dimensions, and cautions | CHART + DRAWING + TEXT | MEDIUM | Adjusted flow versus turns/pressure loss, pre-adjustment flow, port orientation, dimensions, circuit-design warning, and low-pressure air bleeding | Adjusted-flow chart in `FVP-FVH-Q-0019` and circuit/bleeding cautions in `FVP-FVH-Q-0017`; pre-adjustment curve, ports, and dimensions remain direct selection/installation evidence |
| FVP-FVH-SI-014 | 18 / 17 | Common hydraulic installation and fluid reference | TEXT + TABLE + DRAWING | HIGH | Fluid selection, contamination control, sealing tape, air-bleeding sequence and 2 MPa limit, tightening checks, and ISO-VG32 oil table | Page-bounded air-bleeding procedure in `FVP-FVH-Q-0015`; fluid table, contamination, sealing tape, and tightening checks remain common installation reference context |
| FVP-FVH-SI-015 | 19 / 18 | Common hydraulic speed-control circuits | STATE_DIAGRAM + TEXT | HIGH | Double-acting meter-out requirement, meter-in instability, single/double-acting circuit separation, back-pressure coupling, and internal-pressure controls | Page-bounded double-acting speed-control, circuit-separation, back-pressure, and internal-pressure safeguards in `FVP-FVH-Q-0020` |
| FVP-FVH-SI-016 | 20 / 19 | Common operation and maintenance safety | TEXT + DRAWING | HIGH | Qualified staff, fall/unintended-motion protection, pressure/power isolation, zero-pressure checks, cooldown, restart inspection, no-touch, and no-modification requirements | Page-bounded operation and maintenance controls in `FVP-FVH-Q-0016` |
| FVP-FVH-SI-017 | 21 / 20 | Warranty | TEXT | LOW | Warranty term, coverage, and exclusions | Exclude from core capability bank; commercial policy |
| FVP-FVH-SI-018 | 1 and 22 / unnumbered | Cover, catalog metadata, and sales network | TEXT + DRAWING | NON-TEST | Product identity, catalog number, publication history, contact details, and sales geography | Product identity retained; commercial/contact material excluded |
| FVP-FVH-SI-019 | 2-21 / 1-20 | Navigation and repeated sidebars | TEXT | NON-TEST | Repeated section navigation, accessory links, and caution navigation | Exclude as navigation chrome; inventory follows the local technical content |

## 3. Question Statistics

- Total: 21
- FACT: 1
- SPEC_LOOKUP: 2
- TABLE: 4
- MODEL: 1
- CALCULATION: 2
- CHART: 2
- PROCEDURE: 3
- CAUTION: 6

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

## FVP-FVH-Q-0002

**Type: FACT**

### Target

- Binding: PRODUCT_SERIES
- Product: FVP/FVH 油压复动式分体式夹钳
- Model / Scope: FVP/FVH product positioning and headline operating envelope

### Question

说明 FVP/FVH 分体式夹钳相对于对心夹钳的定位特点，并给出目录首页列出的滑块
行程、最大压板高度和容许偏心量。

### Standard Answer

FVP/FVH 采用分体式结构，可按工件宽度自由配置，压板间隔不受对心机构限制；
它在工件实际所在位置夹紧，而不是先把工件定位到夹钳中心。目录列出的滑块
行程为 `8 mm`，最大压板高度为 `75 mm`，容许偏心量为 `50 mm`。

### Scoring Standard

- P1 [20]: 正确说明分体式结构可按工件宽度自由配置。
- P2 [20]: 正确说明压板间隔不受对心机构限制。
- P3 [20]: 正确说明夹钳追随工件实际位置，而非先把工件定位到夹钳中心。
- P4 [15]: 正确给出滑块行程 8 mm。
- P5 [15]: 正确给出最大压板高度 75 mm。
- P6 [10]: 正确给出容许偏心量 50 mm。

### Accepted Variants

- `追随工件实际位置` 可写为 `在工件所在位置夹紧`。
- `分体式` 可写为 `split configuration`。

### Forbidden Errors

- 声称 FVP/FVH 必须把工件定位到夹钳中心后才能夹紧。
- 声称两侧压板间隔由固定本体宽度决定。
- 交换或遗漏 8 mm、75 mm、50 mm 的技术对象或单位。

### Tolerance

- Exact 8 mm stroke, 75 mm maximum platen height, and 50 mm allowable eccentricity are required.

### Source

- PDF: SBR-FVP001-02-C1N.pdf
- Physical page: 2-3
- Printed page: 1-2
- Section: 特点 / 使用实例
- Local scope path: 分体式可自由配置组合；追随工件的位置；滑块行程 / 最大压板高度 / 容许偏心量
- Evidence type: TEXT + DRAWING
- Evidence: 首页对比对心夹钳与分体式夹钳的定位方式，并在特点页列出 8 mm 滑块行程、75 mm 最大压板高度和 50 mm 容许偏心量。

## FVP-FVH-Q-0003

**Type: SPEC_LOOKUP**

### Target

- Binding: PRODUCT_SERIES
- Product: FVP/FVH 油压复动式分体式夹钳
- Model / Scope: FVP0600/FVH0600 shared specification limits

### Question

从 FVP0600/FVH0600 共用规格中列出：滑块行程、最大压板高度范围、容许偏心量、
最高使用压力、最低动作压力、耐压和使用温度范围。

### Standard Answer

FVP0600 与 FVH0600 的共用规格为：滑块行程 `8 mm`；最大压板高度
`-50 mm 至 +75 mm`；容许偏心量 `50 mm`；最高使用压力 `7.0 MPa`；
最低动作压力 `1.5 MPa`；耐压 `10.5 MPa`；使用温度 `0-70 °C`。

### Scoring Standard

- P1 [15]: 正确给出滑块行程 8 mm。
- P2 [15]: 正确给出最大压板高度范围 -50 mm 至 +75 mm。
- P3 [15]: 正确给出容许偏心量 50 mm。
- P4 [15]: 正确给出最高使用压力 7.0 MPa。
- P5 [15]: 正确给出最低动作压力 1.5 MPa。
- P6 [15]: 正确给出耐压 10.5 MPa。
- P7 [10]: 正确给出使用温度范围 0-70 °C。

### Accepted Variants

- `-50 mm 至 +75 mm` 可写为 `负侧 50 mm、正侧 75 mm`。
- `0-70 °C` 可写为 `0 至 70 摄氏度`。

### Forbidden Errors

- 把 7.0 MPa、1.5 MPa 或 10.5 MPa 对应到错误的压力项目。
- 将最大压板高度写成只有 +75 mm 而遗漏负侧范围。
- 将 50 mm 容许偏心量写成滑块行程。
- 省略数值对应的单位。

### Tolerance

- All listed specification values and units are exact.

### Source

- PDF: SBR-FVP001-02-C1N.pdf
- Physical page: 6
- Printed page: 5
- Section: 规格
- Local scope path: FVP0600 / FVH0600 共用规格行 > 滑块行程、最大压板高度、容许偏心量、压力、温度
- Evidence type: TABLE
- Evidence: FVP0600/FVH0600 规格表的共用行列出 8 mm、-50/+75 mm、50 mm、7.0/1.5/10.5 MPa 和 0-70 °C。

## FVP-FVH-Q-0004

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: FVP/FVH 油压复动式分体式夹钳
- Model / Scope: FVP0600 and FVH0600 hydraulic capacities, mass, and FVH maximum platen mass

### Question

比较 FVP0600 与 FVH0600 的夹紧侧容量、释放侧容量和本体重量，并给出 FVH0600
允许的最大压板重量。

### Standard Answer

- FVP0600：夹紧侧容量 `5.2 cm³`，释放侧容量 `3.8 cm³`，重量 `2.1 kg`。
- FVH0600：夹紧侧容量 `8.0 cm³`，释放侧容量 `6.2 cm³`，重量 `2.0 kg`。
- FVH0600 的最大压板重量为 `3.0 kg`；FVP0600 该栏为不适用。

### Scoring Standard

- P1 [15]: 正确给出 FVP0600 夹紧侧容量 5.2 cm³。
- P2 [15]: 正确给出 FVP0600 释放侧容量 3.8 cm³。
- P3 [10]: 正确给出 FVP0600 重量 2.1 kg。
- P4 [15]: 正确给出 FVH0600 夹紧侧容量 8.0 cm³。
- P5 [15]: 正确给出 FVH0600 释放侧容量 6.2 cm³。
- P6 [10]: 正确给出 FVH0600 重量 2.0 kg。
- P7 [20]: 正确给出 FVH0600 最大压板重量 3.0 kg，并且不把该值扩展到 FVP0600。

### Accepted Variants

- `cm³` 可写为 `cm3` 或 `立方厘米`。
- `夹紧侧容量` 可写为 `clamp-side volume`。

### Forbidden Errors

- 交换 FVP0600 与 FVH0600 的任一容量或重量。
- 交换夹紧侧与释放侧容量。
- 声称 FVP0600 的最大压板重量也是 3.0 kg。
- 省略容量或重量单位。

### Tolerance

- Exact tabulated values and units are required.

### Source

- PDF: SBR-FVP001-02-C1N.pdf
- Physical page: 6
- Printed page: 5
- Section: 规格
- Local scope path: FVP0600 / FVH0600 规格表 > 夹紧器容量、最大压板重量、重量
- Evidence type: TABLE
- Evidence: 型号列分别给出两侧液压容量和本体重量；最大压板重量仅在 FVH0600 栏列为 3.0 kg。

## FVP-FVH-Q-0005

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: FVP/FVH 油压复动式分体式夹钳
- Model / Scope: FVP0600 platen-height force coefficients and FVH0600 support-force coefficient

### Question

列出 FVP0600 在压板高度 `H = 0、25、50、75 mm` 时的滑块推力公式系数，
并给出 FVH0600 的支撑力公式。说明公式中 `P` 的含义和单位。

### Standard Answer

FVP0600 的滑块推力 `F` 为：

- `H = 0 mm: F = 0.43 × P`
- `H = 25 mm: F = 0.41 × P`
- `H = 50 mm: F = 0.39 × P`
- `H = 75 mm: F = 0.37 × P`

FVH0600 的支撑力公式为 `Fk = 0.57 × P`。`P` 是供给油压，单位为
`MPa`；`F` 和 `Fk` 的结果单位为 `kN`。

### Scoring Standard

- P1 [15]: 正确给出 H=0 mm 时系数 0.43。
- P2 [15]: 正确给出 H=25 mm 时系数 0.41。
- P3 [15]: 正确给出 H=50 mm 时系数 0.39。
- P4 [15]: 正确给出 H=75 mm 时系数 0.37。
- P5 [20]: 正确给出 FVH0600 支撑力公式 Fk = 0.57 × P。
- P6 [10]: 正确说明 P 是供给油压且单位为 MPa。
- P7 [10]: 正确说明 F/Fk 的结果单位为 kN。

### Accepted Variants

- 乘号可写为 `×`、`*` 或等价乘法表达式。
- `Fk` 可写为 `F_k`。

### Forbidden Errors

- 交换任意压板高度与 FVP 系数。
- 把 FVP 滑块推力系数用于 FVH 支撑力。
- 把 `P` 解释为压板高度、偏心量或载荷。
- 省略 MPa 或 kN 单位定义。

### Tolerance

- Formula coefficients are exact; this question does not request a calculated result.

### Source

- PDF: SBR-FVP001-02-C1N.pdf
- Physical page: 7
- Printed page: 6
- Section: 能力曲线图
- Local scope path: FVP 滑块推力曲线图 > 压板高度公式表；FVH 支撑力曲线图 > 支撑力计算公式
- Evidence type: FORMULA + TABLE
- Evidence: 能力页直接列出四个 FVP 高度系数、FVH 的 0.57 系数以及 P、F、Fk 的变量和单位定义。

## FVP-FVH-Q-0006

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: FVP/FVH 油压复动式分体式夹钳
- Model / Scope: FVP0600/FVH0600 platen and body mounting fasteners

### Question

对 FVP0600/FVH0600，列出压板安装螺栓及本体从法兰上部、下部安装时的螺栓
规格和紧固力矩，并说明本体安装螺栓数量、强度等级及压板的无间隙安装要求。

### Standard Answer

压板安装使用强度等级 `12.9` 的 `M6` 内六角螺栓，紧固力矩为
`10 N·m`。本体安装使用 `6` 根强度等级 `12.9` 的内六角螺栓：
从法兰上部安装时用 `M6`、`10 N·m`；从法兰下部安装时用 `M8`、
`25 N·m`。压板必须顶住限位块、无间隙安装。

### Scoring Standard

- P1 [10]: 正确说明压板螺栓强度等级为 12.9。
- P2 [10]: 正确给出压板安装螺栓 M6。
- P3 [10]: 正确给出压板安装紧固力矩 10 N·m。
- P4 [5]: 正确说明本体使用 6 根内六角螺栓。
- P5 [5]: 正确说明本体螺栓强度等级为 12.9。
- P6 [10]: 正确给出法兰上部安装使用 M6。
- P7 [10]: 正确给出法兰上部安装紧固力矩 10 N·m。
- P8 [10]: 正确给出法兰下部安装使用 M8。
- P9 [10]: 正确给出法兰下部安装紧固力矩 25 N·m。
- P10 [10]: 正确说明压板应顶住限位块。
- P11 [10]: 正确说明压板必须无间隙安装。

### Accepted Variants

- `N·m` 可写为 `Nm`。
- `内六角螺栓` 可写为 `socket-head cap screw`。

### Forbidden Errors

- 交换法兰上部与下部安装的 M6/M8 或 10/25 N·m。
- 将压板或本体螺栓强度等级写成非 12.9。
- 使用少于或多于 6 根本体安装螺栓。
- 允许压板与限位块之间保留间隙。

### Tolerance

- Exact bolt sizes, count, strength grade, and tightening torques are required.

### Source

- PDF: SBR-FVP001-02-C1N.pdf
- Physical page: 14
- Printed page: 13
- Section: 安装施工方面的注意事项
- Local scope path: 压板的安装及拆卸；本体的安装；从法兰上部 / 下部安装力矩表
- Evidence type: TABLE + DRAWING + TEXT
- Evidence: 安装页列出压板 M6/10 N·m、本体上部 M6/10 N·m、下部 M8/25 N·m，规定 12.9 强度、6 根本体螺栓和压板无间隙安装。

## FVP-FVH-Q-0007

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: FVP/FVH 油压复动式分体式夹钳
- Model / Scope: dry-air-cleaning lubrication schedule for FVP0600 and FVH0600

### Question

使用干燥空气进行喷气清洁时，FVP0600 与 FVH0600 的推荐润滑频率和每次给油量
分别是多少？同时说明规定的润滑脂类型和目录推荐品。

### Standard Answer

- FVP0600：推荐 `每周 1 次` 或 `每 5,000 次动作 1 次`，每次 `1 mL`。
- FVH0600：推荐 `每月 1 次` 或 `每 50,000 次动作 1 次`，每次 `1 mL`。
- 应使用含二硫化钼的皂基润滑脂；目录推荐 DuPont Toray 的
  `二硫化钼润滑脂 BR2+`。

### Scoring Standard

- P1 [15]: 正确给出 FVP0600 每周 1 次的时间频率。
- P2 [15]: 正确给出 FVP0600 每 5,000 次动作 1 次的动作频率。
- P3 [10]: 正确给出 FVP0600 每次 1 mL。
- P4 [15]: 正确给出 FVH0600 每月 1 次的时间频率。
- P5 [15]: 正确给出 FVH0600 每 50,000 次动作 1 次的动作频率。
- P6 [10]: 正确给出 FVH0600 每次 1 mL。
- P7 [10]: 正确说明使用含二硫化钼的皂基润滑脂。
- P8 [10]: 正确给出推荐品 BR2+。

### Accepted Variants

- `1 mL` 可写为 `1 mℓ` 或 `润滑油枪 1 发`。
- `BR2+` 可写为 `DuPont Toray BR2+`。

### Forbidden Errors

- 交换 FVP0600 与 FVH0600 的润滑周期。
- 将 5,000 次与 50,000 次动作频率交换。
- 使用 1 mL 以外的每次给油量。
- 将润滑脂写成不含二硫化钼的普通液压油。

### Tolerance

- Exact schedules and 1 mL amount are required.

### Source

- PDF: SBR-FVP001-02-C1N.pdf
- Physical page: 15
- Printed page: 14
- Section: 保养・检查
- Local scope path: 使用干燥空气进行喷气清洁时的润滑频率表；润滑脂要求
- Evidence type: TABLE + TEXT
- Evidence: 保养页分别列出 FVP0600/FVH0600 的时间和动作次数频率、每次 1 mL，并指定含二硫化钼的皂基润滑脂与 BR2+ 推荐品。

## FVP-FVH-Q-0008

**Type: SPEC_LOOKUP**

### Target

- Binding: EXACT_MODEL
- Product: BZL 低压用速度控制阀
- Model / Scope: BZL0101-B specifications and FVP/FVH compatibility

### Question

列出 `BZL0101-B` 的控制方式、G 螺纹尺寸、最高使用压力、耐压、开启压力、
最大流道面积、使用温度、本体推荐紧固力矩，并说明它在本 PDF 中对应的
FVP/FVH 型号。

### Standard Answer

`BZL0101-B` 是回油节流速度控制阀，G 螺纹尺寸为 `G1/8A`；最高使用压力
`7 MPa`，耐压 `10.5 MPa`，开启压力 `0.12 MPa`，最大流道面积
`2.6 mm²`，使用温度 `0-70 °C`，本体推荐紧固力矩 `10 N·m`。本 PDF
将它列为 `FVP0600` 的对应机器，并明确不对应支撑型 `FVH0600`。

### Scoring Standard

- P1 [10]: 正确说明控制方式为回油节流。
- P2 [10]: 正确给出 G1/8A 螺纹。
- P3 [10]: 正确给出最高使用压力 7 MPa。
- P4 [10]: 正确给出耐压 10.5 MPa。
- P5 [10]: 正确给出开启压力 0.12 MPa。
- P6 [10]: 正确给出最大流道面积 2.6 mm²。
- P7 [10]: 正确给出使用温度 0-70 °C。
- P8 [10]: 正确给出本体推荐紧固力矩 10 N·m。
- P9 [10]: 正确说明对应 FVP0600。
- P10 [10]: 正确说明不对应 FVH0600。

### Accepted Variants

- `回油节流` 可写为 `meter-out`。
- `mm²` 可写为 `mm2`。
- `N·m` 可写为 `Nm`。

### Forbidden Errors

- 将控制方式写成进油节流。
- 交换最高使用压力、耐压或开启压力。
- 声称 BZL0101-B 对应 FVH0600。
- 省略任一数值的技术对象或单位。

### Tolerance

- Exact specifications, units, and compatibility are required.

### Source

- PDF: SBR-FVP001-02-C1N.pdf
- Physical page: 16
- Printed page: 15
- Section: 速度控制阀（低压用）model BZL > 规格 / 对应机器型号
- Local scope path: BZL0101-B 规格表；对应机器型号表；FVH 不对应注记
- Evidence type: TABLE + DRAWING
- Evidence: BZL 型号页列出回油节流、G1/8A、压力、流道面积、温度、10 N·m 力矩，并在对应表中仅列 FVP0600 且注明不对应 FVH 支撑型。

## FVP-FVH-Q-0009

**Type: CALCULATION**

### Target

- Binding: EXACT_MODEL
- Product: FVP 推紧型分体式夹钳
- Model / Scope: FVP0600, platen height H = 50 mm

### Question

`FVP0600` 在压板高度 `H = 50 mm`、供给油压 `P = 4.5 MPa` 时，按目录公式计算滑块推力 `F`。给出代入过程、未舍入结果，并按 `ROUND_HALF_UP` 保留两位小数，单位为 `kN`。

### Standard Answer

在 `H = 50 mm` 时使用 `F = 0.39 × P`。代入 `P = 4.5 MPa`：
`F = 0.39 × 4.5 = 1.755 kN`。按 `ROUND_HALF_UP` 保留两位小数，结果为
`1.76 kN`。

### Scoring Standard

- P1 [20]: 正确选择 H=50 mm 对应的系数 0.39。
- P2 [15]: 正确写出并代入 `F = 0.39 × 4.5`。
- P3 [20]: 正确给出未舍入结果 1.755 kN。
- P4 [20]: 正确给出舍入结果 1.76 kN。
- P5 [15]: 正确使用 ROUND_HALF_UP 并保留两位小数。
- P6 [10]: 正确标注最终单位 kN。

### Accepted Variants

- 乘号可写为 `×` 或 `*`。
- 可使用等价的十进制定点计算过程。

### Forbidden Errors

- 使用其他压板高度的系数。
- 将 4.5 MPa 当作 4.5 kN。
- 将 1.755 按截断法写成 1.75。
- 省略最终单位。

### Tolerance

- Final result must be exactly `1.76 kN` under the stated rounding rule.

### Source

- PDF: SBR-FVP001-02-C1N.pdf
- Physical page: 7
- Printed page: 6
- Section: 能力曲线图 > 滑块推力曲线图
- Local scope path: FVP0600 滑块推力计算公式表 > H=50 mm 行
- Evidence type: FORMULA + TABLE
- Evidence: 公式表规定 H=50 mm 时 F=0.39×P，并定义 P 为供给油压 MPa、F 为滑块推力 kN。

## FVP-FVH-Q-0010

**Type: CALCULATION**

### Target

- Binding: EXACT_MODEL
- Product: FVH 支撑型分体式夹钳
- Model / Scope: FVH0600 support force at P = 5 MPa

### Question

`FVH0600` 在供给油压 `P = 5 MPa` 时，按目录公式计算支撑力 `Fk`。给出未舍入结果，并按 `ROUND_HALF_UP` 保留一位小数以与目录表格精度一致，单位为 `kN`。

### Standard Answer

使用公式 `Fk = 0.57 × P`。代入 `P = 5 MPa`：
`Fk = 0.57 × 5 = 2.85 kN`。按 `ROUND_HALF_UP` 保留一位小数，结果为
`2.9 kN`，与目录表格的 5 MPa 行一致。

### Scoring Standard

- P1 [20]: 正确选择公式 Fk=0.57×P。
- P2 [15]: 正确代入 P=5 MPa。
- P3 [20]: 正确给出未舍入结果 2.85 kN。
- P4 [20]: 正确给出舍入结果 2.9 kN。
- P5 [15]: 正确使用 ROUND_HALF_UP 并保留一位小数。
- P6 [10]: 正确标注最终单位 kN。

### Accepted Variants

- `Fk` 可写为 `F_k`。
- 乘号可写为 `×` 或 `*`。

### Forbidden Errors

- 使用 FVP 的压板高度系数。
- 将 2.85 四舍五入为 2.8。
- 把 2.9 kN 写成供给油压。
- 省略最终单位。

### Tolerance

- Final result must be exactly `2.9 kN` under the stated rounding rule.

### Source

- PDF: SBR-FVP001-02-C1N.pdf
- Physical page: 7
- Printed page: 6
- Section: 能力曲线图 > 支撑力曲线图
- Local scope path: FVH0600 支撑力计算公式与供给油压 5 MPa 表格行
- Evidence type: FORMULA + TABLE
- Evidence: 页面规定 Fk=0.57×P，并在供给油压 5 MPa 行列出支撑力 2.9 kN。

## FVP-FVH-Q-0011

**Type: CHART**

### Target

- Binding: EXACT_MODEL
- Product: FVH 支撑型分体式夹钳
- Model / Scope: FVH0600 load/displacement chart at 7 MPa supply pressure

### Question

读取 `FVH0600` 的载荷/变位曲线图：在供给油压 `7 MPa`、反作用载荷为
`3.0 kN` 时，滑块沿后退方向的变位约为多少？同时说明图中的变位定义。

### Standard Answer

曲线在 `3.0 kN` 处对应约 `15 μm`。图中的变位是实际滑块位置（无载荷状态）
与施加反作用载荷后滑块位置之间、沿滑块后退方向的位移差。

### Scoring Standard

- P1 [20]: 正确限定图表条件为 FVH0600、供给油压 7 MPa。
- P2 [35]: 正确读取 3.0 kN 对应约 15 μm。
- P3 [20]: 正确说明基准是无载荷时的实际滑块位置。
- P4 [15]: 正确说明比较对象是施加载荷后的滑块位置。
- P5 [10]: 正确说明变位方向为滑块后退方向。

### Accepted Variants

- `15 μm` 可写为 `约 0.015 mm`。
- `反作用载荷` 可写为 `加工推力的反作用力`。

### Forbidden Errors

- 用公式推导代替读取该图表。
- 把横轴载荷写成供给油压。
- 把 15 μm 写成 15 mm。
- 将变位解释为 8 mm 滑块行程。

### Tolerance

- CHART read tolerance: `15 μm ± 1 μm` at 3.0 kN.

### Source

- PDF: SBR-FVP001-02-C1N.pdf
- Physical page: 7
- Printed page: 6
- Section: 能力曲线图 > 载荷/变位曲线图
- Local scope path: FVH0600、供给油压 7 MPa 的载荷/变位曲线；右侧变位定义图
- Evidence type: CHART + DRAWING + TEXT
- Evidence: 图表横轴为载荷 kN、纵轴为变位 μm，直线在 3 kN 处约为 15 μm；定义图标示无载荷位置与加反作用载荷后位置的后退方向差值。

## FVP-FVH-Q-0012

**Type: PROCEDURE**

### Target

- Binding: MODEL_FAMILY
- Product: FVP/FVH 油压复动式分体式夹钳
- Model / Scope: FVP0600 pusher and FVH0600 support operating sequence

### Question

分别说明 `FVP0600` 和 `FVH0600` 从释放到夹紧/支撑、再返回释放状态时的动作顺序，并指出两者在保持工件方面的功能差异。

### Standard Answer

- FVP0600：释放侧供压时滑块退回；切换为夹紧侧供压后，滑块追随工件位置前进，接触后持续施加推力；再次向释放侧供压时滑块退回。
- FVH0600：释放侧供压时滑块后退；切换为夹紧侧供压后滑块前进，接触工件后停止；随后内置楔型机构动作并锁紧滑块，使其在接触位置承受载荷；切换回释放侧供压后解除楔锁并使滑块后退。释放过程中内置弹簧可能使滑块瞬时前移并对工件产生约 `50 N` 推力，这不是异常。
- 功能差异：FVP 主动持续推紧，FVH 在接触位置锁紧并承受反作用载荷。

### Scoring Standard

- P1 [15]: 正确说明 FVP 释放侧供压使滑块退回。
- P2 [15]: 正确说明 FVP 夹紧侧供压使滑块前进并持续推紧。
- P3 [15]: 正确说明 FVH 释放侧供压使滑块后退。
- P4 [15]: 正确说明 FVH 夹紧侧供压使滑块前进，接触工件后停止。
- P5 [15]: 正确说明 FVH 夹紧侧供压后楔型机构锁紧。
- P6 [15]: 正确说明切回释放侧供压后解除楔锁。
- P7 [10]: 正确区分 FVP 持续推力与 FVH 锁紧支撑。

### Accepted Variants

- `楔型机构` 可写为 `wedge mechanism`。
- `前进`、`后退` 可用与页面箭头一致的等价方向描述。

### Forbidden Errors

- 交换 FVP 和 FVH 的持续推紧/锁紧支撑功能。
- 声称 FVH 靠持续液压推进压板追随工件。
- 声称 FVP 接触后由楔型机构锁死。
- 省略释放状态或压力侧切换。

### Tolerance

- Sequence, pressure-side roles, and family function boundary must all be correct.

### Source

- PDF: SBR-FVP001-02-C1N.pdf
- Physical page: 4-5
- Printed page: 3-4
- Section: 动作说明
- Local scope path: FVP 推紧型动作状态图；FVH 支撑型释放、压板移动、锁紧状态图
- Evidence type: STATE_DIAGRAM + DRAWING + TEXT
- Evidence: 两页动作图分别显示 FVP 的释放/夹紧供压方向和持续推力，以及 FVH 的释放后退、夹紧前进、接触后楔锁保持和释放过程；注意事项说明释放时约 50 N 的瞬时弹簧推力。

## FVP-FVH-Q-0013

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: FVP/FVH 油压复动式分体式夹钳
- Model / Scope: hydraulic, opposed-use, and air-cleaning design controls

### Question

设计 FVP/FVH 回路及对向使用方案时，列出必须遵守的五项控制：夹紧/释放供压禁忌、FVP/FVH 对向顺序、两个 FVP 对向的速度要求、FVH 两侧压力要求，以及喷气清洁供气要求。

### Standard Answer

1. 严禁同时向夹紧侧和释放侧供给油压。
2. FVP 与 FVH 对向使用时，必须先让 FVH 锁紧，再调整或动作 FVP。
3. 两个 FVP 对向使用时，应尽量调到同时接触工件，避免单侧压力使工件变形。
4. FVH 的夹紧侧与释放侧应供给相同压力；释放侧压力较低时可能无法释放。
5. 喷气清洁供气必须持续保持，推荐空气压力为 `0.2-0.3 MPa`；断气会使异物侵入并导致动作不良。

### Scoring Standard

- P1 [20]: 正确说明不得同时向夹紧侧和释放侧供压。
- P2 [20]: 正确说明 FVP/FVH 对向时 FVH 必须先锁紧。
- P3 [15]: 正确说明两个 FVP 应同步接触工件。
- P4 [10]: 正确说明单侧先接触可能使工件变形。
- P5 [15]: 正确说明 FVH 夹紧侧与释放侧应使用相同压力。
- P6 [10]: 正确说明释放侧压力较低时 FVH 可能无法释放。
- P7 [5]: 正确说明喷气清洁供气必须持续保持。
- P8 [3]: 正确给出推荐空气压力 0.2-0.3 MPa。
- P9 [2]: 正确说明断气会使异物侵入并导致动作不良。

### Accepted Variants

- `同时接触` 可写为 `同步接触`。
- `0.2-0.3 MPa` 可写为 `0.2 至 0.3 MPa`。

### Forbidden Errors

- 允许夹紧侧和释放侧同时供压。
- 让 FVP 在 FVH 锁紧前推紧工件。
- 建议两个 FVP 刻意错开接触时间。
- 建议 FVH 释放侧使用更低压力。
- 将喷气清洁描述为间歇、无需保持或超出规定压力范围。

### Tolerance

- All five controls and the 0.2-0.3 MPa range are required.

### Source

- PDF: SBR-FVP001-02-C1N.pdf
- Physical page: 12-13
- Printed page: 11-12
- Section: 设计方面的注意事项 / 参考油压回路
- Local scope path: 回路设计、喷气清洁、FVH 等压要求；FVP/FVP 与 FVP/FVH 对向参考回路
- Evidence type: TEXT + STATE_DIAGRAM
- Evidence: 设计注意事项列出同时供压禁令、对向顺序、同步接触、FVH 等压和持续 0.2-0.3 MPa 喷气；参考回路图确认对应顺序关系。

## FVP-FVH-Q-0014

**Type: PROCEDURE**

### Target

- Binding: PRODUCT_SERIES
- Product: FVP/FVH 油压复动式分体式夹钳
- Model / Scope: FVP0600/FVH0600 action-speed adjustment

### Question

说明 FVP0600/FVH0600 动作速度的安全调整流程、目标全行程时间，以及调整过程中必须检查的压力、空气和温度条件。

### Standard Answer

安装流量调节阀，从低速侧的小流量状态开始，逐渐增加流量，直到滑块全行程时间达到 `0.5-1 s`。不得从高速/大流量开始，否则可能产生异常脉动高压或过载并损坏设备。调整时必须确认没有异常高压；若回路混入大量空气，速度调整可能失效，应先排气；油温升高会降低油液黏度并加快动作，因此应在实际使用温度下完成最终调整。FVH 过慢还会延长保持力建立的时间延迟。

### Scoring Standard

- P1 [10]: 正确说明使用流量调节阀调整速度。
- P2 [10]: 正确说明从低速/小流量状态开始。
- P3 [10]: 正确说明逐渐增加流量至规定速度。
- P4 [20]: 正确给出全行程目标 0.5-1 s。
- P5 [15]: 正确说明从高速起调可能产生异常脉动高压或过载损坏。
- P6 [10]: 正确说明调整时检查异常高压。
- P7 [10]: 正确说明大量空气会使速度调整失效并应排气。
- P8 [10]: 正确说明应在实际使用温度下调整及油温影响。
- P9 [5]: 正确说明 FVH 过慢会延长保持力建立。

### Accepted Variants

- `0.5-1 s` 可写为 `0.5 至 1 秒`。
- `流量调节阀` 可写为 `flow-control valve`。

### Forbidden Errors

- 从高速或最大流量开始调整。
- 使用 0.5-1 s 以外的目标范围。
- 忽略异常高压、空气或实际油温。
- 声称极慢速度能缩短 FVH 保持力建立时间。

### Tolerance

- Exact 0.5-1 s target and low-flow-to-high-flow adjustment direction are required.

### Source

- PDF: SBR-FVP001-02-C1N.pdf
- Physical page: 14
- Printed page: 13
- Section: 安装施工方面的注意事项 > 动作速度的调整
- Local scope path: FVP/FVH 滑块全行程速度调整、异常高压、空气和实际温度条件
- Evidence type: TEXT
- Evidence: 安装页规定 0.5-1 s、从低速小流量渐进调整、检查异常高压，并说明空气、油温及 FVH 保持力延迟的影响。

## FVP-FVH-Q-0015

**Type: PROCEDURE**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK 油压系列通用事项
- Model / Scope: SBR-FVP001-02-C1N.pdf :: physical page 18 / printed page 17, hydraulic-circuit air bleeding after piping or tank-empty air entry

### Question

按本 PDF 的油压系列通用事项，说明配管完成后或泵油箱放空导致空气进入时的完整排气步骤，包括压力上限、接头操作、排油动作、复紧和推荐排气位置。

### Standard Answer

1. 将油压回路供油压力调整到 `2 MPa 以下`。
2. 将离分体式夹钳最近的配管接头螺母旋松一圈。
3. 左右摇动配管，使连接部位松动并排出混有空气的液压油。
4. 空气排净后拧紧管接头螺母。
5. 在回路最上端和最末端附近排气效果更好，并应在回路最上端附近设置排气阀。

### Scoring Standard

- P1 [20]: 正确给出供油压力不超过 2 MPa。
- P2 [20]: 正确说明旋松最近接头螺母一圈。
- P3 [20]: 正确说明左右摇动配管并排出含气液压油。
- P4 [20]: 正确说明排净后复紧接头螺母。
- P5 [10]: 正确说明在回路最上端和最末端附近排气效果更好。
- P6 [10]: 正确说明应在回路最上端附近设置排气阀。

### Accepted Variants

- `2 MPa 以下` 可写为 `≤2 MPa`。
- `含气液压油` 可写为 `aerated hydraulic oil`。

### Forbidden Errors

- 在高于 2 MPa 的压力下排气。
- 旋松非最近接头或完全拆下接头。
- 不复紧接头即恢复运行。

### Tolerance

- Exact pressure limit, one-turn loosening, ordered steps, and page-bounded scope are required.

### Source

- PDF: SBR-FVP001-02-C1N.pdf
- Physical page: 18
- Printed page: 17
- Section: 安装施工方面的注意事项（油压系列通用事项）> 排净油压回路内的空气
- Local scope path: 本 PDF 第17印刷页的五步排气流程
- Evidence type: TEXT + DRAWING
- Evidence: 该页依次规定 2 MPa 以下、最近接头旋松一圈、摇管排出含气油、排净后复紧，以及最上端/最末端位置和排气阀建议。

## FVP-FVH-Q-0016

**Type: CAUTION**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK 油压系列通用事项
- Model / Scope: SBR-FVP001-02-C1N.pdf :: physical page 20 / printed page 19, operation and maintenance safety

### Question

按本 PDF 第 19 印刷页的通用安全要求，说明谁可以操作/维护液压装置，以及检查、拆卸、重新启动、运行中接触和产品改造分别必须遵守的控制。

### Standard Answer

仅应由具备丰富知识和专业经验的人员操作、维护液压/气动装置。检查或拆卸前，应对被驱动物体采取防坠落和防误动作措施；拆卸时切断压力源和电源，确认油压/气压回路为零压，并等待刚停机设备完全冷却。重新启动前检查螺栓等连接部位是否异常。运行中严禁接触工件、配件和分体式夹钳。不得擅自拆解、改造或修理产品；大修应委托厂家。

### Scoring Standard

- P1 [12]: 正确限定由有知识和专业经验的人员操作维护。
- P2 [12]: 正确说明对被驱动物体采取防坠落措施。
- P3 [12]: 正确说明采取防止误动作的措施。
- P4 [10]: 正确说明拆卸前切断压力源。
- P5 [10]: 正确说明拆卸前切断电源。
- P6 [10]: 正确说明确认油压/气压回路为零压。
- P7 [8]: 正确说明等待设备完全冷却。
- P8 [8]: 正确说明重新启动前检查螺栓等连接部位。
- P9 [8]: 正确说明运行中不得接触工件、配件和夹钳。
- P10 [5]: 正确说明不得擅自拆解、改造或修理。
- P11 [5]: 正确说明大修应委托厂家。

### Accepted Variants

- `零压` 可写为 `压力为零`。
- `防误动作` 可写为 `防止意外运动`。

### Forbidden Errors

- 允许无专业经验人员操作或维护。
- 只停泵而不切断电源或确认零压。
- 在设备仍热时拆卸。
- 允许运行中接触工件或夹钳。
- 允许用户自行改造或大修。

### Tolerance

- All safety controls are mandatory; page-bounded DOCUMENT_COMMON scope must be preserved.

### Source

- PDF: SBR-FVP001-02-C1N.pdf
- Physical page: 20
- Printed page: 19
- Section: 操作方面的注意事项 / 保养・检查
- Local scope path: 本 PDF 第19印刷页的人员资质、隔离、零压、冷却、重启、接触和改造要求
- Evidence type: TEXT + DRAWING
- Evidence: 操作与保养页明确规定人员资质、安全隔离、零压和冷却确认、重启检查、运行中禁触及禁止擅自解体改造。

## FVP-FVH-Q-0017

**Type: CAUTION**

### Target

- Binding: EXACT_MODEL
- Product: BZL 低压用速度控制阀
- Model / Scope: BZL0101-B installation, reuse, circuit design, and air bleeding

### Question

安装和使用 `BZL0101-B` 时，说明本体紧固、跨夹钳再使用、回路设计和排气压力的四项注意事项及其主要风险。

### Standard Answer

1. 必须按推荐本体紧固力矩 `10 N·m` 安装；端面为金属密封，力矩不足会导致无法调节流量。
2. 已在一个夹钳上使用过的 BZL 不得转装到另一夹钳；不同夹钳 G 螺纹底面深度差异可能造成金属密封不严并使流量无法调节。
3. 回路必须按夹紧器速度控制回路注意事项正确设计；错误设计可能导致误动作或损坏。
4. 排气必须在低压下进行，高压排气危险，压力参考回路内机器的最低动作压力。

### Scoring Standard

- P1 [10]: 正确给出本体推荐紧固力矩 10 N·m。
- P2 [8]: 正确说明端面采用金属密封。
- P3 [7]: 正确说明力矩不足会导致无法调节流量。
- P4 [10]: 正确禁止将已使用的 BZL 转装到另一夹钳。
- P5 [10]: 正确说明不同夹钳 G 螺纹底面深度可能不同。
- P6 [5]: 正确说明跨夹钳转装可能导致密封不严、流量无法调节。
- P7 [10]: 正确说明必须按夹紧器速度控制回路规则设计。
- P8 [5]: 正确说明错误回路设计可能导致误动作。
- P9 [5]: 正确说明错误回路设计可能导致设备损坏。
- P10 [10]: 正确说明排气必须在低压下进行。
- P11 [10]: 正确说明高压排气危险。
- P12 [10]: 正确说明排气压力参考回路内机器的最低动作压力。

### Accepted Variants

- `跨夹钳再使用` 可写为 `转装到其他夹钳`。
- `10 N·m` 可写为 `10 Nm`。

### Forbidden Errors

- 使用低于推荐值的力矩且声称不影响密封。
- 允许将已使用 BZL 转装到其他夹钳。
- 忽略速度控制回路规则。
- 在高压下排气。

### Tolerance

- Exact 10 N·m torque and all four cautions are required.

### Source

- PDF: SBR-FVP001-02-C1N.pdf
- Physical page: 16-17
- Printed page: 15-16
- Section: 速度控制阀（低压用）model BZL > 规格注意事项 / 能力曲线图注意事项
- Local scope path: BZL0101-B 本体推荐力矩、金属密封、禁止转装、回路设计和低压排气
- Evidence type: TEXT + TABLE
- Evidence: BZL 规格页规定 10 N·m、金属密封及禁止跨夹钳再使用；下一页规定正确回路设计和低压排气。

## FVP-FVH-Q-0018

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: FVP/FVH 油压复动式分体式夹钳
- Model / Scope: platen height, eccentricity, load positioning, and mounting-bolt selection

### Question

设计 FVP/FVH 压板时，说明压板高度和偏心量的使用边界、偏心量超过 `12 mm` 时的定位建议，以及正/负压板高度和大偏移量分别应如何选择 6 个安装螺栓孔。

### Standard Answer

必须在最大压板高度和容许偏心量规格以内使用；超限可能损坏机器，而且推力/支撑能力会随压板高度和偏心量变化。偏心量大于 `12 mm` 时，建议按滑块宽度定位，滑块宽度为 `25g7`。安装部共有 6 个螺栓孔：正压板高度使用前方 4 孔，负压板高度使用后方 4 孔；偏移量较大时推荐 6 孔全部使用。

### Scoring Standard

- P1 [20]: 正确说明必须在最大压板高度和容许偏心量内使用。
- P2 [10]: 正确说明超限可能损坏机器。
- P3 [5]: 正确说明能力随压板高度和偏心量变化。
- P4 [20]: 正确说明偏心量大于 12 mm 时按 25g7 滑块宽度定位。
- P5 [15]: 正确说明安装部共有 6 个螺栓孔。
- P6 [10]: 正确说明正高度使用前方 4 孔。
- P7 [10]: 正确说明负高度使用后方 4 孔。
- P8 [10]: 正确说明大偏移量推荐全部 6 孔。

### Accepted Variants

- `正/负压板高度` 可写为 `(+)/(−) 压板高度`。
- `25g7` 可附带图示公差，但不得改变基本尺寸或配合等级。

### Forbidden Errors

- 允许超过最大高度或容许偏心量使用。
- 把 12 mm 写成最大容许偏心量。
- 交换正高度前 4 孔与负高度后 4 孔。
- 大偏移量时减少到 2 个或 4 个孔。

### Tolerance

- Exact 12 mm trigger, 25g7 positioning width, and bolt-hole rules are required.

### Source

- PDF: SBR-FVP001-02-C1N.pdf
- Physical page: 12
- Printed page: 11
- Section: 设计方面的注意事项 > 压板高度、容许偏心量、螺栓位置
- Local scope path: 压板载荷位置与 25g7 滑块宽度图；正/负高度安装孔示意
- Evidence type: TEXT + TABLE + DRAWING
- Evidence: 设计页规定高度/偏心量边界、偏心量大于 12 mm 时按 25g7 定位，并给出正高度前 4 孔、负高度后 4 孔及大偏移量全部 6 孔规则。

## FVP-FVH-Q-0019

**Type: CHART**

### Target

- Binding: EXACT_MODEL
- Product: BZL 低压用速度控制阀
- Model / Scope: BZL0101-B adjusted flow-distribution chart for ISO-VG32 hydraulic oil at 25-35 °C

### Question

读取 `BZL0101-B` 调整后的流量分布图。在液压油为 `ISO-VG32`、油温
`25-35 °C`、调节阀从关闭位置打开 `4` 圈时，压力损失为 `1 MPa`、
`3 MPa`、`5 MPa` 三条曲线对应的流量各约为多少？说明曲线随压力损失增大的关系。

### Standard Answer

在打开 4 圈时，曲线读数约为：压力损失 `1 MPa` 时 `3.2 L/min`，
`3 MPa` 时 `4.8 L/min`，`5 MPa` 时 `7.0 L/min`。在相同开启圈数下，
压力损失越大，流量越大。

### Scoring Standard

- P1 [15]: 正确限定 ISO-VG32、25-35 °C 和打开 4 圈。
- P2 [25]: 正确读取 1 MPa 曲线约 3.2 L/min。
- P3 [25]: 正确读取 3 MPa 曲线约 4.8 L/min。
- P4 [25]: 正确读取 5 MPa 曲线约 7.0 L/min。
- P5 [10]: 正确说明相同开启圈数下压力损失越大、流量越大。

### Accepted Variants

- `L/min` 可写为 `L/minute` 或 `升/分钟`。
- 可按图表分辨率报告一位小数或相近的近似值。

### Forbidden Errors

- 用计算公式替代真实图表读数。
- 交换 1、3、5 MPa 三条曲线。
- 将横轴 4 解释为 4 MPa。
- 省略油液、温度或开启圈数条件。

### Tolerance

- CHART read tolerance: each flow may differ by `±0.5 L/min` from 3.2, 4.8, and 7.0 L/min respectively.

### Source

- PDF: SBR-FVP001-02-C1N.pdf
- Physical page: 17
- Printed page: 16
- Section: 流量特性图 > 调整后的流量分布
- Local scope path: BZL0101-B 回油节流，ISO-VG32 25-35 °C，打开 4 圈，压力损失 1/3/5 MPa 曲线
- Evidence type: CHART + TEXT
- Evidence: 调整后流量图以开启圈数为横轴、L/min 为纵轴，绿色/红色/蓝色曲线分别标示 1/3/5 MPa；4 圈端点约为 3.2/4.8/7.0 L/min。

## FVP-FVH-Q-0020

**Type: CAUTION**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK 油压系列通用事项
- Model / Scope: SBR-FVP001-02-C1N.pdf :: physical page 19 / printed page 18, double-acting clamp speed-control circuits applicable to FVP/FVH

### Question

按本 PDF 第 18 印刷页的通用回路要求，为 FVP/FVH 复动夹紧器设计速度控制时，
夹紧侧和释放侧应采用什么节流方式？为什么不推荐进油节流？复动与单动夹紧器
并用时回路应如何处理，并需防范哪些背压和内压上升风险？

### Standard Answer

FVP/FVH 属于复动夹紧器，夹紧侧和释放侧都应采用回油节流。进油节流容易受
回路内混入空气的影响，难以稳定控制速度。复动与单动夹紧器并用时，原则上
不要在同一回路中进行速度控制，应将控制回路各自分开。即使分开，共通油箱
管路存在背压时，仍可能出现复动夹紧器动作后带动单动夹紧器动作。回油节流
过程中还可能因供油量造成回路内压上升，超过顺序阀或动作确认压力开关的设定
压力后使系统无法动作；应通过流量调节阀预先减少供油量等措施抑制内压上升。

### Scoring Standard

- P1 [20]: 正确说明夹紧侧采用回油节流。
- P2 [20]: 正确说明释放侧也采用回油节流。
- P3 [15]: 正确说明进油节流易受回路内空气影响而难以稳定控制速度。
- P4 [20]: 正确说明复动与单动夹紧器的速度控制回路原则上应分开。
- P5 [15]: 正确说明共通油箱管路背压可能造成意外联动。
- P6 [5]: 正确指出回油节流可能造成回路内压上升并影响压力控制元件。
- P7 [5]: 正确提出预先减少供油量等流量控制措施。

### Accepted Variants

- `回油节流` 可写为 `meter-out`；`进油节流` 可写为 `meter-in`。
- `各自分开` 可写为 `使用独立控制回路`。

### Forbidden Errors

- 将夹紧侧或释放侧设置为进油节流。
- 声称复动与单动夹紧器在同一速度控制回路中不会相互影响。
- 忽略共通回油背压导致的意外联动风险。
- 把供油流量控制写成增加供油量以提高内压。

### Tolerance

- N/A

### Source

- PDF: SBR-FVP001-02-C1N.pdf
- Physical page: 19
- Printed page: 18
- Section: 油压夹紧器的速度控制回路及注意事项
- Local scope path: 本 PDF 第18印刷页 > 复动夹紧器速度控制回路；复动与单动夹紧器并用注意事项 1-2
- Evidence type: STATE_DIAGRAM + TEXT
- Evidence: 通用页要求复动夹紧器两侧均采用回油节流，图示进油节流受空气影响，并说明混用系统的回路分离、背压联动、内压上升和供油量调整措施。

## FVP-FVH-Q-0021

**Type: CAUTION**

### Target

- Binding: MODEL_FAMILY
- Product: FVP/FVH 油压复动式分体式夹钳
- Model / Scope: FVP0600/FVH0600 maintenance, excess-grease, and contamination controls

### Question

对 FVP0600/FVH0600 进行保养时，FVH 给油过多会产生什么后果？为什么要定期
清洁夹钳周围环境，污垢附着状态下继续使用会带来哪些风险？

### Standard Answer

FVH 给油过多会使支撑力下降，填充过多的润滑脂还可能在动作过程中从夹钳本体
和滑块之间的间隙溢出。应定期清洁分体式夹钳周围环境；本产品不是完全密封
结构，切粉和冷却液可能从零件间隙侵入。污垢附着状态下继续使用可能造成定位
精度不良、动作不良和漏油。

### Scoring Standard

- P1 [20]: 正确说明 FVH 给油过多会使支撑力下降。
- P2 [10]: 正确说明过量润滑脂可能从本体与滑块间隙溢出。
- P3 [15]: 正确说明应定期清洁夹钳周围环境。
- P4 [10]: 正确说明产品不是完全密封结构且异物可能从间隙侵入。
- P5 [15]: 正确说明污垢会造成定位精度不良。
- P6 [15]: 正确说明污垢会造成动作不良。
- P7 [15]: 正确说明污垢会造成漏油。

### Accepted Variants

- `支撑力下降` 可写为 `holding/support force decreases`。
- `切粉` 可写为 `切屑`。

### Forbidden Errors

- 声称增加润滑脂会提高 FVH 支撑力。
- 声称本产品为完全密封、无需清洁。
- 忽略污垢导致的定位、动作或漏油风险。

### Tolerance

- N/A

### Source

- PDF: SBR-FVP001-02-C1N.pdf
- Physical page: 15
- Printed page: 14
- Section: 保养・检查
- Local scope path: 给油量过多的 FVH 后果；定期清洁及非完全密封结构注意事项
- Evidence type: TEXT
- Evidence: 保养页说明过量给油会降低 FVH 支撑力并可能溢脂；同页要求定期清洁，并列出异物侵入导致定位精度不良、动作不良和漏油的后果。
