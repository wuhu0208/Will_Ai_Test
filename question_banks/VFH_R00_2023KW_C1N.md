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

`HIGH` and `MEDIUM` items remain open until the planned question or audit is
completed. The disposition column identifies the next Work Package and does not
claim question coverage in advance.

| Inventory ID | Physical / printed page | Local scope | Evidence type | Priority | Testable object | Initial disposition |
|---|---|---|---|---|---|---|
| VFH-SI-001 | 1 / 1309 | Product introduction > locating principle | TEXT + DRAWING | HIGH | Expansion/retraction mechanism, zero-clearance positioning, and D/C pin roles | WP2 `FACT` |
| VFH-SI-002 | 1 / 1309 | Product introduction > family performance | TEXT | HIGH | VFH1000 30 um and VFH2000/3000 10 um repeatability | WP2 `SPEC_LOOKUP` |
| VFH-SI-003 | 2 / 1310 | Features > expansion amount and automation clearance | TEXT + DRAWING | HIGH | 1.1 mm expansion; VFH1000 0.7 mm; release-state clearance | WP2 `SPEC_LOOKUP` |
| VFH-SI-004 | 2 / 1310 | Features > concentric nose measurement | TEXT + DRAWING | MEDIUM | VFH2000/3000 allow installation-spacing measurement; VFH1000 does not | WP2 `FACT` |
| VFH-SI-005 | 2 / 1310 | Features > air cleaning | TEXT + DRAWING | HIGH | Air path and contamination-prevention purpose | WP3 `PROCEDURE` / `CAUTION` |
| VFH-SI-006 | 3-5 / 1311-1313 | Application and system examples | DRAWING | MEDIUM | Robot/gantry handling and D/C two-pin fixture arrangement | WP2 `FACT` |
| VFH-SI-007 | 4 / 1312 | Product family comparison | TABLE + DRAWING | MEDIUM | VFL/VFM/VFH/VFJ/VFK class, control, pressure, action, and use-case differences | WP2 `TABLE` |
| VFH-SI-008 | 6 / 1314 | Necessary items > locating workpiece holes | TEXT + DRAWING | HIGH | Hole range phi 5-15 mm and the two tolerance bands | WP2 `SPEC_LOOKUP` |
| VFH-SI-009 | 6 / 1314 | Necessary items > VFH-C installation phase | TEXT + DRAWING | HIGH | VFH-D datum role, VFH-C Y-axis role, and required phase orientation | WP2 `MODEL`; WP3 `PROCEDURE` |
| VFH-SI-010 | 6 / 1314 | Necessary items > seating and workpiece clamp | TEXT + DRAWING | HIGH | No built-in Z datum seat and no clamping function | WP3 `CAUTION` |
| VFH-SI-011 | 7 / 1315 | Model designation | TABLE + DRAWING | HIGH | Field order, legal values, family/hole pairing, D/C, and seat-height grammar | Started with `VFH-Q-0001`; expand and audit in WP2/WP4 |
| VFH-SI-012 | 7 / 1315 | Specification table | TABLE | HIGH | Repeatability, eccentricity, expansion force, shear load, capacity, oil volume, pressure, temperature, and fluid | WP2 `TABLE` / `SPEC_LOOKUP` |
| VFH-SI-013 | 8 / 1316 | Workpiece weight formula > horizontal mounting | FORMULA | HIGH | Weight bound using expansion force, efficiency, friction coefficient, and 9.8 | WP3 `CALCULATION` |
| VFH-SI-014 | 8 / 1316 | Workpiece weight formula > vertical mounting | FORMULA | HIGH | Weight bound using expansion force, 9.8, and efficiency | WP3 `CALCULATION` |
| VFH-SI-015 | 8 / 1316 | Shear load/displacement > VFH1000 | CHART | HIGH | Visual displacement reads for 050/060/070/080 series | WP3 `CHART` |
| VFH-SI-016 | 8 / 1316 | Shear load/displacement > VFH2000 | CHART | HIGH | Visual displacement reads for 090/100/110/120/130 series | WP3 `CHART` |
| VFH-SI-017 | 8 / 1316 | Shear load/displacement > VFH3000 | CHART | HIGH | Visual displacement reads for 140/150 series | WP3 `CHART` |
| VFH-SI-018 | 9-10 / 1317-1318 | VFH1000 outline and mounting dimensions | DRAWING + TABLE | HIGH | Released/full-stroke geometry, workpiece-hole machining, mounting ports, dimensions, and mass | WP2 `TABLE` / `SPEC_LOOKUP` |
| VFH-SI-019 | 11-12 / 1319-1320 | VFH2000/3000 outline and mounting dimensions | DRAWING + TABLE | HIGH | Released/full-stroke geometry, workpiece-hole machining, mounting ports, dimensions, and mass | WP2 `TABLE` / `SPEC_LOOKUP` |
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
| VFH-SI-031 | 19 / 1729 | Common appendix > surface roughness notation | TABLE | MEDIUM | 2021 old/new JIS notation mapping | WP2 `TABLE`; bind as `DOCUMENT_COMMON` |
| VFH-SI-032 | 20 / 1730 | Common appendix > O-ring notation | TABLE + MODEL | MEDIUM | New/old notation mapping and field meanings | WP2 `TABLE` / `MODEL`; bind as `DOCUMENT_COMMON` |
| VFH-SI-033 | 21-22 / 1749-1750 | Sales addresses and network | TEXT + DRAWING | NON-TEST | Contact details and geographic sales map | Exclude; not durable VFH technical knowledge |

## 3. Question Statistics

- Total: 1
- MODEL: 1

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

- N/A

### Source

- PDF: VFH_R00_2023KW_C1N.pdf
- Physical page: 7
- Printed page: 1315
- Section: 型号表示 / 规格
- Local scope path: 型号表示 > VFH2000-090-D-H20 字段图；工件孔径表 > 090；功能分类；着座高度
- Evidence type: TABLE
- Evidence: 型号表示图按主体尺寸、设计编号、工件孔径、功能分类、着座高度排列字段；同页表格将 VFH2000 与 090 绑定，定义 090 为 phi 9 mm、+0.7/-0.3 mm，D 为基准销，H20 为 20 mm。
