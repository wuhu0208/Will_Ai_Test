---
schema_version: will-ai-question-bank/v1
source_pdf: VFH_R00_2023KW_C1N.pdf
source_sha256: 009d801e20543b0f2ad14cb10b0b0e4e86474c63548f6e4bac9af3f64696a772
source_pages: 22
question_bank_version: V1
product_scope: VFH
---

# VFH_R00_2023KW_C1N 题库与判定标准

## 1. Source Information

- Source PDF: `VFH_R00_2023KW_C1N.pdf`
- SHA-256: `009d801e20543b0f2ad14cb10b0b0e4e86474c63548f6e4bac9af3f64696a772`
- Physical pages: 22
- Product: KOSMEK VFH 大扩径量型通用扩径定位销
- Product printed pages: 1309-1322
- Included common-reference printed pages: 1725-1730, 1749-1750
- Evidence paths used for construction: PDF page images for visual truth and local OCR text for navigation; OCR alone is not treated as source truth.

## 2. Scope

### 2.1 Product and document scope

This bank covers the VFH hydraulic double-acting locating-pin series described by
this PDF: product purpose and mechanism, VFH1000/VFH2000/VFH3000 families,
D/C functional variants, legal model construction, specifications, workpiece-hole
requirements, selection calculations, displacement charts, dimensions, installation,
hydraulic circuits, cautions, maintenance, and applicable common hydraulic reference
material included in the source PDF.

Sales addresses and the sales-network map on physical pages 21-22 are retained in
the source inventory but excluded from product capability questions because they are
contact metadata rather than durable VFH technical knowledge.

### 2.2 Model Grammar

Canonical pattern:

`VFH<BodySize>00<DesignNo>-<HoleCode>-<Function>-<SeatHeight>`

Fields must appear in that order and use the following legal values.

| Field | Legal values | Meaning and constraint |
|---|---|---|
| BodySize | `1`, `2`, `3` | Selects the VFH1000, VFH2000, or VFH3000 family. |
| Fixed digits | `00` | Fixed characters shown in the model designation. |
| DesignNo | `0` | Product version/design number listed by this PDF. |
| HoleCode for BodySize `1` | `050`, `060`, `070`, `080` | Nominal workpiece holes are phi 5-8 mm. |
| HoleCode for BodySize `2` | `090`, `100`, `110`, `120`, `130` | Nominal workpiece holes are phi 9-13 mm. |
| HoleCode for BodySize `3` | `140`, `150` | Nominal workpiece holes are phi 14-15 mm. |
| Function | `D`, `C` | `D` is the datum pin for datum positioning; `C` is the diamond pin for one-direction positioning. |
| SeatHeight for BodySize `1` | `H20` | VFH1000 permits only 20 mm. |
| SeatHeight for BodySize `2` or `3` | `H15`, `H20`, `H25` | Selects 15, 20, or 25 mm. |

Positive grammar cases:

- `VFH1000-050-D-H20`
- `VFH2000-130-C-H25`
- `VFH3000-150-D-H15`

Negative grammar cases and reasons:

- `VFH1000-090-D-H20`: hole code `090` is outside the VFH1000 range.
- `VFH1000-050-C-H15`: VFH1000 permits only `H20`.
- `VFH2000-080-D-H20`: hole code `080` belongs to VFH1000.
- `VFH3000-130-D-H20`: hole code `130` belongs to VFH2000.
- `VFH2001-090-D-H20`: design number `1` is not listed.
- `VFH2000-090-X-H20`: function code `X` is not listed.
- `VFH2000-090-D-H30`: seat height `H30` is not listed.

### 2.3 Source-first inventory and initial dispositions

`HIGH` and `MEDIUM` items remain open until their mapped questions and later
construction audits are complete. The disposition column records current question
coverage or the next Work Package; it does not claim audit completion in advance.

| Inventory ID | Physical / printed page | Local scope | Evidence type | Priority | Testable object | Initial disposition |
|---|---|---|---|---|---|---|
| VFH-SI-001 | 1 / 1309 | Product introduction > locating principle | TEXT + DRAWING | HIGH | Expansion/retraction mechanism, zero-clearance positioning, and D/C pin roles | Covered by `VFH-Q-0002` and `VFH-Q-0006`; audit in WP4 |
| VFH-SI-002 | 1 / 1309 | Product introduction > family performance | TEXT | HIGH | VFH1000 30 um and VFH2000/3000 10 um repeatability | Covered by `VFH-Q-0003`; audit in WP4 |
| VFH-SI-003 | 2 / 1310 | Features > expansion amount and automation clearance | TEXT + DRAWING | HIGH | 1.1 mm expansion; VFH1000 0.7 mm; release-state clearance | Covered by `VFH-Q-0004`; automation handling remains WP3 |
| VFH-SI-004 | 2 / 1310 | Features > concentric nose measurement | TEXT + DRAWING | MEDIUM | VFH2000/3000 allow installation-spacing measurement; VFH1000 does not | Covered by `VFH-Q-0005`; audit in WP4 |
| VFH-SI-005 | 2 / 1310 | Features > air cleaning | TEXT + DRAWING | HIGH | Air path and contamination-prevention purpose | WP3 `PROCEDURE` / `CAUTION` |
| VFH-SI-006 | 3-5 / 1311-1313 | Application and system examples | DRAWING | MEDIUM | Robot/gantry handling and D/C two-pin fixture arrangement | Fixture arrangement covered by `VFH-Q-0006`; robot/gantry images are illustrative and need no separate numeric-swap question |
| VFH-SI-007 | 4 / 1312 | Product family comparison | TABLE + DRAWING | MEDIUM | VFL/VFM/VFH/VFJ/VFK class, control, pressure, action, and use-case differences | Nearest VFM/VFH selection comparison covered by `VFH-Q-0007`; non-VFH product rows are outside this product bank |
| VFH-SI-008 | 6 / 1314 | Necessary items > locating workpiece holes | TEXT + DRAWING | HIGH | Hole range phi 5-15 mm and the two tolerance bands | Covered by `VFH-Q-0008`; audit in WP4 |
| VFH-SI-009 | 6 / 1314 | Necessary items > VFH-C installation phase | TEXT + DRAWING | HIGH | VFH-D datum role, VFH-C Y-axis role, and required phase orientation | D/C roles covered by `VFH-Q-0006`; orientation procedure remains WP3 |
| VFH-SI-010 | 6 / 1314 | Necessary items > seating and workpiece clamp | TEXT + DRAWING | HIGH | No built-in Z datum seat and no clamping function | WP3 `CAUTION` |
| VFH-SI-011 | 7 / 1315 | Model designation | TABLE + DRAWING | HIGH | Field order, legal values, family/hole pairing, D/C, and seat-height grammar | Covered by `VFH-Q-0001` and `VFH-Q-0009`; grammar validation remains WP4 |
| VFH-SI-012 | 7 / 1315 | Specification table | TABLE | HIGH | Repeatability, eccentricity, expansion force, shear load, capacity, oil volume, pressure, temperature, and fluid | Covered by `VFH-Q-0003` and `VFH-Q-0010`-`VFH-Q-0014`; audit in WP4 |
| VFH-SI-013 | 8 / 1316 | Workpiece weight formula > horizontal mounting | FORMULA | HIGH | Weight bound using expansion force, efficiency, friction coefficient, and 9.8 | WP3 `CALCULATION` |
| VFH-SI-014 | 8 / 1316 | Workpiece weight formula > vertical mounting | FORMULA | HIGH | Weight bound using expansion force, 9.8, and efficiency | WP3 `CALCULATION` |
| VFH-SI-015 | 8 / 1316 | Shear load/displacement > VFH1000 | CHART | HIGH | Visual displacement reads for 050/060/070/080 series | WP3 `CHART` |
| VFH-SI-016 | 8 / 1316 | Shear load/displacement > VFH2000 | CHART | HIGH | Visual displacement reads for 090/100/110/120/130 series | WP3 `CHART` |
| VFH-SI-017 | 8 / 1316 | Shear load/displacement > VFH3000 | CHART | HIGH | Visual displacement reads for 140/150 series | WP3 `CHART` |
| VFH-SI-018 | 9-10 / 1317-1318 | VFH1000 outline and mounting dimensions | DRAWING + TABLE | HIGH | Released/full-stroke geometry, workpiece-hole machining, mounting ports, dimensions, and mass | Representative selection covered by `VFH-Q-0015`; audit in WP4 |
| VFH-SI-019 | 11-12 / 1319-1320 | VFH2000/3000 outline and mounting dimensions | DRAWING + TABLE | HIGH | Released/full-stroke geometry, workpiece-hole machining, mounting ports, dimensions, and mass | Representative selection covered by `VFH-Q-0016`; audit in WP4 |
| VFH-SI-020 | 9-12 / 1317-1320 | Installation notes attached to dimension drawings | TEXT + DRAWING | HIGH | Bolt class, washer prohibition, O-ring order, lifting, port placement, and hole-depth risks | WP3 `PROCEDURE` / `CAUTION` |
| VFH-SI-021 | 13 / 1321 | Design cautions > pressure, circuit, air, clamp, phase, seat | TEXT + DRAWING | HIGH | Preconditions and failure consequences for core fixture design | WP3 `CAUTION` |
| VFH-SI-022 | 13 / 1321 | Design cautions > vertical use and tilt | TEXT + DRAWING | HIGH | Pre-clamping, wear checks, 4/100-5/100 tilt limit, and rough guide pin | WP3 `CAUTION` / `PROCEDURE` |
| VFH-SI-023 | 13 / 1321 | Design cautions > wall, spacing, and hole depth | TEXT + DRAWING | HIGH | Thin-wall deformation, eccentricity-aware spacing, and insufficient-expansion/damage risk | WP3 `CAUTION` |
| VFH-SI-024 | 14 / 1322 | Installation > fluid, cleaning, tape, bolts, O-ring | TEXT + TABLE + DRAWING | HIGH | Fluid selection, contamination control, tape practice, 6.3 N-m bolt torque, and seal installation | WP3 `PROCEDURE` / `CAUTION` |
| VFH-SI-025 | 14 / 1322 | Hydraulic reference circuits | STATE_DIAGRAM + TEXT | HIGH | VFH-before-actuator sequence, independent/shared circuits, back-pressure check valve, and surge avoidance | WP3 `PROCEDURE` / `CAUTION` |
| VFH-SI-026 | 15 / 1725 | Common hydraulic appendix > oil and air bleeding | TABLE + PROCEDURE | MEDIUM | ISO-VG-32 examples and the five-step air-bleeding process | WP3 `TABLE` / `PROCEDURE`; bind as `DOCUMENT_COMMON` |
| VFH-SI-027 | 16 / 1726 | Common hydraulic appendix > speed control | STATE_DIAGRAM + TEXT | MEDIUM | Single/double-acting meter-in/meter-out circuit constraints | WP3 `PROCEDURE`; bind as `DOCUMENT_COMMON` |
| VFH-SI-028 | 17 / 1727 | Common hydraulic appendix > operation safety | TEXT | HIGH | Qualified operation, zero-energy disassembly, pinch avoidance, and no modification | WP3 `CAUTION`; bind as `DOCUMENT_COMMON` |
| VFH-SI-029 | 17 / 1727 | Common hydraulic appendix > maintenance | TEXT | HIGH | Cleaning, datum-surface care, air bleeding, fastening, oil, sound/motion, storage, and overhaul | WP3 `PROCEDURE`; bind as `DOCUMENT_COMMON` |
| VFH-SI-030 | 18 / 1728 | Common hydraulic appendix > warranty | TEXT | LOW | Warranty term, coverage, and exclusions | Exclude from core capability bank; low-value commercial policy |
| VFH-SI-031 | 19 / 1729 | Common appendix > surface roughness notation | TABLE | MEDIUM | 2021 old/new JIS notation mapping | Covered by `VFH-Q-0017`; audit in WP4 |
| VFH-SI-032 | 20 / 1730 | Common appendix > O-ring notation | TABLE + MODEL | MEDIUM | New/old notation mapping and field meanings | Covered by `VFH-Q-0018`; audit in WP4 |
| VFH-SI-033 | 21-22 / 1749-1750 | Sales addresses and network | TEXT + DRAWING | NON-TEST | Contact details and geographic sales map | Exclude; not durable VFH technical knowledge |

## 3. Question Statistics

- Total: 18
- FACT: 3
- SPEC_LOOKUP: 5
- MODEL: 3
- TABLE: 7

## 4. Questions

## VFH-Q-0001

**Type: MODEL**

### Target

- Binding: EXACT_MODEL
- Product: VFH 大扩径量型通用扩径定位销
- Model / Scope: VFH2000-090-D-H20

### Question

请按 PDF 的型号字段顺序，解读 `VFH2000-090-D-H20` 的主体尺寸、设计编号、
工件孔径符号及其孔公差、功能分类和着座高度，并判断该字段组合是否合法。

### Standard Answer

该型号的主体尺寸为 `2`，即 VFH2000；设计编号为 `0`；工件孔径符号 `090`
表示公称孔径 phi 9 mm，孔公差为 +0.7/-0.3 mm；`D` 表示用于基准定位的
基准销；`H20` 表示着座高度 20 mm。VFH2000 的合法孔径符号包含 `090`，
功能代码 `D` 合法，且 VFH2000 可选择 `H20`，所以该组合合法。

### Scoring Standard

- P1 [15]: 正确识别主体尺寸 `2` 对应 VFH2000。
- P2 [10]: 正确识别设计编号为 `0`。
- P3 [10]: 正确识别孔径符号 `090` 表示公称孔径 phi 9 mm。
- P4 [10]: 正确给出 phi 9 mm 孔的公差为 +0.7/-0.3 mm。
- P5 [15]: 正确说明 `D` 是用于基准定位的基准销。
- P6 [15]: 正确说明 `H20` 是 20 mm 着座高度。
- P7 [10]: 正确确认 VFH2000 与孔径符号 `090` 的组合合法。
- P8 [5]: 正确确认功能代码 `D` 合法。
- P9 [5]: 正确确认 VFH2000 可选择 `H20`。
- P10 [5]: 明确得出完整字段组合合法的结论。

### Accepted Variants

- `phi 9 mm` 可写为 `φ9 mm`、`Φ9 mm` 或 `直径 9 mm`。
- `基准销` 可表述为 `基准定位用销`，但不得改变其基准定位含义。
- 公差可等价写为上偏差 `+0.7 mm`、下偏差 `-0.3 mm`。

### Forbidden Errors

- 将 `D` 解释为菱形销或单个方向定位用销。
- 将 `090` 的孔公差写成 `±0.3 mm`。
- 将 `H20` 解释为产品自带着座面，而不是型号指定的着座高度。
- 在任一字段不合法时仍判定完整型号合法。

### Tolerance

- Exact source values and units are required; no numerical tolerance.

### Source

- PDF: VFH_R00_2023KW_C1N.pdf
- Physical page: 7
- Printed page: 1315
- Section: 型号表示 / 规格
- Local scope path: 型号表示 > VFH2000-090-D-H20 字段图；工件孔径表 > 090；功能分类；着座高度
- Evidence type: TABLE
- Evidence: 型号表示图按主体尺寸、设计编号、工件孔径、功能分类、着座高度排列字段；同页表格将 VFH2000 与 090 绑定，定义 090 为 phi 9 mm、+0.7/-0.3 mm，D 为基准销，H20 为 20 mm。

## VFH-Q-0002

**Type: FACT**

### Target

- Binding: PRODUCT_SERIES
- Product: VFH 大扩径量型通用扩径定位销
- Model / Scope: VFH1000 / VFH2000 / VFH3000 operating principle

### Question

VFH 扩径定位销在扩径状态和缩径状态下，定位销与工件基准孔的间隙分别
处于什么状态，各自对应什么用途？

### Standard Answer

扩径时，定位销与工件基准孔的间隙为零，用于高精度定位。缩径时，定位销
与工件孔之间保留足够间隙，用于顺利搬入、搬出或更换工件。

### Scoring Standard

- P1 [25]: 正确说明扩径时定位销与工件基准孔的间隙为零。
- P2 [25]: 正确说明扩径状态用于高精度定位。
- P3 [25]: 正确说明缩径时保留足够间隙。
- P4 [25]: 正确说明缩径状态便于搬入、搬出或更换工件。

### Accepted Variants

- `间隙为零` 可表述为 `零间隙`。
- `搬入、搬出` 可表述为 `装卸`，但必须保留缩径后提供间隙的含义。

### Forbidden Errors

- 声称扩径状态仍保留定位间隙。
- 声称缩径状态用于夹紧工件。

### Tolerance

- N/A

### Source

- PDF: VFH_R00_2023KW_C1N.pdf
- Physical page: 1
- Printed page: 1309
- Section: 所谓扩径定位销 / 定位销的扩缩径功能
- Local scope path: 产品介绍 > 定位销的扩缩径功能 > 扩径时与缩径时
- Evidence type: TEXT
- Evidence: 扩径时定位销与工件基准孔的间隙为零并实现高精度定位；缩径时确保足够间隙以便搬入、搬出和更换工件。

## VFH-Q-0003

**Type: SPEC_LOOKUP**

### Target

- Binding: PRODUCT_SERIES
- Product: VFH 大扩径量型通用扩径定位销
- Model / Scope: VFH1000 / VFH2000 / VFH3000 repeatability comparison

### Question

分别给出 VFH1000、VFH2000 和 VFH3000 的重复定位精度，并说明该精度的
规定测量条件。

### Standard Answer

VFH1000 的重复定位精度为 30 um；VFH2000 和 VFH3000 均为 10 um。该指标
表示在同一条件、无载荷时的重复定位精度。

### Scoring Standard

- P1 [30]: 正确给出 VFH1000 的重复定位精度为 30 um。
- P2 [30]: 正确给出 VFH2000 的重复定位精度为 10 um。
- P3 [30]: 正确给出 VFH3000 的重复定位精度为 10 um。
- P4 [10]: 正确说明测量条件为同一条件且无载荷。

### Accepted Variants

- `um` 可写为 `μm`。
- 30 um 和 10 um 可分别写为 0.03 mm 和 0.01 mm。

### Forbidden Errors

- 将 VFH1000 的 30 um 套用于 VFH2000 或 VFH3000。
- 将该指标表述为承受额定载荷时的定位精度。

### Tolerance

- Exact source values and units are required; no numerical tolerance.

### Source

- PDF: VFH_R00_2023KW_C1N.pdf
- Physical page: 7
- Printed page: 1315
- Section: 规格
- Local scope path: 规格表 > 重复定位精度；注意事项 1
- Evidence type: TABLE
- Evidence: 规格表列出 VFH1000 为 0.03 mm、VFH2000/3000 为 0.01 mm，并在注 1 定义为同一条件下无载荷时的重复定位精度。

## VFH-Q-0004

**Type: SPEC_LOOKUP**

### Target

- Binding: MODEL_FAMILY
- Product: VFH 大扩径量型通用扩径定位销
- Model / Scope: VFH1000 versus VFH2000 / VFH3000 expansion amount

### Question

VFH 系列的标准扩径量是多少，VFH1000 的扩径量例外是多少？

### Standard Answer

VFH 系列标示的标准扩径量为 1.1 mm；选择 VFH1000 时，扩径量为 0.7 mm。

### Scoring Standard

- P1 [50]: 正确给出标准扩径量为 1.1 mm。
- P2 [50]: 正确给出 VFH1000 的扩径量为 0.7 mm。

### Accepted Variants

- 可明确写成 VFH2000/3000 为 1.1 mm、VFH1000 为 0.7 mm。

### Forbidden Errors

- 将 1.1 mm 和 0.7 mm 对调。
- 声称所有 VFH 主体尺寸的扩径量都相同。

### Tolerance

- Exact source values and units are required; no numerical tolerance.

### Source

- PDF: VFH_R00_2023KW_C1N.pdf
- Physical page: 2
- Printed page: 1310
- Section: 特点 > 大的扩径量
- Local scope path: 特点 > 大的扩径量 > VFH1000 例外
- Evidence type: TEXT
- Evidence: 特点页标示扩径量 1.1 mm，并注明选择 VFH1000 时为 0.7 mm。

## VFH-Q-0005

**Type: FACT**

### Target

- Binding: MODEL_FAMILY
- Product: VFH 大扩径量型通用扩径定位销
- Model / Scope: VFH1000 versus VFH2000 / VFH3000 installation-position measurement

### Question

哪些 VFH 主体尺寸可利用前端同芯部位检查安装间距精度？VFH1000 是否支持
这种测量？

### Standard Answer

VFH2000 和 VFH3000 可利用前端同芯部位测量安装间距精度；VFH1000 不支持
这种测量。

### Scoring Standard

- P1 [40]: 正确说明 VFH2000 支持通过前端同芯部位测量安装间距精度。
- P2 [40]: 正确说明 VFH3000 支持通过前端同芯部位测量安装间距精度。
- P3 [20]: 正确说明 VFH1000 不支持这种测量。

### Accepted Variants

- `安装间距精度` 可写为 `安装位置间距精度`。

### Forbidden Errors

- 声称 VFH1000 支持前端同芯部位测量。

### Tolerance

- N/A

### Source

- PDF: VFH_R00_2023KW_C1N.pdf
- Physical page: 2
- Printed page: 1310
- Section: 特点 > 便于检查安装的位置精度
- Local scope path: 特点 > 前端同芯部位 > 测定间距精度
- Evidence type: TEXT
- Evidence: 页面说明可通过前端同芯部位测量间距精度，并明确注明选择 VFH1000 时无法测量。

## VFH-Q-0006

**Type: FACT**

### Target

- Binding: PRODUCT_SERIES
- Product: VFH 大扩径量型通用扩径定位销
- Model / Scope: VFH system reference fixture arrangement

### Question

在 PDF 的 VFH 系统参考范例中，两只定位销、工件夹紧器和粗导销分别承担
什么角色？

### Standard Answer

VFH-D 相当于圆销，承担基准定位；VFH-C 相当于削边销，承担单个方向定位；
涨紧下拉式夹紧器用于固定工件；粗导销用于工件搬入、搬出时的粗导向。

### Scoring Standard

- P1 [30]: 正确说明 VFH-D 相当于圆销并承担基准定位。
- P2 [30]: 正确说明 VFH-C 相当于削边销并承担单个方向定位。
- P3 [20]: 正确说明涨紧下拉式夹紧器用于固定工件。
- P4 [20]: 正确说明粗导销用于搬入、搬出时的粗导向。

### Accepted Variants

- `削边销` 可写为 `菱形销`，但必须保留单个方向定位含义。
- `粗导向` 可写为 `预导向`。

### Forbidden Errors

- 对调 VFH-D 和 VFH-C 的定位角色。
- 声称 VFH 定位销本身完成工件夹紧。

### Tolerance

- N/A

### Source

- PDF: VFH_R00_2023KW_C1N.pdf
- Physical page: 5-6
- Printed page: 1313-1314
- Section: 系统参考范例 / 必要事项
- Local scope path: 系统参考范例 > 夹具俯视图与工件侧视图 > 标号 1-5；必要事项 > 关于工件夹紧器的设置
- Evidence type: DRAWING + TEXT
- Evidence: 系统图将 VFH-D 标为相当于圆销、VFH-C 标为相当于削边销，并标出涨紧下拉式工件夹紧器和粗导销；相邻必要事项明确工件由另设夹紧器固定。

## VFH-Q-0007

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK 液压扩径定位销
- Model / Scope: VFM high-precision family versus VFH general-purpose family

### Question

按产品种类比较表，对比 VFM 与 VFH 的类别、重复定位精度、控制方式和使用
压力范围。

### Standard Answer

VFM 属于高精度型，重复定位精度 3 um，采用油压定位/油压释放的复动控制，
使用压力范围 2.5-7 MPa。VFH 属于通用型，VFH1000 的重复定位精度 30 um、
VFH2000/3000 为 10 um，同样采用油压定位/油压释放的复动控制，使用压力
范围 1.5-7 MPa。

### Scoring Standard

- P1 [10]: 正确说明 VFM 属于高精度型。
- P2 [15]: 正确给出 VFM 重复定位精度为 3 um。
- P3 [10]: 正确说明 VFM 为油压定位/油压释放的复动控制。
- P4 [15]: 正确给出 VFM 使用压力范围为 2.5-7 MPa。
- P5 [10]: 正确说明 VFH 属于通用型。
- P6 [10]: 正确给出 VFH1000 重复定位精度为 30 um。
- P7 [10]: 正确给出 VFH2000/3000 重复定位精度为 10 um。
- P8 [10]: 正确说明 VFH 为油压定位/油压释放的复动控制。
- P9 [10]: 正确给出 VFH 使用压力范围为 1.5-7 MPa。

### Accepted Variants

- `复动` 可写为 `双作用`，但必须明确定位与释放均由油压驱动。
- `um` 可写为 `μm`。

### Forbidden Errors

- 将 VFM 的 2.5-7 MPa 压力范围套用于 VFH。
- 声称 VFH 为高精度型或将 VFH1000 的精度写成 10 um。

### Tolerance

- Exact source values and units are required; no numerical tolerance.

### Source

- PDF: VFH_R00_2023KW_C1N.pdf
- Physical page: 4
- Printed page: 1312
- Section: 产品种类
- Local scope path: 产品种类比较表 > VFM 列与 VFH 列 > 类别、重复定位精度、控制、使用压力范围
- Evidence type: TABLE
- Evidence: 比较表将 VFM 列为高精度型、3 um、复动、2.5-7 MPa；将 VFH 列为通用型、VFH1000 30 um、VFH2000/3000 10 um、复动、1.5-7 MPa。

## VFH-Q-0008

**Type: SPEC_LOOKUP**

### Target

- Binding: PRODUCT_SERIES
- Product: VFH 大扩径量型通用扩径定位销
- Model / Scope: Workpiece locating-hole range and tolerance bands

### Question

VFH 定位用工件孔的公称孔径指定范围是什么？phi 5-8 mm 与 phi 9-15 mm
两段分别采用什么孔公差？

### Standard Answer

公称孔径指定范围为 phi 5-15 mm，按 1 mm 递增。phi 5-8 mm 的孔公差为
±0.3 mm；phi 9-15 mm 的孔公差为 +0.7/-0.3 mm。

### Scoring Standard

- P1 [20]: 正确给出指定范围为 phi 5-15 mm 且按 1 mm 递增。
- P2 [40]: 正确给出 phi 5-8 mm 的孔公差为 ±0.3 mm。
- P3 [40]: 正确给出 phi 9-15 mm 的孔公差为 +0.7/-0.3 mm。

### Accepted Variants

- `phi` 可写为 `φ`、`Φ` 或 `直径`。
- `按 1 mm 递增` 可写为 `单位为 1 mm` 或列出 5、6、...、15 mm。

### Forbidden Errors

- 将 phi 9-15 mm 的非对称公差写成 ±0.3 mm。
- 声称可直接指定本范围之外的标准孔径符号。

### Tolerance

- Exact source tolerance bands and units are required; no additional numerical tolerance.

### Source

- PDF: VFH_R00_2023KW_C1N.pdf
- Physical page: 6
- Printed page: 1314
- Section: 必要事项 > 关于定位用工件孔
- Local scope path: 必要事项 > 1 关于定位用工件孔 > 指定范围与对象孔公差
- Evidence type: TEXT
- Evidence: 页面规定工件孔径指定范围为 phi 5-15 mm、单位 1 mm，并分别列出 phi 5-8 为 ±0.3 mm、phi 9-15 为 +0.7/-0.3 mm。

## VFH-Q-0009

**Type: MODEL**

### Target

- Binding: PRODUCT_SERIES
- Product: VFH 大扩径量型通用扩径定位销
- Model / Scope: Model grammar family boundaries and function codes

### Question

下列四个型号中，哪一个符合 PDF 的 VFH 型号语法？指出合法项，并分别说明
其余三项不合法的字段。

- A. `VFH1000-090-D-H20`
- B. `VFH2000-130-C-H25`
- C. `VFH3000-130-D-H20`
- D. `VFH2000-090-X-H20`

### Standard Answer

合法项是 B：`VFH2000-130-C-H25`。A 不合法，因为孔径符号 `090` 不属于
VFH1000；C 不合法，因为孔径符号 `130` 属于 VFH2000 而不属于 VFH3000；
D 不合法，因为功能代码只允许 `D` 或 `C`，不允许 `X`。

### Scoring Standard

- P1 [25]: 正确识别 B 为唯一合法项。
- P2 [25]: 正确指出 A 的 `090` 与 VFH1000 主体尺寸不匹配。
- P3 [25]: 正确指出 C 的 `130` 与 VFH3000 主体尺寸不匹配。
- P4 [25]: 正确指出 D 的功能代码 `X` 不在 `D`/`C` 合法集合内。

### Accepted Variants

- 对 A 可说明 `090` 属于 VFH2000 选择范围。
- 对 C 可说明 VFH3000 仅接受 `140`、`150`。

### Forbidden Errors

- 将 A、C 或 D 判定为合法。
- 仅凭示例 allowlist 判定而不指出字段约束。

### Tolerance

- N/A

### Source

- PDF: VFH_R00_2023KW_C1N.pdf
- Physical page: 7
- Printed page: 1315
- Section: 型号表示
- Local scope path: 型号表示 > 主体尺寸选择范围、工件孔径符号、功能分类、着座高度
- Evidence type: TABLE
- Evidence: 型号表将 VFH1000 绑定 050-080、VFH2000 绑定 090-130、VFH3000 绑定 140-150，并仅列出 D/C 两种功能代码。

## VFH-Q-0010

**Type: TABLE**

### Target

- Binding: EXACT_MODEL
- Product: VFH 大扩径量型通用扩径定位销
- Model / Scope: VFH2000-120-D-H20 specification row

### Question

对 `VFH2000-120-D-H20`，分别给出 1.5 MPa、5.0 MPa、7.0 MPa 时的扩径力，
以及该孔径符号对应的容许剪切载荷。

### Standard Answer

扩径力分别为：1.5 MPa 时 90 N、5.0 MPa 时 340 N、7.0 MPa 时 480 N。
孔径符号 `120` 对应的容许剪切载荷为 1000 N。

### Scoring Standard

- P1 [25]: 正确给出 1.5 MPa 时扩径力为 90 N。
- P2 [25]: 正确给出 5.0 MPa 时扩径力为 340 N。
- P3 [25]: 正确给出 7.0 MPa 时扩径力为 480 N。
- P4 [25]: 正确给出容许剪切载荷为 1000 N。

### Accepted Variants

- 可用表格或按压力升序列出数值。

### Forbidden Errors

- 将 VFH3000 的 160/580/810 N 扩径力套用于本型号。
- 将扩径力与容许剪切载荷混为同一物理量。

### Tolerance

- Exact source values and units are required; no numerical tolerance.

### Source

- PDF: VFH_R00_2023KW_C1N.pdf
- Physical page: 7
- Printed page: 1315
- Section: 规格
- Local scope path: 规格表 > 工件孔径符号 120 列 > 扩径力 1.5/5.0/7.0 MPa 与容许剪切载荷
- Evidence type: TABLE
- Evidence: 120 列按压力列出扩径力 90 N、340 N、480 N，并列出容许剪切载荷 1000 N。

## VFH-Q-0011

**Type: SPEC_LOOKUP**

### Target

- Binding: PRODUCT_SERIES
- Product: VFH 大扩径量型通用扩径定位销
- Model / Scope: Common hydraulic pressure and fluid specifications

### Question

给出 VFH 系列的使用压力范围、耐压和规定使用流体。

### Standard Answer

使用压力范围为 1.5-7.0 MPa；耐压为 10.5 MPa；使用流体为相当于
ISO-VG-32 粘度等级的普通液压油。

### Scoring Standard

- P1 [30]: 正确给出使用压力范围为 1.5-7.0 MPa。
- P2 [30]: 正确给出耐压为 10.5 MPa。
- P3 [40]: 正确说明使用流体为相当于 ISO-VG-32 粘度等级的普通液压油。

### Accepted Variants

- `普通液压油` 可写为 `一般液压油`，但必须保留 ISO-VG-32 等级。

### Forbidden Errors

- 将耐压 10.5 MPa 当作连续使用压力上限。
- 将使用压力范围写成 2.5-7 MPa。

### Tolerance

- Exact source values and units are required; no numerical tolerance.

### Source

- PDF: VFH_R00_2023KW_C1N.pdf
- Physical page: 7
- Printed page: 1315
- Section: 规格
- Local scope path: 规格表 > 使用压力范围、耐压、使用流体
- Evidence type: TABLE
- Evidence: 规格表列出 1.5-7.0 MPa 使用压力、10.5 MPa 耐压和相当于 ISO-VG-32 粘度等级的普通液压油。

## VFH-Q-0012

**Type: SPEC_LOOKUP**

### Target

- Binding: PRODUCT_SERIES
- Product: VFH 大扩径量型通用扩径定位销
- Model / Scope: Common air-cleaning pressure and temperature specifications

### Question

给出 VFH 系列的推荐喷气清洁用气压和使用温度范围。

### Standard Answer

推荐喷气清洁用气压为 0.2-0.3 MPa；使用温度范围为 0-70 °C。

### Scoring Standard

- P1 [50]: 正确给出推荐喷气清洁用气压为 0.2-0.3 MPa。
- P2 [50]: 正确给出使用温度范围为 0-70 °C。

### Accepted Variants

- 温度单位可写为 `℃`。

### Forbidden Errors

- 将喷气清洁气压写成液压使用压力范围。
- 遗漏任一范围的单位。

### Tolerance

- Exact source values and units are required; no numerical tolerance.

### Source

- PDF: VFH_R00_2023KW_C1N.pdf
- Physical page: 7
- Printed page: 1315
- Section: 规格
- Local scope path: 规格表 > 推荐喷气清洁用气压、使用温度范围
- Evidence type: TABLE
- Evidence: 规格表列出推荐喷气清洁用气压 0.2-0.3 MPa、使用温度范围 0-70 °C。

## VFH-Q-0013

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: VFH 大扩径量型通用扩径定位销
- Model / Scope: VFH-C allowable eccentricity by family and hole limit

### Question

对 C 型菱形销，分别给出 VFH1000 与 VFH2000/3000 在最小孔和最大孔时的
容许偏心量。

### Standard Answer

VFH1000 在最小孔和最大孔时均为 ±0.10 mm。VFH2000/3000 在最小孔时为
±0.05 mm，在最大孔时为 ±0.55 mm。

### Scoring Standard

- P1 [25]: 正确给出 VFH1000 最小孔时为 ±0.10 mm。
- P2 [25]: 正确给出 VFH1000 最大孔时为 ±0.10 mm。
- P3 [25]: 正确给出 VFH2000/3000 最小孔时为 ±0.05 mm。
- P4 [25]: 正确给出 VFH2000/3000 最大孔时为 ±0.55 mm。

### Accepted Variants

- 可将 VFH2000 和 VFH3000 分别列出相同数值。

### Forbidden Errors

- 将最小孔与最大孔的 VFH2000/3000 数值对调。
- 将这些容许偏心量套用于 D 型基准销。

### Tolerance

- Exact source tolerance values and units are required; no additional numerical tolerance.

### Source

- PDF: VFH_R00_2023KW_C1N.pdf
- Physical page: 7
- Printed page: 1315
- Section: 规格
- Local scope path: 规格表 > 容许偏心量（C：菱形销）> 最小孔时与最大孔时
- Evidence type: TABLE
- Evidence: 表中 VFH1000 两行均为 ±0.10 mm；VFH2000/3000 的最小孔为 ±0.05 mm、最大孔为 ±0.55 mm。

## VFH-Q-0014

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: VFH 大扩径量型通用扩径定位销
- Model / Scope: VFH1000 / VFH2000 / VFH3000 empty-stroke oil volumes

### Question

按规格表中的“释放时”和“夹紧时”两行，比较 VFH1000、VFH2000、VFH3000
空动作时的油量。

### Standard Answer

VFH1000：释放时 0.16 cm3，夹紧时 0.07 cm3；VFH2000：释放时 0.21 cm3，
夹紧时 0.10 cm3；VFH3000：释放时 0.40 cm3，夹紧时 0.16 cm3。表中的
“夹紧时”对 VFH 表示定位/扩径侧动作，不表示 VFH 具有工件夹紧功能。

### Scoring Standard

- P1 [15]: 正确给出 VFH1000 释放时油量为 0.16 cm3。
- P2 [15]: 正确给出 VFH1000 夹紧时油量为 0.07 cm3。
- P3 [15]: 正确给出 VFH2000 释放时油量为 0.21 cm3。
- P4 [15]: 正确给出 VFH2000 夹紧时油量为 0.10 cm3。
- P5 [20]: 正确给出 VFH3000 释放时油量为 0.40 cm3。
- P6 [20]: 正确给出 VFH3000 夹紧时油量为 0.16 cm3。

### Accepted Variants

- `cm3` 可写为 `cm³`。
- `夹紧时` 可写为 `定位时` 或 `扩径时`，但不得误解为产品具有工件夹紧功能。

### Forbidden Errors

- 对调释放侧和定位侧油量。
- 将油量单位写成流量单位。

### Tolerance

- Exact source values and units are required; no numerical tolerance.

### Source

- PDF: VFH_R00_2023KW_C1N.pdf
- Physical page: 7
- Printed page: 1315
- Section: 规格
- Local scope path: 规格表 > 夹紧器容量（空动作时）> 释放时与夹紧时
- Evidence type: TABLE
- Evidence: 规格表按 VFH1000/2000/3000 分别列出释放时 0.16/0.21/0.40 cm3、定位侧 0.07/0.10/0.16 cm3。

## VFH-Q-0015

**Type: TABLE**

### Target

- Binding: EXACT_MODEL
- Product: VFH 大扩径量型通用扩径定位销
- Model / Scope: VFH1000-080-D-H20 locating-pin geometry

### Question

对 `VFH1000-080-D-H20`，给出释放时定位销直径上限、全行程时定位销直径
下限和定位销行程。

### Standard Answer

释放时定位销直径为 phi 7.6 mm 以下；全行程时为 phi 8.3 mm 以上；定位销
行程为 2.1 mm。

### Scoring Standard

- P1 [35]: 正确给出释放时定位销直径为 phi 7.6 mm 以下。
- P2 [35]: 正确给出全行程时定位销直径为 phi 8.3 mm 以上。
- P3 [30]: 正确给出定位销行程为 2.1 mm。

### Accepted Variants

- `以下` 可写为 `<=`；`以上` 可写为 `>=`。
- `phi` 可写为 `φ`、`Φ` 或 `直径`。

### Forbidden Errors

- 对调释放时上限与全行程时下限。
- 将 2.1 mm 行程写成直径值。

### Tolerance

- Exact source limits and units are required; no additional numerical tolerance.

### Source

- PDF: VFH_R00_2023KW_C1N.pdf
- Physical page: 10
- Printed page: 1318
- Section: 外形尺寸表以及安装部加工尺寸表
- Local scope path: VFH1000 表 > 工件孔径符号 080 列 > 定位销直径与定位销行程
- Evidence type: TABLE
- Evidence: 080 列列出释放时 phi 7.6 mm 以下、全行程时 phi 8.3 mm 以上；定位销行程公共行为 2.1 mm。

## VFH-Q-0016

**Type: TABLE**

### Target

- Binding: EXACT_MODEL
- Product: VFH 大扩径量型通用扩径定位销
- Model / Scope: VFH3000-150-D-H25 locating-pin geometry and mass

### Question

对 `VFH3000-150-D-H25`，给出释放时定位销直径上限、全行程时定位销直径
下限、定位销行程和重量。

### Standard Answer

释放时定位销直径为 phi 14.6 mm 以下；全行程时为 phi 15.7 mm 以上；
定位销行程为 3 mm；重量为 140 g。

### Scoring Standard

- P1 [25]: 正确给出释放时定位销直径为 phi 14.6 mm 以下。
- P2 [25]: 正确给出全行程时定位销直径为 phi 15.7 mm 以上。
- P3 [25]: 正确给出定位销行程为 3 mm。
- P4 [25]: 正确给出 H25 组合的重量为 140 g。

### Accepted Variants

- `以下` 可写为 `<=`；`以上` 可写为 `>=`。
- `phi` 可写为 `φ`、`Φ` 或 `直径`。

### Forbidden Errors

- 使用 VFH2000 的定位销直径或重量行数据。
- 忽略 H25 高度列而给出 H15/H20 的重量。

### Tolerance

- Exact source limits and units are required; no additional numerical tolerance.

### Source

- PDF: VFH_R00_2023KW_C1N.pdf
- Physical page: 12
- Printed page: 1320
- Section: 外形尺寸表以及安装部加工尺寸表
- Local scope path: VFH3000 表 > 工件孔径符号 150 / 着座高度 H25 列 > 定位销直径、行程、重量
- Evidence type: TABLE
- Evidence: 150 列列出释放时 phi 14.6 mm 以下、全行程时 phi 15.7 mm 以上、行程 3 mm；150/H25 重量列为 140 g。

## VFH-Q-0017

**Type: TABLE**

### Target

- Binding: DOCUMENT_COMMON
- Product: VFH PDF 通用技术参考
- Model / Scope: VFH_R00_2023KW_C1N.pdf :: common appendix / surface roughness notation change

### Question

在 2021 年后的表面粗糙度新标示中，`Rz 25` 对应的 Rz 值、Ra 参考值和旧
JIS B 0601:1982 的 Rmax 范围分别是什么？

### Standard Answer

`Rz 25` 的 Rz 值为 25，Ra 参考值为 6.3；对应旧标示的 Rmax 范围为
12.5S-25S。

### Scoring Standard

- P1 [35]: 正确给出 Rz 值为 25。
- P2 [30]: 正确给出 Ra 参考值为 6.3。
- P3 [35]: 正确给出旧标示 Rmax 范围为 12.5S-25S。

### Accepted Variants

- 范围连接符可写为 `~`、`-` 或 `至`。

### Forbidden Errors

- 将 Ra 6.3 当作 Rz 值。
- 将旧标示写成 1.6S-6.3S 或 50S-100S。

### Tolerance

- Exact source mapping is required; no numerical tolerance.

### Source

- PDF: VFH_R00_2023KW_C1N.pdf
- Physical page: 19
- Printed page: 1729
- Section: 表面粗糙度（表面性状）符号的标示更改
- Local scope path: 标示更改通知 > 新标示/旧标示比较表 > Rz 25 行
- Evidence type: TABLE
- Evidence: Rz 25 行在新标示列给出 Rz 25、Ra 参考值 6.3，在旧标示列对应 Rmax 12.5S-25S。

## VFH-Q-0018

**Type: MODEL**

### Target

- Binding: DOCUMENT_COMMON
- Product: VFH PDF 通用技术参考
- Model / Scope: VFH_R00_2023KW_C1N.pdf :: common appendix / O-ring notation change

### Question

将新 O 形密封圈标示 `OR NBR-90 P5-N` 转换为旧 JIS 标示，并按字段解释
`NBR-90`、`P`、`5` 和 `N`。

### Standard Answer

旧 JIS 标示为 `1BP5`。`NBR-90`（旧材料识别符号 `1B`）表示一般用丁腈
橡胶、A 型硬度 90；`P` 表示滑动用；`5` 是公称号；末尾 `N` 表示一般用
品质等级。

### Scoring Standard

- P1 [25]: 正确转换为旧标示 `1BP5`。
- P2 [25]: 正确解释 `NBR-90`/`1B` 为一般用丁腈橡胶、A 型硬度 90。
- P3 [15]: 正确解释 `P` 为滑动用种类标记。
- P4 [15]: 正确解释 `5` 为公称号。
- P5 [20]: 正确解释末尾 `N` 为一般用品质等级。

### Accepted Variants

- `丁腈橡胶` 可写为 `NBR`，但必须保留 A 型硬度 90。
- `一般用` 可写为 `通用`。

### Forbidden Errors

- 将旧标示写成 `1AP5`。
- 将 `P` 解释为材料硬度或将末尾 `N` 解释为公称号。

### Tolerance

- N/A

### Source

- PDF: VFH_R00_2023KW_C1N.pdf
- Physical page: 20
- Printed page: 1730
- Section: O 形密封圈的标示更改
- Local scope path: 标示更改通知 > 新旧标示比较表与字段说明 > OR NBR-90 P5-N / 1BP5
- Evidence type: TABLE
- Evidence: 比较表将 OR NBR-90 P5-N 映射为 1BP5；字段图定义 NBR-90/1B、P、5、N 分别为材料识别、滑动用、公称号和一般用品质等级。
