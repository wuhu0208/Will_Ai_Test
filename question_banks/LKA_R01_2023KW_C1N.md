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
- Product printed pages: 749-778
- Included lever-clamp/common-caution printed pages: 943-948
- Included common-reference printed pages: 1729-1730
- Included control-valve printed pages: 1257-1262, 1265-1272
- Included manifold-block printed pages: 1697-1700
- Included sales-reference physical pages: 57-58 (unnumbered)
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

### 2.3 Source coverage inventory and dispositions

The disposition column maps each source area to representative questions or records
why the material is retained as context rather than tested separately. Every `HIGH`
and `MEDIUM` item has a final disposition.

| Inventory ID | Physical / printed page | Local scope | Evidence type | Priority | Testable object | Final disposition |
|---|---|---|---|---|---|---|
| LKA-SI-001 | 1 / 749 | Product family introduction > LKA identity and operating principle | TEXT + DRAWING | HIGH | LKA position in the link-clamp family, release/clamp motion, and representative applications | LKA product identity and structure are represented by `LKA-Q-0002`; the qualitative release/clamp end-state drawing is retained as operating context because it supplies no additional stable setpoint or procedure |
| LKA-SI-002 | 2 / 750 | Product-family examples | TEXT + DRAWING | LOW | Contextual examples of other link-clamp models | Context only; exclude facts not bound to LKA |
| LKA-SI-003 | 3-4 / 751-752 | Product lineup and accessory overview | TABLE + DRAWING | MEDIUM | Product-type boundaries, variant selection, and accessory relationships | No separate question: broader product-comparison context is not an LKA operating rule; LKA-specific selection is covered by `LKA-Q-0002`, `LKA-Q-0005`, and `LKA-Q-0006` |
| LKA-SI-004 | 5 / 753 | Table of contents | TEXT | NON-TEST | Navigation map for LKA product, common cautions, valves, and manifold blocks | Navigation only |
| LKA-SI-005 | 6 / 754 | LKA features and cross-section | TEXT + DRAWING | HIGH | Compact body, integrated fulcrum, coolant protection, eccentric-load allowance, arm directions, and direct speed-control mounting | Compactness, fulcrum, and sealing facts in `LKA-Q-0002`; eccentricity and operating controls in `LKA-Q-0020`, `LKA-Q-0021`, and `LKA-Q-0022` |
| LKA-SI-006 | 7 / 755 | Model designation | TABLE + DRAWING | HIGH | Six-field order, legal body/piping/arm/confirmation/option values, and H-option size restriction | `LKA-Q-0001`, `LKA-Q-0005`, and `LKA-Q-0006`; deterministic grammar cases cover field order, allowlists, invalid fields, and the H-option body-size boundary |
| LKA-SI-007 | 8 / 756 | Specifications | TABLE + FORMULA | HIGH | Clamp area, clamp-force formula, capacities, strokes, pressure, temperature, fluid, and weight for eight body sizes and confirmation variants | Representative lookup and common limits in `LKA-Q-0003`, `LKA-Q-0004`; deterministic calculation in `LKA-Q-0017` |
| LKA-SI-008 | 9-12 / 757-760 | Clamp-force capability curves | CHART + FORMULA | HIGH | Pressure/arm-length/clamp-force relationships with and without action confirmation | Deterministic comparison in `LKA-Q-0017`; genuine curve read in `LKA-Q-0018` |
| LKA-SI-009 | 13-16 / 761-764 | Allowable eccentricity curves | CHART + DRAWING | HIGH | Standard versus high-strength-link eccentricity limits and consequences of exceeding them | Genuine visual eccentricity read in `LKA-Q-0021`; limit consequence in `LKA-Q-0020` |
| LKA-SI-010 | 17-18 / 765-766 | Standard model dimensions and dimension table | DRAWING + TABLE | HIGH | External, mounting, port, arm, and interference dimensions | Representative LKA0480 stroke/mounting/port lookup in `LKA-Q-0012`; high-consequence mounting controls in `LKA-Q-0020` |
| LKA-SI-011 | 19-20 / 767-768 | Probe dual-rod confirmation type `D` | DRAWING + TABLE | HIGH | Model-specific construction, confirmation interface, and dimensions | `D` semantics in `LKA-Q-0005`; repeated body-size dimension grids are retained as lookup evidence rather than numeric-swap questions |
| LKA-SI-012 | 21-22 / 769-770 | Air-sensor manifold confirmation type `M` | DRAWING + TABLE | HIGH | Model-specific air interface, construction, and dimensions | `M` semantics in `LKA-Q-0005`; connection and installation procedure in `LKA-Q-0019`; repeated dimensions are retained as lookup evidence |
| LKA-SI-013 | 23-24 / 771-772 | Air-sensor external-piping types `N/NC/NL/NR` | DRAWING + TABLE | HIGH | Four port phases, external piping, and dimensions | Four-phase model semantics in `LKA-Q-0005`; connection procedure in `LKA-Q-0019`; repeated dimensions are retained without numeric-swap questions |
| LKA-SI-014 | 25-26 / 773-774 | Quick-change arm option `A` | DRAWING + TABLE + TEXT | HIGH | Quick-change construction, dimensions, installation, and fastening | Option/attachment and delivery controls in `LKA-Q-0013` and `LKA-Q-0009`; fastening data already included there and is not repeated as an operational numeric swap |
| LKA-SI-015 | 18, 20, 22, 24, 26 / 766, 768, 770, 772, 774 | Repeated option notes and model/dimension tables | DRAWING + TABLE + TEXT | HIGH | `H`/`K` option construction, A-type differences, and confirmation-variant dimension grids | `H`/`K` model boundaries in `LKA-Q-0006`; A-type differences in `LKA-Q-0013`; repeated dimension grids are retained as source rather than converted into numeric-swap questions |
| LKA-SI-016 | 27 / 775 | Air-sensor connection and confirmation | TEXT + DRAWING + TABLE | HIGH | Differential-pressure confirmation, sensor connection limit, exhaust protection, arm alignment, and O-ring grease controls | Connection and installation controls in `LKA-Q-0019` |
| LKA-SI-017 | 28 / 776 | Air-sensor circuit and process charts | STATE_DIAGRAM + CHART | HIGH | Clamp/release sensing sequence, pressure/stroke states, and sensor-output conditions | Circuit limit in `LKA-Q-0019`; clamp/release detection-port state sequence in `LKA-Q-0027` |
| LKA-SI-018 | 29 / 777 | Clamp-arm design | DRAWING + FORMULA + CHART | HIGH | Arm dimensions, clamp-point distance, force-curve selection, and geometric limits | Force/arm-length decision in `LKA-Q-0017` and eccentricity decision in `LKA-Q-0021`; geometry table remains fabrication lookup because no single custom arm target is specified |
| LKA-SI-019 | 30 / 778 | Blank arm and fastening kit | DRAWING + TABLE + TEXT | MEDIUM | Blank-arm selection, machining, fastener kit, and compatibility constraints | Representative LKA0480 selection and exact fastening kit in `LKA-Q-0009`; remaining repeated sizes are fabrication context rather than separate questions |
| LKA-SI-020 | 31 / 943 | Lever-clamp design and installation cautions, including LKA | TEXT + DRAWING + TABLE | HIGH | Hydraulic circuit, simultaneous pressure prohibition, axial loading, eccentricity, contamination, parallel clamping, pins, mounting, and sensor references | High-consequence LKA design and installation controls in `LKA-Q-0020` |
| LKA-SI-021 | 32 / 944 | Lever-clamp operation and adjustment, including LKA | TEXT + DRAWING + TABLE | HIGH | Quick-change fastening, action time, air bleeding, speed adjustment, fulcrum adjustment, and probe installation | LKA speed-adjustment procedure in `LKA-Q-0022`; exact quick-change fastening data already appears in `LKA-Q-0009`; specialized fulcrum/probe rows remain variant-local reference |
| LKA-SI-022 | 33 / 945 | Common hydraulic installation cautions | TEXT + DRAWING | HIGH | Oil selection, cleaning, sealing tape, air bleeding, and fastener checks | Page-bounded common installation and air-bleed procedure in `LKA-Q-0023` |
| LKA-SI-023 | 34 / 946 | Common hydraulic speed-control circuits | STATE_DIAGRAM + TEXT | HIGH | Single/double-acting circuit differences, meter-out/meter-in behavior, air instability, circuit separation, and back pressure | Page-bounded common circuit controls in `LKA-Q-0024` |
| LKA-SI-024 | 35 / 947 | Common operation and maintenance cautions | TEXT | HIGH | Qualified staff, energy isolation, restart checks, moving-part avoidance, modification prohibition, inspection, storage, and overhaul | Page-bounded safety and maintenance controls in `LKA-Q-0025` |
| LKA-SI-025 | 36 / 948 | Warranty | TEXT | LOW | Warranty term, coverage, and exclusions | Exclude from core capability bank; commercial policy |
| LKA-SI-026 | 37-38 / 1729-1730 | Common notation references | TABLE | MEDIUM | Surface-roughness and O-ring old/new notation mappings | Surface-roughness mapping in `LKA-Q-0010`; O-ring grammar/mapping in `LKA-Q-0014`; both page-bounded `DOCUMENT_COMMON` |
| LKA-SI-027 | 39 / 1257 | Control-valve family introduction | TEXT + DRAWING | MEDIUM | BZL/BZT/BZX/JZG/BZS family purpose and direct-mount relationship | Family roles covered by `LKA-Q-0011`; ancillary scope |
| LKA-SI-028 | 40 / 1258 | Control-valve type comparison | TABLE + DRAWING | MEDIUM | Pressure classes and functions of speed, exhaust, plug, and sequence-valve types | `LKA-Q-0011` |
| LKA-SI-029 | 41-44 / 1259-1262 | BZL/BZT speed-control valves | TABLE + CHART + DRAWING | MEDIUM | Model grammar, specifications, compatible threads, flow curves, dimensions, and circuit cautions | Representative BZL lookup in `LKA-Q-0007`; sizing curves are ancillary valve-selection evidence and are not converted into repeated LKA questions without a specified circuit flow target |
| LKA-SI-030 | 45-48 / 1265-1268 | BZX exhaust valves and JZG plugs | TABLE + DRAWING + TEXT | MEDIUM | Model grammar, pressure/specification limits, compatibility, dimensions, and exhaust safety | Family function/pressure in `LKA-Q-0011`; LKA size mapping repeats G-thread groups already tested by `LKA-Q-0008`; product-specific exhaust installation is ancillary and excluded from the core LKA operating bank |
| LKA-SI-031 | 49-52 / 1269-1272 | BZS direct-mounted sequence valves | TABLE + CHART + DRAWING + TEXT | HIGH | Model grammar, operating/setting pressure, compatibility, dimensions, pressure-flow behavior, contamination, air, and adjustment cautions | LKA compatibility in `LKA-Q-0008`, representative specifications in `LKA-Q-0016`, and high-consequence setup/operation controls in `LKA-Q-0026` |
| LKA-SI-032 | 53-56 / 1697-1700 | Manifold blocks | TABLE + DRAWING + TEXT | MEDIUM | WHZ/LZY/LZ/TMZ/DZ families, applicable models, dimensions, machining, height adjustment, and bolt cautions | Representative LKA plate-seat selection in `LKA-Q-0015`; other families and custom machining/bolt details are accessory-fabrication context without a specified installation target |
| LKA-SI-033 | 57-58 / unnumbered | Sales addresses and network | TEXT + DRAWING | NON-TEST | Contact details, sales geography, and certification marks | Exclude; not durable LKA technical knowledge |

## 3. Question Statistics

- Total: 27
- FACT: 2
- SPEC_LOOKUP: 3
- TABLE: 7
- MODEL: 4
- CALCULATION: 1
- CHART: 2
- PROCEDURE: 5
- CAUTION: 3

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
`LKA0480-CR--` 的型号表示是否合法。

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
- P5 [5]: 正确说明 `C` 型可安装另购的直装式速度控制阀。
- P6 [5]: 正确给出推荐速度控制阀 BZL-B。
- P7 [15]: 正确说明 `R` 是从配管口正面观察时向右夹紧。
- P8 [10]: 正确说明空白动作确认字段表示无动作确认的标准型。
- P9 [10]: 正确说明空白选配字段表示无选配的标准型。
- P10 [5]: 明确判断 `LKA0480-CR--` 的字段顺序和取值合法。

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

- Binding: MODEL_FAMILY
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

- Binding: MODEL_FAMILY
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

- Binding: MODEL_FAMILY
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
- P6 [5]: 正确说明快换组件包含压板销。
- P7 [5]: 正确说明快换组件需另行购买，不随夹紧器本体交付。
- P8 [10]: 正确给出 LKA0480-A 对应 `LZK0480-W`。

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
- P2 [10]: 正确说明 `NBR` 表示一般用丁腈橡胶。
- P3 [10]: 正确说明 `90` 表示 A 型硬度 90。
- P4 [15]: 正确说明 `NBR-90` 对应旧材料识别符号 `1B`。
- P5 [15]: 正确说明 `P` 表示运动用。
- P6 [15]: 正确说明 `22A` 是公称号。
- P7 [10]: 正确说明末尾 `N` 是一般用品质等级。
- P8 [15]: 正确给出完整旧标示 `1BP22A`。

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

## LKA-Q-0017

**Type: CALCULATION**

### Target

- Binding: MODEL_FAMILY
- Product: LKA 油压杠杆式夹紧器
- Model / Scope: LKA0480 标准无动作确认型与 D/M/N/NC/NL/NR 动作确认型的夹紧力计算

### Question

LKA0480 在供油压力 `P = 5.0 MPa`、压板长度 `L = 60 mm` 时，分别计算
标准无动作确认型和带 D/M/N 动作确认型的夹紧力 `F`。结果以 kN 表示，
采用 `ROUND_HALF_UP` 保留两位小数；同时说明使用的两个公式系数。

### Standard Answer

标准无动作确认型使用 `F = 11.76 x P / L`，所以
`11.76 x 5.0 / 60 = 0.980 kN`，保留两位小数为 `0.98 kN`。

带 D/M/N/NC/NL/NR 动作确认型使用 `F = 9.20 x P / L`，所以
`9.20 x 5.0 / 60 = 0.766666... kN`，采用 `ROUND_HALF_UP` 保留两位
小数为 `0.77 kN`。在相同压力和压板长度下，本题的标准无动作确认型夹紧力
更大。

### Scoring Standard

- P1 [15]: 正确给出标准无动作确认型系数 11.76。
- P2 [15]: 正确计算标准型未舍入结果 0.980 kN。
- P3 [15]: 正确给出 D/M/N/NC/NL/NR 动作确认型系数 9.20。
- P4 [15]: 正确计算动作确认型未舍入结果 0.766666... kN。
- P5 [15]: 按 `ROUND_HALF_UP` 正确得到标准型最终结果 0.98 kN。
- P6 [15]: 按 `ROUND_HALF_UP` 正确得到动作确认型最终结果 0.77 kN。
- P7 [10]: 正确判断相同输入下标准无动作确认型夹紧力更大。

### Accepted Variants

- 乘号可写为 `x`、`×` 或 `*`。
- 未舍入结果可给出更多或更少循环小数位，但必须足以确定 0.77 kN 的舍入结果。

### Forbidden Errors

- 使用夹紧面积代替本页给定的夹紧力公式。
- 交换 11.76 与 9.20 两个系数的适用对象。
- 将压板长度 60 mm 换算成 0.06 m 后仍直接代入以 mm 定义的公式。
- 使用截断法把动作确认型结果写成 0.76 kN。

### Tolerance

- Deterministic calculation: inputs and units are exact; final values must be 0.98 kN and 0.77 kN under `ROUND_HALF_UP` to two decimal places.

### Source

- PDF: LKA_R01_2023KW_C1N.pdf
- Physical page: 8
- Printed page: 756
- Section: 规格 > 夹紧力计算公式
- Local scope path: LKA0480 列 > 标准无动作确认型公式；D/M/N 动作确认型公式
- Evidence type: FORMULA + TABLE
- Evidence: LKA0480 的两列公式分别给出 11.76 和 9.20 的系数，并定义 F 为 kN、P 为 MPa、L 为 mm；Gold 由 Decimal 脚本按指定舍入规则计算。

## LKA-Q-0018

**Type: CHART**

### Target

- Binding: MODEL_FAMILY
- Product: LKA 油压杠杆式夹紧器
- Model / Scope: LKA0480 标准无动作确认型夹紧力能力曲线

### Question

从 LKA0480 标准无动作确认型的夹紧力能力曲线读取：供油压力为 `4.0 MPa`、
压板长度为 `60 mm` 时，夹紧力约为多少 kN？

### Standard Answer

应选择 LKA0480 图中的 `L = 60` 曲线，在 `P = 4.0 MPa` 处读取约
`0.8 kN` 的夹紧力。

### Scoring Standard

- P1 [20]: 明确选择 LKA0480 标准无动作确认型曲线组。
- P2 [20]: 明确选择 `L = 60` 曲线。
- P3 [20]: 在横轴使用 `P = 4.0 MPa`。
- P4 [40]: 从纵轴读出约 0.8 kN，且结果落入规定图读容差。

### Accepted Variants

- `约 0.8 kN` 可写为容差范围内更精细的图读值。

### Forbidden Errors

- 使用 D/M/N 动作确认型曲线代替标准无动作确认型曲线。
- 使用 `L = 80` 或其他压板长度曲线。
- 将横轴压力或纵轴夹紧力的单位互换。
- 将异常输出力的灰色区域当作正常工作读数。

### Tolerance

- CHART: accept 0.70-0.90 kN for the visual read at P = 4.0 MPa and L = 60 mm.

### Source

- PDF: LKA_R01_2023KW_C1N.pdf
- Physical page: 9
- Printed page: 757
- Section: 能力曲线图（动作确认方式：无符号：标准型）
- Local scope path: LKA0480 图 > L=60 曲线 > P=4.0 MPa 交点
- Evidence type: CHART
- Evidence: Gold 直接由页面右侧 LKA0480 能力曲线的轴、L=60 曲线和交点进行视觉读取；公式仅用于独立合理性检查，不作为 Chart Gold 来源。

## LKA-Q-0019

**Type: PROCEDURE**

### Target

- Binding: MODEL_FAMILY
- Product: LKA-M/N 空气传感器动作确认型
- Model / Scope: LKA 的 M 板式连接与 N/NC/NL/NR 外配管空气传感器连接和安装控制

### Question

为 LKA-M/N 动作确认型配置空气传感器时，应采用什么推荐供气压力和推荐
传感器型号，每台传感器最多串联多少台夹紧器？同时说明排气口、压板标记
方向和 M 型 O 形密封圈润滑的关键安装要求。

### Standard Answer

推荐供气压力为 `0.2 MPa`。推荐空气传感器为 SMC `ISA3-G` 或 CKD
`GPS3-E`，每台传感器最多串联 4 台夹紧器。夹紧端和释放端排气口必须
向大气开放，并防止冷却液、切屑等异物进入。安装压板时，不得使活塞杆
标记相对夹紧器法兰标记处于反方向 180 度，否则不能正常检测。M 型板式
连接安装时，应在传感器 O 形密封圈上涂适量润滑脂；润滑不足可能造成
O 形圈扭曲或损坏，过量则可能堵塞检测孔并导致无法检测。

### Scoring Standard

- P1 [10]: 正确给出推荐供气压力 0.2 MPa。
- P2 [10]: 正确给出 SMC ISA3-G 或 CKD GPS3-E 推荐型号中的至少一个。
- P3 [15]: 正确说明每台传感器最多串联 4 台夹紧器。
- P4 [15]: 正确说明夹紧端和释放端排气口必须向大气开放。
- P5 [10]: 正确说明必须防止冷却液、切屑等异物进入排气口。
- P6 [15]: 正确说明活塞杆标记不得与法兰标记反向 180 度。
- P7 [5]: 正确说明 M 型 O 形密封圈需要涂适量润滑脂。
- P8 [5]: 正确说明润滑不足可能使 O 形密封圈扭曲或损坏。
- P9 [15]: 正确说明润滑脂过量可能堵塞检测孔并导致无法检测。

### Accepted Variants

- 同时给出 ISA3-G 和 GPS3-E，或仅给出其中一个完整推荐型号，均可接受。
- `最多 4 台` 可写为 `4 台以下（含 4 台）`。

### Forbidden Errors

- 将 0.2 MPa 写成液压夹紧压力而非空气传感器供气压力。
- 让排气口封闭或接入有背压的回路。
- 声称压板反向 180 度安装仍能可靠检测。
- 建议用大量润滑脂填满检测孔。

### Tolerance

- Exact pressure, connection limit, and installation controls are required.

### Source

- PDF: LKA_R01_2023KW_C1N.pdf
- Physical page: 27-28
- Printed page: 775-776
- Section: 空气传感器连接型 > 关于空气传感器 / 使用方面・施工方面的注意事项 / 空气传感器回路图
- Local scope path: 推荐供气压力和推荐传感器表；连接台数说明；排气口、压板标记和 M 型密封圈注意图；最多 4 台连接注记
- Evidence type: TEXT + TABLE + DRAWING + STATE_DIAGRAM
- Evidence: 第 775 页给出压力、型号、排气及安装控制，第 776 页的回路说明确认单传感器连接台数上限为 4 台。

## LKA-Q-0020

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: LKA 油压杠杆式夹紧器
- Model / Scope: LKA 系列设计、压板受力和本体安装的高后果注意事项

### Question

设计并安装 LKA 油压杠杆式夹紧器时，为避免误动作、活塞杆弯曲、夹紧器
损坏和安装故障，应遵守哪些关于夹紧/释放回路、压板受力、偏心量、夹紧面、
焊接飞溅和本体螺栓的要求？

### Standard Answer

- 严禁同时向夹紧侧和释放侧供给油压。
- 不得向活塞杆施加轴向以外的作用力。
- 压板承受偏心载荷时必须在容许偏心量范围内，且不得使用偏心压板。
- 夹紧倾斜工件时，应使工件夹紧面与夹紧器安装面保持平行。
- 用于焊接夹具时，必须保护活塞杆滑动面，避免焊接飞溅造成动作不良或漏油。
- 安装本体时必须使用全部安装螺栓孔，并按该型号规定的力矩紧固；过大力矩会导致基座塌陷或螺栓热粘等故障。

### Scoring Standard

- P1 [15]: 正确禁止同时向夹紧侧和释放侧供压。
- P2 [15]: 正确禁止向活塞杆施加非轴向力。
- P3 [10]: 正确要求偏心载荷处于容许偏心量范围。
- P4 [10]: 正确禁止使用偏心压板。
- P5 [15]: 正确要求夹紧面与安装面保持平行。
- P6 [15]: 正确要求保护活塞杆滑动面免受焊接飞溅。
- P7 [7]: 正确要求使用全部安装螺栓孔。
- P8 [7]: 正确要求按对应型号规定力矩紧固。
- P9 [6]: 正确说明过大紧固力矩会导致安装故障。

### Accepted Variants

- `焊接飞溅` 可写为 `焊渣` 或 `weld spatter`。
- `螺栓热粘` 可写为 `螺栓咬死`。

### Forbidden Errors

- 允许夹紧侧和释放侧同时供压。
- 允许通过活塞杆承担横向载荷。
- 将容许偏心量曲线当作可以任意超过的推荐值。
- 建议只使用部分安装螺栓孔或任意提高紧固力矩。

### Tolerance

- N/A

### Source

- PDF: LKA_R01_2023KW_C1N.pdf
- Physical page: 31
- Printed page: 943
- Section: 油压杠杆式夹紧器 > 注意事项 > 设计方面 / 压板设计 / 安装施工
- Local scope path: 回路设计禁令；活塞杆受力和偏心压板图；平行夹紧图；焊接夹具说明；本体安装说明
- Evidence type: TEXT + DRAWING + TABLE
- Evidence: 页面逐项给出同时供压、非轴向力、偏心、平行度、焊接飞溅和安装螺栓的禁止或强制要求，并在页面型号范围中包含 LKA。

## LKA-Q-0021

**Type: CHART**

### Target

- Binding: MODEL_FAMILY
- Product: LKA 油压杠杆式夹紧器
- Model / Scope: LKA0480 标准连接板、无 H 高强度选配的容许偏心量曲线

### Question

从 LKA0480 标准连接板的容许偏心量曲线读取：供油压力为 `5.0 MPa`、
压板长度为 `90 mm` 时，容许偏心量 `H` 约为多少 mm？

### Standard Answer

应选择 LKA0480 标准型图中的 `5 MPa` 曲线，在压板长度 `L = 90 mm`
处读取容许偏心量约 `14 mm`。

### Scoring Standard

- P1 [20]: 明确选择 LKA0480 标准连接板而非 H 高强度连接板曲线组。
- P2 [20]: 明确选择 `5 MPa` 曲线。
- P3 [20]: 在横轴使用压板长度 `L = 90 mm`。
- P4 [40]: 从纵轴读出约 14 mm，且结果落入规定图读容差。

### Accepted Variants

- `约 14 mm` 可写为容差范围内更精细的图读值。

### Forbidden Errors

- 使用 LKA0480-H 高强度连接板曲线代替标准曲线。
- 将 90 mm 当作容许偏心量而非压板长度。
- 选择 5 MPa 以外的压力曲线。
- 将曲线读数解释为可超过的推荐偏心量。

### Tolerance

- CHART: accept 13-15 mm for the visual read at P = 5.0 MPa and L = 90 mm.

### Source

- PDF: LKA_R01_2023KW_C1N.pdf
- Physical page: 13
- Printed page: 761
- Section: 容许偏心量曲线图（选配件：无符号：标准型）
- Local scope path: LKA0480 标准型图 > 5 MPa 曲线 > L=90 mm 交点
- Evidence type: CHART
- Evidence: Gold 由 LKA0480 标准型曲线的压板长度横轴、偏心量纵轴和 5 MPa 系列交点直接视觉读取；90 mm 不是离散表格列。

## LKA-Q-0022

**Type: PROCEDURE**

### Target

- Binding: PRODUCT_SERIES
- Product: LKA 油压杠杆式夹紧器
- Model / Scope: LKA 系列动作速度调整

### Question

调整 LKA 的动作速度时，全部动作时间应满足什么下限？调整前和调整过程中
应按什么顺序操作速度控制阀，过快动作会产生什么后果？

### Standard Answer

应将全部动作时间调整为超过 `1 秒`。调整前必须排净油压回路中的空气，
否则无法准确调整速度。开始调整时应把速度控制阀置于低速侧的小流量状态，
然后缓慢向高速侧的大流量方向增加。动作过快会加速各部件磨耗或造成损伤。

### Scoring Standard

- P1 [25]: 正确说明全部动作时间必须超过 1 秒。
- P2 [25]: 正确说明调整前必须排净回路空气。
- P3 [20]: 正确说明从低速侧的小流量状态开始。
- P4 [15]: 正确说明应缓慢向高速侧的大流量方向增加。
- P5 [15]: 正确说明过快会加速磨耗或造成部件损伤。

### Accepted Variants

- `超过 1 秒` 可写为 `大于 1 s`，但不可写成等于 1 秒即可。

### Forbidden Errors

- 在回路仍混有空气时进行最终速度设定。
- 从全开或最大流量开始试调。
- 将 1 秒写成最大允许动作时间。
- 为缩短节拍而允许瞬时高速冲击。

### Tolerance

- Exact lower-bound direction and adjustment sequence are required.

### Source

- PDF: LKA_R01_2023KW_C1N.pdf
- Physical page: 32
- Printed page: 944
- Section: 杠杆式夹紧器 > 注意事项 > 速度调整
- Local scope path: 速度调整条目 > 全部动作时间 / 排气 / 低速侧至高速侧调整
- Evidence type: TEXT
- Evidence: 页面要求全部动作时间超过 1 秒，调整前排气，并从低速小流量缓慢转向高速大流量，同时说明过快会造成磨耗或损伤。

## LKA-Q-0023

**Type: PROCEDURE**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK 液压系列通用安装
- Model / Scope: LKA_R01_2023KW_C1N.pdf :: physical page 33, printed page 945, piping cleanliness and hydraulic-circuit air bleeding

### Question

根据该 PDF 的液压系列通用安装页，配管施工时如何防止异物和密封带进入
回路？配管结束或油箱变空导致进气后，应如何完成排气并选择更有效的排气
位置？

### Standard Answer

投入使用前必须彻底清洁配管、管接头和配件油孔，并在清洁环境中正确施工；
密封带不得让碎片残留在回路内。需要排气时，先降低回路供油压力，再将离
夹紧器或支撑器最近的管接头螺母稍微旋松，左右摇动配管排出混有空气的
液压油，空气排净后重新紧固。优先在回路最高端和最末端附近排气；板式配管
应在回路最高端附近设置排气阀。

### Scoring Standard

- P1 [15]: 正确要求彻底清洁配管、管接头和配件油孔。
- P2 [15]: 正确要求避免密封带碎片或其他异物残留在回路内。
- P3 [15]: 正确说明排气前降低回路供油压力。
- P4 [15]: 正确说明稍微旋松最靠近夹紧器或支撑器的管接头螺母。
- P5 [8]: 正确说明摇动配管以排出含气液压油。
- P6 [7]: 正确说明空气排净后重新紧固接头。
- P7 [15]: 正确说明最高端和最末端附近是更有效的排气位置。
- P8 [10]: 正确说明板式配管应在回路最高端附近设置排气阀。

### Accepted Variants

- `左右摇动配管` 可写为 `轻轻移动配管使连接处松动并排气`。

### Forbidden Errors

- 在高压状态下直接大幅拆松管接头。
- 允许密封带碎片留在回路中。
- 排气后不重新紧固接头。
- 将最低点描述为唯一推荐排气位置。

### Tolerance

- N/A

### Source

- PDF: LKA_R01_2023KW_C1N.pdf
- Physical page: 33
- Printed page: 945
- Section: 安装施工方面的注意事项（油压系列通用）
- Local scope path: 配管前的处理 / 密封胶带的缠绕方法 / 排净油压回路内的空气
- Evidence type: TEXT + DRAWING
- Evidence: 页面连续给出清洁和密封带控制，并以图文步骤说明降低压力、松开最近接头、摇动排气、重新紧固及最高端/最末端排气位置。

## LKA-Q-0024

**Type: CAUTION**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK 液压夹紧器通用回路
- Model / Scope: LKA_R01_2023KW_C1N.pdf :: physical page 34, printed page 946, double-acting clamp speed-control circuit

### Question

根据该 PDF 的夹紧器速度控制回路页，复动夹紧器通常应如何设置夹紧侧和
释放侧的节流方式？为什么进油节流容易不稳定，同时使用单动和复动夹紧器时
应如何隔离回路，并应如何防止回油节流导致的回路压力上升？

### Standard Answer

复动夹紧器通常应在夹紧侧和释放侧都使用回油节流。进油节流容易受到回路
混入空气的影响，速度难以稳定控制；但产品专页明确规定的例外必须按专用
回路执行。单动和复动夹紧器同时使用时，原则上不要在同一回路中进行速度
控制，应将控制回路分开；通向油箱的管路存在背压时还可能造成动作次序异常。
回油节流时，供油量可能使动作中的回路压力上升，应预先用流量调节阀减少
供油量，尤其要防止压力超过顺序阀或动作确认压力开关的设定值。

### Scoring Standard

- P1 [20]: 正确说明复动夹紧器通常两侧均采用回油节流。
- P2 [15]: 正确说明进油节流受混入空气影响而难以稳定控制速度。
- P3 [10]: 正确保留产品专页规定例外，不将通用规则绝对化。
- P4 [20]: 正确说明单动和复动夹紧器原则上应分开速度控制回路。
- P5 [10]: 正确说明油箱回路背压可能造成动作次序异常。
- P6 [15]: 正确说明回油节流时供油量可能导致动作中回路压力上升。
- P7 [10]: 正确说明用流量调节阀减少供油量以限制压力上升。

### Accepted Variants

- `回油节流` 可写为 `meter-out`，`进油节流` 可写为 `meter-in`。

### Forbidden Errors

- 将复动夹紧器的通用设置写成两侧均进油节流。
- 忽略混入空气对进油节流稳定性的影响。
- 建议单动和复动夹紧器不加分析地共用同一速度控制回路。
- 将压力上升处理方式写成继续增加供油量。

### Tolerance

- N/A

### Source

- PDF: LKA_R01_2023KW_C1N.pdf
- Physical page: 34
- Printed page: 946
- Section: 夹紧器的速度控制回路及注意事项
- Local scope path: 复动夹紧器的速度控制回路；单动/复动混合回路；回油节流压力上升说明
- Evidence type: TEXT + STATE_DIAGRAM
- Evidence: 页面用文字和回路图规定复动两侧回油节流、说明进油节流的空气影响，并给出混合回路隔离、背压和供油量导致压力上升的控制要求。

## LKA-Q-0025

**Type: CAUTION**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK 液压/气动装置通用安全与维护
- Model / Scope: LKA_R01_2023KW_C1N.pdf :: physical page 35, printed page 947, operation safety and maintenance checklist

### Question

根据该 PDF 的通用注意事项，在操作、拆卸、重新启动和维护液压/气动夹紧
装置时，人员资格、能量隔离、运动部件、擅自改造、清洁检查和长期存放方面
有哪些关键要求？

### Standard Answer

操作和维护必须由具备相关知识与经验的人员进行。拆卸前必须落实防坠落和
防误动作措施，切断压力源和电源，并确认液压/气压回路压力为零；刚停机的
设备还须等待完全降温。重新启动前应检查螺栓等连接部位。严禁接触动作中的
夹紧器，也不得擅自解体或改造产品。维护时应定期清洁活塞杆、柱塞及定位
基准面，检查配管和紧固件松动、液压油老化、异音及动作顺畅性。产品应存放
在阴凉干燥处，解体大修应委托制造商。

### Scoring Standard

- P1 [15]: 正确要求由具备知识和经验的人员操作与维护。
- P2 [15]: 正确要求拆卸前落实防坠落和防误动作措施。
- P3 [15]: 正确要求切断压力源和电源并确认回路压力为零。
- P4 [5]: 正确说明刚停机设备需等待完全降温。
- P5 [5]: 正确说明重启前检查螺栓等连接部位。
- P6 [10]: 正确禁止接触动作中的夹紧器。
- P7 [10]: 正确禁止擅自解体或改造。
- P8 [5]: 正确要求定期清洁活塞杆、柱塞或定位基准面。
- P9 [10]: 正确要求检查松动、油液老化、异音或动作状态。
- P10 [5]: 正确说明产品应存放在阴凉干燥处。
- P11 [5]: 正确说明解体大修应委托制造商。

### Accepted Variants

- `压力为零` 可写为 `完全卸压`。
- `制造商` 可写为 `KOSMEK` 或 `本公司`。

### Forbidden Errors

- 仅切断电源而不切断压力源或确认零压。
- 在夹紧器动作时接触运动部位。
- 允许未经授权的产品改造。
- 将潮湿高温环境描述为推荐存放条件。

### Tolerance

- N/A

### Source

- PDF: LKA_R01_2023KW_C1N.pdf
- Physical page: 35
- Printed page: 947
- Section: 操作方面的注意事项 / 保养、检查
- Local scope path: 人员资格与安全措施；拆卸和重启；运动部件与改造；清洁、检查、存放和大修
- Evidence type: TEXT + DRAWING
- Evidence: 页面左栏给出操作与拆卸安全禁令，右栏给出零压、重启、清洁、松动/油液/动作检查、存放和制造商大修要求。

## LKA-Q-0026

**Type: PROCEDURE**

### Target

- Binding: MODEL_FAMILY
- Product: BZS 直装式顺序阀
- Model / Scope: BZS0100/BZS0200/BZS0300 回路设计、压力设定和投运控制

### Question

在 LKA 的 C 配管上使用 BZS 直装式顺序阀时，如何控制异物、供给流量、
回路空气和压力设定？多台夹紧器需要一致动作时如何调整，压力设定结束后
还必须完成什么锁定？

### Standard Answer

BZS 内部没有过滤网，必须防止切屑、密封带碎片等异物进入；内部零件一旦
受损，即使清除异物也可能无法恢复正常。过大的供给流量可能使顺序阀不能
按序动作，应根据夹紧器容量及配管直径、长度考虑流量控制。回路混入空气会
造成动作不良，投运前必须排气。阀门出厂时顺序压力未设定，应在实际回路中
使用压力表按需要设定。多台夹紧器需要一致动作时，应观察各夹紧器动作并
微调相应顺序阀。设定完成后，至少锁紧一侧旋转防止套件。

### Scoring Standard

- P1 [7]: 正确说明 BZS 内部没有过滤网。
- P2 [8]: 正确要求防止切屑、密封带碎片等异物进入。
- P3 [10]: 正确说明内部损伤后清除异物也可能无法恢复。
- P4 [15]: 正确说明过大供给流量可能阻止顺序动作。
- P5 [15]: 正确说明应按夹紧器容量和配管条件进行流量控制。
- P6 [10]: 正确说明回路必须排气。
- P7 [5]: 正确说明阀门出厂时顺序压力未设定。
- P8 [10]: 正确说明应使用压力表按实际回路设定压力。
- P9 [10]: 正确说明多台一致动作需观察动作并逐阀微调。
- P10 [10]: 正确说明设定后至少锁紧一侧旋转防止套件。

### Accepted Variants

- `旋转防止套件` 可写为 `防转锁定件`。
- `压力表` 可写为 `压力计`。

### Forbidden Errors

- 假定 BZS 自带过滤网，可容忍切屑或密封带碎片。
- 用增加供给流量解决不能顺序动作的问题。
- 不排气就进行最终压力和同步调整。
- 将出厂状态当作已完成压力设定，或设定后不锁定防转件。

### Tolerance

- N/A

### Source

- PDF: LKA_R01_2023KW_C1N.pdf
- Physical page: 52
- Printed page: 1272
- Section: 直装式顺序阀 > 注意事项 / 动作说明
- Local scope path: 过滤与异物；供给流量；排气；出厂未设定压力；多台同步微调；旋转防止套件
- Evidence type: TEXT + STATE_DIAGRAM
- Evidence: 页面注意事项明确无过滤网、流量和排气风险，并要求以压力表设定、逐阀微调及最终锁紧防转件；动作图说明顺序阀达到设定压力后的开闭次序。

## LKA-Q-0027

**Type: PROCEDURE**

### Target

- Binding: MODEL_FAMILY
- Product: LKA-M/N 空气传感器动作确认型
- Model / Scope: 单台 LKA 的夹紧确认口与释放确认口检测时序

### Question

根据 LKA 空气传感器流程图，从释放状态开始夹紧、以及从夹紧状态开始释放
时，夹紧确认口和释放确认口的检测气压分别在行程的什么阶段上升？空气
传感器何时输出对应端状态，设定压力变化会产生什么影响？

### Standard Answer

从释放状态开始夹紧时，夹紧确认口的检测气压在大部分夹紧行程保持较低，
接近夹紧端时迅速上升；超过空气传感器元件设定压力后，输出夹紧端确认。
从夹紧状态开始释放时，释放确认口的检测气压在大部分释放行程保持较低，
接近释放端时迅速上升；超过设定压力后，输出释放端确认。传感器输出发生的
具体行程位置会随传感器设定压力而变化，不能把图中的转折位置当成与设定
无关的固定机械位置。

### Scoring Standard

- P1 [20]: 正确说明夹紧确认口在大部分夹紧行程保持低压。
- P2 [10]: 正确说明接近夹紧端时夹紧确认口压力上升。
- P3 [10]: 正确说明越过设定压力后输出夹紧确认。
- P4 [20]: 正确说明释放确认口在大部分释放行程保持低压。
- P5 [10]: 正确说明接近释放端时释放确认口压力上升。
- P6 [10]: 正确说明越过设定压力后输出释放确认。
- P7 [20]: 正确说明输出行程位置会随传感器设定压力变化。

### Accepted Variants

- `低压` 可写为 `低于传感器元件设定压力`。
- `输出确认` 可写为 `传感器 ON`，但必须绑定到正确的夹紧端或释放端。

### Forbidden Errors

- 声称夹紧确认口在释放端输出夹紧确认。
- 声称释放确认口在夹紧端输出释放确认。
- 把供给气压水平直接当作全过程的检测输出压力。
- 声称设定压力变化不会改变输出发生的行程位置。

### Tolerance

- N/A

### Source

- PDF: LKA_R01_2023KW_C1N.pdf
- Physical page: 28
- Printed page: 776
- Section: 空气传感器流程图 > 连接 1 台夹紧器时
- Local scope path: 夹紧检测口气压曲线；释放检测口气压曲线；空气传感器元件设定压力；注意事项
- Evidence type: STATE_DIAGRAM + CHART
- Evidence: 两条带动作方向箭头的曲线分别显示对应检测口仅在接近夹紧端或释放端时越过设定压力；页下注明信号输出位置随传感器设定而异。
