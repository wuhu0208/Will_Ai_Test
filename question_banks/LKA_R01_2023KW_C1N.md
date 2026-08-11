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
- Product printed pages: 749-784
- Included common-reference printed pages: 1729-1730
- Included control-valve printed pages: 1257-1262, 1265-1272
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
| LKA-SI-001 | 1 / 749 | Product family introduction > LKA identity and operating principle | TEXT + DRAWING | HIGH | LKA position in the link-clamp family, release/clamp motion, and representative applications | LKA product identity and structural features are represented by `LKA-Q-0002`; the release/clamp motion is a state sequence reserved for WP3 `PROCEDURE` |
| LKA-SI-002 | 2 / 750 | Product-family examples | TEXT + DRAWING | LOW | Contextual examples of other link-clamp models | Context only; exclude facts not bound to LKA |
| LKA-SI-003 | 3-4 / 751-752 | Product lineup and accessory overview | TABLE + DRAWING | MEDIUM | Product-type boundaries, variant selection, and accessory relationships | No separate question: broader product-comparison context is not an LKA operating rule; LKA-specific selection is covered by `LKA-Q-0002`, `LKA-Q-0005`, and `LKA-Q-0006` |
| LKA-SI-004 | 5 / 753 | Table of contents | TEXT | NON-TEST | Navigation map for LKA product, common cautions, valves, and manifold blocks | Navigation only |
| LKA-SI-005 | 6 / 754 | LKA features and cross-section | TEXT + DRAWING | HIGH | Compact body, integrated fulcrum, coolant protection, eccentric-load allowance, arm directions, and direct speed-control mounting | Compactness, fulcrum, and sealing facts in `LKA-Q-0002`; eccentricity and operating cautions remain WP3 |
| LKA-SI-006 | 7 / 755 | Model designation | TABLE + DRAWING | HIGH | Six-field order, legal body/piping/arm/confirmation/option values, and H-option size restriction | `LKA-Q-0001`, `LKA-Q-0005`, `LKA-Q-0006`; grammar audit remains WP4 |
| LKA-SI-007 | 8 / 756 | Specifications | TABLE + FORMULA | HIGH | Clamp area, clamp-force formula, capacities, strokes, pressure, temperature, fluid, and weight for eight body sizes and confirmation variants | Representative lookup and common limits in `LKA-Q-0003`, `LKA-Q-0004`; calculations remain WP3 |
| LKA-SI-008 | 9-12 / 757-760 | Clamp-force capability curves | CHART + FORMULA | HIGH | Pressure/arm-length/clamp-force relationships with and without action confirmation | WP3 `CHART` / `CALCULATION` |
| LKA-SI-009 | 13-16 / 761-764 | Allowable eccentricity curves | CHART + DRAWING | HIGH | Standard versus high-strength-link eccentricity limits and consequences of exceeding them | WP3 `CHART` / `CAUTION` |
| LKA-SI-010 | 17-18 / 765-766 | Standard model dimensions and dimension table | DRAWING + TABLE | HIGH | External, mounting, port, arm, and interference dimensions | Representative LKA0480 stroke/mounting/port lookup in `LKA-Q-0012`; installation cautions remain WP3 |
| LKA-SI-011 | 19-20 / 767-768 | Probe dual-rod confirmation type `D` | DRAWING + TABLE | HIGH | Model-specific construction, confirmation interface, and dimensions | `D` semantics in `LKA-Q-0005`; body-size dimension grid is retained as lookup evidence but not repeated as numeric-swap questions; installation remains WP3 |
| LKA-SI-012 | 21-22 / 769-770 | Air-sensor manifold confirmation type `M` | DRAWING + TABLE | HIGH | Model-specific air interface, construction, and dimensions | `M` semantics in `LKA-Q-0005`; dimension grid is retained without repetitive body-size questions; air connection procedure remains WP3 |
| LKA-SI-013 | 23-24 / 771-772 | Air-sensor external-piping types `N/NC/NL/NR` | DRAWING + TABLE | HIGH | Four port phases, external piping, and dimensions | Four-phase model semantics in `LKA-Q-0005`; dimension grid is retained without repetitive phase questions; air connection procedure remains WP3 |
| LKA-SI-014 | 25-26 / 773-774 | Quick-change arm option `A` | DRAWING + TABLE + TEXT | HIGH | Quick-change construction, dimensions, installation, and fastening | Option/attachment facts in `LKA-Q-0013` and `LKA-Q-0009`; installation remains WP3 |
| LKA-SI-015 | 18, 20, 22, 24, 26 / 766, 768, 770, 772, 774 | Repeated option notes and model/dimension tables | DRAWING + TABLE + TEXT | HIGH | `H`/`K` option construction, A-type differences, and confirmation-variant dimension grids | `H`/`K` model boundaries in `LKA-Q-0006`; A-type differences in `LKA-Q-0013`; repeated dimension grids are retained as source rather than converted into numeric-swap questions |
| LKA-SI-016 | 27 / 775 | Air-sensor connection and confirmation | TEXT + DRAWING + TABLE | HIGH | Differential-pressure confirmation, sensor connection limit, exhaust protection, arm alignment, and O-ring grease controls | WP3 `PROCEDURE` / `CAUTION` |
| LKA-SI-017 | 28 / 776 | Air-sensor circuit and process charts | STATE_DIAGRAM + CHART | HIGH | Clamp/release sensing sequence, pressure/stroke states, and sensor-output conditions | WP3 `PROCEDURE` / `CHART` |
| LKA-SI-018 | 29 / 777 | Clamp-arm design | DRAWING + FORMULA + CHART | HIGH | Arm dimensions, clamp-point distance, force-curve selection, and geometric limits | WP3 `CALCULATION` / `PROCEDURE` / `CAUTION` |
| LKA-SI-019 | 30 / 778 | Blank arm and fastening kit | DRAWING + TABLE + TEXT | MEDIUM | Blank-arm selection, machining, fastener kit, and compatibility constraints | Representative LKA0480 selection in `LKA-Q-0009`; machining and installation remain WP3 |
| LKA-SI-020 | 31 / 779 | LKA-specific design and installation cautions | TEXT + DRAWING | HIGH | Hydraulic circuit, simultaneous pressure prohibition, axial loading, eccentricity, contamination, parallel clamping, pins, mounting, and sensor references | WP3 `CAUTION` / `PROCEDURE` |
| LKA-SI-021 | 32 / 780 | LKA-specific operation and adjustment | TEXT + DRAWING + TABLE | HIGH | Quick-change fastening, action time, air bleeding, speed adjustment, fulcrum adjustment, and probe installation | WP3 `PROCEDURE` / `CAUTION` |
| LKA-SI-022 | 33 / 781 | Common hydraulic installation cautions | TEXT + DRAWING | HIGH | Oil selection, cleaning, sealing tape, air bleeding, and fastener checks | WP3 `PROCEDURE` / `CAUTION`; bind as page-bounded `DOCUMENT_COMMON` |
| LKA-SI-023 | 34 / 782 | Common hydraulic speed-control circuits | STATE_DIAGRAM + TEXT | HIGH | Single/double-acting circuit differences, meter-out/meter-in behavior, air instability, circuit separation, and back pressure | WP3 `PROCEDURE` / `CAUTION`; bind as page-bounded `DOCUMENT_COMMON` |
| LKA-SI-024 | 35 / 783 | Common operation and maintenance cautions | TEXT | HIGH | Qualified staff, energy isolation, restart checks, moving-part avoidance, modification prohibition, inspection, storage, and overhaul | WP3 `CAUTION` / `PROCEDURE`; bind as page-bounded `DOCUMENT_COMMON` |
| LKA-SI-025 | 36 / 784 | Warranty | TEXT | LOW | Warranty term, coverage, and exclusions | Exclude from core capability bank; commercial policy |
| LKA-SI-026 | 37-38 / 1729-1730 | Common notation references | TABLE | MEDIUM | Surface-roughness and O-ring old/new notation mappings | Surface-roughness mapping in `LKA-Q-0010`; O-ring grammar/mapping in `LKA-Q-0014`; both page-bounded `DOCUMENT_COMMON` |
| LKA-SI-027 | 39 / 1257 | Control-valve family introduction | TEXT + DRAWING | MEDIUM | BZL/BZT/BZX/JZG/BZS family purpose and direct-mount relationship | Family roles covered by `LKA-Q-0011`; ancillary scope |
| LKA-SI-028 | 40 / 1258 | Control-valve type comparison | TABLE + DRAWING | MEDIUM | Pressure classes and functions of speed, exhaust, plug, and sequence-valve types | `LKA-Q-0011` |
| LKA-SI-029 | 41-44 / 1259-1262 | BZL/BZT speed-control valves | TABLE + CHART + DRAWING | MEDIUM | Model grammar, specifications, compatible threads, flow curves, dimensions, and circuit cautions | Representative BZL lookup in `LKA-Q-0007`; curves and cautions remain WP3 |
| LKA-SI-030 | 45-48 / 1265-1268 | BZX exhaust valves and JZG plugs | TABLE + DRAWING + TEXT | MEDIUM | Model grammar, pressure/specification limits, compatibility, dimensions, and exhaust safety | Family function/pressure in `LKA-Q-0011`; LKA size mapping repeats the same G-thread size groups already tested by `LKA-Q-0008` and is not duplicated; exhaust/install safety remains WP3 |
| LKA-SI-031 | 49-52 / 1269-1272 | BZS direct-mounted sequence valves | TABLE + CHART + DRAWING + TEXT | HIGH | Model grammar, operating/setting pressure, compatibility, dimensions, pressure-flow behavior, contamination, air, and adjustment cautions | LKA compatibility in `LKA-Q-0008`; representative specifications in `LKA-Q-0016`; flow behavior and operation/cautions remain WP3 |
| LKA-SI-032 | 53-56 / 1697-1700 | Manifold blocks | TABLE + DRAWING + TEXT | MEDIUM | WHZ/LZY/LZ/TMZ/DZ families, applicable models, dimensions, machining, height adjustment, and bolt cautions | Representative LKA plate-seat selection in `LKA-Q-0015`; other product families are contextual; machining/bolt cautions remain WP3 |
| LKA-SI-033 | 57-58 / 947-948 | Sales addresses and network | TEXT + DRAWING | NON-TEST | Contact details, sales geography, and certification marks | Exclude; not durable LKA technical knowledge |

## 3. Question Statistics

- Total: 16
- FACT: 2
- SPEC_LOOKUP: 3
- TABLE: 7
- MODEL: 4

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

## LKA-Q-0002

**Type: FACT**

### Target

- Binding: PRODUCT_SERIES
- Product: LKA 油压杠杆式夹紧器
- Model / Scope: LKA 系列紧凑结构、支点强度和冷却液防护特征

### Question

LKA 系列通过哪些主体、油路、杠杆支点和防尘设计实现夹具紧凑化、高强度
以及冷却液环境下的密封耐久性？

### Standard Answer

LKA 的法兰安装面下部相对本公司传统产品最多缩小 40%，有助于夹具紧凑化
和轻量化。主体紧凑后，内部油路可布置到夹紧器下方，从而减少夹具设计中的
干涉。杠杆支点与锻造本体为一体结构，体积更紧凑；独特锻造工艺同时提高了
支点强度。专用防尘结构即使面对高压冷却液也具有较高密封性能；高性能耐腐蚀
防尘材料在长期使用水溶性冷却液时也不会降低密封性能。

### Scoring Standard

- P1 [15]: 正确说明法兰安装面下部相对传统产品最多缩小 40%。
- P2 [15]: 正确说明该缩小有助于夹具紧凑化和轻量化。
- P3 [15]: 正确说明内部油路可布置到夹紧器下方。
- P4 [15]: 正确说明下置油路可减少或解决夹具设计干涉。
- P5 [10]: 正确说明杠杆支点与锻造本体为一体结构。
- P6 [10]: 正确说明独特锻造工艺提高支点强度。
- P7 [10]: 正确说明专用防尘结构可应对高压冷却液。
- P8 [10]: 正确说明耐腐蚀防尘材料在长期水溶性冷却液环境下保持密封性能。

### Accepted Variants

- `最多缩小 40%` 可写为 `最大缩小 40%`。
- `水溶性冷却液` 可写为 `water-soluble coolant`。
- `减少干涉` 可写为 `解决干涉现象`。

### Forbidden Errors

- 将 40% 描述成所有外形尺寸或夹紧力的缩减值。
- 声称杠杆支点是与本体分离的普通装配件。
- 声称无需防尘结构即可承受高压冷却液。
- 将耐腐蚀材料的结论扩大为任何冷却液、任何时间下绝对不会老化。

### Tolerance

- N/A

### Source

- PDF: LKA_R01_2023KW_C1N.pdf
- Physical page: 6
- Printed page: 754
- Section: 剖面结构 / 紧凑型设计 / 高强度支点部位 / 优异的防止冷却液侵入结构
- Local scope path: 产品特点 > 法兰下部尺寸、内部油路、锻造支点及防尘材料说明
- Evidence type: TEXT + DRAWING
- Evidence: 页面分别给出法兰下部最多缩小 40%、内部油路下置、支点与锻造本体一体化及冷却液防护材料的产品特征。

## LKA-Q-0003

**Type: SPEC_LOOKUP**

### Target

- Binding: EXACT_MODEL
- Product: LKA 油压杠杆式夹紧器
- Model / Scope: LKA0480 标准无动作确认型与带动作确认型

### Question

请比较 LKA0480 在无动作确认和带动作确认两种配置下的夹紧侧受压面积、
夹紧力公式以及夹紧侧/释放侧油量。公式中 `P` 的单位为 MPa、`L` 的单位
为 mm，结果 `F` 的单位为 kN。

### Standard Answer

无动作确认的 LKA0480 夹紧侧受压面积为 7.07 cm2，夹紧力公式为
`F = (11.76 x P) / L` kN，夹紧侧/释放侧油量为 16.6/13.0 cm3。
带动作确认的 LKA0480 夹紧侧受压面积为 5.53 cm2，夹紧力公式为
`F = (9.20 x P) / L` kN，夹紧侧/释放侧油量为 13.0/13.0 cm3。

### Scoring Standard

- P1 [10]: 正确给出无动作确认型受压面积 7.07 cm2。
- P2 [15]: 正确给出无动作确认型公式 `F = (11.76 x P) / L`。
- P3 [10]: 正确给出无动作确认型夹紧侧油量 16.6 cm3。
- P4 [10]: 正确给出无动作确认型释放侧油量 13.0 cm3。
- P5 [10]: 正确给出带动作确认型受压面积 5.53 cm2。
- P6 [15]: 正确给出带动作确认型公式 `F = (9.20 x P) / L`。
- P7 [10]: 正确给出带动作确认型夹紧侧油量 13.0 cm3。
- P8 [10]: 正确给出带动作确认型释放侧油量 13.0 cm3。
- P9 [10]: 明确区分两种配置，未交换任一组数据。

### Accepted Variants

- `x` 可写为 `×` 或乘号表达。
- `cm2`、`cm3` 可写为 `cm²`、`cm³`。
- 公式可等价写为 `11.76P/L` 和 `9.20P/L`。

### Forbidden Errors

- 以夹紧侧受压面积直接代替 PDF 给出的夹紧力公式系数。
- 交换无动作确认和带动作确认两组数据。
- 省略公式中的压板长度 `L` 或将其放在分子。
- 将油量单位写成 L 或 mm3。

### Tolerance

- Exact table values and units are required.

### Source

- PDF: LKA_R01_2023KW_C1N.pdf
- Physical page: 8
- Printed page: 756
- Section: 规格
- Local scope path: 规格表 > LKA0480 列 > 动作确认方式无符号与选择时 > 夹紧侧受压面积 / 夹紧力 / 油量
- Evidence type: TABLE + FORMULA
- Evidence: 规格表在 LKA0480 列中分别列出无动作确认和带动作确认的受压面积、公式系数以及夹紧侧/释放侧油量。

## LKA-Q-0004

**Type: SPEC_LOOKUP**

### Target

- Binding: PRODUCT_SERIES
- Product: LKA 油压杠杆式夹紧器
- Model / Scope: LKA0360-LKA1050 系列共同使用条件

### Question

请给出 LKA0360 至 LKA1050 系列共同的最高使用压力、最低使用压力、耐压、
使用温度范围和适用液压油，并说明最低使用压力的测试条件。

### Standard Answer

系列最高使用压力为 7.0 MPa，最低使用压力为 0.5 MPa，耐压为 10.5 MPa，
使用温度范围为 0-70 degrees C。使用流体为相当于 ISO-VG-32 粘度等级的
一般液压油。最低使用压力 0.5 MPa 是夹紧器在无负载状态下动作的最低压力。

### Scoring Standard

- P1 [20]: 正确给出最高使用压力 7.0 MPa。
- P2 [15]: 正确给出最低使用压力 0.5 MPa。
- P3 [15]: 正确给出耐压 10.5 MPa。
- P4 [15]: 正确给出使用温度范围 0-70 degrees C。
- P5 [20]: 正确给出 ISO-VG-32 粘度等级的一般液压油。
- P6 [15]: 明确最低使用压力是在无负载状态下动作的最低压力。

### Accepted Variants

- `degrees C` 可写为 `°C` 或 `摄氏度`。
- `一般液压油` 可写为 `general hydraulic oil`。

### Forbidden Errors

- 将耐压 10.5 MPa 当作允许持续使用压力。
- 将最低使用压力描述为在任意负载下保证夹紧的压力。
- 将适用流体写为压缩空气或指定为其他粘度等级。

### Tolerance

- Exact values, units, and the no-load qualifier are required.

### Source

- PDF: LKA_R01_2023KW_C1N.pdf
- Physical page: 8
- Printed page: 756
- Section: 规格
- Local scope path: 规格表 > LKA0360-LKA1050 共通行 > 压力 / 温度 / 使用流体；表下注释 4
- Evidence type: TABLE + TEXT
- Evidence: 规格表跨全部八种主体尺寸列出共同压力、温度和流体条件，并在注释中限定最低使用压力为无负载动作条件。

## LKA-Q-0005

**Type: MODEL**

### Target

- Binding: PRODUCT_SERIES
- Product: LKA 油压杠杆式夹紧器
- Model / Scope: LKA 系列动作确认字段

### Question

请列出 LKA 型号中动作确认字段的全部合法表示，并说明空白、`D`、`M`、
`N`、`NC`、`NL`、`NR` 分别代表的确认方式或空气口相位。

### Standard Answer

动作确认字段可以为空、`D`、`M`、`N`、`NC`、`NL` 或 `NR`。空白表示
无动作确认的标准型；`D` 表示探头双出杆型；`M` 表示空气传感器板式连接型；
`N` 表示空气传感器外配管型，并使用标准空气口相位。`NC`、`NL`、`NR`
也是空气传感器外配管型，表示其余三个可选空气口相位。`N/NC/NL/NR`
合计提供四个相位选择。

### Scoring Standard

- P1 [10]: 正确说明空白字段是无动作确认的标准型。
- P2 [15]: 正确说明 `D` 为探头双出杆型。
- P3 [20]: 正确说明 `M` 为空气传感器板式连接型。
- P4 [20]: 正确说明 `N` 为空气传感器外配管型。
- P5 [10]: 正确说明 `N` 使用标准空气口相位。
- P6 [25]: 正确说明 `NC`、`NL`、`NR` 是其余三个空气口相位，连同 `N` 共四种。

### Accepted Variants

- `探头双出杆型` 可写为 `probe dual-rod type`。
- `板式连接型` 可写为 `manifold connection type`。
- `外配管型` 可写为 `external piping type`。

### Forbidden Errors

- 将 `D`、`M` 或 `N` 解释为压板方向。
- 将 `M` 与 `N` 的配管方式互换。
- 声称 `NC`、`NL`、`NR` 是三个不同的传感器工作原理。
- 遗漏空白标准型或将四个空气口相位说成四台传感器。

### Tolerance

- Exact codes and meanings are required.

### Source

- PDF: LKA_R01_2023KW_C1N.pdf
- Physical page: 7
- Printed page: 755
- Section: 型号表示 > 动作确认方式
- Local scope path: 型号字段 5 > 无符号 / D / M / N 与 NC/NL/NR 相位注释
- Evidence type: TABLE + DRAWING
- Evidence: 型号页定义无符号、D、M、N 的确认方式，并注明 N 为标准相位、NC/NL/NR 为其他空气传感孔相位。

## LKA-Q-0006

**Type: MODEL**

### Target

- Binding: PRODUCT_SERIES
- Product: LKA 油压杠杆式夹紧器
- Model / Scope: LKA 系列选配字段与 H 选配主体尺寸边界

### Question

请说明 LKA 型号选配字段中空白、`A`、`H`、`K` 的含义，列出允许选择
`H` 的主体尺寸，并说明 090/105 主体和其他选配组合应如何判断。

### Standard Answer

选配字段为空表示标准型；`A` 表示快换压板 A 型；`H` 表示高强度链接板型；
`K` 表示带凸缘销、C 形定位环型。`H` 只允许用于 036、040、048、055、
065、075 六种主体尺寸，不允许用于 090 和 105。PDF 对其他选配组合没有
给出完整兼容矩阵，而是要求另行询问，因此不能仅凭单个字段都存在就断言
某一组合合法。

### Scoring Standard

- P1 [10]: 正确说明空白选配字段表示标准型。
- P2 [15]: 正确说明 `A` 为快换压板 A 型。
- P3 [15]: 正确说明 `H` 为高强度链接板型。
- P4 [15]: 正确说明 `K` 为带凸缘销、C 形定位环型。
- P5 [20]: 完整列出 `H` 可用于 036/040/048/055/065/075。
- P6 [15]: 明确 `H` 不可用于 090/105。
- P7 [10]: 明确其他未记录组合须另行询问，不能自行推定合法。

### Accepted Variants

- `链接板` 可写为 `连杆板` 或 `link plate`。
- `C 形定位环` 可写为 `C-retaining ring`。

### Forbidden Errors

- 声称 `H` 可用于 090 或 105。
- 将 `A` 解释为空气传感器选配。
- 将 `K` 解释为高强度链接板。
- 将任意字段拼接结果自动判定为合法组合。

### Tolerance

- Exact option codes and the H-size boundary are required.

### Source

- PDF: LKA_R01_2023KW_C1N.pdf
- Physical page: 7
- Printed page: 755
- Section: 型号表示 > 选配项
- Local scope path: 型号字段 6 > 无符号 / A / H / K；主体尺寸限制与组合询问注释
- Evidence type: TABLE + TEXT + DRAWING
- Evidence: 选配字段表定义四种表示，红色注释将 H 限定为 036-075 六种主体尺寸，页下注释要求另行询问选配组合。

## LKA-Q-0007

**Type: TABLE**

### Target

- Binding: EXACT_MODEL
- Product: BZL 低压用速度控制阀
- Model / Scope: BZL0101-B

### Question

请解读 `BZL0101-B` 的 G 螺纹尺寸、设计编号和控制方式，并给出其最高使用
压力、耐压、最小流路面积、使用流体、使用温度、本体推荐紧固力矩和重量。

### Standard Answer

`10` 表示 G1/8A，设计编号为 `1`，`B` 表示回油节流。最高使用压力为
7 MPa，耐压为 10.5 MPa，最小流路面积为 2.6 mm2。使用流体为相当于
ISO-VG-32 粘度等级的一般液压油，使用温度为 0-70 degrees C。本体推荐
紧固力矩为 10 N-m，重量为 12 g。

### Scoring Standard

- P1 [10]: 正确说明 `10` 对应 G1/8A。
- P2 [10]: 正确说明设计编号为 `1`。
- P3 [15]: 正确说明 `B` 为回油节流。
- P4 [15]: 正确给出最高使用压力 7 MPa。
- P5 [10]: 正确给出耐压 10.5 MPa。
- P6 [10]: 正确给出最小流路面积 2.6 mm2。
- P7 [10]: 正确给出 ISO-VG-32 一般液压油。
- P8 [10]: 正确给出使用温度 0-70 degrees C。
- P9 [5]: 正确给出推荐紧固力矩 10 N-m。
- P10 [5]: 正确给出重量 12 g。

### Accepted Variants

- `回油节流` 可写为 `meter-out`。
- `mm2` 可写为 `mm²`，`N-m` 可写为 `N·m`。

### Forbidden Errors

- 将 `B` 解释为进油节流；进油节流代码为 `A`。
- 将 G1/8A 写成 G1/4A 或 G3/8A。
- 将 10.5 MPa 耐压当作最高持续使用压力。
- 交换紧固力矩和重量数值。

### Tolerance

- Exact model fields, table values, and units are required.

### Source

- PDF: LKA_R01_2023KW_C1N.pdf
- Physical page: 41
- Printed page: 1259
- Section: 控制阀 > 速度控制阀（低压用） > 型号表示 / 规格
- Local scope path: BZL 型号表示 > 10 / 1 / B；规格表 > BZL0101-B 列
- Evidence type: TABLE + MODEL
- Evidence: 型号字段表定义 G 螺纹、设计编号和控制方式，规格表在 BZL0101-B 列给出压力、流路面积、流体、温度、力矩和重量。

## LKA-Q-0008

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: BZS 直装式顺序阀
- Model / Scope: LKA0360-LKA1050 的 C 配管型顺序阀尺寸选择

### Question

对于采用 `C` 板式配管的 LKA0360 至 LKA1050，分别应按主体尺寸组选择
哪一种 BZS 直装式顺序阀？

### Standard Answer

LKA0360、LKA0400、LKA0480、LKA0550 选择 `BZS0100`；LKA0650、LKA0750
选择 `BZS0200`；LKA0900、LKA1050 选择 `BZS0300`。BZS 是直接安装在
`C` 配管方式夹紧器 G 螺纹专用底孔上的顺序阀。

### Scoring Standard

- P1 [35]: 正确将 LKA0360/0400/0480/0550 映射到 BZS0100。
- P2 [30]: 正确将 LKA0650/0750 映射到 BZS0200。
- P3 [30]: 正确将 LKA0900/1050 映射到 BZS0300。
- P4 [5]: 明确该映射适用于 `C` 板式配管的 G 螺纹专用底孔直装方式。

### Accepted Variants

- 各主体尺寸可带合法的压板方向、动作确认和选配后缀；顺序阀尺寸映射仍按主体尺寸判断。

### Forbidden Errors

- 将 BZS0100 用于 LKA0900 或 LKA1050。
- 将 BZS0300 用于 LKA0360-LKA0550。
- 声称该表允许在 `S` 外配管型的无板式连接口位置直接安装。

### Tolerance

- Exact body-size groups and BZS model mappings are required.

### Source

- PDF: LKA_R01_2023KW_C1N.pdf
- Physical page: 49-50
- Printed page: 1269-1270
- Section: 直装式顺序阀 > 型号表示 / 对应机器型号
- Local scope path: BZS 产品说明 > C 配管直装条件；对应机器型号表 > LKA（复动式杠杆夹紧器）列
- Evidence type: TABLE + MODEL
- Evidence: BZS 说明限定 C 配管直装，适用型号表按 LKA 主体尺寸将 0360-0550、0650-0750、0900-1050 分配给 BZS0100/0200/0300。

## LKA-Q-0009

**Type: TABLE**

### Target

- Binding: EXACT_MODEL
- Product: LKA 油压杠杆式夹紧器
- Model / Scope: LKA0480 标准压板附件与 LKA0480-A 快换压板安装组件

### Question

为 LKA0480 选择毛坯压板、并为 LKA0480-A 选择快换压板安装组件时，各自
应使用什么附件型号？同时给出快换安装组件的压板紧固螺栓规格、六角扳手
尺寸和紧固力矩。

### Standard Answer

LKA0480 的毛坯压板型号为 `LZK0480-L`。LKA0480-A 的快换压板安装组件
型号为 `LZK0480-W`。该安装组件使用 M3 x 0.5 压板紧固螺栓，六角扳手
尺寸为 2.5 mm，紧固力矩为 1.3 N-m。

### Scoring Standard

- P1 [20]: 正确选择毛坯压板 `LZK0480-L`。
- P2 [10]: 明确该毛坯压板对应 LKA0480。
- P3 [20]: 正确选择快换安装组件 `LZK0480-W`。
- P4 [15]: 明确该安装组件对应 LKA0480-A。
- P5 [15]: 正确给出压板紧固螺栓 M3 x 0.5。
- P6 [10]: 正确给出六角扳手尺寸 2.5 mm。
- P7 [10]: 正确给出紧固力矩 1.3 N-m。

### Accepted Variants

- `M3 x 0.5` 可写为 `M3×0.5`。
- `N-m` 可写为 `N·m`。
- `快换压板安装组件` 可写为 `快换压板 A 型安装套件`。

### Forbidden Errors

- 将毛坯压板 `-L` 与快换安装组件 `-W` 互换。
- 将快换组件绑定到不带 `A` 的标准 LKA0480。
- 将 2.5 mm 扳手尺寸写成螺栓直径或紧固力矩。

### Tolerance

- Exact accessory models, fastener specification, wrench size, and torque are required.

### Source

- PDF: LKA_R01_2023KW_C1N.pdf
- Physical page: 30
- Printed page: 778
- Section: 附件：毛坯压板 / 附件：快换压板 A 型用紧固件
- Local scope path: LZK0480-L 行；LZK0480-W 行 > 对应机器型号 / 压板紧固螺栓 / 六角扳手 / 紧固力矩
- Evidence type: TABLE + DRAWING
- Evidence: 两张附件表分别将 LZK0480-L 对应 LKA0480、LZK0480-W 对应 LKA0480-A，并列出 M3 x 0.5、2.5 mm 和 1.3 N-m。

## LKA-Q-0010

**Type: TABLE**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK 液压产品目录公共参考
- Model / Scope: LKA_R01_2023KW_C1N.pdf :: physical page 37, printed page 1729, surface-roughness notation comparison table

### Question

根据该 PDF 的表面粗糙度新旧标示对照表，分别给出新标示 Rz 6.3、Rz 25、
Rz 100 对应的 Ra 参考值和旧标示范围。

### Standard Answer

- Rz 6.3 的 Ra 参考值为 1.6，对应旧标示 1.6S-6.3S。
- Rz 25 的 Ra 参考值为 6.3，对应旧标示 12.5S-25S。
- Rz 100 的 Ra 参考值为 25，对应旧标示 50S-100S。

其中新标示采用 JIS B 0601:2013，旧标示采用 JIS B 0601:1982。

### Scoring Standard

- P1 [15]: 正确给出 Rz 6.3 的 Ra 参考值 1.6。
- P2 [15]: 正确给出 Rz 6.3 的旧标示范围 1.6S-6.3S。
- P3 [15]: 正确给出 Rz 25 的 Ra 参考值 6.3。
- P4 [15]: 正确给出 Rz 25 的旧标示范围 12.5S-25S。
- P5 [15]: 正确给出 Rz 100 的 Ra 参考值 25。
- P6 [15]: 正确给出 Rz 100 的旧标示范围 50S-100S。
- P7 [10]: 正确区分新标示 JIS B 0601:2013 与旧标示 JIS B 0601:1982。

### Accepted Variants

- 范围连接符可写为 `~`、`-` 或 `至`。
- `Ra 参考值` 可写为 `算术平均粗糙度参考值`。

### Forbidden Errors

- 将 Rz 最大高度值直接当作 Ra 参考值。
- 交换任意两行的 Ra 或旧标示范围。
- 将本公共对照表声称为 LKA 独有的型号规格。

### Tolerance

- Exact mapping values are required.

### Source

- PDF: LKA_R01_2023KW_C1N.pdf
- Physical page: 37
- Printed page: 1729
- Section: 关于表面粗糙度、O 形密封圈的标示更改通知 > 表面粗糙度标示新旧对照
- Local scope path: physical page 37 > 新标示 JIS B 0601:2013 / 旧标示 JIS B 0601:1982 对照表
- Evidence type: TABLE
- Evidence: 三行对照表逐行绑定新 Rz、Ra 参考值和旧 S 范围，并在表头注明新旧 JIS 版本。

## LKA-Q-0011

**Type: TABLE**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK 液压控制阀
- Model / Scope: LKA_R01_2023KW_C1N.pdf :: physical page 40, printed page 1258, control-valve type comparison

### Question

请将 BZL、BZT、BZX、JZG、BZS 五个控制阀系列分别对应到其功能，并给出
各系列页面标示的最高使用压力。

### Standard Answer

- BZL：低压用速度控制阀，最高使用压力 7 MPa。
- BZT：高压用速度控制阀，最高使用压力 35 MPa。
- BZX：排气阀，最高使用压力 35 MPa。
- JZG：带排气功能的 G 螺纹堵头，最高使用压力 35 MPa。
- BZS：直装式顺序阀，最高使用压力 7 MPa。

### Scoring Standard

- P1 [10]: 正确说明 BZL 是低压用速度控制阀。
- P2 [10]: 正确给出 BZL 最高使用压力 7 MPa。
- P3 [10]: 正确说明 BZT 是高压用速度控制阀。
- P4 [10]: 正确给出 BZT 最高使用压力 35 MPa。
- P5 [10]: 正确说明 BZX 是排气阀。
- P6 [10]: 正确给出 BZX 最高使用压力 35 MPa。
- P7 [10]: 正确说明 JZG 是带排气功能的 G 螺纹堵头。
- P8 [10]: 正确给出 JZG 最高使用压力 35 MPa。
- P9 [10]: 正确说明 BZS 是直装式顺序阀。
- P10 [10]: 正确给出 BZS 最高使用压力 7 MPa。

### Accepted Variants

- `速度控制阀` 可写为 `flow-control valve`。
- `排气阀` 可写为 `air-bleed valve`。
- `顺序阀` 可写为 `sequence valve`。

### Forbidden Errors

- 交换 BZL 与 BZT 的压力等级。
- 将 JZG 说成速度控制阀或顺序阀。
- 将耐压值当作题目要求的最高使用压力。
- 将 BZS 最高使用压力写成 35 MPa。

### Tolerance

- Exact family functions and maximum operating pressures are required.

### Source

- PDF: LKA_R01_2023KW_C1N.pdf
- Physical page: 40
- Printed page: 1258
- Section: 控制阀 > 种类与动作说明
- Local scope path: 控制阀种类列表 > BZL / BZT / BZX / JZG / BZS 产品名称与最高使用压力
- Evidence type: TABLE + DRAWING
- Evidence: 类型比较页逐项列出五个系列的产品功能，并在各产品说明中标示 7 MPa 或 35 MPa 的最高使用压力。

## LKA-Q-0012

**Type: TABLE**

### Target

- Binding: EXACT_MODEL
- Product: LKA 油压杠杆式夹紧器
- Model / Scope: LKA0480 标准外形、安装和配管接口

### Question

请给出 LKA0480 标准外形尺寸表中的全行程、夹紧行程和行程余量，并说明
本体安装螺纹、`C` 板式连接的 G 螺纹尺寸、`S` 外配管连接的 Rc 螺纹尺寸，
以及 `C` 型夹紧/释放油口使用的 O 形密封圈型号。

### Standard Answer

LKA0480 的全行程为 23.5 mm，夹紧行程为 20.5 mm，行程余量为 3 mm。
本体安装螺纹 `CA` 为 M5 x 0.8。`C` 板式连接的夹紧和释放油口均为
G1/8；`S` 外配管连接的夹紧和释放油口均为 Rc1/8。`C` 型两个油口均使用
`OR NBR-90 P5-N` O 形密封圈。

### Scoring Standard

- P1 [15]: 正确给出全行程 23.5 mm。
- P2 [15]: 正确给出夹紧行程 20.5 mm。
- P3 [10]: 正确给出行程余量 3 mm。
- P4 [15]: 正确给出本体安装螺纹 M5 x 0.8。
- P5 [15]: 正确给出 `C` 型夹紧/释放油口均为 G1/8。
- P6 [15]: 正确给出 `S` 型夹紧/释放油口均为 Rc1/8。
- P7 [15]: 正确给出 `C` 型两个油口的密封圈均为 `OR NBR-90 P5-N`。

### Accepted Variants

- `M5 x 0.8` 可写为 `M5×0.8`。
- `OR NBR-90 P5-N` 可保留或省略字段间空格，但字段顺序不得变化。

### Forbidden Errors

- 交换全行程、夹紧行程和行程余量。
- 将 `C` 型写成 Rc 螺纹，或将 `S` 型写成 G 螺纹。
- 将 O 形密封圈型号写成 NBR-70-1、P7 或其他公称号。
- 将耐压或夹紧力数据当作尺寸表字段。

### Tolerance

- Exact dimensions, thread designations, and O-ring model are required.

### Source

- PDF: LKA_R01_2023KW_C1N.pdf
- Physical page: 17-18
- Printed page: 765-766
- Section: 外形尺寸（标准型） / 外形尺寸表及安装部位加工尺寸表
- Local scope path: LKA0480 列 > 全行程 / 夹紧行程 / 行程余量 / CA / C型夹紧释放油口 / S型夹紧释放油口 / O形密封圈
- Evidence type: DRAWING + TABLE
- Evidence: 标准外形图定义 C/S 配管接口，随后尺寸表在 LKA0480 列绑定行程、安装螺纹、两类油口螺纹和 C 型密封圈型号。

## LKA-Q-0013

**Type: FACT**

### Target

- Binding: MODEL_FAMILY
- Product: LKA 油压杠杆式夹紧器
- Model / Scope: LKA0360-A 至 LKA1050-A 快换压板 A 型

### Question

LKA 快换压板 `A` 选配在型号、压板安装销、本体尺寸和快换安装组件交付方面
与标准/H/K 选配有何区别？以 LKA0480-A 为例说明所需安装组件型号。

### Standard Answer

快换压板型在选配字段使用 `A`。与选配字段为空、`H` 或 `K` 的形式不同，
选择 `A` 时不附带压板安装用销钉；但杠杆夹紧器本体尺寸与空白/H/K 型一致。
快换压板安装所需的安装螺栓、活塞杆销和压板销组成另售的快换安装组件，
不是随夹紧器本体交付。LKA0480-A 对应的组件型号为 `LZK0480-W`。

### Scoring Standard

- P1 [15]: 正确说明快换压板选配代码为 `A`。
- P2 [20]: 正确说明 `A` 型不附带压板安装用销钉。
- P3 [20]: 正确说明 `A` 型夹紧器本体尺寸与空白/H/K 型一致。
- P4 [15]: 正确说明快换组件包含安装螺栓。
- P5 [10]: 正确说明快换组件包含活塞杆销。
- P6 [10]: 正确说明快换组件包含压板销且组件另售。
- P7 [10]: 正确给出 LKA0480-A 对应 `LZK0480-W`。

### Accepted Variants

- `快换安装组件` 可写为 `快换套件` 或 `quick-change mounting kit`。
- `另售` 可写为 `需另行购买`。

### Forbidden Errors

- 声称 `A` 型随本体附带全部快换安装组件。
- 声称 `A` 型本体尺寸与标准/H/K 型完全不同。
- 将 `LZK0480-L` 毛坯压板误写成 LKA0480-A 的快换安装组件。
- 将 `A` 解释为空气传感器动作确认代码。

### Tolerance

- N/A

### Source

- PDF: LKA_R01_2023KW_C1N.pdf
- Physical page: 25-26, 30
- Printed page: 773-774, 778
- Section: 快换压板 A 型 / 附件：快换压板 A 型用紧固件
- Local scope path: A 型号表示注释 > 销钉与本体尺寸；外形页注意事项 > 快换组件另售；附件表 > LZK0480-W
- Evidence type: TEXT + TABLE + DRAWING
- Evidence: A 型型号页注明不附带压板安装销且本体尺寸与空白/H/K 一致；外形和附件页定义另售组件内容及 LKA0480-A 对应型号。

## LKA-Q-0014

**Type: MODEL**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK 液压产品目录公共参考
- Model / Scope: LKA_R01_2023KW_C1N.pdf :: physical page 38, printed page 1730, O-ring notation grammar and mapping

### Question

请解读新标示 `OR NBR-90 P22A-N` 的材料识别、种类、公称号和品质等级，
并给出它在同页新旧标示对照表中的旧标示。

### Standard Answer

`OR` 表示 O 形密封圈。`NBR-90` 是一般用丁腈橡胶、A 型硬度 90，对应
旧材料识别符号 `1B`。`P` 是运动用种类标记，`22A` 是公称号，末尾 `N`
是一般用品质等级。完整新标示 `OR NBR-90 P22A-N` 对应旧标示 `1BP22A`。

### Scoring Standard

- P1 [10]: 正确说明 `OR` 表示 O 形密封圈。
- P2 [20]: 正确说明 `NBR-90` 是一般用丁腈橡胶、A 型硬度 90。
- P3 [15]: 正确说明 `NBR-90` 对应旧材料识别符号 `1B`。
- P4 [15]: 正确说明 `P` 表示运动用。
- P5 [15]: 正确说明 `22A` 是公称号。
- P6 [10]: 正确说明末尾 `N` 是一般用品质等级。
- P7 [15]: 正确给出完整旧标示 `1BP22A`。

### Accepted Variants

- `丁腈橡胶` 可写为 `NBR` 或 `nitrile rubber`。
- `A 型硬度 90` 可写为 `durometer A 90`。

### Forbidden Errors

- 将 `90` 解释为公称号或尺寸。
- 将 `P` 解释为固定用或品质等级。
- 将 `N` 解释为材料代码。
- 将旧标示写成 `1AP22A`；`1A` 对应 NBR-70-1，不对应 NBR-90。

### Tolerance

- Exact field meanings and old/new mapping are required.

### Source

- PDF: LKA_R01_2023KW_C1N.pdf
- Physical page: 38
- Printed page: 1730
- Section: O 形密封圈的标示更改 > 新旧标示比较 / 新标示字段说明
- Local scope path: OR NBR-90 P22A-N 字段图；对照表 > OR NBR-90 P22A-N / 1BP22A 行
- Evidence type: TABLE + MODEL
- Evidence: 字段图定义材料、种类、公称号和品质等级，对照表将该完整新标示与 1BP22A 逐行绑定。

## LKA-Q-0015

**Type: TABLE**

### Target

- Binding: EXACT_MODEL
- Product: LZY-MD 板式安装座
- Model / Scope: LZY0480-MD 用于 LKA0480

### Question

为 LKA0480 选择 LZY-MD 板式安装座时，应使用什么型号？请同时给出其
设计编号、材料和表面处理、附带 O 形密封圈、重量，以及适用型号表对
LKA0480 的确认。

### Standard Answer

应选择 `LZY0480-MD`，其设计编号为 `0`。材料为 S45C，表面处理为黑色
氧化皮膜。附带 O 形密封圈为 `OR NBR-90 P5-N`，重量为 0.3 kg。
适用机器型号表在 `LZY0480-MD` 列明确列出 LKA0480。

### Scoring Standard

- P1 [20]: 正确选择 `LZY0480-MD`。
- P2 [10]: 正确给出设计编号 `0`。
- P3 [15]: 正确给出材料 S45C。
- P4 [15]: 正确给出黑色氧化皮膜表面处理。
- P5 [15]: 正确给出 O 形密封圈 `OR NBR-90 P5-N`。
- P6 [10]: 正确给出重量 0.3 kg。
- P7 [15]: 明确适用型号表将 LZY0480-MD 与 LKA0480 绑定。

### Accepted Variants

- `黑色氧化皮膜` 可写为 `black oxide coating`。
- O 形密封圈字段间空格可省略，但字段顺序不得变化。

### Forbidden Errors

- 将 LKA0480 选择为 WHZ0480-MD、LZ-MS 或 LZ-MP。
- 将设计编号写为 `1`。
- 将密封圈材料或公称号写成 NBR-70-1 或 P7。
- 将 0.3 kg 写成 0.3 g。

### Tolerance

- Exact model, material, O-ring, and weight are required.

### Source

- PDF: LKA_R01_2023KW_C1N.pdf
- Physical page: 54-55
- Printed page: 1698-1699
- Section: 板式安装座 > 适用型号 / LZY-MD 型号表示与外形尺寸
- Local scope path: 适用型号表 > LZY-MD / LKA；LZY0480-MD 列 > 设计编号 / O形密封圈 / 重量；页下注释 1
- Evidence type: TABLE + MODEL
- Evidence: 适用型号页将 LZY-MD 分配给 LKA，规格页在 LZY0480-MD 列列出 LKA0480、P5 密封圈和 0.3 kg，并在注释中给出 S45C 与黑色氧化皮膜。

## LKA-Q-0016

**Type: SPEC_LOOKUP**

### Target

- Binding: EXACT_MODEL
- Product: BZS 直装式顺序阀
- Model / Scope: BZS0100

### Question

请解读 `BZS0100` 的 G 螺纹尺寸和设计编号，并给出使用压力范围、开启压力
范围、耐压、本体推荐紧固力矩和重量。

### Standard Answer

`10` 表示 G1/8A，设计编号为 `0`。使用压力范围为 1.0-6.0 MPa，开启压力
范围为 2.0-7.0 MPa，耐压为 10.5 MPa。本体推荐紧固力矩为 10 N-m，
重量为 35 g。

### Scoring Standard

- P1 [10]: 正确说明 `10` 对应 G1/8A。
- P2 [10]: 正确说明设计编号为 `0`。
- P3 [20]: 正确给出使用压力范围 1.0-6.0 MPa。
- P4 [20]: 正确给出开启压力范围 2.0-7.0 MPa。
- P5 [15]: 正确给出耐压 10.5 MPa。
- P6 [15]: 正确给出推荐紧固力矩 10 N-m。
- P7 [10]: 正确给出重量 35 g。

### Accepted Variants

- 范围连接符可写为 `~`、`-` 或 `至`。
- `N-m` 可写为 `N·m`。

### Forbidden Errors

- 交换使用压力范围和开启压力范围。
- 将 10.5 MPa 耐压当作持续使用压力上限。
- 将 G1/8A 写成 G1/4A 或 G3/8A。
- 将重量 35 g 与紧固力矩 10 N-m 互换。

### Tolerance

- Exact ranges, values, and units are required.

### Source

- PDF: LKA_R01_2023KW_C1N.pdf
- Physical page: 49
- Printed page: 1269
- Section: 直装式顺序阀 > 型号表示 / 规格
- Local scope path: BZS0100 型号字段 > 10 / 0；规格表 > BZS0100 列
- Evidence type: TABLE + MODEL
- Evidence: 型号表示定义 G 螺纹和设计编号，规格表在 BZS0100 列列出使用/开启压力范围、耐压、紧固力矩和重量。
