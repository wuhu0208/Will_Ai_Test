---
schema_version: will-ai-question-bank/v1
source_pdf: SWA_R00_FA2026-C1N.pdf
source_sha256: 91f032cd253112733c358f45d78c24847a5b7dbe35105f1028b39252d65f87ac
source_pages: 32
question_bank_version: V1
product_scope: SWA
---

# SWA_R00_FA2026-C1N 题库与判定标准

## 1. Source Information

- Source PDF: `SWA_R00_FA2026-C1N.pdf`
- SHA-256: `91f032cd253112733c358f45d78c24847a5b7dbe35105f1028b39252d65f87ac`
- Physical pages: 32
- Product: KOSMEK SWA 气动涨紧下拉夹紧器
- Product printed pages: 693-718
- Included common-reference printed pages: 925-928, 947-948
- Source-evidence policy: PDF page images control visual facts; OCR is a navigation aid and is not source truth.

## 2. Scope

### 2.1 Product and document scope

This bank covers the SWA pneumatic double-acting expanding pull-down clamp series:
purpose and mechanism, SWA1000/SWA2000 bodies, straight-hole and tapered-hole
forms, workpiece-lift and no-pull-down variants, model grammar, specifications,
force formulae and curves, dimensions, installation, pneumatic circuits, sensing,
design and operating cautions, maintenance, and applicable common-reference
material included in the PDF.

Warranty terms and sales-network material are retained in the inventory but excluded
from core capability questions because they are commercial metadata rather than
durable SWA technical knowledge.

### 2.2 Model Grammar

The PDF defines separate straight-hole and tapered-hole forms.

Straight-hole pattern:

`SWA<BodySize>00<DesignNo>-<Lift>-<HoleCode>-<SeatHeight?>-<ClawShape?>-<Option?>`

Tapered-hole pattern:

`SWA<BodySize>00<DesignNo>-<Lift>-<HoleCode>-<SeatHeight?>-T`

An optional blank field is represented by the unmarked position between separators.
Fields must stay in the printed order and follow these rules.

| Field | Legal values | Meaning and constraint |
|---|---|---|
| BodySize | `1`, `2` | Selects SWA1000 or SWA2000. |
| Fixed digits | `00` | Fixed digits printed between body size and design number. |
| DesignNo | `0` | Product version/design number listed by this PDF. |
| Lift | `A`, `N` | `A` lifts the released workpiece 0.2 mm; `N` has no workpiece-lift function. Use `N` when combined with the listed expanding locating pins. |
| Straight HoleCode for BodySize `1` | `060`, `065`, `070`, `075`, `080`, `085`, `090` | Straight workpiece holes phi 6-9 mm in 0.5 mm steps. |
| Straight HoleCode for BodySize `2` | `090`, `095`, `100`, `105`, `110`, `115`, `120`, `125`, `130` | Straight workpiece holes phi 9-13 mm in 0.5 mm steps. |
| Tapered HoleCode for BodySize `1` | `065`, `070`, `075`, `080`, `085`, `090` | Tapered holes phi 6.5-9 mm; code `060` is forbidden. |
| Tapered HoleCode for BodySize `2` | `090`, `095`, `100`, `105`, `110`, `115`, `120`, `125`, `130` | Tapered holes phi 9-13 mm. |
| SeatHeight | blank, `H35`, `H40`, `H45`, `H50`, `H55`, `H60` | Blank is the standard 30 mm height; explicit nonstandard heights use 5 mm steps. `H30` is not the printed notation. |
| Straight ClawShape | blank, `F` | Blank is serrated for strong internal-wall clamping; `F` is non-serrated. |
| Tapered ClawShape | `T` | Tapered-hole form is serrated and uses the terminal `T`; `F` is unavailable. |
| Straight Option | blank, `W` | Blank is the standard pull-down form; `W` has no pull-down function, no seating-confirmation air port, and no lift spring. `W` requires Lift `N`. |

Additional model constraints:

- The tapered-hole form has no `W` option field and permits a taper angle up to 3 degrees; below 1 degree requires consultation with KOSMEK.
- Straight SWA1000 codes `060` and `065` are limited to 0.5 MPa maximum supply pressure.
- Tapered SWA1000 codes `065` and `070` are limited to 0.5 MPa maximum supply pressure.
- No-pull-down SWA1000 code `060` or `065`, with or without `F`, is limited to 0.5 MPa maximum supply pressure.
- Straight-hole object tolerance depends on Lift: `A` uses phi d +/-0.3 mm; `N` uses phi d +0.7/-0.3 mm.
- Tapered-hole tolerance depends on body, hole code, and taper-angle band; it must be taken from the printed table rather than inferred from the straight-hole rule.

Positive grammar cases:

- `SWA1000-N-065-H45-F-W`
- `SWA1000-A-090--T`
- `SWA2000-N-130-H60-F-W`

Negative grammar cases and reasons:

- `SWA1000-A-060--T`: tapered form forbids hole code `060`.
- `SWA1000-A-065-H45-F-W`: option `W` requires Lift `N`.
- `SWA1000-N-095-H40-F-W`: code `095` is outside the SWA1000 range.
- `SWA2000-N-085-H40-F-W`: code `085` is outside the SWA2000 range.
- `SWA1000-N-070-H45-F-T`: tapered `T` cannot be combined with straight non-serrated `F`.
- `SWA1000-N-070-H30-F-W`: standard 30 mm height uses a blank field, not `H30`.
- `SWA1001-N-065-H45-F-W`: design number `1` is not listed.
- `SWA1000-N-065-H45-F-X`: option `X` is not listed.

### 2.3 Source-first inventory and initial dispositions

`HIGH` and `MEDIUM` items remain open until their mapped questions and construction
audits are complete. The disposition column identifies the planned Work Package and
does not claim coverage in advance.

| Inventory ID | Physical / printed page | Local scope | Evidence type | Priority | Testable object | Initial disposition |
|---|---|---|---|---|---|---|
| SWA-SI-001 | 1 / 693 | Product introduction > operating principle | TEXT + DRAWING | HIGH | Expand against the workpiece-hole wall, then pull the workpiece down for clamping | WP2 `FACT` |
| SWA-SI-002 | 2 / 694 | Features > fixture and machining benefits | TEXT + DRAWING | MEDIUM | Shorter tool overhang, improved machining accuracy, compact fixture/rotary-table examples | WP2 `FACT` |
| SWA-SI-003 | 3 / 695 | Features > body and application range | TEXT + TABLE + DRAWING | HIGH | SWA/SWE/SWH installation-size boundary; two body sizes; variable seat height and hole diameter | WP2 `TABLE` / `SPEC_LOOKUP` |
| SWA-SI-004 | 4 / 696 | Features > seating and no-pull-down applications | TEXT + DRAWING | HIGH | Seating reference, positioning behavior, and W-form deformation-control use | WP2 `FACT`; WP3 `CAUTION` |
| SWA-SI-005 | 5 / 697 | Features > protection and cleaning | TEXT + DRAWING | HIGH | Protective cap, small sliding clearance, air-cleaning effect, replaceable claw, and rough-guide conditions | WP2 `FACT`; WP3 `CAUTION` |
| SWA-SI-006 | 6 / 698 | Features > self-lock and pull-down mechanism | TEXT + DRAWING | HIGH | Spring clamp/self-lock at zero pressure, pull-down travel, and simplified internal structure | WP2 `FACT`; WP3 `CAUTION` |
| SWA-SI-007 | 7 / 699 | Features > workpiece lift and confirmation | TEXT + DRAWING | HIGH | Lift-option dependency, lift travel, action confirmation, excessive lift, and broken-rod states | WP2 `FACT`; WP3 `CAUTION` |
| SWA-SI-008 | 8 / 700 | Operating principle and sensing states | STATE_DIAGRAM + TEXT | HIGH | Release/clamp sequences, pull-down threshold, seating confirmation, continuous air supply, and abnormal-state detection | WP3 `PROCEDURE` / `CAUTION` |
| SWA-SI-009 | 9-10 / 701-702 | Model designation > straight-hole form | TABLE + DRAWING | HIGH | Seven-field order, body/lift/hole/height/claw/option meanings, body-hole ranges, and W dependencies | Started with `SWA-Q-0001`; expand and audit in WP2/WP4 |
| SWA-SI-010 | 11-12 / 703-704 | Model designation > tapered-hole form | TABLE + DRAWING | HIGH | Six-field order, terminal T, legal holes, angle-dependent tolerances, serration rule, and unavailable options | WP2 `MODEL` / `TABLE` |
| SWA-SI-011 | 13 / 705 | Specifications > straight-hole form | TABLE | HIGH | A/N hole tolerances, eccentric allowance, travel, lift force, air volume, pressure, temperature, fluid, and special pressure limits | WP2 `TABLE` / `SPEC_LOOKUP` |
| SWA-SI-012 | 14 / 706 | Specifications > tapered-hole form | TABLE | HIGH | Taper angle/tolerance binding, eccentric allowance, travel, capacity, pressure, and unavailable 060 code | WP2 `TABLE` / `SPEC_LOOKUP` |
| SWA-SI-013 | 15 / 707 | Standard form > clamping-force table, formula, and chart | FORMULA + CHART + TABLE | HIGH | Force-pressure relationships for serrated/T and F forms, spring force at 0 MPa, and restricted pressure ranges | WP3 `CALCULATION` / `CHART` |
| SWA-SI-014 | 16 / 708 | W form > expansion-force table, formula, and chart | FORMULA + CHART + TABLE | HIGH | Expansion-force relationships, friction assumption, 0 MPa spring force, 0.1 mm maximum pull-down, and pressure limits | WP3 `CALCULATION` / `CHART` |
| SWA-SI-015 | 17-18 / 709-710 | SWA1000 outline and mounting dimensions | DRAWING + TABLE | HIGH | Released/full-stroke geometry, workpiece/mounting-hole machining, height variants, ports, mass, and interference cautions | WP2 `TABLE` / `SPEC_LOOKUP`; WP3 `CAUTION` |
| SWA-SI-016 | 19-20 / 711-712 | SWA2000 outline and mounting dimensions | DRAWING + TABLE | HIGH | Released/full-stroke geometry, workpiece/mounting-hole machining, height variants, ports, mass, and interference cautions | WP2 `TABLE` / `SPEC_LOOKUP`; WP3 `CAUTION` |
| SWA-SI-017 | 21 / 713 | Configuration example > SWA-N with VWM | DRAWING + TEXT | HIGH | D/C locating-pin arrangement, rough-guide design, SWA vertical orientation, and mandatory Lift N selection | WP2 `FACT`; WP3 `PROCEDURE` |
| SWA-SI-018 | 22 / 714 | Pneumatic-circuit examples | STATE_DIAGRAM + TABLE + TEXT | HIGH | One/two-solenoid circuits, VWM-before-SWA sequence, speed-control fallback, sensor-per-clamp rule, sensing states, and failure consequences | WP3 `PROCEDURE` / `CAUTION` |
| SWA-SI-019 | 23 / 715 | Design cautions > unpowered state and seating | TEXT + DRAWING | HIGH | Spring-clamped zero-pressure state, release-air requirement for loading, Z datum, full-seat contact, and seating confirmation | WP3 `CAUTION` |
| SWA-SI-020 | 23 / 715 | Design cautions > force and workpiece constraints | TEXT + DRAWING | HIGH | Trial clamping, insufficient-force drop risk, hole size/depth/taper/hardness limits, thin-wall deformation, and continuous cleaning/sensing air | WP3 `CAUTION` / `PROCEDURE` |
| SWA-SI-021 | 24 / 716 | Handling cautions > horizontal and manual loading | TEXT + DRAWING | HIGH | Pre-clamping for horizontal use, no tilted/floating loading, fully released loading, small support clearance, and rough guides | WP3 `CAUTION` / `PROCEDURE` |
| SWA-SI-022 | 24 / 716 | Robot handling | TEXT + DRAWING | HIGH | Perpendicular insertion/removal, complete withdrawal before coordinate motion, controlled insertion speed, and motion interlock | WP3 `PROCEDURE` / `CAUTION` |
| SWA-SI-023 | 25 / 717 | Installation > air, cleaning, tape, bolts, and ports | TEXT + TABLE | HIGH | Filtered dry air/no lubrication, pre-cleaning, tape practice, M5 class 12.9 at 6.3 N-m, port identities, and phi 6/4 minimum tubing | WP3 `PROCEDURE` / `CAUTION` |
| SWA-SI-024 | 25 / 717 | Operation safety | TEXT | HIGH | Qualified operator, anti-drop/anti-motion controls, zero-energy disassembly, cooling, restart inspection, pinch avoidance, no modification, and spring hazard | WP3 `CAUTION`; bind as product-local safety |
| SWA-SI-025 | 26 / 718 | SWA maintenance and claw replacement | TEXT + TABLE | HIGH | Cleaning clamp/seat surfaces, contamination consequences, manufacturer overhaul, wear replacement, and 1,000,000/500,000-cycle reference values | WP2 `TABLE`; WP3 `PROCEDURE` |
| SWA-SI-026 | 27 / 925 | Common pneumatic appendix > operation and maintenance | TEXT | MEDIUM | Shared zero-energy safety, cleaning, leak/sound/motion checks, storage, and overhaul rules | WP3 `CAUTION` / `PROCEDURE`; bind as `DOCUMENT_COMMON` and avoid duplication |
| SWA-SI-027 | 28 / 926 | Common appendix > warranty | TEXT | LOW | Warranty term, coverage, and exclusions | Exclude from core capability bank; low-value commercial policy |
| SWA-SI-028 | 29 / 927 | Common appendix > surface roughness notation | TABLE | MEDIUM | 2021 old/new JIS notation mapping | WP2 `TABLE`; bind as `DOCUMENT_COMMON` |
| SWA-SI-029 | 30 / 928 | Common appendix > O-ring notation | TABLE + MODEL | MEDIUM | New/old notation mapping and field meanings | WP2 `TABLE` / `MODEL`; bind as `DOCUMENT_COMMON` |
| SWA-SI-030 | 31-32 / 947-948 | Sales addresses and network | TEXT + DRAWING | NON-TEST | Contact details, sales geography, and certification marks | Exclude; not durable SWA technical knowledge |

## 3. Question Statistics

- Total: 1
- MODEL: 1

## 4. Questions

## SWA-Q-0001

**Type: MODEL**

### Target

- Binding: EXACT_MODEL
- Product: SWA 气动涨紧下拉夹紧器
- Model / Scope: SWA1000-N-065-H45-F-W

### Question

请按 PDF 的直孔型号字段顺序，解读 `SWA1000-N-065-H45-F-W` 的主体尺寸、
设计编号、工件提升方式、工件孔径及孔公差、着座高度、涨爪形状和选配功能；
同时给出该组合的最高使用压力，并判断字段组合是否合法。

### Standard Answer

`SWA1000` 的主体尺寸字段为 `1`，适用直径 phi 6-9 mm 的工件孔；固定数字
后面的设计编号为 `0`。`N` 表示无工件提升功能。孔径符号 `065` 表示直孔
phi 6.5 mm；Lift `N` 对应的对象孔公差为 +0.7/-0.3 mm。`H45` 表示着座高度
45 mm。`F` 表示直孔用无锯齿涨爪。`W` 表示无下拉功能，并且该选配必须与
Lift `N` 组合。SWA1000 的 `060`/`065` 无下拉型号最高使用压力为 0.5 MPa。
因此该型号的字段顺序、各字段取值和依赖关系均合法。

### Scoring Standard

- P1 [10]: 正确识别主体尺寸 `1` 对应 SWA1000 及 phi 6-9 mm 范围。
- P2 [5]: 正确识别设计编号为 `0`。
- P3 [10]: 正确解释 `N` 为无工件提升功能。
- P4 [10]: 正确解释 `065` 为直孔 phi 6.5 mm。
- P5 [10]: 正确给出 Lift `N` 下的孔公差 +0.7/-0.3 mm。
- P6 [10]: 正确解释 `H45` 为 45 mm 着座高度。
- P7 [10]: 正确解释 `F` 为直孔用无锯齿涨爪。
- P8 [10]: 正确解释 `W` 为无下拉功能。
- P9 [10]: 明确 `W` 必须与 Lift `N` 组合。
- P10 [10]: 正确给出最高使用压力 0.5 MPa。
- P11 [5]: 明确得出完整字段组合合法的结论。

### Accepted Variants

- `phi 6.5 mm` 可写为 `φ6.5 mm`、`Φ6.5 mm` 或 `直径 6.5 mm`。
- 公差可等价写为上偏差 `+0.7 mm`、下偏差 `-0.3 mm`。
- `无下拉功能` 可写为 `不执行下拉`，但不得与无提升功能混淆。

### Forbidden Errors

- 将 `N` 解释为无下拉功能，或将 `W` 解释为无工件提升功能。
- 将 `F` 解释为锥孔代码或有锯齿涨爪。
- 将对象孔公差写为 +/-0.3 mm；该公差属于 Lift `A`，不是本型号的 `N`。
- 将本型号最高使用压力写为 0.7 MPa。
- 在 `W` 与非 `N` 提升字段组合时仍判定合法。

### Tolerance

- Exact model fields, hole tolerance, and 0.5 MPa pressure limit are required.

### Source

- PDF: SWA_R00_FA2026-C1N.pdf
- Physical page: 9-10, 13, 16
- Printed page: 701-702, 705, 708
- Section: 型号表示（工件孔形状：直孔） / 规格（工件孔形状：直孔） / 能力曲线图（W：无下拉功能）
- Local scope path: 直孔型号字段图 > SWA1000 / N / 065 / H45 / F / W；直孔规格表 > N 孔公差；W 能力页 > SWA1000 060/065 压力限制
- Evidence type: TABLE + DRAWING
- Evidence: 型号页按主体尺寸、设计编号、提升方式、孔径、着座高度、涨爪形状和选配项排列字段；表格定义 N、065、H45、F 和 W，并规定 W 必须选择 N；规格与 W 能力页将 SWA1000 的 060/065 型号最高压力限制为 0.5 MPa。
