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

- Total: 8
- FACT: 1
- SPEC_LOOKUP: 2
- TABLE: 4
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
- P4 [10]: 正确说明本体使用 6 根强度等级 12.9 的内六角螺栓。
- P5 [10]: 正确给出法兰上部安装使用 M6。
- P6 [10]: 正确给出法兰上部安装紧固力矩 10 N·m。
- P7 [10]: 正确给出法兰下部安装使用 M8。
- P8 [10]: 正确给出法兰下部安装紧固力矩 25 N·m。
- P9 [20]: 正确说明压板应顶住限位块并无间隙安装。

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
